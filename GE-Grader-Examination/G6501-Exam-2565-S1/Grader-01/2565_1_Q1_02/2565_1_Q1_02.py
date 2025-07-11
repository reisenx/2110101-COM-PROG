# --------------------------------------------------
# File Name : 2565_1_Q1_02.py
# Problem   : Multiplexer
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------


# Returns the minimum positive integer from a, b, c
def f1(a: int, b: int, c: int) -> int:
    positives = []
    if a > 0:
        positives += [a]
    if b > 0:
        positives += [b]
    if c > 0:
        positives += [c]
    return min(positives)


# Returns the maximum negative integer from a, b, c
def f2(a: int, b: int, c: int) -> int:
    negatives = []
    if a < 0:
        negatives += [a]
    if b < 0:
        negatives += [b]
    if c < 0:
        negatives += [c]
    return max(negatives)


# Returns the first digit of the absolute sum of a, b, c
def f3(a: int, b: int, c: int) -> str:
    sums = abs(a + b + c)
    return str(sums)[0]


# Returns the last digit of the absolute sum of a, b, c
def f4(a: int, b: int, c: int) -> str:
    sums = abs(a + b + c)
    return str(sums)[-1]


# Main function to read input and call the appropriate function based on s1 and s2
def main() -> None:
    s1, s2, a, b, c = [int(e) for e in input().split()]
    if [s1, s2] == [0, 0]:
        print(f1(a, b, c))
    elif [s1, s2] == [0, 1]:
        print(f2(a, b, c))
    elif [s1, s2] == [1, 0]:
        print(f3(a, b, c))
    elif [s1, s2] == [1, 1]:
        print(f4(a, b, c))
    else:
        print("Error")


# Execute a input string as code
exec(input().strip())
