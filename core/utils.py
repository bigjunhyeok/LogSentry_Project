import os

# 로그 파일이 없을 경우 디렉토리와 빈 파일 생성
def ensure_log_file(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        open(path, "w").close()