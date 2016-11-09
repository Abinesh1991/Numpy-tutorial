"""
Indexing and Slicing
Assigning to and accessing the elements of an array is similar to other sequential data types of Python,
i.e. lists and tuples. We have also many options to indexing, which makes indexing in Numpy very powerful and
similar to core Python.
Arrays of Ones and of Zeros - Intializing Arrays with 0's and 1's



"""

import numpy as np
F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
# print the first element of F, i.e. the element with the index 0
print(F[0])
# print the last element of F
print(F[-1])
B = np.array([[[111, 112], [121, 122]],
               [[211, 212], [221, 222]],
               [[311, 312], [321, 322]]])
print(B[0][1][0])

# numpy way of getting data
print B[0, 0, 1]


tmp = B[1]
print(tmp)
print(tmp[0])

# slicing for multidimentional
# output - [[13 14 15][23 24 25][33 34 35]]
A = np.array([
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]])
print(A[:3, 2:])


"""
Arrays of Ones and of Zeros
There are two ways of initializing Arrays with Zeros or Ones.
The method ones(t) takes a tuple t with the shape of the array and fills the array accordingly with ones.
By default it will be filled with Ones of type float.
If you need integer Ones, you have to set the optional parameter dtype to int:

"""

# intializing an array as 1
E = np.ones((2,3))
print(E)
F = np.ones((3,4),dtype=int)
print(F)

# intializing an array as 0
Z = np.zeros((2,4),dtype=int)
print(Z)

# There is another interesting way to create an array with Ones or with Zeros,
# if it has to have the same shape as another existing array 'a'.
# Numpy supplies for this purpose the methods ones_like(a) and zeros_like(a)
x = np.array([2,5,18,14,4])
E = np.ones_like(x)
print(E)
Z = np.zeros_like(x)
print(Z)