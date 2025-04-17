import os
import requests

def notify(message, targets):
    if "console" in targets:
        print(f"[ALERT]\n{message}")

    if "slack" in targets:
        webhook_url = os.getenv("SLACK_WEBHOOK_URL")
        if webhook_url:
            requests.post(webhook_url, json={"text": message})
        else:
            print("[WARN] Slack Webhook 설정 안됨")
