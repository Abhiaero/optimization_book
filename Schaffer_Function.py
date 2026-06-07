import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the Schaffer Function F6
def schaffer_f6_function(x, y):
    temp = x**2 + y**2
    numerator = np.sin(np.sqrt(temp))**2 - 0.5
    denominator = (1 + 0.001 * temp)**2
    return 0.5 + (numerator / denominator)

# Generate grid
# Standard domain: x1, x2 in [-100, 100]
# We use [-20, 20] here to better visualize the high-frequency central ripples
x_vals = np.linspace(-20, 20, 400)
y_vals = np.linspace(-20, 20, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = schaffer_f6_function(X, Y)

# Global Minimum: f(x*) = 0 at x* = (0, 0)
optimal_x, optimal_y = 0.0, 0.0
optimal_z = schaffer_f6_function(optimal_x, optimal_y)

# Create figure
fig = plt.figure(figsize=(16, 8))

# --- 1. 3D Surface Plot ---
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(
    X, Y, Z, cmap=cm.plasma, edgecolor='k', linewidth=0.01, antialiased=True, alpha=0.8
)

# Adjust axes labels
ax1.set_xlabel("$X_1$", labelpad=15, fontsize=16)
ax1.set_ylabel("$X_2$", labelpad=15, fontsize=16)
ax1.set_zlabel("$f(X_1, X_2)$", labelpad=15, fontsize=16)

# Set ticks
ax1.set_xticks(np.linspace(-20, 20, 5))
ax1.set_yticks(np.linspace(-20, 20, 5))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 5))

ax1.tick_params(axis='both', labelsize=12)

# Mark the global minimum
ax1.scatter(optimal_x, optimal_y, optimal_z, color='red', s=100, edgecolors='white',
            label=f'Global Min = {optimal_z:.1f}', zorder=10)
ax1.legend(loc='upper right', fontsize=12)

# Adjust view angle to show the concentric circular ripples
ax1.view_init(elev=40, azim=-45)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# --- 2. Contour Plot ---
ax2 = fig.add_subplot(122)
# 30 levels capture the concentric circular traps effectively
contour = ax2.contourf(X, Y, Z, levels=30, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X, Y, Z, levels=30, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solution
ax2.scatter(optimal_x, optimal_y, color='red', s=100, edgecolors='white', label='Global Minimum')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_xticks(np.linspace(-20, 20, 5))
ax2.set_yticks(np.linspace(-20, 20, 5))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot", fontsize=16, pad=15)

plt.tight_layout()
plt.show()