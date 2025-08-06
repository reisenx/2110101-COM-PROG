# --------------------------------------------------
# File Name : 01_Expr_04.py
# Problem   : Body Surface Area
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math

# Input width and height
w = float(input())
h = float(input())

# Mosteller's formula for body surface area
mosteller = math.sqrt(w * h) / 60
print(mosteller)

# Haycock's formula for body surface area
haycock = 0.024265 * (w**0.5378) * (h**0.3964)
print(haycock)

# Boyd's formula for body surface area
boyd = 0.0333 * (w ** (0.6157 - (0.0188 * math.log10(w)))) * (h**0.3)
print(boyd)
