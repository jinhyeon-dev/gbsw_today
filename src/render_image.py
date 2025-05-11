from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

FONT_PATH = "fonts/Pretendard-Bold.otf"
BASE_IMAGE_PATH = "assets/base.png"
OUTPUT_DIR = "outputs"
TITLE_FONT_SIZE = 36
BODY_FONT_SIZE = 44
TEXT_COLOR = "black"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def render_meal_image(meal_type: str, meal_text: str, date: str):
    image = Image.open(BASE_IMAGE_PATH).convert("RGB")
    draw = ImageDraw.Draw(image)

    title_font = ImageFont.truetype(FONT_PATH, TITLE_FONT_SIZE)
    body_font = ImageFont.truetype(FONT_PATH, BODY_FONT_SIZE)

    title_text = f"{date} {meal_type}"
    body_lines = meal_text.strip().split("\n")

    padding_left = 160           
    content_top_y = 420           
    title_y = content_top_y - 220 
    line_spacing = 70

    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    image_width, image_height = image.size
    title_x = (image_width - (title_bbox[2] - title_bbox[0])) // 2
    draw.text((title_x, title_y), title_text, font=title_font, fill=TEXT_COLOR)

    for i, line in enumerate(body_lines):
        y = content_top_y + i * line_spacing
        line_bbox = draw.textbbox((0, 0), line, font=body_font)
        line_width = line_bbox[2] - line_bbox[0]
        line_x = (image_width - line_width) // 2
        draw.text((line_x, y), line, font=body_font, fill=TEXT_COLOR)

    output_path = os.path.join(OUTPUT_DIR, f"{meal_type.lower()}.jpg")
    image.save(output_path)
    return output_path