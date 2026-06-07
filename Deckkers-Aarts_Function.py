import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the Deckkers-Aarts Function
def deckkers_aarts_function(x, y):
    term1 = 10**5 * x**2
    term2 = y**2
    term3 = -(x**2 + y**2)**2
    term4 = 10**-5 * (x**2 + y**2)**4
    return term1 + term2 + term3 + term4

# Generate grid
# Standard domain: x1, x2 in [-20, 20]
x_vals = np.linspace(-20, 20, 400)
y_vals = np.linspace(-20, 20, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = deckkers_aarts_function(X, Y)

# Global Minima: f(x*) = -24771.09375
# Two global minima exist at (0, 15) and (0, -15)
optima = [(0, 15), (0, -15)]

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
ax1.set_zlabel("$f(X_1, X_2)$", labelpad=15, fontsize=16)

# Set ticks
ax1.set_xticks(np.linspace(-20, 20, 5))
ax1.set_yticks(np.linspace(-20, 20, 5))
z_min, z_max = Z.min(), Z.max()
ax1.set_zticks(np.linspace(z_min, z_max, 5))

ax1.tick_params(axis='both', labelsize=12)

# Mark the global minima
for i, (ox, oy) in enumerate(optima):
    oz = deckkers_aarts_function(ox, oy)
    label = 'Global Min' if i == 0 else ""
    ax1.scatter(ox, oy, oz, color='red', s=100, edgecolors='white', label=label, zorder=10)

ax1.legend(loc='upper right', fontsize=12)

# Adjust view angle to see the two deep wells
ax1.view_init(elev=30, azim=45)

# Add color bar
fig.colorbar(cm.ScalarMappable(cmap=cm.plasma), ax=ax1, shrink=0.5, aspect=10, pad=0.1)

# --- 2. Contour Plot ---
ax2 = fig.add_subplot(122)
# Using logarithmic-like spacing or more levels to handle the massive range of values
contour = ax2.contourf(X, Y, Z, levels=35, cmap=cm.plasma, alpha=0.8)
contour_lines = ax2.contour(X, Y, Z, levels=35, colors='k', linewidths=0.5)
fig.colorbar(contour, ax=ax2, shrink=0.8, aspect=15)

# Mark optimal solutions
for ox, oy in optima:
    ax2.scatter(ox, oy, color='red', s=100, edgecolors='white', zorder=5)

# Single legend entry for minima
ax2.scatter([], [], color='red', s=100, edgecolors='white', label='Global Minima')
ax2.legend(loc='upper right', fontsize=12)

# Axes labels, ticks, and grid
ax2.set_xlabel("$X_1$", fontsize=14)
ax2.set_ylabel("$X_2$", fontsize=14)
ax2.set_xticks(np.linspace(-20, 20, 5))
ax2.set_yticks(np.linspace(-20, 20, 5))
ax2.grid(color='gray', linestyle='--', linewidth=0.6, alpha=0.8)
ax2.set_title("Contour Plot", fontsize=16, pad=15)

plt.tight_layout()
plt.show()