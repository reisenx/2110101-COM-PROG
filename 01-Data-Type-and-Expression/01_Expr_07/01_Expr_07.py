# --------------------------------------------------
# File Name : 01_Expr_07.py
# Problem   : Body Surface Area (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math


# Calculate the body surface area using the Mosteller formula
def mosteller(W: float, H: float) -> float:
    return math.sqrt((W * H) / 3600)


# Calculate the body surface area using the Du Bois formula
def du_bois(W: float, H: float) -> float:
    return 0.007184 * (W**0.425) * (H**0.725)


# Calculate the body surface area using the Fujimoto formula
def fujimoto(W: float, H: float) -> float:
    return 0.008883 * (W**0.444) * (H**0.663)


# Main function to read input and display results
def main() -> None:
    # Read weight and height from input
    W = float(input())
    H = float(input())

    # Calculate body surface areas using different formulas
    mosteller_area = mosteller(W, H)
    du_bois_area = du_bois(W, H)
    fujimoto_area = fujimoto(W, H)

    # Print the results formatted to 2 decimal places
    print("Mosteller =", round(mosteller_area, 5))
    print("Du Bois =", round(du_bois_area, 5))
    print("Fujimoto =", round(fujimoto_area, 5))


# Execute the input string as code
exec(input())
