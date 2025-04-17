# LogSentry

실시간 로그 감시 및 이상 탐지 시스템
지정된 로그 파일을 실시간으로 감시하고, 특정 키워드 또는 에러 패턴이 일정 기준 이상 감지되면 Slack 또는 콘솔로 알림을 전송합니다.

---

## 🛠 주요 기능

- 실시간 로그 파일 모니터링 (`tail -f` 유사)
- 키워드 기반 오류 탐지 (`ERROR`, `Exception` 등)
- 일정 횟수 이상 반복 감지 시 자동 알림
- Slack Webhook 또는 콘솔 출력 방식 지원
- 감시 간격 및 조건은 `config.json`에서 설정 가능

---

## 📁 프로젝트 구조

'''
logsentry/
├── main.py              # 실행 진입점
├── watcher.py           # 로그 감시 로직
├── notifier.py          # 알림 전송 모듈
├── config.json          # 감시 설정 파일
├── .env                 # 슬랙 웹훅 보안 키 저장
├── logs/                # 샘플 로그 위치
└── requirements.txt     # 필요 패키지 목록
'''

---

## ⚙️ 설정 방법

### 1. 의존성 설치

'''
pip install -r requirements.txt
'''

### 2. `.env` 설정

'''
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/xxx/yyy/zzz
'''

### 3. `config.json` 구성 예시

'''
{
  "interval": 1,
  "log_file": "logs/sample.log",
  "keywords": ["ERROR", "Exception", "OutOfMemory"],
  "alert_on_repeat": 3,
  "notify": ["console", "slack"]
}
'''

---

## 🚀 실행 방법

'''
python main.py
'''

---

## 🧪 테스트

'''
echo "2025-04-18 23:15:00 - ERROR - DB 연결 실패" >> logs/sample.log
'''

→ 일정 횟수 이상 감지되면 알림 전송

---

## 📌 향후 확장 가능 기능

- 다중 로그 파일 동시 감시
- 정규표현식 기반 패턴 탐지
- 이메일, Discord, Webhook 등 다양한 알림 채널 추가
- 주간 리포트 자동 생성 (PDF 또는 Markdown)
- GUI 대시보드 (Flask 기반)
