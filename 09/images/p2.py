from PIL import Image
import random
import os

# --- 設定 ---
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200
SCALE = 0.2  # 全体の縮小率（30%）

# 配置したい画像パスと、それぞれの配置個数を指定
IMAGES_CONFIG = [
    {"path": "/Volumes/NBPlan/TTC/授業資料/2025年度/1020201.アルゴリズム２/09/p3.png", "count": 2},
    {"path": "/Volumes/NBPlan/TTC/授業資料/2025年度/1020201.アルゴリズム２/09/p1.png", "count": 18},
]

# 1. 透明なキャンバスを作成 (RGBAモード, 背景は完全に透明)
canvas = Image.new("RGBA", (CANVAS_WIDTH, CANVAS_HEIGHT), (0, 0, 0, 0))

random.seed()

# 各画像の設定に基づいてループ
for config in IMAGES_CONFIG:
    file_path = config["path"]
    count = config["count"]
    
    if not os.path.exists(file_path):
        print(f"警告: ファイルが見つかりません: {file_path}")
        continue

    # 2. 画像の読み込みとリサイズ
    img = Image.open(file_path).convert("RGBA")
    new_size = (int(img.width * SCALE), int(img.height * SCALE))
    resized_img = img.resize(new_size, Image.LANCZOS)
    
    w, h = resized_img.size
    
    # 3. 指定された個数分、ランダムに配置
    for _ in range(count):
        x = random.randint(0, CANVAS_WIDTH - w)
        y = random.randint(0, CANVAS_HEIGHT - h)
        
        # 貼り付け（第3引数にresized_imgを渡すことで透過を維持）
        canvas.paste(resized_img, (x, y), resized_img)

# 4. 保存
output_name = "random_arrangement.png"
canvas.save(output_name)
print(f"保存完了: {output_name}")

# 表示（確認用）
canvas.show()