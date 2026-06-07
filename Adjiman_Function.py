# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
#
# # Define the Adjiman Function
# def adjiman_function(x1, x2):
#     """
#     Evaluate the Adjiman function for given x1 and x2.
#     Parameters:
#         x1: float or ndarray, first input variable in [-1, 2]
#         x2: float or ndarray, second input variable in [-1, 1]
#     Returns:
#         float or ndarray, function value
#     """
#     return np.cos(x1) * np.sin(x2) - x1 / (x2**2 + 1)
#
# # Generate grid for visualization
# x1_vals = np.linspace(-1, 2, 400)
# x2_vals = np.linspace(-1, 1, 400)
# X1, X2 = np.meshgrid(x1_vals, x2_vals)
# Z = adjiman_function(X1, X2)
#
# # Global minimum point
# optimal_x1, optimal_x2 = 2, 0.10578
# optimal_z = adjiman_function(optimal_x1, optimal_x2)
#
# # Create figure
# fig = plt.figure(figsize=(16, 8))
#
# # 3D Surface plot
# ax1 = fig.add_subplot(121, projection='3d')
# surf = ax1.plot_surface(
#     X1, X2, Z, cmap=cm.viridis, edgecolor='k', linewidth=0.2, alpha=0.8
# )
# ax1.scatter(optimal_x1, optimal_x2, optimal_z, color='red', s=100, label='Global Minimum')
# ax1.set_xlabel("$X_1$", labelpad=15, fontsize=14)
# ax1.set_ylabel("$X_2$", labelpad=15, fontsize=14)
# ax1.set_zlabel("$f(X_1, X_2)$", labelpad=15, fontsize=14)
# ax1.set_title("3D Surface Plot of Adjiman Function", fontsize=16)
# ax1.legend()
#
# # Add color bar
# fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=10)
#
# # Contour plot
# ax2 = fig.add_subplot(122)
# contour = ax2.contourf(X1, X2, Z, levels=50, cmap=cm.viridis, alpha=0.8)
# contour_lines = ax2.contour(X1, X2, Z, levels=20, colors='k', linewidths=0.5)
# ax2.scatter(optimal_x1, optimal_x2, color='red', s=100, label='Global Minimum')
# ax2.set_xlabel("$X_1$", fontsize=14)
# ax2.set_ylabel("$X_2$", fontsize=14)
# ax2.set_title("Contour Plot of Adjiman Function", fontsize=16)
# ax2.legend()
#
# # Add color bar
# fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)
#
# plt.tight_layout()
# plt.show()






import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the Adjiman Function
def adjiman_function(x, y):
    term1 = np.cos(x) * np.sin(y)
    term2 = x / (y**2 + 1)
    return term1 - term2

# Generate grid based on the standard domain: x1 in [-1, 2], x2 in [-1, 1]
x_vals = np.linspace(-1, 2, 400)
y_vals = np.linspace(-1, 1, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = adjiman_function(X, Y)

# Global Minimum: f(x*) ≈ -2.0218 at x* = (2, 0.10578)
optimal_x, optimal_y = 2.0, 0.10578
optimal_z = adjiman_function(optimal_x, optimal_y)

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

# Set ticks for better readability
ax1.set_xticks(np.linspace(-1, 2, 4))
ax1.set_yticks(np.linspace(-1, 1, 5))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 5))

ax1.tick_params(axis='both', labelsize=12)

# Mark the global minimum
ax1.scatter(optimal_x, optimal_y, optimal_z, color='red', s=100, edgecolors='white',
            label=f'Global Min $\\approx$ {optimal_z:.4f}')
ax1.legend(loc='upper right', fontsize=12)

# Adjust view angle to see the asymmetric slope clearly
ax1.view_init(elev=30, azim=-60)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# --- 2. Contour Plot ---
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Z, levels=20, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X, Y, Z, levels=20, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solution
ax2.scatter(optimal_x, optimal_y, color='red', s=100, edgecolors='white', label='Global Minimum')
ax2.legend(loc='upper left', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_xticks(np.linspace(-1, 2, 4))
ax2.set_yticks(np.linspace(-1, 1, 5))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot", fontsize=16, pad=15)

plt.tight_layout()
plt.show()