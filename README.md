# 📸 GBSW 급식 자동 스토리 봇

경북소프트웨어마이스터고등학교의 급식 정보를 매일 아침 6시에 인스타그램 스토리에 자동으로 업로드하는 Python 기반 자동화 봇입니다.

---

## 🧩 주요 기능

- 📅 **NEIS OpenAPI**를 활용한 조/중/석 급식 정보 수집
- 🖼️ **Pillow**를 사용해 급식 정보를 이미지로 렌더링
- 🤖 **instagrapi**로 Instagram 스토리 자동 업로드
- 🕕 **schedule/cron**으로 매일 아침 6시 자동 실행
- 🔐 로그인 세션을 `session.json`으로 저장하여 반복 로그인 방지

---

## ⚙️ 사용 방법

1. `.env` 파일 생성

```env
NEIS_API_KEY=your_neis_api_key
IG_USERNAME=your_instagram_username
IG_PASSWORD=your_instagram_password
```

2. 의존성 설치
```zshrc
pip install -r requirements.txt
```

3.	전체 실행
```zshrc
python main.py           # 급식 이미지 생성
python src/upload_story.py  # 스토리 업로드
```

---

## 🛠 기술 스택
- Python 3.10+
- NEIS OpenAPI
- Pillow
- instagrapi
- schedule or macOS launchd

---

⚠️ 주의사항
- 이 프로젝트는 **비공식 Instagram API(instagrapi)**를 사용합니다.
- 실제 계정보다는 테스트 전용 계정 사용을 권장합니다.
- instagrapi 사용 시 계정이 제한될 수 있으니 주의하세요.
