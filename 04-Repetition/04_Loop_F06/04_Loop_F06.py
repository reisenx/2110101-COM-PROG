# --------------------------------------------------
# File Name : 04_Loop_F06.py
# Problem   : Print Triangle (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------


# Construct a function to print a triangle pattern
def print_triangle(h: int) -> None:
    triangle = ""
    for i in range(h - 1):
        # Add leading dots
        triangle += "." * (h - i - 1)
        # Add the first star
        triangle += "*"
        # Add dots between stars and the second star
        if i > 0:
            triangle += "." * ((2 * i) - 1)
            triangle += "*"
        # Add newline character
        triangle += "\n"
    # Add base of the triangle
    triangle += "*" * ((2 * h) - 1)

    # Output the triangle
    print(triangle)


# Execute the input string as code
exec(input())
