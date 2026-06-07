# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
#
# # Define the Bird Function (Mishra Variant)
# def bird_function(x, y):
#     term1 = np.sin(x) * np.exp((1 - np.cos(y))**2)
#     term2 = np.cos(y) * np.exp((1 - np.sin(x))**2)
#     term3 = (x - y)**2
#     return term1 + term2 + term3
#
# # Generate grid
# # Using [-2pi, 2pi] to show the periodic nature and the global minimum
# x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 400)
# y_vals = np.linspace(-2 * np.pi, 2 * np.pi, 400)
# X, Y = np.meshgrid(x_vals, y_vals)
# Z = bird_function(X, Y)
#
# # Global Minimum: f(x*) ≈ -106.7645
# # For the formula used: x* ≈ -1.5821, y* ≈ -3.1302
# optimal_x, optimal_y = -1.58214, -3.13024
# optimal_z = bird_function(optimal_x, optimal_y)
#
# # Create figure
# fig = plt.figure(figsize=(16, 8))
#
# # --- 1. 3D Surface Plot ---
# ax1 = fig.add_subplot(121, projection='3d')
# surf = ax1.plot_surface(
#     X, Y, Z, cmap=cm.viridis, edgecolor='k', linewidth=0.05, antialiased=True, alpha=0.8
# )
#
# # Adjust axes labels
# ax1.set_xlabel("$X_1$", labelpad=15, fontsize=16)
# ax1.set_ylabel("$X_2$", labelpad=15, fontsize=16)
# ax1.set_zlabel("$f(X_1, X_2)$", labelpad=15, fontsize=16)
#
# # Set ticks
# ax1.set_xticks(np.linspace(-2*np.pi, 2*np.pi, 5))
# ax1.set_yticks(np.linspace(-2*np.pi, 2*np.pi, 5))
# z_min, z_max = Z.min(), Z.max()
# ax1.set_zticks(np.linspace(z_min, z_max, 5))
#
# ax1.tick_params(axis='both', labelsize=10)
#
# # Mark the global minimum
# ax1.scatter(optimal_x, optimal_y, optimal_z, color='red', s=100, edgecolors='white',
#             label=f'Global Min $\\approx$ {optimal_z:.2f}', zorder=5)
# ax1.legend(loc='upper right', fontsize=12)
#
# # Adjust view angle to see the deep valleys
# ax1.view_init(elev=45, azim=-135)
#
# # Add color bar
# fig.colorbar(cm.ScalarMappable(cmap=cm.viridis), ax=ax1, shrink=0.5, aspect=10, pad=0.1)
#
# # --- 2. Contour Plot ---
# ax2 = fig.add_subplot(122)
# # The Bird function has huge value ranges, so levels=25 helps define the valleys
# contour = ax2.contourf(X, Y, Z, levels=25, cmap=cm.viridis, alpha=0.8)
# contour_lines = ax2.contour(X, Y, Z, levels=25, colors='k', linewidths=0.5)
# fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)
#
# # Mark optimal solution
# ax2.scatter(optimal_x, optimal_y, color='red', s=100, edgecolors='white', label='Global Minimum')
# ax2.legend(loc='upper right', fontsize=12)
#
# # Axes labels, ticks, and grid
# ax2.set_xlabel("$X_1$", fontsize=14)
# ax2.set_ylabel("$X_2$", fontsize=14)
# ax2.set_xticks(np.linspace(-2*np.pi, 2*np.pi, 5))
# ax2.set_yticks(np.linspace(-2*np.pi, 2*np.pi, 5))
# ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.5)
# ax2.set_title("Contour Plot (Bird Function)", fontsize=16, pad=15)
#
# plt.tight_layout()
# plt.show()



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the Bird Function (Mathematical Formulation from Section 2.3)
def bird_function(x, y):
    term1 = np.sin(x) * np.exp((1 - np.cos(y))**2)
    term2 = np.cos(y) * np.exp((1 - np.sin(x))**2)
    term3 = (x - y)**2
    return term1 + term2 + term3

# Generate grid
# Using [-2pi, 2pi] as specified in the research domain
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y_vals = np.linspace(-2 * np.pi, 2 * np.pi, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = bird_function(X, Y)

# Global Minimum: f(x*) ≈ -106.7645
# Note: This function is symmetric; one global minimum is at approx (-1.58, -3.13)
optimal_x, optimal_y = -1.58214, -3.13024
optimal_z = bird_function(optimal_x, optimal_y)

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

# Set ticks for a clean look
ax1.set_xticks(np.linspace(-2*np.pi, 2*np.pi, 5))
ax1.set_yticks(np.linspace(-2*np.pi, 2*np.pi, 5))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 5))

ax1.tick_params(axis='both', labelsize=12)

# Mark the global minimum
ax1.scatter(optimal_x, optimal_y, optimal_z, color='red', s=100, edgecolors='white',
            label=f'Global Min $\\approx$ {optimal_z:.2f}', zorder=5)
ax1.legend(loc='upper right', fontsize=12)

# Adjust view angle
ax1.view_init(elev=45, azim=-135)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# --- 2. Contour Plot ---
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Z, levels=20, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X, Y, Z, levels=20, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solution
ax2.scatter(optimal_x, optimal_y, color='red', s=100, edgecolors='white', label='Global Minimum')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_xticks(np.linspace(-2*np.pi, 2*np.pi, 5))
ax2.set_yticks(np.linspace(-2*np.pi, 2*np.pi, 5))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot", fontsize=16, pad=15)

plt.tight_layout()
plt.show()