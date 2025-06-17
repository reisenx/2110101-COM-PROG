# --------------------------------------------------
# File Name : P3_01_Gray.py
# Problem   : Part-III Gray Codes
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------


# Check if n and k are valid integers
def is_valid(n: int, k: int) -> bool:
    if n < 1 or k < 1:
        if n < 1 and k < 1:
            print("Invalid n and k")
        elif n < 1:
            print("Invalid n")
        elif k < 1:
            print("Invalid k")
        return False
    return True


# Print the number pattern based on n and k
def num_pattern(n: int, k: int) -> None:
    line = ""
    for num in range(1, k + 1):
        if num == k:
            line += f"{num}{(n - len(str(num))) * '-'}"
        else:
            line += f"{num}{(n - len(str(num)) + 1) * '-'}"
    print(line)


# Generate Gray codes for a given number of bits
def gray_codes(bits: int) -> list[str]:
    # Initialize the list with the first two Gray codes
    n = 2
    codes = ["0", "1"]
    # Generate Gray codes
    for _ in range(bits - 1):
        # Append the reverse of the current codes
        codes += codes[::-1]
        # Prefix '0' to the first half and '1' to the second half
        for i in range(n):
            codes[i] = "0" + codes[i]
            codes[n + i] = "1" + codes[n + i]
        n *= 2
    return codes


# Input n and k
n = int(input())
k = int(input())

# Check if n and k are valid
if is_valid(n, k):
    # Print the number pattern
    num_pattern(n, k)
    # Generate and print Gray codes in groups of k
    codes = gray_codes(n)
    idx = 0
    while idx < len(codes):
        print(",".join(codes[idx : idx + k]))
        idx += k
