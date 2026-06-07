import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


# Define the Hartmann 3 Function
def hartmann_3_function(x, y, z_fixed=0.477649):
    # Coefficients for Hartmann 3
    alpha = np.array([1.0, 1.2, 3.0, 3.2])
    A = np.array([
        [3.0, 10.0, 30.0],
        [0.1, 10.0, 35.0],
        [3.0, 10.0, 30.0],
        [0.1, 10.0, 35.0]
    ])
    P = 10 ** -4 * np.array([
        [3689, 1170, 2673],
        [4699, 4387, 7470],
        [1091, 8732, 5547],
        [381, 5743, 8828]
    ])

    external_sum = 0
    # Reshape x and y to handle meshgrid inputs
    x_flat = x.flatten()
    y_flat = y.flatten()
    z_vals = np.full_like(x_flat, z_fixed)

    results = np.zeros_like(x_flat)

    for i in range(4):
        inner_sum = (A[i, 0] * (x_flat - P[i, 0]) ** 2 +
                     A[i, 1] * (y_flat - P[i, 1]) ** 2 +
                     A[i, 2] * (z_vals - P[i, 2]) ** 2)
        results += alpha[i] * np.exp(-inner_sum)

    return -results.reshape(x.shape)


# Generate grid
# Standard domain for Hartmann 3: xi in [0, 1]
x_vals = np.linspace(0, 1, 400)
y_vals = np.linspace(0, 1, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = hartmann_3_function(X, Y)

# Global Minimum: f(x*) ≈ -3.86278
# Located at: (0.114614, 0.555649, 0.477649)
optimal_x, optimal_y = 0.114614, 0.555649
optimal_z = hartmann_3_function(np.array([[optimal_x]]), np.array([[optimal_y]]))[0, 0]

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
ax1.set_zlabel("$f(X_1, X_2, x_3^*)$", labelpad=15, fontsize=16)

# Set ticks
ax1.set_xticks(np.linspace(0, 1, 5))
ax1.set_yticks(np.linspace(0, 1, 5))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 5))

ax1.tick_params(axis='both', labelsize=12)

# Mark the global minimum
ax1.scatter(optimal_x, optimal_y, optimal_z, color='red', s=100, edgecolors='white',
            label=f'Global Min $\\approx$ {optimal_z:.4f}', zorder=10)
ax1.legend(loc='upper right', fontsize=12)

# Adjust view angle
ax1.view_init(elev=30, azim=-135)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# --- 2. Contour Plot ---
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Z, levels=25, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X, Y, Z, levels=25, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solution
ax2.scatter(optimal_x, optimal_y, color='red', s=100, edgecolors='white', label='Global Minimum')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_xticks(np.linspace(0, 1, 5))
ax2.set_yticks(np.linspace(0, 1, 5))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot (Hartmann 3 - 2D Slice)", fontsize=16, pad=15)

plt.tight_layout()
plt.show()