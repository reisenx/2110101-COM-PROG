# --------------------------------------------------
# File Name : 02_StrList_F06.py
# Problem   : Add Vector (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------


# Create a function to add two vectors
def add_vector(u: list[float], v: list[float]) -> list[float]:
    total = [0.0, 0.0, 0.0]
    total[0] = float(u[0]) + float(v[0])
    total[1] = float(u[1]) + float(v[1])
    total[2] = float(u[2]) + float(v[2])
    return total


# Execute the input string as code
exec(input())
