import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the Six-Hump Camel Function
def six_hump_camel_function(x, y):
    term1 = (4 - 2.1 * x**2 + (x**4 / 3)) * x**2
    term2 = x * y
    term3 = (-4 + 4 * y**2) * y**2
    return term1 + term2 + term3

# Generate grid
# Standard domain for visualization: x in [-2, 2], y in [-1, 1]
x_vals = np.linspace(-2, 2, 400)
y_vals = np.linspace(-1, 1, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = six_hump_camel_function(X, Y)

# Global Minima: f(x*) = -1.0316
# Two global minima exist at: (0.0898, -0.7126) and (-0.0898, 0.7126)
optima = [
    (0.0898, -0.7126),
    (-0.0898, 0.7126)
]

# Create figure
fig = plt.figure(figsize=(16, 8))

# --- 1. 3D Surface Plot ---
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(
    X, Y, Z, cmap=cm.plasma, edgecolor='k', linewidth=0.05, antialiased=True, alpha=0.8
)

# Adjust axes labels
ax1.set_xlabel("$X_1$", labelpad=15, fontsize=16)
ax1.set_ylabel("$X_2$", labelpad=15, fontsize=16)
ax1.set_zlabel("$f(X_1, X_2)$", labelpad=15, fontsize=16)

# Set ticks
ax1.set_xticks(np.linspace(-2, 2, 5))
ax1.set_yticks(np.linspace(-1, 1, 5))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 5))

ax1.tick_params(axis='both', labelsize=12)

# Mark the global minima
for i, (ox, oy) in enumerate(optima):
    oz = six_hump_camel_function(ox, oy)
    label = 'Global Min' if i == 0 else ""
    ax1.scatter(ox, oy, oz, color='red', s=100, edgecolors='white', label=label, zorder=10)

ax1.legend(loc='upper right', fontsize=12)
ax1.view_init(elev=35, azim=-120)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# --- 2. Contour Plot ---
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Z, levels=20, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X, Y, Z, levels=20, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solutions
for ox, oy in optima:
    ax2.scatter(ox, oy, color='red', s=100, edgecolors='white', zorder=5)

# Add single legend entry for optima
ax2.scatter([], [], color='red', s=100, edgecolors='white', label='Global Minima')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_xticks(np.linspace(-2, 2, 5))
ax2.set_yticks(np.linspace(-1, 1, 5))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot", fontsize=16, pad=15)

plt.tight_layout()
plt.show()