<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Spiral Square ★★★☆ (
      <a href="https://drive.google.com/file/d/1R_KGdDjiZfEVLHv9dntXGvGLEBCq6aeb/view?usp=drive_link">
        <code>P3_05_Spiral</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**Solution**](#solution)

---

<div align="center">
  <h2>เฉลยอย่างละเอียดจะตามมาทีหลัง</h2>
</div>

---

# Solution

```python
# --------------------------------------------------
# File Name : P3_05_Spiral.py
# Problem   : Part-III Spiral Square
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------

# List of directions to move in the spiral
# Order: Right, Up, Left, Down
DIRECTIONS = ((0, 1), (-1, 0), (0, -1), (1, 0))


# Generate an n x n spiral matrix
def spiral_square(n):
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
def print_square(matrix):
    for row in matrix:
        print(" ".join([f"  {num}"[-3:] for num in row]))


# Execute an input string as code
exec(input().strip())
```
