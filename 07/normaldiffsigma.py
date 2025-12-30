import numpy as np
import matplotlib.pyplot as plt

def normal_pdf(x, mu, sigma):
    return (1.0 / (sigma * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((x - mu)/sigma)**2)

# 例：標準偏差だけ変える（平均は同じ）
mu = 0.0
sigmas = [0.5, 1.0, 2.0]

x = np.linspace(-8, 8, 800)

plt.figure(figsize=(8, 4))
for sigma in sigmas:
    y = normal_pdf(x, mu, sigma)
    plt.plot(x, y, label=f"µ={mu}, σ={sigma}")

#plt.title("Normal distributions (same mu, different sigma)")
#plt.xlabel("x")
#plt.ylabel("density")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
