import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the Egg Holder Function
def eggholder_function(x, y):
    term1 = -(y + 47) * np.sin(np.sqrt(np.abs(x/2 + (y + 47))))
    term2 = -x * np.sin(np.sqrt(np.abs(x - (y + 47))))
    return term1 + term2

# Generate grid
# Standard domain: x1, x2 in [-512, 512]
x_vals = np.linspace(-512, 512, 400)
y_vals = np.linspace(-512, 512, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = eggholder_function(X, Y)

# Global Minimum: f(x*) = -959.6407 at x* = (512, 404.2319)
optimal_x, optimal_y = 512.0, 404.2319
optimal_z = eggholder_function(optimal_x, optimal_y)

# Create figure
fig = plt.figure(figsize=(16, 8))

# --- 1. 3D Surface Plot ---
ax1 = fig.add_subplot(121, projection='3d')
# Using a very small linewidth for edgecolors to keep the high-frequency peaks clean
surf = ax1.plot_surface(
    X, Y, Z, cmap=cm.plasma, edgecolor='k', linewidth=0.01, antialiased=True, alpha=0.8
)

# Adjust axes labels
ax1.set_xlabel("$X_1$", labelpad=15, fontsize=16)
ax1.set_ylabel("$X_2$", labelpad=15, fontsize=16)
ax1.set_zlabel("$f(X_1, X_2)$", labelpad=15, fontsize=16)

# Set ticks
ax1.set_xticks(np.linspace(-512, 512, 5))
ax1.set_yticks(np.linspace(-512, 512, 5))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 5))

ax1.tick_params(axis='both', labelsize=12)

# Mark the global minimum
ax1.scatter(optimal_x, optimal_y, optimal_z, color='red', s=100, edgecolors='white',
            label=f'Global Min $\\approx$ {optimal_z:.2f}', zorder=10)
ax1.legend(loc='upper right', fontsize=12)

# Adjust view angle to show the multi-modal nature
ax1.view_init(elev=45, azim=-120)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# --- 2. Contour Plot ---
ax2 = fig.add_subplot(122)
# Using 40 levels to clearly define the numerous local basins
contour = ax2.contourf(X, Y, Z, levels=40, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X, Y, Z, levels=40, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solution
ax2.scatter(optimal_x, optimal_y, color='red', s=100, edgecolors='white', label='Global Minimum')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_xticks(np.linspace(-512, 512, 5))
ax2.set_yticks(np.linspace(-512, 512, 5))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot", fontsize=16, pad=15)

plt.tight_layout()
plt.show()