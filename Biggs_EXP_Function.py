import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


# Define the Biggs EXP6 Function (as a 2D slice)
def biggs_exp6_function(x1, x2):
    # Fixed parameters at their optimal values for visualization
    x3_opt, x4_opt, x5_opt, x6_opt = 1.0, 5.0, 4.0, 3.0

    # Target points for the summation (m=13)
    m = 13
    ti = np.array([0.1 * i for i in range(1, m + 1)])

    # The target function value y_i based on the global optimum (1, 10, 1, 5, 4, 3)
    yi = np.exp(-ti) - 5 * np.exp(-10 * ti) + 3 * np.exp(-4 * ti)

    # Reshape for meshgrid broadcasting
    x1_flat = x1.flatten()
    x2_flat = x2.flatten()
    f_vals = np.zeros_like(x1_flat)

    for i in range(m):
        # The residual: f(x, t) - y_i
        # Model: x3*exp(-x1*t) - x4*exp(-x2*t) + x6*exp(-x5*t)
        term = x3_opt * np.exp(-x1_flat * ti[i]) - x4_opt * np.exp(-x2_flat * ti[i]) + x6_opt * np.exp(-x5_opt * ti[i])
        f_vals += (term - yi[i]) ** 2

    return f_vals.reshape(x1.shape)


# Generate grid
# Standard domain for Biggs: x in [0, 20]
x_vals = np.linspace(0, 20, 400)
y_vals = np.linspace(0, 20, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = biggs_exp6_function(X, Y)

# Global Minimum: f(x*) = 0 at x1=1, x2=10
optimal_x, optimal_y = 1.0, 10.0
optimal_z = biggs_exp6_function(np.array([[optimal_x]]), np.array([[optimal_y]]))[0, 0]

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
ax1.set_zlabel("$f(X_1, X_2, \dots)$", labelpad=15, fontsize=16)

# Set ticks
ax1.set_xticks(np.linspace(0, 20, 5))
ax1.set_yticks(np.linspace(0, 20, 5))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 5))

ax1.tick_params(axis='both', labelsize=12)

# Mark the global minimum
ax1.scatter(optimal_x, optimal_y, optimal_z, color='red', s=100, edgecolors='white',
            label=f'Global Min = {optimal_z:.1f}', zorder=10)
ax1.legend(loc='upper right', fontsize=12)

# Adjust view angle to see the smooth exponential decay basin
ax1.view_init(elev=30, azim=45)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# --- 2. Contour Plot ---
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Z, levels=30, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X, Y, Z, levels=30, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solution
ax2.scatter(optimal_x, optimal_y, color='red', s=100, edgecolors='white', label='Global Minimum')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_xticks(np.linspace(0, 20, 5))
ax2.set_yticks(np.linspace(0, 20, 5))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot", fontsize=16, pad=15)

plt.tight_layout()
plt.show()