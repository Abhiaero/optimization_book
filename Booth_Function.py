import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def booth_function(x1, x2):
    return (x1 + 2 * x2 - 7)**2 + (2 * x1 + x2 - 5)**2

# Generate grid
x1_vals = np.linspace(-10, 10, 200)
x2_vals = np.linspace(-10, 10, 200)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Z = booth_function(X1, X2)

# Optimal solution
optimal_x1, optimal_x2 = 1, 3
optimal_z = booth_function(optimal_x1, optimal_x2)

# Create figure
fig = plt.figure(figsize=(16, 8))

# 3D Surface plot
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(
    X1, X2, Z, cmap=cm.plasma, edgecolor='k', linewidth=0.2, antialiased=True, alpha=0.6
)  # Reduced opacity with alpha
ax1.set_xlabel("$X_1$", labelpad=15, fontsize=16)
ax1.set_ylabel("$X_2$", labelpad=15, fontsize=16)
ax1.set_zlabel("$f(X_1, X_2)$", labelpad=15, fontsize=16)
ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)
ax1.tick_params(axis='z', labelsize=12)

# Set ticks with intervals of 5 units
ax1.set_xticks(np.arange(-10, 11, 5))
ax1.set_yticks(np.arange(-10, 11, 5))
ax1.set_zticks(np.arange(0, 2500, 500))
ax1.view_init(elev=30, azim=120)  # Adjust the view angle

# Mark optimal solution functional value on the surface
ax1.scatter(optimal_x1, optimal_x2, optimal_z, color='red', s=100, label='Optimal Functional Value')
ax1.legend(loc='upper right', fontsize=14)

# Increase axis lines and ticks
ax1.xaxis.line.set_linewidth(1.75)
ax1.yaxis.line.set_linewidth(1.75)
ax1.zaxis.line.set_linewidth(1.75)
ax1.tick_params(axis='x', width=2, length=8)
ax1.tick_params(axis='y', width=2, length=8)
ax1.tick_params(axis='z', width=2, length=8)

# Color bar for 3D plot
mappable = cm.ScalarMappable(cmap=cm.plasma)
mappable.set_array(Z)
fig.colorbar(mappable, ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# Enhanced Contour Plot
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X1, X2, Z, levels=30, cmap=cm.plasma, alpha=0.9)
contour_lines = ax2.contour(X1, X2, Z, levels=30, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solution in contour plot
ax2.scatter(optimal_x1, optimal_x2, color='red', s=100, label='Optimal Solution')
ax2.legend(loc='upper right', fontsize=14)

# Enhance axes appearance for contour
for spine in ax2.spines.values():
    spine.set_linewidth(1.75)
    spine.set_edgecolor('black')

# Add grid and ticks
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.tick_params(axis='x', width=2, length=8, labelsize=12)
ax2.tick_params(axis='y', width=2, length=8, labelsize=12)
ax2.set_xlabel("$X_1$", fontsize=16)
ax2.set_ylabel("$X_2$", fontsize=16)

ax2.set_title("Contour Plot", fontsize=18, pad=15)

plt.tight_layout()
plt.show()
