import os
import requests
from datetime import datetime

# 로그 출력 포맷 함수
def format_log_line(timestamp, source, level, message):
    return f"{timestamp} | {source:<9} | {level:<9} | {message}"

# 알림 전송 함수 (콘솔 + Slack)
def notify(message, targets):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 콘솔 출력
    if "console" in targets:
        print(format_log_line(timestamp, "WATCHER", "ALERT", message))
    # Slack Webhook 전송
    if "slack" in targets:
        webhook_url = os.getenv("SLACK_WEBHOOK_URL")
        if webhook_url:
            requests.post(webhook_url, json={"text": f"[알림] 🔔 {message}"})
        else:
            print(format_log_line(timestamp, "WATCHER", "WARN", "Slack Webhook 설정 안됨"))