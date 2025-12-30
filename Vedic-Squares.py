import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.colors import ListedColormap, BoundaryNorm

# number base for square
b = 20
L = b - 1
# mess around with L later, should just equal b for now haha

data = np.ones((L, L))

for j in range(L):
    for i in range(L):
        data[i, j] = (i + 1) * (j + 1) - (b - 1) * math.floor(((i + 1) * (j + 1) - 1) / (b - 1))

# print(data)


# Sample a continuous colormap at b-1 discrete points
base_cmap = plt.cm.rainbow  # red → violet
colors = base_cmap(np.linspace(1, 0, b-1))

cmap = ListedColormap(colors)
norm = BoundaryNorm(boundaries=np.arange(0.5, b + 0.5), ncolors=b-1)

plt.imshow(data, cmap=cmap, norm=norm)
plt.xticks([])
plt.yticks([])
#plt.colorbar(ticks=[1, b//2, b-1])
plt.show()