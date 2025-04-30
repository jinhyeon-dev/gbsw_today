from instagrapi import Client
import os
from dotenv import load_dotenv

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

    meal_order = ["조식", "중식", "석식"]
    for meal in meal_order:
        image_path = f"outputs/{meal}.jpg"
        if os.path.exists(image_path):
            print(f"[업로드 중] {meal}")
            cl.photo_upload_to_story(image_path, f"{meal} 🍽️")
        else:
            print(f"[경고] {image_path} 파일이 존재하지 않습니다.")

if __name__ == "__main__":
    upload_meal_images()