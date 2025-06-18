# --------------------------------------------------
# File Name : P3_05_Spiral.py
# Problem   : Part-III Spiral Square
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# List of directions to move in the spiral
# Order: Right, Up, Left, Down
DIRECTIONS = ((0, 1), (-1, 0), (0, -1), (1, 0))


# Generate an n x n spiral matrix
def spiral_square(n: int) -> list[list[int]]:
    # Create an n x n matrix filled with zeros
    matrix = [[0] * n for _ in range(n)]

    # Initialize the first number and the direction mode
    num = 1
    mode = 0

    # Starting position at the center of the matrix
    row = n // 2
    col = n // 2
    matrix[row][col] = num

    # Iterate from 1 to n-1 to define the length of each spiral arm
    for step in range(1, n):
        # Move in the current direction for 'step' times
        for _ in range(step):
            num += 1
            row += DIRECTIONS[mode][0]
            col += DIRECTIONS[mode][1]
            matrix[row][col] = num

        # Change direction for the next arm of the spiral
        mode = (mode + 1) % 4

        # Move in the current direction for 'step' times
        for _ in range(step):
            num += 1
            row += DIRECTIONS[mode][0]
            col += DIRECTIONS[mode][1]
            matrix[row][col] = num

        # Change direction for the next arm of the spiral
        mode = (mode + 1) % 4

    # Complete the final row of the spiral
    for _ in range(n - 1):
        num += 1
        row += DIRECTIONS[mode][0]
        col += DIRECTIONS[mode][1]
        matrix[row][col] = num

    # Return the completed spiral matrix
    return matrix


# Prints the matrix with formatted spacing.
def print_square(matrix: list[list[int]]) -> None:
    for row in matrix:
        print(" ".join([f"  {num}"[-3:] for num in row]))


# Execute an input string as code
exec(input().strip())
