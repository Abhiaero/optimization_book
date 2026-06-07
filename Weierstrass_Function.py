import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


# Define the Weierstrass Function
def weierstrass_function(x1, x2, a=0.5, b=3, k_max=20):
    def inner_sum(x):
        res = 0
        for k in range(k_max + 1):
            res += (a ** k) * np.cos(2 * np.pi * (b ** k) * (x + 0.5))
        return res

    # Constant term to shift global minimum to zero
    constant = 0
    for k in range(k_max + 1):
        constant += (a ** k) * np.cos(np.pi * (b ** k))

    # f(x) for n=2
    return (inner_sum(x1) + inner_sum(x2)) - 2 * constant


# Generate grid (Standard domain for Weierstrass is [-0.5, 0.5])
x1_vals = np.linspace(-0.5, 0.5, 400)
x2_vals = np.linspace(-0.5, 0.5, 400)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Z = weierstrass_function(X1, X2)

# Optimal solution
optimal_x1, optimal_x2 = 0.0, 0.0
optimal_z = weierstrass_function(optimal_x1, optimal_x2)

# Create figure
fig = plt.figure(figsize=(16, 8))

# 3D Surface plot
ax1 = fig.add_subplot(121, projection='3d')
# Using a slightly smaller linewidth to emphasize the fractal peaks
surf = ax1.plot_surface(
    X1, X2, Z, cmap=cm.plasma, edgecolor='k', linewidth=0.05, antialiased=True, alpha=0.8
)

# Adjust axes labels
ax1.set_xlabel("$X_1$", labelpad=15, fontsize=16)
ax1.set_ylabel("$X_2$", labelpad=15, fontsize=16)
ax1.set_zlabel("$f(X_1, X_2)$", labelpad=15, fontsize=16)

# Explicitly set fewer ticks to increase the gap and reduce clutter
ax1.set_xticks(np.linspace(-0.5, 0.5, 5))
ax1.set_yticks(np.linspace(-0.5, 0.5, 5))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 4))

ax1.tick_params(axis='both', labelsize=12)

# Optimal solution point
ax1.scatter(optimal_x1, optimal_x2, optimal_z, color='red', s=100, label=f'Optimal Value = {optimal_z:.4f}')
ax1.legend(loc='upper right', fontsize=12)
ax1.view_init(elev=30, azim=130)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# Contour Plot
ax2 = fig.add_subplot(122)
# Reduced levels to 15 to maintain the clean gaps despite the fractal nature
contour = ax2.contourf(X1, X2, Z, levels=15, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X1, X2, Z, levels=15, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solution
ax2.scatter(optimal_x1, optimal_x2, color='red', s=100, label='Optimal Solution = ($0$, $0$)')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_xticks(np.linspace(-0.5, 0.5, 5))
ax2.set_yticks(np.linspace(-0.5, 0.5, 5))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot", fontsize=16, pad=15)

plt.tight_layout()
plt.show()