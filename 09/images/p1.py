from PIL import Image
import random

# 設定
CANVAS_WIDTH = 150
CANVAS_HEIGHT = 150
NUM_IMAGES = 10
IMG_PATH = "/Volumes/NBPlan/TTC/授業資料/2025年度/1020201.アルゴリズム２/09/p1.png"

# 元画像読み込み
original_img = Image.open(IMG_PATH).convert("RGBA")

# --- サイズ変更の追加 ---
SCALE = 0.15  # 30%の大きさに縮小
new_size = (int(original_img.width * SCALE), int(original_img.height * SCALE))
resized_img = original_img.resize(new_size, Image.LANCZOS)
# ----------------------

img_width, img_height = resized_img.size

# 透明キャンバス作成
canvas = Image.new("RGBA", (CANVAS_WIDTH, CANVAS_HEIGHT), (0, 0, 0, 0))

for _ in range(NUM_IMAGES):
    x = random.randint(0, CANVAS_WIDTH - img_width)
    y = random.randint(0, CANVAS_HEIGHT - img_height)
    
    # リサイズした画像（resized_img）を貼り付ける
    canvas.paste(resized_img, (x, y), resized_img)

canvas.save("resized_placement.png")
canvas.show()