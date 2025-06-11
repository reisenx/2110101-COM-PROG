# --------------------------------------------------
# File Name : 03_If_F02.py
# Problem   : Change of Major (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------


def choose(stu1: list, stu2: list) -> list:
    # Initialize the result list
    result = []

    # Set initial values for success of change of major
    # A student must have COM equal to A and CAL at least C
    success01 = stu1[2] == "A" and stu1[3] <= "C" and stu1[4] <= "C"
    success02 = stu2[2] == "A" and stu2[3] <= "C" and stu2[4] <= "C"

    # Find the result of change of major
    if success01 and success02:
        # Compare GPAX then CAL1 and CAL2
        student01 = [-stu1[1], stu1[3], stu1[4]]
        student02 = [-stu2[1], stu2[3], stu2[4]]
        if student01 < student02:
            result += [stu1[0]]
        elif student01 > student02:
            result += [stu2[0]]
        else:
            result += [stu1[0], stu2[0]]

    elif success01:
        result += [stu1[0]]

    elif success02:
        result += [stu2[0]]

    return result


# Execute the input string as code
exec(input())
