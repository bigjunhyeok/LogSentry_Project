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

```
LogSentry_Project/
├── config/                  # 설정 파일 저장 디렉터리
│   ├── config.json          # 감시 대상 로그 파일, 키워드, 알림 설정 등 메인 설정 파일
│   └── log_config.json      # 로그 메시지 템플릿 (레벨, 메시지 종류 등 정의)
│
├── logs/                    # 실시간 생성되는 로그 파일 저장 디렉터리
│   ├── app.log              # 애플리케이션 로그
│   └── db.log               # DB 관련 로그
│
├── core/                    # 핵심 기능 모듈 디렉터리
│   ├── loader.py            # 설정 파일 로드 함수 모듈
│   ├── generator.py         # 로그 메시지 생성기 (랜덤 로그 발생)
│   ├── watcher.py           # 로그 파일 감시기 (키워드 감지 및 이벤트 알림)
│   └── notifier.py          # 알림 전송 모듈 (Slack, Console 등)
│
├── main.py                  # 메인 실행 스크립트 (감시기 및 생성기 구동)
├── requirements.txt         # Python 패키지 의존성 정의
└── README.md                # 프로젝트 설명 문서 (바로 이 파일)
```

---

## ⚙️ 설정 방법

### 1. 의존성 설치

```
pip install -r requirements.txt
```

### 2. `.env` 설정

```
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/xxx/yyy/zzz
```

### 3. `config.json` 구성 예시

```
{
  "interval": 1,
  "log_file": "logs/sample.log",
  "keywords": ["ERROR", "Exception", "OutOfMemory"],
  "alert_on_repeat": 3,
  "notify": ["console", "slack"]
}
```

---

## 🚀 실행 방법

```
python main.py
```

---

## 🧪 테스트

```
echo "2025-04-18 23:15:00 - ERROR - DB 연결 실패" >> logs/sample.log
```

→ 일정 횟수 이상 감지되면 알림 전송

---

## 📌 향후 확장 가능 기능

- 다중 로그 파일 동시 감시
- 정규표현식 기반 패턴 탐지
- 이메일, Discord, Webhook 등 다양한 알림 채널 추가
- 주간 리포트 자동 생성 (PDF 또는 Markdown)
- GUI 대시보드 (Flask 기반)
