from src.fetch_meal import get_meal
from src.render_image import render_meal_image
import datetime
import subprocess

def main():
    # 오늘 날짜
    today = datetime.date.today().strftime("%Y%m%d")
    display_date = datetime.date.today().strftime("%Y.%m.%d")

    # 급식 정보 가져오기
    meals = get_meal(today)

    # 끼니별 이미지 생성
    for meal_type_kor, meal_text in zip(["조식", "중식", "석식"], [meals["breakfast"], meals["lunch"], meals["dinner"]]):
        path = render_meal_image(meal_type_kor, meal_text, display_date)
        print(f"{meal_type_kor} 이미지 저장 완료:", path)

        # Mac에서 자동 열기 (선택)
        subprocess.run(["open", path])

if __name__ == "__main__":
    main()