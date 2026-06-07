import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the Mishra Bird Function
def mishra_bird_function(x, y):
    term1 = np.sin(y) * np.exp((1 - np.cos(x))**2)
    term2 = np.cos(x) * np.exp((1 - np.sin(y))**2)
    term3 = (x - y)**2
    return term1 + term2 + term3

# Generate grid (Domain typically used to show global minima)
x_vals = np.linspace(-10, 0, 400)
y_vals = np.linspace(-6, 0, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = mishra_bird_function(X, Y)

# Global Minima (There are two: approx (-3.13, -1.58) and (-2.82, -9.52))
# We will mark the one visible in this range:
optimal_x, optimal_y = -3.1302, -1.5821
optimal_z = mishra_bird_function(optimal_x, optimal_y)

# Create figure
fig = plt.figure(figsize=(16, 8))

# 3D Surface plot
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(
    X, Y, Z, cmap=cm.plasma, edgecolor='k', linewidth=0.05, antialiased=True, alpha=0.8
)

# Adjust axes labels
ax1.set_xlabel("$X$", labelpad=15, fontsize=16)
ax1.set_ylabel("$Y$", labelpad=15, fontsize=16)
ax1.set_zlabel("$f(X, Y)$", labelpad=15, fontsize=16)

# Explicitly set fewer ticks to increase the gap
ax1.set_xticks(np.linspace(-10, 0, 5))
ax1.set_yticks(np.linspace(-6, 0, 4))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 4))

ax1.tick_params(axis='both', labelsize=12)

# Optimal solution point (marking one of the global minima)
ax1.scatter(optimal_x, optimal_y, optimal_z, color='red', s=100, label=f'Global Min $\\approx$ {optimal_z:.2f}')
ax1.legend(loc='upper right', fontsize=12)
ax1.view_init(elev=40, azim=-120)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# Contour Plot
ax2 = fig.add_subplot(122)
# Using 15 levels for clean spacing
contour = ax2.contourf(X, Y, Z, levels=15, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X, Y, Z, levels=15, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solution
ax2.scatter(optimal_x, optimal_y, color='red', s=100, label='Global Minimum')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X$", fontsize=14)
ax2.set_ylabel("$Y$", fontsize=14)
ax2.set_xticks(np.linspace(-10, 0, 5))
ax2.set_yticks(np.linspace(-6, 0, 4))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot (Bird's Eye View)", fontsize=16, pad=15)

plt.tight_layout()
plt.show()