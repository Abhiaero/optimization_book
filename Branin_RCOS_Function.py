import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


# Define the Branin RCOS Function
def branin_function(x, y):
    # Standard coefficients
    a = 1.0
    b = 5.1 / (4.0 * np.pi ** 2)
    c = 5.0 / np.pi
    r = 6.0
    s = 10.0
    t = 1.0 / (8.0 * np.pi)

    term1 = a * (y - b * x ** 2 + c * x - r) ** 2
    term2 = s * (1 - t) * np.cos(x)
    return term1 + term2 + s


# Generate grid based on standard domain: x in [-5, 10], y in [0, 15]
x_vals = np.linspace(-5, 10, 400)
y_vals = np.linspace(0, 15, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = branin_function(X, Y)

# Global Minima: f(x*) ≈ 0.397887
# Three global minima exist at:
# (-pi, 12.275), (pi, 2.275), and (9.42478, 2.475)
optima = [
    (-np.pi, 12.275),
    (np.pi, 2.275),
    (9.42478, 2.475)
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
ax1.set_xticks(np.linspace(-5, 10, 4))
ax1.set_yticks(np.linspace(0, 15, 4))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 5))

ax1.tick_params(axis='both', labelsize=12)

# Mark the global minima
for i, (ox, oy) in enumerate(optima):
    oz = branin_function(ox, oy)
    label = f'Global Min' if i == 0 else ""
    ax1.scatter(ox, oy, oz, color='red', s=100, edgecolors='white', label=label, zorder=10)

ax1.legend(loc='upper right', fontsize=12)
ax1.view_init(elev=40, azim=-120)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# --- 2. Contour Plot ---
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Z, levels=25, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X, Y, Z, levels=25, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solutions
for ox, oy in optima:
    ax2.scatter(ox, oy, color='red', s=100, edgecolors='white')

# Simple trick to add one label for multiple points in legend
ax2.scatter([], [], color='red', s=100, edgecolors='white', label='Global Minima')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_xticks(np.linspace(-5, 10, 4))
ax2.set_yticks(np.linspace(0, 15, 4))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot", fontsize=16, pad=15)

plt.tight_layout()
plt.show()