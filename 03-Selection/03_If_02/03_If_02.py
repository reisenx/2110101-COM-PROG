# --------------------------------------------------
# File Name : 03_If_02.py
# Problem   : Change of Major
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input two students' information
ID01, GPAX01, COM01, CAL1_01, CAL2_01 = input().strip().split()
ID02, GPAX02, COM02, CAL1_02, CAL2_02 = input().strip().split()
GPAX01, GPAX02 = float(GPAX01), float(GPAX02)

# Set initial values for success of change of major
# A student must have COM equal to A and CAL at least C
success01 = COM01 == "A" and CAL1_01 <= "C" and CAL2_01 <= "C"
success02 = COM02 == "A" and CAL1_02 <= "C" and CAL2_02 <= "C"

# Output the result for each student
if success01 and success02:
    # Compare GPAX then CAL1 and CAL2
    student01 = [-GPAX01, CAL1_01, CAL2_01]
    student02 = [-GPAX02, CAL1_02, CAL2_02]
    if student01 < student02:
        print(ID01)
    elif student01 > student02:
        print(ID02)
    else:
        print("Both")

elif success01:
    print(ID01)

elif success02:
    print(ID02)

else:
    print("None")
