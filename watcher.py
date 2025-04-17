import os
from notifier import notify

class LogWatcher:
    def __init__(self, config):
        self.log_file = config["log_file"]
        self.keywords = config["keywords"]
        self.alert_on_repeat = config["alert_on_repeat"]
        self.notify_targets = config["notify"]
        self.recent_hits = []

        self.file = open(self.log_file, "r", encoding="utf-8")
        self.file.seek(0, os.SEEK_END)  # 파일 끝으로 이동

    def watch_once(self):
        line = self.file.readline()
        if not line:
            return

        for keyword in self.keywords:
            if keyword in line:
                self.recent_hits.append(line.strip())
                print(f"[HIT] {keyword} → {line.strip()}")

        if len(self.recent_hits) >= self.alert_on_repeat:
            message = f"⚠️ 경고: {len(self.recent_hits)}건 이상 감지됨\n" + "\n".join(self.recent_hits)
            notify(message, self.notify_targets)
            self.recent_hits = []  # 초기화
