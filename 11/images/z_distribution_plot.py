import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib  # 日本語表示を可能にする
from pathlib import Path

script_path = Path(__file__)
script_dir = script_path.parent
script_stem = script_path.stem  # 拡張子なしのベース名（例: 'script'）
output_path = script_dir / f"{script_stem}.pgf"  # .pgfに変更

# 1. データの作成（TikZの 1.5*exp(-x^2) を再現）
x_curve = np.linspace(-2.1, 2.1, 100)
y_curve = 1.5 * np.exp(-(x_curve**2))

# 2. グラフのサイズ設定（スライドのカラムに合わせるため小さめに）
fig, ax = plt.subplots(figsize=(4, 2.5))

# 3. 曲線の描画（smooth, thick）
ax.plot(x_curve, y_curve, color='black', linewidth=2)

# 4. 横軸の描画（矢印付き）
ax.annotate('', xy=(2.3, 0), xytext=(-2.3, 0),
            arrowprops=dict(arrowstyle="->", color='black', lw=1))
ax.text(2.3, -0.1, "$Z$", fontsize=10, ha='right', va='top')

# 5. 中心線（dashed）と 0 のラベル
ax.plot([0, 0], [0, 1.5], color='black', linestyle='--', linewidth=1)
ax.text(0, -0.1, "0", ha='center', va='top', fontsize=10)

# 6. 指定位置 Z を示す下向き矢印（TikZの -1.6 の位置）
ax.annotate('', xy=(-1.6, 0), xytext=(-1.6, 0.25),
            arrowprops=dict(arrowstyle="->", color='black', lw=1.5))
ax.text(-1.6, -0.1, "$Z$", ha='center', va='top', fontsize=10)

# 7. 上部の説明ラベル（改行対応）
ax.text(0, 1.75, "分布の上の\n位置", ha='center', va='bottom', fontsize=9)

# 8. 仕上げ：軸や枠線を消してTikZ風にする
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-0.4, 2.2)
ax.axis('off')

try:
    fig.savefig(output_path, format="pgf", bbox_inches="tight", pad_inches=0.02, transparent=True)
    print("saved:", output_path.exists(), output_path)
except Exception as e:
    print("SAVE ERROR:", e)
    raise