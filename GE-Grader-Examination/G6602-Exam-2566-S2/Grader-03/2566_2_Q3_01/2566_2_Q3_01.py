# --------------------------------------------------
# File Name : 2566_2_Q3_01.py
# Problem   : Peak 2D
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------


# Read input data and return a list of lists of integers.
def read_data() -> list[list[int]]:
    data = []
    rows = int(input())
    for _ in range(rows):
        data.append([int(num) for num in input().strip().split()])
    return data


# Count the number of peak elements in a 2D grid.
def count_peak(data: list[list[int]]) -> int:
    # Initialize the peak count to zero.
    ans = 0
    # Get the number of rows in the data.
    rows = len(data)
    # Iterate through the data, skipping the first and last rows and columns.
    for r in range(1, rows - 1):
        # Get the number of columns in the current row.
        cols = len(data[r])
        for c in range(1, cols - 1):
            # Check if the current element is greater than its four neighbors.
            if (
                data[r][c] > data[r - 1][c]
                and data[r][c] > data[r + 1][c]
                and data[r][c] > data[r][c - 1]
                and data[r][c] > data[r][c + 1]
            ):
                # If it is, increment the peak count.
                ans += 1
    # Return the total count of peak elements.
    return ans


# Execute the input string as code
exec(input().strip())
