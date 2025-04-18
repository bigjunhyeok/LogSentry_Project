import time
import json
from watcher import LogWatcher
from dotenv import load_dotenv

load_dotenv()

def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    config = load_config()
    watcher = LogWatcher(config)
    print(f"[LogSentry] 감시 시작: {config['log_file']}")

    while True:
        watcher.watch_once()
        time.sleep(config["interval"])

if __name__ == "__main__":
    main()