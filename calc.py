import numpy as np
import math
# Define the vector
o3 = np.array([0.866100,0.747600,0.514600]) 


# Define the matrix
matrix = np.array([
    [-5.15949960595400, 5.15949960595400, 5.15949960595400],
    [5.15949960595400, -5.15949960595400, 5.15949960595400],
    [5.15949960595400, 5.15949960595400, -5.15949960595400]
])

a = math.sqrt(3*5.1594*5.1594)*2/math.sqrt(3)

# Multiply the vector by the matrix
result = np.dot(matrix, o3)/a

print("Result of multiplication:", result)