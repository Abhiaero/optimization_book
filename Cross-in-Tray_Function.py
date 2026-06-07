import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


# Define the Cross-in-Tray Function
def cross_in_tray_function(x, y):
    # The term inside the exponent creates the cross-like ridges
    exponent_term = np.abs(100 - (np.sqrt(x ** 2 + y ** 2) / np.pi))

    # Outer term with absolute value sine modulations
    inner_term = np.abs(np.sin(x) * np.sin(y) * np.exp(exponent_term)) + 1

    return -0.0001 * (inner_term) ** 0.1


# Generate grid
# Standard domain: x1, x2 in [-10, 10]
x_vals = np.linspace(-10, 10, 400)
y_vals = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = cross_in_tray_function(X, Y)

# Global Minima: f(x*) ≈ -2.06261
# Four identical global minima exist at approx:
# (1.34941, 1.34941), (1.34941, -1.34941), (-1.34941, 1.34941), (-1.34941, -1.34941)
optima = [
    (1.34941, 1.34941),
    (1.34941, -1.34941),
    (-1.34941, 1.34941),
    (-1.34941, -1.34941)
]

# Create figure
fig = plt.figure(figsize=(16, 8))

# --- 1. 3D Surface Plot ---
ax1 = fig.add_subplot(121, projection='3d')
# Using a low linewidth for edgecolors to keep the sharp ridges clean
surf = ax1.plot_surface(
    X, Y, Z, cmap=cm.plasma, edgecolor='k', linewidth=0.01, antialiased=True, alpha=0.8
)

# Adjust axes labels
ax1.set_xlabel("$X_1$", labelpad=15, fontsize=16)
ax1.set_ylabel("$X_2$", labelpad=15, fontsize=16)
ax1.set_zlabel("$f(X_1, X_2)$", labelpad=15, fontsize=16)

# Set ticks
ax1.set_xticks(np.linspace(-10, 10, 5))
ax1.set_yticks(np.linspace(-10, 10, 5))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 5))

ax1.tick_params(axis='both', labelsize=12)

# Mark the global minima
for i, (ox, oy) in enumerate(optima):
    oz = cross_in_tray_function(ox, oy)
    label = 'Global Min' if i == 0 else ""
    ax1.scatter(ox, oy, oz, color='red', s=80, edgecolors='white', label=label, zorder=10)

ax1.legend(loc='upper right', fontsize=12)
ax1.view_init(elev=35, azim=45)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# --- 2. Contour Plot ---
ax2 = fig.add_subplot(122)
# Using 30 levels to highlight the sharp "X" shape
contour = ax2.contourf(X, Y, Z, levels=30, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X, Y, Z, levels=30, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solutions
for ox, oy in optima:
    ax2.scatter(ox, oy, color='red', s=80, edgecolors='white', zorder=5)

# Add single legend entry for optima
ax2.scatter([], [], color='red', s=80, edgecolors='white', label='Global Minima')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_xticks(np.linspace(-10, 10, 5))
ax2.set_yticks(np.linspace(-10, 10, 5))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot", fontsize=16, pad=15)

plt.tight_layout()
plt.show()