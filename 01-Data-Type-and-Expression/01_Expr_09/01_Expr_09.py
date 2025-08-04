# --------------------------------------------------
# File Name : 01_Expr_09.py
# Problem   : Duration (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Constants
SECONDS_IN_MIN = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400


# Convert a string in the format HH:MM:SS to 3 integers h, m, s
def str2hms(hms_str: str) -> tuple[int, int, int]:
    h, m, s = hms_str.split(":")
    return int(h), int(m), int(s)


# Convert 3 integers h, m, s to a string in the format HH:MM:SS
def hms2str(h: int, m: int, s: int) -> str:
    time = f"0{h}"[-2:]  # Add hours with leading zero if needed
    time += f":0{m}"[-2:]  # Add minutes with leading zero if needed
    time += f":0{s}"[-2:]  # Add seconds with leading zero if needed
    return time


# Calculate total seconds from hours, minutes, and seconds
def to_sec(h: int, m: int, s: int) -> int:
    return (h * SECONDS_IN_HOUR) + (m * SECONDS_IN_MIN) + s


# Convert total seconds to hours, minutes, and seconds
def to_hms(s: int) -> tuple[int, int, int]:
    h = s // SECONDS_IN_HOUR
    s %= SECONDS_IN_HOUR
    m = s // SECONDS_IN_MIN
    s %= SECONDS_IN_MIN
    return h, m, s


# Calculate the difference between two times given in hours, minutes, and seconds
def diff(h1: int, m1: int, s1: int, h2: int, m2: int, s2: int) -> tuple[int, int, int]:
    # Convert both times to total seconds
    t1 = to_sec(h1, m1, s1)
    t2 = to_sec(h2, m2, s2)

    # Calculate the difference in seconds
    dt = (SECONDS_IN_DAY + t2 - t1) % SECONDS_IN_DAY

    # Convert the difference back to hours, minutes, and seconds
    return to_hms(dt)


# Main function to read input times, calculate the difference, and print the result
def main() -> None:
    # Read input times in the format HH:MM:SS
    hms_start = input()
    hms_end = input()

    # Convert input strings to hours, minutes, and seconds
    h1, m1, s1 = str2hms(hms_start)
    h2, m2, s2 = str2hms(hms_end)

    # Calculate the difference and convert it to a string
    dh, dm, ds = diff(h1, m1, s1, h2, m2, s2)

    # Convert the difference to a string in the format HH:MM:SS
    time = hms2str(dh, dm, ds)
    print(time)


# Execute the input string as code
exec(input())
