import datetime
from instagrapi import Client
import os
from dotenv import load_dotenv

from fetch_meal import get_meal

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

def upload_meal_images():
    cl = login_instagram()

    # 오늘 날짜 가져오기
    today = datetime.date.today().strftime("%Y%m%d")
    meals = get_meal(today)

    meal_order = [("조식", meals["breakfast"]), ("중식", meals["lunch"]), ("석식", meals["dinner"])]
    for meal_type, meal_text in meal_order:
        if meal_text == "없음":  # 급식이 없을 경우 건너뛰기
            print(f"[건너뜀] {meal_type} 급식이 없습니다.")
            continue

        image_path = f"outputs/{meal_type}.jpg"
        if os.path.exists(image_path):
            print(f"[업로드 중] {meal_type}")
            cl.photo_upload_to_story(image_path, f"{meal_type} 🍽️")
        else:
            print(f"[경고] {image_path} 파일이 존재하지 않습니다.")


if __name__ == "__main__":
    upload_meal_images()