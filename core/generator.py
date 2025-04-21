import time
import random
from datetime import datetime
from core.loader import load_log_template
from core.utils import ensure_log_file

# 로그 메시지 템플릿 로드
template_data = load_log_template()

# 로그 한 줄 생성
def generate_log_line(file_path):
    level = random.choice(template_data["levels"])

    # 로그 파일 종류에 따라 메시지 선택
    if "db.log" in file_path:
        template = random.choice(template_data["db_messages"])
    elif "app.log" in file_path:
        template = random.choice(template_data["app_messages"])
    else:
        template = random.choice(template_data["app_messages"] + template_data["db_messages"])

    log = template.format(
        user=random.choice(template_data["users"]),
        file=random.choice(template_data["files"]),
        module=random.choice(template_data["modules"]),
        exception=random.choice(template_data["exceptions"])
    )

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return timestamp, level, log

# 로그 생성 실행 함수
def run_log_generator(file_path, formatter):
    ensure_log_file(file_path)

    while True:
        timestamp, level, log = generate_log_line(file_path)
        full_line = f"{timestamp} | {level:<9} | {log}"

        # 로그 파일에 기록
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(full_line + "\n")

        # ERROR 이상 로그만 콘솔 출력
        if level in ("ERROR", "CRITICAL"):
            print(formatter(timestamp, "GENERATOR", level, log))

        time.sleep(random.uniform(0.2, 2.0))