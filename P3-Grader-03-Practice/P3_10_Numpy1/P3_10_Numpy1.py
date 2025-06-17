# --------------------------------------------------
# File Name : P3_10_Numpy.py
# Problem   : Part-III NumPy Functions
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

import numpy as np


# Calculate percentage of equal elements between two arrays
# Return True if the percentage is greater than or equal to the target, otherwise False
def eq(A: np.ndarray, B: np.ndarray, target: int) -> bool:
    percentage = np.mean(A == B) * 100
    return percentage >= target


# Get indexes of the closest points in a 2D array to a target point
def closest_point_indexes(points: np.ndarray, target: np.ndarray) -> np.ndarray:
    # Calculate the distance from each point to the target
    distance_x = points[:, 0] - target[0]
    distance_y = points[:, 1] - target[1]
    distances = ((distance_x**2) + (distance_y**2)) ** 0.5
    # Find the indices of the points with the minimum distance
    indices = np.arange(len(distances))[distances == np.min(distances)]
    return indices


# Count the number of inversions in an array
# A pair (i, j) is an inversion if i < j and A[i] > A[j]
def number_of_inversions(A: np.ndarray) -> int:
    count = 0
    for i in range(len(A)):
        count += np.sum(A[i] > A[i + 1 :])
    return count


# Execute an input string as code
exec(input().strip())
