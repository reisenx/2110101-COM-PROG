# --------------------------------------------------
# File Name : 2567_1_Q2_B1-S.py
# Problem   : Median of Median of K
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------


# Function to calculate the median of a unsorted list
def get_median(unsorted_nums):
    # Sort the list in ascending order
    nums = sorted(unsorted_nums)

    # Get the length of the list and middle index
    n = len(nums)
    mid = n // 2

    # Return the median value of the even length list
    if n % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2

    # Return the median value of the odd length list
    return float(nums[mid])


# Input k and the list of integers
k = int(input())
nums = [int(num) for num in input().split()]

# Initialize a list to store medians of each k-sized segment
medians = []

# Calculate the median for each segment of size k
for idx in range(0, len(nums), k):
    medians.append(get_median(nums[idx : idx + k]))

# Calculate and print the median of the medians
print(get_median(medians))
