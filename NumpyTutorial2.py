"""
Different dimensional arrays
Zero-dimensional,One-dimensional,two dimensional etc...
Shape of an array
"""
import numpy as np

"""
Zero dimensional
Output:
('x: ', array(42))
('The type of x: ', <type 'numpy.ndarray'>)
('The dimension of x:', 0)
"""

x = np.array(42)
print("x: ", x)
print("The type of x: ", type(x))
# ndim(a) - Return the number of dimensions of an array.
# Input array.  If it is not already an ndarray, a conversion in attempted.
print("The dimension of x:", np.ndim(x))


"""
One Dimensional Array
Output:
('F: ', array([ 1,  1,  2,  3,  5,  8, 13, 21]))
('V: ', array([  3.4,   6.9,  99.8,  12.8]))
('Type of F: ', dtype('int64'))
('Type of V: ', dtype('float64'))
('Dimension of F: ', 1)
('Dimension of V: ', 1)
"""
F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
V = np.array([3.4, 6.9, 99.8, 12.8])
print("F: ", F)
print("V: ", V)
print("Type of F: ", F.dtype)
print("Type of V: ", V.dtype)
print("Dimension of F: ", np.ndim(F))
print("Dimension of V: ", np.ndim(V))


"""
Two Dimensional array
Output:
[[  3.4   8.7   9.9]
 [  1.1  -7.8  -0.7]
 [  4.1  12.3   4.8]]
2

"""
A = np.array([[3.4, 8.7, 9.9],
              [1.1, -7.8, -0.7],
              [4.1, 12.3, 4.8]])
print(A)
print(A.ndim)


"""
Shape of an array
The shape is a tuple of integers. These numbers denote the lengths of the corresponding array dimension

"""
x = np.array([[67, 63, 87],
              [77, 69, 59],
              [85, 87, 99],
              [79, 72, 71],
              [63, 89, 93],
              [68, 92, 78]])
print(np.shape(x))

# change the shape of the array
x.shape = (2, 9)
print x


# Three dimensional array shape
B = np.array([[[111, 112], [121, 122]],
              [[211, 212], [221, 222]],
              [[311, 312], [321, 322]]])
print(B.shape)
# count from the inner depth array value
# example : 122,122 = 2,we have 2 list [[111, 112], [121, 122]],3([[[111 112 121],[122 211 212]],
#                                                                                        [[221 222 311],[312 321 322]]])
B.shape = (2, 2, 3)
print B
