# --------------------------------------------------
# File Name : 11_Numpy_22.py
# Problem   : Outer Product
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

import numpy as np


# Calculate the multiplication table of size rows x cols
def mult_table(rows, cols):
    row = np.arange(1, rows + 1).reshape(-1, 1)
    col = np.arange(1, cols + 1)
    return row * col


# Execute an input string as code
exec(input().strip())
