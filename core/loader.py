import os
import json

# 메인 설정 파일 로드 (config.json)
def load_config():
    with open("config/config.json", "r", encoding="utf-8") as f:
        return json.load(f)

# 로그 메시지 템플릿 로드 (log_config.json)
def load_log_template():
    path = os.path.join("config", "log_config.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)