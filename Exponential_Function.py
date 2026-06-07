import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the Exponential Function
def exponential_function(x1, x2):
    return -np.exp(-0.5 * (x1**2 + x2**2))

# Generate grid (Domain for Exponential is typically [-1, 1])
x1_vals = np.linspace(-5, 5, 200)
x2_vals = np.linspace(-5, 5, 200)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Z = exponential_function(X1, X2)

# Optimal solution
optimal_x1, optimal_x2 = 0.0, 0.0
optimal_z = exponential_function(optimal_x1, optimal_x2)

# Create figure
fig = plt.figure(figsize=(16, 8))

# 3D Surface plot
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(
    X1, X2, Z, cmap=cm.plasma, edgecolor='k', linewidth=0.2, antialiased=True, alpha=0.8
)

# Adjust axes labels
ax1.set_xlabel("$X_1$", labelpad=15, fontsize=16)
ax1.set_ylabel("$X_2$", labelpad=15, fontsize=16)
ax1.set_zlabel("$f(X_1, X_2)$", labelpad=15, fontsize=16)

# Explicitly set fewer ticks to increase the gap and reduce clutter
ax1.set_xticks(np.linspace(-5, 5, 5))
ax1.set_yticks(np.linspace(-5, 5, 5))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 4)) # Reduced to 4 ticks for the Z-axis

ax1.tick_params(axis='both', labelsize=12)

# Optimal solution point
ax1.scatter(optimal_x1, optimal_x2, optimal_z, color='red', s=100, label=f'Optimal Value = {optimal_z:.4f}')
ax1.legend(loc='upper right', fontsize=12)
ax1.view_init(elev=30, azim=120)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# Contour Plot
ax2 = fig.add_subplot(122)
# Reduced levels to 15 to widen the gaps between contour lines
contour = ax2.contourf(X1, X2, Z, levels=15, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X1, X2, Z, levels=15, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solution
ax2.scatter(optimal_x1, optimal_x2, color='red', s=100, label='Optimal Solution = ($0$, $0$)')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_xticks(np.linspace(-5, 5, 5))
ax2.set_yticks(np.linspace(-5, 5, 5))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot", fontsize=16, pad=15)

plt.tight_layout()
plt.show()