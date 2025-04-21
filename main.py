import time
import threading
from core.loader import load_config
from core.generator import run_log_generator
from core.watcher import LogWatcher

# 로그 출력 포맷 정렬 함수 (날짜 | SOURCE | 레벨 | 메시지)
def format_log_line(timestamp, source, level, message):
    return f"{timestamp:<19} | {source:<9} | {level:<9} | {message}"

# 감시기 스레드 실행 함수
def run_watcher(config, file_conf):
    watcher = LogWatcher(config, file_conf, format_log_line)
    while True:
        watcher.watch_once()
        time.sleep(config["interval"])

# 메인 함수
def main():
    config = load_config()

    # 로그 생성기 실행
    if config.get("generate_log", False):
        for file_conf in config["log_files"]:
            t = threading.Thread(
                target=run_log_generator,
                args=(file_conf["path"], format_log_line),
                daemon=True
            )
            t.start()
            print(format_log_line(time.strftime("%Y-%m-%d %H:%M:%S"), "GENERATOR", "", f"[실행] ➡️{file_conf['path']}"))

    # 로그 감시기 실행
    for file_conf in config["log_files"]:
        t = threading.Thread(
            target=run_watcher,
            args=(config, file_conf),
            daemon=True
        )
        t.start()
        print(format_log_line(time.strftime("%Y-%m-%d %H:%M:%S"), "WATCHER", "", f"[감시] ➡️{file_conf['path']}"))

    # 메인 스레드는 대기 유지
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()