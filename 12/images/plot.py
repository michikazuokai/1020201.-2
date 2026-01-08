import matplotlib.pyplot as plt
import japanize_matplotlib  # 日本語表示用
from pathlib import Path

script_path = Path(__file__)
script_dir = script_path.parent
script_stem = script_path.stem  # 拡張子なしのベース名（例: 'script'）

output_path = script_dir / f"{script_stem}.pgf"  # .pgfに変更



# 1. グラフのサイズ設定（TikZの[x=1.1cm, y=1.0cm]に近い比率に調整）
plt.figure(figsize=(5, 4))

# 2. データの準備（TikZコード内の座標をそのまま使用）
points = [
    (0.5, 0.8), (0.7, 0.7), (0.9, 1.1), (1.1, 1.0), (1.3, 1.2),
    (1.5, 1.4), (1.7, 1.3), (1.9, 1.7), (2.1, 1.6), (2.3, 1.9)
]
x_coords, y_coords = zip(*points)

# 3. 散布図（点）の描画
plt.scatter(x_coords, y_coords, color='black', s=20) # sは点のサイズ

# 4. 回帰直線の描画
# TikZの (0.4,0.6) -- (2.6,2.1) を再現
plt.plot([0.4, 2.6], [0.6, 2.1], color='black', linewidth=1.5)
plt.text(1.5, 2.25, "回帰直線\n（中心の傾向）", fontsize=12, ha='center')

# 5. 予測用の補助線（破線）と予測値 y-hat
plt.vlines(2.0, 0, 1.65, colors='black', linestyles='dashed', linewidth=1)
plt.scatter(2.0, 1.65, color='black', s=25) # 予測値の点
plt.text(2.1, 1.85, r"$\hat{y}$", fontsize=12)

# 6. 軸の設定とラベル
plt.xlim(0, 3.0)
plt.ylim(0, 2.6)
plt.xlabel("$x$（ハンバーガー）", fontsize=10)
plt.ylabel("$y$（ポテト）", fontsize=10)

# 軸の矢印を擬似的に表現（Matplotlibは通常、枠で囲む形式）
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 7. 保存と表示
# LaTeXで使う場合は下の行のコメントアウトを外します
# plt.savefig("hamburger_plot.pgf") 

# print("グラフを表示します...")
# plt.show()

# .pgf 形式で保存（TikZと同様に LaTeX で読み込めます）
plt.savefig(output_path)