# --------------------------------------------------
# File Name : 05_List_F14.py
# Problem   : Peaks (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Create a function to find index of peaks in a list of numbers
def peaks(numbers: list) -> list:
    peaks = []
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            peaks.append(i)
    return peaks


# Execute the input string as code
exec(input())
