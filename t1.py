import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ==================== UPDATED 3D VISUALIZATION ====================
# • Two linear constraints (x₁ ≥ 0, x₂ ≥ 0)
# • One non-linear constraint (circle: (x₁-2.5)² + (x₂-2.5)² ≤ 9)
# • New objective function (different multimodal landscape)
# • Function space lifted slightly above solution space

fig = plt.figure(figsize=(13, 10), dpi=300)
ax = fig.add_subplot(111, projection='3d')

# Offset to lift the function landscape above the solution space
offset = 1.3

# ------------------- NEW Objective Function Landscape (lifted) -------------------
x = np.linspace(-0.4, 5.4, 45)
y = np.linspace(-0.4, 5.4, 45)
X, Y = np.meshgrid(x, y)

# New different multimodal function (different from previous quadratic + sin/cos)
Z = (X - 2.8)**2 + (Y - 2.2)**2 + 7*np.sin(2.8*X) + 6*np.cos(2.1*Y) + offset

surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.78, linewidth=0.4, antialiased=True, edgecolor='none')

# Colorbar
cbar = fig.colorbar(surf, ax=ax, shrink=0.6, aspect=20, pad=0.15)
cbar.set_label(r'$f(\mathbf{x})$ value', fontsize=13, labelpad=15)

# ------------------- Solution Space: Feasible Region (with non-linear constraint) -------------------
# Non-linear constraint boundary: circle centered at (2.5, 2.5) with radius 3
theta = np.linspace(0, np.pi/2, 120)          # quarter-circle in first quadrant
x_circle = 2.5 + 3 * np.cos(theta)
y_circle = 2.5 + 3 * np.sin(theta)
z_circle = np.zeros_like(theta)

# Create filled feasible region (quarter-disk inside circle + x1≥0 + x2≥0)
verts = np.column_stack((x_circle, y_circle, z_circle))
verts = np.vstack(([0, 0, 0], verts, [0, 0, 0]))   # close the polygon
poly = Poly3DCollection([verts], alpha=0.45, facecolor='limegreen', edgecolor='darkgreen', linewidth=3)
ax.add_collection3d(poly)

# Constraint boundary lines
# g1: x₁ ≥ 0 (linear)
ax.plot([0, 5], [0, 0], [0, 0], color='red', linestyle='--', linewidth=3)
# g2: x₂ ≥ 0 (linear)
ax.plot([0, 0], [0, 5], [0, 0], color='orange', linestyle='--', linewidth=3)
# g3: (x₁-2.5)² + (x₂-2.5)² ≤ 9 (non-linear circle)
ax.plot(x_circle, y_circle, z_circle, color='blue', linestyle='--', linewidth=3)

# ------------------- Constraint labels -------------------
ax.text(1.9, 3.8, 0.4, r'$g_3(\mathbf{x})\leq 0$', color='blue', fontsize=13, fontweight='bold', ha='center')
ax.text(-0.7, 2.1, 0.4, r'$g_2(\mathbf{x})\leq 0$', color='orange', fontsize=13, fontweight='bold', ha='right')
ax.text(2.4, -0.8, 0.4, r'$g_1(\mathbf{x})\leq 0$', color='red', fontsize=13, fontweight='bold', ha='center')

# ------------------- Global minimum (inside feasible region) -------------------
ax.scatter(2.8, 2.2, 2.9 + offset, color='red', s=280, marker='*', edgecolor='white', linewidth=2.5, zorder=20)
ax.text(3.1, 1.9, 5.8 + offset, 'Global Minimum $x^*$', color='red', fontsize=14, fontweight='bold')

# ------------------- Space labels -------------------
ax.text(2.4, -1.6, 22, r'Solution Space $\mathbf{x}\in\mathbb{R}^2$', fontsize=14, fontweight='bold', ha='center')
ax.text(-2.4, 2.7, 12 + offset/2, r'Function Landscape $f(\mathbf{x})\in\mathbb{R}$',
        fontsize=14, fontweight='bold', rotation=90, va='center', ha='center')

# Axis labels and title
ax.set_xlabel(r'$x_1$', fontsize=16, labelpad=12)
ax.set_ylabel(r'$x_2$', fontsize=16, labelpad=12)
ax.set_zlabel(r'$f(\mathbf{x})$', fontsize=16, labelpad=12)

ax.set_title('3D Visualization with Non-Linear Constraint\n(Solution Space + Lifted Objective Function Landscape)',
              fontsize=17, fontweight='bold', pad=25)

# View settings
ax.view_init(elev=33, azim=58)
ax.grid(True, linestyle='--', alpha=0.4)

ax.set_xlim(-0.6, 5.6)
ax.set_ylim(-0.6, 5.6)
ax.set_zlim(0, 23)

# Save high-quality files for your book
plt.savefig('3d_nonlinear_constraints_new_function.pdf', bbox_inches='tight', dpi=300)
plt.savefig('3d_nonlinear_constraints_new_function.png', bbox_inches='tight', dpi=300)

print("✅ SAVED SUCCESSFULLY!")
print("   • 3d_nonlinear_constraints_new_function.pdf   ← use this in your Springer book")
print("   • 3d_nonlinear_constraints_new_function.png")

plt.show()