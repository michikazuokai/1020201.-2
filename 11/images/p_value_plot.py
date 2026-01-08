import matplotlib as mpl
mpl.use("pgf")
mpl.rcParams.update({
    "pgf.texsystem": "lualatex",
    "text.usetex": True,
    "pgf.rcfonts": False,
})

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

script_path = Path(__file__)
output_path = script_path.parent / f"{script_path.stem}.pgf"

x_curve = np.linspace(-2.2, 2.2, 100)
y_curve = 1.45 * np.exp(-(x_curve**2) / 1.2)

fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(x_curve, y_curve, color='black', linewidth=2)

x_right = np.linspace(1.5, 2.2, 50)
y_right = 1.45 * np.exp(-(x_right**2) / 1.2)
ax.fill_between(x_right, 0, y_right, color='gray', alpha=0.3)

x_left = np.linspace(-2.2, -1.5, 50)
y_left = 1.45 * np.exp(-(x_left**2) / 1.2)
ax.fill_between(x_left, 0, y_left, color='gray', alpha=0.3)

ax.annotate('', xy=(2.3, 0), xytext=(-2.3, 0),
            arrowprops=dict(arrowstyle="->", color='black', lw=1))
ax.text(2.3, -0.1, r"$t$", fontsize=12, ha='right')

ax.plot([0, 0], [0, 1.45], color='black', linestyle='--', linewidth=1)
ax.text(0, -0.2, "0", ha='center', fontsize=10)

ax.annotate('', xy=(1.5, 0), xytext=(1.5, 0.25),
            arrowprops=dict(arrowstyle="->", color='black', lw=1.5))
ax.text(1.5, -0.2, r"$t$", ha='center', fontsize=12)

ax.text(0, 1.75, r"外側の面積$\Rightarrow p$値", ha='center', fontsize=10)

ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-0.4, 2.0)
ax.axis('off')

# ★透明背景 + showより先に保存
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)
fig.savefig(output_path, transparent=True)

