# --------------------------------------------------
# File Name : 2565_2_Q1_02.py
# Problem   : Air Quality Index (AQI)
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

# Input
aqi = [int(e) for e in input().split()]

# Output
print("AQI|1 2 3 4 5")
print("-------------")
for i in range(7):
    if aqi[i] < 25:
        print(f"{i + 1}..|+........")
    if 25 <= aqi[i] < 50:
        print(f"{i + 1}..|..+......")
    if 50 <= aqi[i] < 100:
        print(f"{i + 1}..|....+....")
    if 100 <= aqi[i] < 200:
        print(f"{i + 1}..|......+..")
    if aqi[i] >= 200:
        print(f"{i + 1}..|........+")
print("-------------")
