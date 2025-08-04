# --------------------------------------------------
# File Name : 03_If_02.py
# Problem   : Change of Major
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input two students' information
data = input().strip().split()
id_01, com_01, calculus1_01, calculus2_01 = data[0], data[2], data[3], data[1]
gpax_01 = float(data[1])

data = input().strip().split()
id_02, com_02, calculus1_02, calculus2_02 = data[0], data[2], data[3], data[1]
gpax_02 = float(data[1])

# Set initial values for success of change of major
# A student must have COM equal to A and CALCULUS at least C
is_qualified_01 = (com_01 == "A") and (calculus1_01 <= "C") and (calculus2_01 <= "C")
is_qualified_02 = (com_02 == "A") and (calculus1_02 <= "C") and (calculus2_02 <= "C")

# Output the result for each student
if is_qualified_01 and is_qualified_02:
    # Compare GPAX then CALCULUS 1 and CALCULUS 2
    student_01 = [-gpax_01, calculus1_01, calculus2_01]
    student_02 = [-gpax_02, calculus1_02, calculus2_02]
    if student_01 < student_02:
        print(id_01)
    elif student_01 > student_02:
        print(id_02)
    else:
        print("Both")

elif is_qualified_01:
    print(id_01)

elif is_qualified_02:
    print(id_02)

else:
    print("None")
