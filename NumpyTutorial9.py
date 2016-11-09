"""
Boolean Indexing

"""

import numpy as np

A = np.array([4, 7, 3, 4, 2, 8])
print A == 4
# Check if array contains the value
B = A == 4
B.astype(np.int)

# indexing with an integer Array
C = np.array([123, 188, 190, 99, 77, 88, 100])
A = np.array([4, 7, 2, 8, 6, 9, 5])
R = C[A <= 5]  # maked 4 = 123,7=188 etc
print(R)

"""
Extract from the array np.array([3,4,6,10,24,89,45,43,46,99,100]) with Boolean masking all the number

which are not divisible by 3

which are divisible by 5

which are divisible by 3 and 5

which are divisible by 3 and set them to 42
"""

A = np.array([3, 4, 6, 10, 24, 89, 45, 43, 46, 99, 100])
div3 = A[A % 3 != 0]
print("Elements of A not divisible by 3:")
print(div3)
div5 = A[A % 5 == 0]
print("Elements of A divisible by 5:")
print(div5)
print("Elements of A, which are divisible by 3 and 5:")
print(A[(A % 3 == 0) & (A % 5 == 0)])
print("------------------")
A[A % 3 == 0] = 42  # which are divisible by 3 and set them to 42
print("""New values of A after setting the elements of A,which are divisible by 3, to 42:""")
print(A)
