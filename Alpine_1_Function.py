import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the Alpine 1 Function
def alpine_1_function(x1, x2):
    return np.abs(x1 * np.sin(x1) + 0.1 * x1) + np.abs(x2 * np.sin(x2) + 0.1 * x2)

# Generate grid
x1_vals = np.linspace(0, 10, 200)
x2_vals = np.linspace(0, 10, 200)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Z = alpine_1_function(X1, X2)

# Optimal solution
optimal_x1, optimal_x2 = 0, 0
optimal_z = alpine_1_function(optimal_x1, optimal_x2)

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
ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)
ax1.tick_params(axis='z', labelsize=12)

# Z-axis scaling
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 5))

# Optimal solution point
ax1.scatter(optimal_x1, optimal_x2, optimal_z, color='red', s=100, label=f'Optimal Value = {optimal_z:.4f}')
ax1.legend(loc='upper right', fontsize=12)
ax1.view_init(elev=30, azim=120)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# Contour Plot
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X1, X2, Z, levels=30, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X1, X2, Z, levels=30, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solution
ax2.scatter(optimal_x1, optimal_x2, color='red', s=100, label=f'Optimal Solution = ($0$, $0$)')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot", fontsize=16, pad=15)

plt.tight_layout()
plt.show()
