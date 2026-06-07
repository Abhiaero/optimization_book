import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


# Define the Keane Function
def keane_function(x, y):
    # Numerator: (sin^4(x) + cos^4(y) - 2*sin^2(x)*cos^2(y))
    # We use the absolute value as per the standard test suite definition
    num = np.abs(np.sin(x) ** 4 + np.cos(y) ** 4 - 2 * np.sin(x) ** 2 * np.cos(y) ** 2)
    den = np.sqrt(x ** 2 + 2 * y ** 2)

    # Handle the origin to avoid division by zero
    res = np.zeros_like(den)
    mask = den != 0
    res[mask] = num[mask] / den[mask]
    return res


# Generate grid
# Domain: x1, x2 in [0, 10]
x_vals = np.linspace(0, 10, 500)
y_vals = np.linspace(0, 10, 500)
X, Y = np.meshgrid(x_vals, y_vals)
Z = keane_function(X, Y)

# Known Global Optima (Peaks) for the Keane Function
# These are the symmetric peaks near the axes
optima = [(1.3932, 0.0), (0.0, 1.3932)]

# Create figure
fig = plt.figure(figsize=(16, 8))

# --- 1. 3D Surface Plot ---
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(
    X, Y, Z, cmap=cm.plasma, edgecolor='none', antialiased=True, alpha=0.85
)

# Mark the optima in 3D
for i, (ox, oy) in enumerate(optima):
    oz = keane_function(np.array([ox]), np.array([oy]))[0]
    label = "Global Optima" if i == 0 else ""
    ax1.scatter(ox, oy, oz, color='red', s=100, edgecolors='white', depthshade=False, label=label, zorder=10)

# Adjust axes labels
ax1.set_xlabel("$X_1$", labelpad=15, fontsize=14)
ax1.set_ylabel("$X_2$", labelpad=15, fontsize=14)
ax1.set_zlabel("$f(X_1, X_2)$", labelpad=15, fontsize=14)
ax1.set_title("3D Surface with Global Optima", fontsize=16, pad=20)
ax1.legend()

# View angle to see the spikes clearly
ax1.view_init(elev=30, azim=35)

# Add color bar
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# --- 2. Contour Plot ---
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Z, levels=50, cmap=cm.plasma)
contour_lines = ax2.contour(X, Y, Z, levels=15, colors='black', linewidths=0.5, alpha=0.3)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark the optima in 2D
for ox, oy in optima:
    ax2.scatter(ox, oy, color='red', s=120, edgecolors='white', marker='*', zorder=5)

# Add a proxy for the legend
ax2.scatter([], [], color='red', marker='*', s=120, label='Global Optima')
ax2.legend(loc='upper right')

# Axes labels and styling
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_title("Contour Plot", fontsize=16, pad=15)
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()