# 2025.4.30 - 개발자 김진현

import datetime
import os
import subprocess
from instagrapi import Client
from dotenv import load_dotenv
from src.fetch_meal import get_meal
from src.render_image import render_meal_image

load_dotenv()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")
SESSION_PATH = "session.json"

def login_instagram():
    cl = Client()

    if os.path.exists(SESSION_PATH):
        cl.load_settings(SESSION_PATH)
        try:
            cl.login(USERNAME, PASSWORD)
        except Exception:
            print("세션 만료됨. 재로그인 시도 중...")
            cl.set_locale("ko_KR")
            cl.set_timezone_offset(32400)
            cl.login(USERNAME, PASSWORD)
            cl.dump_settings(SESSION_PATH)
    else:
        cl.set_locale("ko_KR")
        cl.set_timezone_offset(32400)
        cl.login(USERNAME, PASSWORD)
        cl.dump_settings(SESSION_PATH)

    return cl

def main():
    # 오늘 날짜
    today = datetime.date.today().strftime("%Y%m%d")
    display_date = datetime.date.today().strftime("%Y.%m.%d")

    # 급식 정보 가져오기
    meals = get_meal(today)

    # Instagram 로그인
    cl = login_instagram()

    # 끼니별 이미지 생성 및 업로드
    for meal_type_kor, meal_text in zip(["조식", "중식", "석식"], [meals["breakfast"], meals["lunch"], meals["dinner"]]):
        if meal_text == "없음":  # 급식이 없을 경우 건너뜀
            print(f"[건너뜀] {meal_type_kor} 급식이 없습니다.")
            continue

        # 이미지 생성 부분
        path = render_meal_image(meal_type_kor, meal_text, display_date)
        print(f"{meal_type_kor} 이미지 저장 완료:", path)

        # Instagram 스토리 업로드
        print(f"[업로드 중] {meal_type_kor}")
        cl.photo_upload_to_story(path, f"{meal_type_kor} 🍽️")

if __name__ == "__main__":
    main()