import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import LogNorm

# Define the Goldstein-Price Function
def goldstein_price_function(x, y):
    term1 = 1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)
    term2 = 30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2)
    return term1 * term2

# Generate grid
# Standard domain: x1, x2 in [-2, 2]
x_vals = np.linspace(-2, 2, 400)
y_vals = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = goldstein_price_function(X, Y)

# Global Minimum: f(x*) = 3 at x* = (0, -1)
optimal_x, optimal_y = 0.0, -1.0
optimal_z = goldstein_price_function(optimal_x, optimal_y)

# Calculate limits for Logarithmic normalization to avoid the "Invalid vmin/vmax" error
z_min, z_max = Z.min(), Z.max()
# Ensure z_min is strictly positive for LogNorm
z_min = max(z_min, 1e-10)
my_norm = LogNorm(vmin=z_min, vmax=z_max)

# Create figure
fig = plt.figure(figsize=(16, 8))

# --- 1. 3D Surface Plot ---
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(
    X, Y, Z, cmap=cm.plasma, norm=my_norm, edgecolor='k',
    linewidth=0.01, antialiased=True, alpha=0.8
)

# Adjust axes labels
ax1.set_xlabel("$X_1$", labelpad=15, fontsize=16)
ax1.set_ylabel("$X_2$", labelpad=15, fontsize=16)
ax1.set_zlabel("$f(X_1, X_2)$", labelpad=15, fontsize=16)

# Set ticks
ax1.set_xticks(np.linspace(-2, 2, 5))
ax1.set_yticks(np.linspace(-2, 2, 5))
ax1.tick_params(axis='both', labelsize=12)

# Mark the global minimum
ax1.scatter(optimal_x, optimal_y, optimal_z, color='red', s=100, edgecolors='white',
            label=f'Global Min = {optimal_z:.1f}', zorder=10)
ax1.legend(loc='upper right', fontsize=12)

# Adjust view angle
ax1.view_init(elev=30, azim=45)

# Add color bar with explicit ScalarMappable mapping
fig.colorbar(cm.ScalarMappable(norm=my_norm, cmap=cm.plasma),
             ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# --- 2. Contour Plot ---
ax2 = fig.add_subplot(122)
# Using Logarithmic levels to show detail across the massive range of values
levels = np.logspace(np.log10(z_min), np.log10(z_max), 20)

contour = ax2.contourf(X, Y, Z, levels=levels, norm=my_norm, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X, Y, Z, levels=levels, norm=my_norm, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solution
ax2.scatter(optimal_x, optimal_y, color='red', s=100, edgecolors='white', label='Global Minimum')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_xticks(np.linspace(-2, 2, 5))
ax2.set_yticks(np.linspace(-2, 2, 5))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot", fontsize=16, pad=15)

plt.tight_layout()
plt.show()