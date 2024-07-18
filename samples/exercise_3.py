
import matplotlib.pyplot as plt
import os
import numpy as np


fig, ax = plt.subplots()
# Customize axes (optional, as these are default locations)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Add your line here, example:
x = [1, 2, 3]
y = [2, 4, 1]
ax.plot(x, y, label='Example Line')

# Labeling axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Sample Graph!')

ax.set_xticks([ 1, 2, 3])  # Set x-axis tick points
ax.set_yticks([ 1, 2, 3, 4])  # Set y-axis tick points

ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))

# Display the plot
plt.show()
