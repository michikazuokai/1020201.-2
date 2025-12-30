import numpy as np
import matplotlib.pyplot as plt

def normal_pdf(x, mu, sigma):
    return (1.0 / (sigma * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((x - mu)/sigma)**2)

# 例：平均だけ変える（分散は同じ）
mus = [-4, 0, 4]
sigma = 1.0

x = np.linspace(-8, 8, 800)

plt.figure(figsize=(8, 4))
for mu in mus:
    y = normal_pdf(x, mu, sigma)
    plt.plot(x, y, label=f"µ={mu}, σ={sigma}")

plt.title("Normal distributions (same sigma, different mu)")
plt.xlabel("x")
plt.ylabel("density")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
