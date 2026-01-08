import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib  # 日本語表示用
from pathlib import Path

script_path = Path(__file__)
script_dir = script_path.parent
script_stem = script_path.stem  # 拡張子なしのベース名（例: 'script'）
output_path = script_dir / f"{script_stem}.pgf"  # .pgfに変更

# 1. データの作成（TikZの 1.5*exp(-x^2) を再現）
x_curve = np.linspace(-2.1, 2.1, 100)
y_curve = 1.5 * np.exp(-(x_curve**2))

# 2. グラフの土台作成
fig, ax = plt.subplots(figsize=(6, 4))

# 3. 曲線の描画（smooth, thick）
ax.plot(x_curve, y_curve, color='black', linewidth=2)

# 4. 横軸の描画（矢印付き）
ax.annotate('', xy=(2.3, 0), xytext=(-2.3, 0),
            arrowprops=dict(arrowstyle="->", color='black', lw=1))
ax.text(2.3, -0.1, "位置", fontsize=9, ha='right')

# 5. 中心線（dashed）と 0 のラベル
ax.plot([0, 0], [0, 1.5], color='black', linestyle='--', linewidth=1)
ax.text(0, -0.2, "0", ha='center', fontsize=10)

# 6. 位置 t を示す下向き矢印（thick, ->）
# TikZの (1.6, 0.15) -- (1.6, 0) を再現
ax.annotate('', xy=(1.6, 0), xytext=(1.6, 0.25),
            arrowprops=dict(arrowstyle="->", color='black', lw=1.5))
ax.text(1.6, -0.2, "$t$", ha='center', fontsize=12)

# 7. 上部の説明ラベル（align=center）
ax.text(0, 1.75, "分布の上の位置", ha='center', fontsize=10, linespacing=1.5)

# 8. 仕上げ（枠線を消してTikZ風にする）
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-0.4, 2.0)
ax.axis('off')

# ★透明背景 + showより先に保存
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)
fig.savefig(output_path, transparent=True)
