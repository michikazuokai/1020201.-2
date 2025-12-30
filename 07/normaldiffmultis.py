import numpy as np
import matplotlib.pyplot as plt

def normal_pdf(x, mu=0.0, sigma=1.0):
    return (1.0 / (sigma * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((x - mu)/sigma)**2)

mu, sigma = 0.0, 1.0
x = np.linspace(-4.5, 4.5, 1200)
y = normal_pdf(x, mu, sigma)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y, lw=2)

# 塗り（内側ほど濃く）
def fill_range(a, b, alpha):
    m = (x >= a) & (x <= b)
    ax.fill_between(x[m], 0, y[m], alpha=alpha)

fill_range(mu-3*sigma, mu+3*sigma, alpha=0.10)
fill_range(mu-2*sigma, mu+2*sigma, alpha=0.16)
fill_range(mu-1*sigma, mu+1*sigma, alpha=0.22)

# ax.set_title("正規分布の経験則（68–95–99.7ルール）  ※μ=0, σ=1")
# ax.set_xlabel("x")
# ax.set_ylabel("density")
ax.set_xlim(-4.2, 4.2)
ax.set_ylim(0, 0.45)
ax.grid(True)

# x軸目盛り
ticks = [-3, -2, -1, 0, 1, 2, 3]
ticklabels = [r"$-3\sigma$", r"$-2\sigma$", r"$-1\sigma$", r"$\mu$",
              r"$+1\sigma$", r"$+2\sigma$", r"$+3\sigma$"]
ax.set_xticks(ticks)
ax.set_xticklabels(ticklabels)

# --- 端点が「曲線上にぴったり合う」両矢印 ---
def range_arrow_on_curve(k, pct_text):
    a = mu - k*sigma
    b = mu + k*sigma

    # 左右対称なので端点のyは同じ（曲線上の値）
    y_end = normal_pdf(b, mu, sigma)

    # 矢印（水平）※両端が曲線上 y_end に一致
    ax.annotate(
        "", xy=(a, y_end), xytext=(b, y_end),
        arrowprops=dict(arrowstyle="<->", lw=1.6),
        zorder=5
    )

    # 表示（矢印の上）
    ax.text((a+b)/2, y_end + 0.012, pct_text, ha="center", va="bottom")

    # 補助：±kσ を矢印の下に出す（不要なら消してOK）
    # ax.text((a+b)/2, y_end - 0.010, rf"$\pm {k}\sigma$", ha="center", va="top")

range_arrow_on_curve(1, "68%")
range_arrow_on_curve(2, "95%")
range_arrow_on_curve(3, "99.7%")

plt.tight_layout()
plt.show()
