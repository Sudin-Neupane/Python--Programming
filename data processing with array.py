import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)

cmap = "viridis"  # try "plasma", "inferno", "rainbow", or other Matplotlib colormaps
plt.imshow(z, cmap=cmap, origin="lower")
plt.colorbar()
plt.title("Image plot of a grid of values")
plt.xlabel("x")
plt.ylabel("y")
plt.show()