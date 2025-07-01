import os
import random
from PIL import Image, ImageDraw, ImageFont

def generate_text_image(text, rgb_color, width, height, output_path, font_size=40):
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    draw.text((x, y), text, fill=rgb_color, font=font)
    image.save(output_path)

def get_contrasting_color(threshold=180):
    while True:
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        luminance = 0.299 * r + 0.587 * g + 0.114 * b
        if luminance < threshold:
            return (r, g, b)

def create_images(n, width=100, height=100):
    for label in ['0', '1']:
        dir_path = os.path.join('data', label)
        os.makedirs(dir_path, exist_ok=True)
        for i in range(n):
            color = get_contrasting_color()
            file_path = os.path.join(dir_path, f"{i}.png")
            generate_text_image(label, color, width, height, file_path)

create_images(n=100)
