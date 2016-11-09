"""
Copying Arrays - Return an array copy of the given object 'obj'.
Identity Array -


"""
import numpy as np

""""
The possible values are {'C', 'F', 'A', 'K'}. This parameter controls the memory layout of the copy. 'C' means C-order,
'F' means Fortran-order, 'A' means 'F' if the object 'obj' is Fortran contiguous,
'C' otherwise. 'K' means match the layout of 'obj' as closely as possible.
numpy.copy()
Output:
[[1001   22   12]
 [  44   53   66]]
[[42 22 12]
 [44 53 66]]
"""
x = np.array([[42,22,12],[44,53,66]], order='F')
y = x.copy()
x[0,0] = 1001
print(x)
print(y)

# Identity Array
"""
An identity array is a square array with ones on its main diagonal. There are two ways to create identity array.
Output :
array([[ 1.,  0.,  0.,  0.],
       [ 0.,  1.,  0.,  0.],
       [ 0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  1.]])
"""

np.identity(4)
