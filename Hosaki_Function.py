import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the Hosaki Function
def hosaki_function(x, y):
    term1 = (1 - 8*x + 7*x**2 - (7/3)*x**3 + (1/4)*x**4)
    term2 = y**2 * np.exp(-y)
    return term1 * term2

# Generate grid
# Standard domain: x1 in [0, 5], x2 in [0, 5]
x_vals = np.linspace(0, 5, 400)
y_vals = np.linspace(0, 5, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = hosaki_function(X, Y)

# Global Minimum: f(x*) ≈ -2.3458 at x* ≈ (4, 2)
optimal_x, optimal_y = 4.0, 2.0
optimal_z = hosaki_function(optimal_x, optimal_y)

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
ax1.set_xticks(np.linspace(0, 5, 6))
ax1.set_yticks(np.linspace(0, 5, 6))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 5))

ax1.tick_params(axis='both', labelsize=12)

# Mark the global minimum
ax1.scatter(optimal_x, optimal_y, optimal_z, color='red', s=100, edgecolors='white',
            label=f'Global Min $\\approx$ {optimal_z:.4f}', zorder=10)
ax1.legend(loc='upper right', fontsize=12)

# Adjust view angle to highlight the global minimum basin
ax1.view_init(elev=30, azim=-135)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# --- 2. Contour Plot ---
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Z, levels=25, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X, Y, Z, levels=25, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solution
ax2.scatter(optimal_x, optimal_y, color='red', s=100, edgecolors='white', label='Global Minimum')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_xticks(np.linspace(0, 5, 6))
ax2.set_yticks(np.linspace(0, 5, 6))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot", fontsize=16, pad=15)

plt.tight_layout()
plt.show()