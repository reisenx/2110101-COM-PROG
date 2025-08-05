# --------------------------------------------------
# File Name : 11_Numpy_24.py
# Problem   : Peak Indexes
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

import numpy as np


# Find the indexes of peaks in a 1D NumPy array
def peak_indexes(numbers):
    # Check if the input array has at least 3 elements
    if len(numbers) < 3:
        return []
    # Create slices for left, center, and right elements
    left = numbers[:-2]
    center = numbers[1:-1]
    right = numbers[2:]
    # Identify peaks where the center element is greater than adjacent elements
    is_peak = (center > left) & (center > right)
    peak_indices = np.arange(1, len(numbers) - 1)[is_peak]
    return peak_indices


# Main function to read input and output peak indexes
def main():
    numbers = np.array(input().split(), float)
    peak_indices = peak_indexes(numbers)
    # Output
    if len(peak_indices) > 0:
        print(", ".join(np.array(peak_indices, str)))
    else:
        print("No peaks")


# Execute an input string as code
exec(input().strip())
