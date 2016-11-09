"""
Numerical Operations on Numpy Arrays
Broadcasting is pending can learn later
"""
import numpy as np

# Using Scalars
lst = [2,3, 7.9, 3.3, 6.9, 0.11, 10.3, 12.9]
v = np.array(lst)
v = v + 2
print(v)
print v*2.2


# Arithmetic Operation with two Arrays

A = np.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
B = np.ones((3,3))
print("Adding to arrays: ")
print(A + B)
print("\nMultiplying two arrays: ")
print(A * (B + 1))


# Matrix Multiplication:
# dot is used to do the matrix multiplication

print np.dot(A, B)

A = np.array([[1, 2, 3],
              [3, 2, 1]])
B = np.array([[2, 3, 4, -2],
              [1, -1, 2, 3],
              [1, 2, 3, 0]])
print A.shape[-1]
print (np.dot(A,B))
print A.ndim


A = np.array([ [1, 2, 3], [2, 2, 2], [3, 3, 3] ])
B = np.array([ [3, 2, 1], [1, 2, 3], [-1, -2, -3] ])
print np.dot(A,B)