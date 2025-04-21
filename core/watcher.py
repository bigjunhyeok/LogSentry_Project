import os
import json
from datetime import datetime
from core.notifier import notify

class LogWatcher:
    def __init__(self, config, file_conf, formatter):
        # 로그 감시 대상 및 설정 초기화
        self.log_file = file_conf["path"]
        self.keywords = file_conf["keywords"]
        self.alert_on_repeat = file_conf["alert_on_repeat"]
        self.notify_targets = config["notify"]
        self.recent_hits = []
        self.format_log_line = formatter

        # 로그 디렉터리 없으면 생성
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

        # 로그 파일 없으면 빈 파일로 생성
        if not os.path.exists(self.log_file):
            open(self.log_file, "w").close()

        # 로그 파일 열기 (tail 방식)
        self.file = open(self.log_file, "r", encoding="utf-8")
        self.file.seek(0, os.SEEK_END)

        # 감지된 로그를 저장할 JSONL 경로
        self.json_log_path = self.log_file.replace(".log", ".jsonl")

    def watch_once(self):
        # 로그 한 줄 읽기
        line = self.file.readline()
        if not line:
            return None

        # 키워드가 포함된 라인 감지
        for keyword in self.keywords:
            if keyword in line:
                clean = line.strip()
                self.recent_hits.append(clean)

                # 감지된 로그 JSONL로 저장
                log_entry = {
                    "timestamp": datetime.now().isoformat(),
                    "file": self.log_file,
                    "keyword": keyword,
                    "message": clean
                }
                with open(self.json_log_path, "a", encoding="utf-8") as jf:
                    jf.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

        # 일정 횟수 이상 감지되면 알림 전송
        if len(self.recent_hits) >= self.alert_on_repeat:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            alert_msg = f"[알림] 🔔 {self.log_file}에서 {len(self.recent_hits)}건 이상 감지됨"
            print(self.format_log_line(timestamp, "WATCHER", "", alert_msg))

            # Slack Webhook 설정 여부 확인
            if "slack" in self.notify_targets and not os.getenv("SLACK_WEBHOOK_URL"):
                print(self.format_log_line(timestamp, "WATCHER", "WARN", "Slack Webhook 설정 안됨"))

            # 감지된 각 로그 출력
            for hit in self.recent_hits:
                print(self.format_log_line(timestamp, "WATCHER", "INFO", hit))

            # 알림 전송 및 상태 초기화
            notify(alert_msg, self.notify_targets)
            self.recent_hits = []

        # 원본 라인 반환 (필요 시 활용 가능)
        return line