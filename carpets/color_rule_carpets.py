import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

# n-colorability settings
n = 5
a = 2
b = 0

# counting black squares, the whole image has dimension (square_len + 2)^2
square_len = n**3

# Create matrix of data values
# Initialize the data matrix with black
data = -np.ones((square_len + 2, square_len + 2))

# populate zeroth row
i = 0
for j in range(2, square_len + 2):
    if j % 2 == 1:
        continue
    else:
        data[i, j] = (j + 1) % n

# populate first row
i = 1
for j in range(2, square_len + 2):
    data[i, j] = (j + 1) % n

# populate zeroth column
j = 0
for i in range(3, square_len + 2):
    if i % 2 == 0:
        continue
    else:
        data[i, j] = (i + 1) % n

# populate first column
j = 1
for i in range(2, square_len + 2):
 data[i, j] = (i + 1) % n

# This is where the magic happens for most of the grid
for j in range(2, square_len + 2):
    for i in range(2, square_len + 2):
        if (i + j) % 2 == 0:
            data[i, j] = (a * data[i - 2, j] * data[i, j - 2] * data[i, j - 2] * data[i, j - 2] + b * data[i - 1, j] * data[i - 1, j]) % n
        else:
            data[i, j] = (a * data[i, j - 2] * data[i, j - 2] * data[i, j - 2] * data[i, j - 2] + b * data[i, j - 1] * data[i - 1, j]) % n

# create discrete colormap
# MODIFY THIS SO NUMBER OF COLORS IS ONE GREATER THAN N
cmap = colors.ListedColormap(['black', 'red', 'blue', 'lime', 'violet', 'yellow'])#, 'sandybrown', 'aquamarine', 'cyan', 'salmon', 'olive', 'rebeccapurple'])
bounds = np.arange(-1, n + 1) # Generates an array from -1 to n+1
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
ax.imshow(data, cmap=cmap, norm=norm)

# draw gridlines (MESS WITH LINE WIDTH HERE)
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=.1)
ax.set_xticks(np.arange(-.5, square_len + 2, 1));
ax.set_yticks(np.arange(-.5, square_len + 2, 1));

# Hide ticks and labels
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.tick_params(which='both', length=0)

plt.show()