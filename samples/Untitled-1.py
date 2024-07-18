'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the point
v = np.array([2., 2., 4.])

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original vector
ax.scatter(v[0], v[1], v[2], color='r')

# Plot the projections onto the x, y, and z axes






# Add legend
ax.legend()

# Show the plot
plt.show()
'''


import numpy as np
'''
# Define the matrix
A = np.array([[6, -9, 1], [4, 24, 8]])

# Scalar multiplication
scalar_product = 2 * A

print("Scalar Product:\n", scalar_product)

I = np.array([[1, 0], [0, 1]])
B = np.array([[6, -9, 1], [4, 24, 8]])

# Dot product
dot_product_1 = np.dot(I, B)

print("Dot Product 1:\n", dot_product_1)

arr = np.array([[0, 1, 2, 3, 4, 5],
                [10, 11, 12, 13, 14, 15],
                [20, 21, 22, 23, 24, 25],
                [30, 31, 32, 33, 34, 35],
                [40, 41, 42, 43, 44, 45],
                [50, 51, 52, 53, 54, 55]])

sub_array1 = arr[1, 2:4]
sub_array2 = arr[2:4, 4:6]
sub_array3 = arr[0:6, 1]
trans = sub_array3.T
print(trans)
'''

'''
def swapc(M, a, b):

    if not isinstance(m, np.ndarray) and m.ndim == 2:
        
        return None

    if m.shape[0]>=a or m.shape[1]>=b:
        return None

    swapped_matrix = M
    swapped_matrix[:, [a, b]] = swapped_matrix[:, [b, a]]
    return swapped_matrix


def swapr(M, a, b):

    if not isinstance(m, np.ndarray) and m.ndim == 2:
        return None

    if m.shape[0]>=a or m.shape[1]>=b:
        return None
    
    swapped_matrix = M
    swapped_matrix[[a,b], :] = swapped_matrix[[b, a],: ]
    return swapped_matrix

m = np.array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

print(m.shape)

'''

'''
def setM(L,  r, c, rowOrder = True):
    if rowOrder ==False:
        temp = r
        r=c
        c=temp

    counter = 0
    new = np.zeros((r, c))
    for i in range(r):
        for j in range(c):

            if counter<len(L):
                new[i,j] = L[counter]
                counter+=1

            else:
                new[i,j] = 0

    return new

elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(setM(elements,3,3, False))

'''