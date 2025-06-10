# --------------------------------------------------
# File Name : 01_Expr_04.py
# Problem   : Body Surface Area
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math

# Input width and height
W = float(input())
H = float(input())

# Mosteller's formula for body surface area
mosteller = math.sqrt(W * H) / 60
print(mosteller)

# Haycock's formula for body surface area
haycock = 0.024265 * (W**0.5378) * (H**0.3964)
print(haycock)

# Boyd's formula for body surface area
boyd = 0.0333 * (W ** (0.6157 - (0.0188 * math.log10(W)))) * (H**0.3)
print(boyd)
