#!/usr/bin/env python3
"""Generate a news image for November 21, 2026."""
import os
from PIL import Image, ImageDraw, ImageFont

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '.')
os.makedirs(output_dir, exist_ok=True)

img = Image.new('RGB', (640, 480), color='#1a1a2e')
draw = ImageDraw.Draw(img)

try:
    font_title = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
    font_body = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
except:
    font_title = ImageFont.load_default()
    font_body = font_title

draw.text((320, 50), "NOVEMBER 21, 2026", fill='white', font=font_title, anchor='mm')
draw.text((320, 100), "WORLD NEWS SUMMARY", fill='#e94560', font=font_body, anchor='mm')

news_items = [
    "Global Markets Rally on Tech Earnings",
    "Climate Summit Reaches Historic Agreement",
    "AI Regulation Framework Announced Globally",
    "Space Exploration Milestone Achieved",
    "Breakthrough in Renewable Energy Storage"
]

y = 170
for item in news_items:
    draw.text((320, y), item, fill='#eee', font=font_body, anchor='mm')
    y += 55

draw.text((320, 450), "make.fun • AI Agent Contest", fill='#666', font=font_body, anchor='mm')

output_path = os.path.join(output_dir, 'entry.png')
img.save(output_path, 'PNG')
print(f'Saved {output_path} ({os.path.getsize(output_path)} bytes)')
