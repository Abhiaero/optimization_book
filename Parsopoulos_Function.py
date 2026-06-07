import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the Parsopoulos Function
def parsopoulos_function(x1, x2):
    # n-dimensional: sum(|xi|^sin(xi) * exp(-xi^2))
    term1 = np.abs(x1)**np.sin(x1) * np.exp(-x1**2)
    term2 = np.abs(x2)**np.sin(x2) * np.exp(-x2**2)
    return term1 + term2

# Generate grid (Domain for Parsopoulos is typically [-5, 5])
x1_vals = np.linspace(-5, 5, 400) # Increased density for sharper peaks
x2_vals = np.linspace(-5, 5, 400)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Z = parsopoulos_function(X1, X2)

# Optimal solution (Dynamically finding the minimum on the generated grid)
min_idx = np.unravel_index(np.argmin(Z, axis=None), Z.shape)
optimal_x1 = X1[min_idx]
optimal_x2 = X2[min_idx]
optimal_z = Z[min_idx]

# Create figure
fig = plt.figure(figsize=(16, 8))

# 3D Surface plot
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(
    X1, X2, Z, cmap=cm.plasma, edgecolor='k', linewidth=0.1, antialiased=True, alpha=0.8
)

# Adjust axes labels
ax1.set_xlabel("$X_1$", labelpad=15, fontsize=16)
ax1.set_ylabel("$X_2$", labelpad=15, fontsize=16)
ax1.set_zlabel("$f(X_1, X_2)$", labelpad=15, fontsize=16)

# Explicitly set fewer ticks to increase the gap and reduce clutter
ax1.set_xticks(np.linspace(-5, 5, 5))
ax1.set_yticks(np.linspace(-5, 5, 5))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 4))

ax1.tick_params(axis='both', labelsize=12)

# Optimal solution point
ax1.scatter(optimal_x1, optimal_x2, optimal_z, color='red', s=100, label=f'Min Value = {optimal_z:.4f}')
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
ax2.scatter(optimal_x1, optimal_x2, color='red', s=100, label=f'Min Solution $\\approx$ ({optimal_x1:.2f}, {optimal_x2:.2f})')
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