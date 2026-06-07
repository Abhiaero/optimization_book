import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define the Brent function
def brent_function(x):
    return (x + 10)**2

# Generate data
x_vals = np.linspace(-15, -5, 500)
y_vals = brent_function(x_vals)

# Optimal solution
optimal_x = -10
optimal_y = brent_function(optimal_x)

# Create figure
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the function curve
ax.plot(x_vals, y_vals, color=cm.plasma(0.5), linewidth=2.5, label="Brent Function")

# Mark the optimal solution
ax.scatter(optimal_x, optimal_y, color='red', s=100, label="Optimal Solution")

# Enhance axes appearance
ax.set_xlabel("$X$", fontsize=16, labelpad=15)
ax.set_ylabel("$f(X)$", fontsize=16, labelpad=15)
ax.tick_params(axis='x', labelsize=12, width=2, length=8)
ax.tick_params(axis='y', labelsize=12, width=2, length=8)

# Increase axis line width
for spine in ax.spines.values():
    spine.set_linewidth(1.75)
    spine.set_edgecolor('black')

# Add grid and legend
ax.grid(color='gray', linestyle='--', linewidth=0.7, alpha=0.8)
ax.legend(loc="upper center", fontsize=14)

# Add title
# ax.set_title("Brent Function with Optimal Solution", fontsize=18, pad=15)

plt.tight_layout()
plt.show()
