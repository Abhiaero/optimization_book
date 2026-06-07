import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the Vincent Function
def vincent_function(x, y):
    return -(np.sin(10 * np.log(x)) + np.sin(10 * np.log(y)))

# STRICT RANGE: 0.25 to 10
x_limit = (0.25, 10)
x_vals = np.linspace(x_limit[0], x_limit[1], 500)
y_vals = np.linspace(x_limit[0], x_limit[1], 500)
X, Y = np.meshgrid(x_vals, y_vals)
Z = vincent_function(X, Y)

# Calculate global minima that fall WITHIN [0.25, 10]
# Formula: xi = exp((4k+1)pi / 20)
k_values = np.arange(0, 6)
all_coords = np.exp(((4 * k_values + 1) * np.pi) / 20)
# Filter to keep only those <= 10
valid_coords = all_coords[all_coords <= 10]

# Generate the grid of valid minima
opt_x, opt_y = np.meshgrid(valid_coords, valid_coords)
opt_z = vincent_function(opt_x, opt_y)

# Create figure
fig = plt.figure(figsize=(16, 7))

# 3D Surface
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none', alpha=0.8)
ax1.scatter(opt_x, opt_y, opt_z, color='red', s=40, edgecolors='white', label=f'{len(valid_coords)**2} Minima in range')
ax1.set_xlim(0.25, 10)
ax1.set_ylim(0.25, 10)
# ax1.set_title("3D View (Range: 0.25 - 10)")
ax1.legend()

# Contour Plot
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Z, levels=50, cmap='plasma')
ax2.scatter(opt_x, opt_y, color='red', marker='*', s=100, label='Global Minima')
ax2.set_xlim(0.25, 10)
ax2.set_ylim(0.25, 10)
ax2.set_title("Contour Plot")
plt.colorbar(contour, ax=ax2)

plt.tight_layout()
plt.show()