import requests
import datetime
import os
import re
from dotenv import load_dotenv

load_dotenv()

NEIS_API_KEY = os.getenv("NEIS_API_KEY")
ATPT_OFCDC_SC_CODE = "R10"     # 경북교육청
SD_SCHUL_CODE = "8750829"      # 경북소프트웨어마이스터고

def clean_meal_text(meal_text: str) -> str:
    # 정규식을 사용하여 괄호 안의 내용 제거
    return re.sub(r"\([^)]*\)", "", meal_text).strip()

def get_meal(date: str):
    url = f"https://open.neis.go.kr/hub/mealServiceDietInfo"
    params = {
        "KEY": NEIS_API_KEY,
        "Type": "json",
        "ATPT_OFCDC_SC_CODE": ATPT_OFCDC_SC_CODE,
        "SD_SCHUL_CODE": SD_SCHUL_CODE,
        "MLSV_YMD": date
    }
    res = requests.get(url, params=params)
    data = res.json()

    if 'mealServiceDietInfo' not in data:
        return {"breakfast": "없음", "lunch": "없음", "dinner": "없음"}

    meals = {"1": "breakfast", "2": "lunch", "3": "dinner"}
    result = {"breakfast": "", "lunch": "", "dinner": ""}

    for row in data['mealServiceDietInfo'][1]['row']:
        meal_type = row['MMEAL_SC_CODE']
        meal_name = meals.get(meal_type, "")
        # 괄호 안의 내용을 제거한 후 저장
        result[meal_name] = clean_meal_text(row['DDISH_NM'].replace("<br/>", "\n"))

    return result

# 테스트
if __name__ == "__main__":
    today = datetime.date.today().strftime("%Y%m%d")
    meal = get_meal(today)
    print(meal)