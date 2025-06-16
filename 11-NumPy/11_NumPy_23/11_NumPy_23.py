# --------------------------------------------------
# File Name : 11_Numpy_23.py
# Problem   : Lower than Mean
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

import numpy as np


# Read data from input
def read_data() -> tuple:
    # Read score weight as a float array
    weight = np.array(input().split(), float)
    # Read student data as an integer array
    n = int(input())
    data = np.array([input().split() for _ in range(n)], int)
    # Return the weight and data
    return weight, data


# Report students with total score lower than the mean score
def report_lower_than_mean(weight: np.ndarray, data: np.ndarray) -> None:
    # Get the student IDs
    student_ids = data[:, 0]
    # Calculate the total score for each student
    total_score = np.dot(data[:, 1:4], weight)
    # Calculate the mean score
    mean_score = np.mean(total_score)
    # Select students with total score lower than the mean score
    # Convert student IDs to string for output
    lower_than_mean = np.array(student_ids[total_score < mean_score], str)

    # Output the result
    if len(lower_than_mean) > 0:
        print(", ".join(lower_than_mean))
    else:
        print(None)


# Execute an input string as code
exec(input().strip())
