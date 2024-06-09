
# 4.You need to perform matrix and linear algebra operations, such as matrix multiplication, 
# finding determinants, solving linear equations, and so on. (explore numpy).

# 1. Matrix Multiplication
# can be performed using 'numpy.dot' or '@' operator

import numpy as np

# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.dot(A, B)
# Or using the @ operator
C = A @ B

print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Matrix C (A * B):")
print(C)



#  2. Finding Determinants
import numpy as np

# define a matrix
A = np.array([[1, 2], [3, 4]])
# Calculate the determinant
det_A = np.linalg.det(A)

print("Matrix A:")
print(A)
print("Determinant of A:")
print(det_A)



# 3. solving linear equations
import numpy as np

# define matrix A and vector b'

A = np.array([[2,3], [1, -2]])
b = np.array([8, -4])

# solve the linear equations Ax = b

x = np.linalg.solve(A,b)

print("Matrix A:")
print(A)
print("Vector b:")
print(b)
print("Solution x (Ax = b):")
print(x)



# 4. Eigenvalue Decomposition
import numpy as np
# define a matrix
A = np.array([[1, 2], [3, 4]])
# perform eigenvalue decomposition
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Matrix A:")
print(A)
print("Eigenvalues of A:")
print(eigenvalues)
print("Eigenvectors of A:")
print(eigenvectors)



#  5. Inverse of a matrix
import numpy as np
# define a matrix
A = np.array([[1, 2], [3, 4]])
# calculate the inverse
inv_A = np.linalg.inv(A)

print("Matrix A:")
print(A)
print("Inverse of A:")
print(inv_A)