# --------------------------------------------------
# File Name : 2565_2_Q3_02.py
# Problem   : Seating Map
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------


# Print the seating assignments in a formatted way
def print_seats(assignments, n_rows, n_cols):
    # Create a 2D list to represent the seating map
    seats = [["| -- "] * n_cols for _ in range(n_rows)]
    # Fill the seating map with the names from the assignments
    for name, pos in assignments:
        # Calculate the row and column based on the position
        r = (pos - 1) // n_cols
        c = (pos - 1) % n_cols
        # Place the name in the correct position in the seating map
        seats[r][c] = f"| {name} "

    # Print the seating map
    for row in seats:
        print("".join(row) + "|")


# Execute a input string as code
exec(input().strip())
