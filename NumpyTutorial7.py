"""
Numpy Arrays: Concatenating, Flattening and Adding Dimensions
Flatten - Makes a matrix 3D array into a singe list
Ravel - same as Flatten
Vector Stacking (row_stack,column_stack)


"""

import numpy as np

A = np.array([[[0, 1],
               [2, 3],
               [4, 5],
               [6, 7]],
              [[8, 9],
               [10, 11],
               [12, 13],
               [14, 15]],
              [[16, 17],
               [18, 19],
               [20, 21],
               [22, 23]]])
Flattened_X = A.flatten()
print(Flattened_X)
print(A.flatten(order="C"))
print(A.flatten(order="F"))
print(A.flatten(order="A"))

# Concatenating Arrays
x = np.array([11, 22])
y = np.array([18, 7, 6])
z = np.array([1, 3, 5])
c = np.concatenate((x, y, z))
print(c)


"""
np.row_stack(a) - Stack arrays in sequence vertically (row wise).
Take a sequence of arrays and stack them vertically to make a single

np.column_stack() - take a sequence of 1-D arrays and stack them as columns
to make a single 2-D array. 2-D arrays are stacked as-is,
just like with `hstack`.  1-D arrays are turned into 2-D columns
first.
"""
A = np.array([3, 4, 5])
B = np.array([1,9,0])
print(np.row_stack((A, B)))
print(np.column_stack((A, B)))
np.shape(A)


"""
Tile - Construct an array by repeating A the number of times given by reps.
output:
array([[1, 2, 1, 2, 1, 2, 1, 2],
       [3, 4, 3, 4, 3, 4, 3, 4],
       [1, 2, 1, 2, 1, 2, 1, 2],
       [3, 4, 3, 4, 3, 4, 3, 4],
       [1, 2, 1, 2, 1, 2, 1, 2],
       [3, 4, 3, 4, 3, 4, 3, 4]])
"""

x = np.array([ [1, 2], [3, 4]])
np.tile(x, (3,4))
