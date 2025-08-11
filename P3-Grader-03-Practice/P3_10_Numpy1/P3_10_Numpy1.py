# --------------------------------------------------
# File Name : P3_10_Numpy1.py
# Problem   : Part-III NumPy Functions
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------

import numpy as np


# Calculate percentage of equal elements between two arrays
# Return True if the percentage is greater than or equal to the target, otherwise False
def eq(a, b, target):
    percentage = np.mean(a == b) * 100
    return percentage >= target


# Get indexes of the closest points in a 2D array to a target point
def closest_point_indexes(points, target):
    # Calculate the distance from each point to the target
    distances_x = (points[:, 0] - target[0]) ** 2
    distances_y = (points[:, 1] - target[1]) ** 2
    squared_distances = distances_x + distances_y

    # Return the indices of the points with the minimum distance
    return np.arange(len(squared_distances))[
        squared_distances == np.min(squared_distances)
    ]


# Count the number of inversions in an array
# A pair (i, j) is an inversion if i < j and A[i] > A[j]
def number_of_inversions(a):
    count = 0
    for i in range(len(a)):
        count += np.sum(a[i] > a[i + 1 :])
    return count


# Execute an input string as code
exec(input().strip())
