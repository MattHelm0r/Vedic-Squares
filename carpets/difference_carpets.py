import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

# p-colorability setting
p = 5

# counting black squares, the whole image has dimension (square_len + 2)^2
square_len = p**4

# Create matrix of data values
# Initialize the data matrix with black
data = -np.ones((square_len + 2, square_len + 2))

# populate zeroth row
i = 0
for j in range(2, square_len + 2):
    if j == 2:
        data[i, j] = 2
    elif j % 2 == 1:
        continue
    else:
        data[i, j] = 1

# populate first row
i = 1
for j in range(2, square_len + 2):
    if j == 2:
        data[i, j] = 2
    else:
        data[i, j] = 1

# populate zeroth column
j = 0
for i in range(3, square_len + 2):
    if i == 2:
        data[i, j] = 2
    elif i % 2 == 0:
        continue
    else:
        data[i, j] = 1

# populate first column
j = 1
for i in range(2, square_len + 2):
    if i == 2:
        data[i, j] = 2
    else:
        data[i, j] = 1

# This is where the magic happens for most of the grid
for j in range(2, square_len + 2):
    for i in range(2, square_len + 2):
        if (i + j) % 2 == 0:
            data[i, j] = (-data[i - 2, j] + 2 * data[i - 1, j]) % p
        else:
            data[i, j] = (-data[i, j - 2] + 2 * data[i, j - 1]) % p

# Take difference between all zero carpet and this carpet
for j in range(0, square_len + 2):
    for i in range(0, square_len + 2):
        if data[i, j] == 1:
            data[i, j] = -1
        elif data[i, j] != -1:
            data[i, j] = 0

# create discrete colormap
# MODIFY THIS SO NUMBER OF COLORS MATCHES p
cmap = colors.ListedColormap(['white', 'black', 'red', 'blue', 'lime', 'violet', 'yellow', 'sandybrown', 'aquamarine', 'cyan', 'brown', 'olive'])
bounds = np.arange(-1, p + 1) # Generates an array from -1 to p+1
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
ax.imshow(data, cmap=cmap, norm=norm)

# draw gridlines (MESS WITH LINE WIDTH HERE)
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=.01)
ax.set_xticks(np.arange(-.5, square_len + 2, 1));
ax.set_yticks(np.arange(-.5, square_len + 2, 1));

# Hide ticks and labels
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.tick_params(which='both', length=0)

plt.show()