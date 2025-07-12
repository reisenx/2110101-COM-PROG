# --------------------------------------------------
# File Name : 2565_2_Q1_01.py
# Problem   : Decryption
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------


# Rotate a string to the left by n positions
def rotate_left(num: str, n: int) -> str:
    idx = n % len(num)
    return num[idx:] + num[:idx]


# Rotate a string to the right by n positions
def rotate_right(num: str, n: int) -> str:
    idx = len(num) - (n % len(num))
    return num[idx:] + num[:idx]


# Modulo each digit of a string by a given modulus
def str_mod(num: str, mod: int) -> str:
    result = ""
    for digit in num:
        result += str(int(digit) % mod)
    return result


# Main function
def main() -> None:
    # Input a string of digits
    number = input().strip()
    # Extract the last two digits as command and n
    cmd = int(number[-2])
    n = int(number[-1])

    # Rotate left number by n positions
    if cmd == 1:
        number = rotate_left(number, n)
    # Rotate right number by n positions
    elif cmd == 2:
        number = rotate_right(number, n)
    # Modulo each digit of number by n
    elif cmd == 3:
        number = str_mod(number, n)
    # Output
    print(number)


# Execute a input string as code
exec(input().strip())
