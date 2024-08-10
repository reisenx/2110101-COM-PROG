import numpy as np

# Calculate similarity percentage of array A and B
# - If the percentage >= p, returns True
# - If the percentage < p, returns False
def eq(A,B,p):
    # Get the boolean array that indicates similarity of each index between array A and B
    # 'similar_boolean' array have the same size with array A and B
    similar_boolean = (A == B)
    # Get percentage from finding mean of the boolean array
    # Since, False = 0 and True = 1. So percentage is mean * 100
    percentage = np.mean(similar_boolean) * 100
    # Returns a value
    if(percentage >= p):
        return True
    else:
        return False

# This function returns an array of index of 'points' in the array that have the closest distance to 'p'
# points is an 2D array that contains [[x1 y1] [x2 y2] [x3 y3] ...]
# p is an 1D array that contains [x0 y0]
def closest_point_indexes(points, p):
    # Calulate distance of each points
    distance_x = points[:,0] - p[0]
    distance_y = points[:,1] - p[1]
    distance = ((distance_x**2) + (distance_y**2))**0.5
    # Find and return an array of index that have minimum distance
    min_distance = np.min(distance)
    index = np.arange(0,len(distance))[distance == min_distance]
    return index

# A is an 1D array that contains integers
# Find number of pairs (A[i],A[j]) that A[i] > A[j] when i < j
# Example: A = [1 2 9 4 8 7]
# Loop i=0: Compare 1 to [2 9 4 8 7]
# Loop i=1: Compare 2 to [9 4 8 7]
# Loop i=2: Compare 9 to [4 8 7]
# Loop i=3: Compare 4 to [8 7]
# Loop i=4: Compare 8 to [7]
def number_of_inversions(A):
    count = 0
    for i in range(len(A)):
        count += np.sum(A[i+1:] <= A[i])
    return count

# Execute an input string
exec(input().strip())