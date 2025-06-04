import numpy as np

# Multiply array M with float c
def f1(M,c):
    return M*c

# Dot Vector
def f2(U,V):
    return np.dot(U,V)

# Transpose a matrix
def f3(M):
    return M.T

# x,y,dx,dy are 1D array with same size
# k,R are float
def f4(x,y,dx,dy,k,R):
    # Check item in array and get boolean array
    neighbors = ((x-x[k])**2 + (y-y[k])**2 <= R**2)

    # Calculate sx,sy
    # True = 1 and False = 0
    sx = np.dot(neighbors,dx)
    sy = np.dot(neighbors,dy)

    # Calculate t
    t = np.arctan2(sy,sx)

    # Returns a value
    return np.cos(t), np.sin(t)

# Execute an input string k times
for k in range(int(input())):
    exec(input().strip())