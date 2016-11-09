"""
Matrix Arithmetics under NumPy and Python

"""

import numpy as np
# Vector Addition/Subration
x = np.array([3,2])
y = np.array([5,1])
z = x + y
a = x - y
print a,z


# Scalar Product / Dot Product /Matrix Product

mul = np.dot(x,y)
print mul


x = np.array([[3,2],[2,1]])
y = np.array([[5,1],[2,1]])
mul = np.dot(x,y)
print mul