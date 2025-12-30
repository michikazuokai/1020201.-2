import numpy as np
import matplotlib.pyplot as plt
from math import erf, sqrt

def normal_cdf(x, mu=0.0, sigma=1.0):
    z = (x - mu) / (sigma * sqrt(2))
    return 0.5 * (1 + erf(z))

mu = 0.0
sigma = 1.0
x0 = 1.0

x = np.linspace(mu - 4.5*sigma, mu + 4.5*sigma, 1200)
F = np.array([normal_cdf(xi, mu, sigma) for xi in x])
Fx0 = normal_cdf(x0, mu, sigma)

fig, ax = plt.subplots(figsize=(9, 4.8))
ax.plot(x, F, lw=2)

ax.axvline(x0, linestyle="--", lw=1.5)
ax.axhline(Fx0, linestyle="--", lw=1.5)
ax.plot([x0], [Fx0], marker="o")

ax.text(0.02, 0.92,
        f"X ~ N({mu}, {sigma})\n"
        f"F(x) = P(X ≤ x)\n"
        f"x0 = {x0}  →  F(x0) ≈ {Fx0:.3f} (約{Fx0*100:.1f}%)",
        transform=ax.transAxes, va="top")

ax.set_title("Normal CDF (cumulative probability)")
ax.set_xlabel("x")
ax.set_ylabel("F(x) = P(X ≤ x)")
ax.set_ylim(-0.02, 1.02)
ax.grid(True)

plt.tight_layout()
plt.show()
