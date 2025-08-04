# --------------------------------------------------
# File Name : 03_If_F02.py
# Problem   : Change of Major (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------


def choose(student_01, student_02):
    # Assign variables
    id_01, gpax_01, com_01, calculus1_01, calculus2_01 = student_01
    id_02, gpax_02, com_02, calculus1_02, calculus2_02 = student_02

    # Set initial values for success of change of major
    # A student must have COM equal to A and CAL at least C
    is_qualified_01 = com_01 == "A" and calculus1_01 <= "C" and calculus2_01 <= "C"
    is_qualified_02 = com_02 == "A" and calculus1_02 <= "C" and calculus2_02 <= "C"

    # Find the result of change of major
    if is_qualified_01 and is_qualified_02:
        # Compare GPAX then CAL1 and CAL2
        grades_01 = [-gpax_01, calculus1_01, calculus2_01]
        grades_02 = [-gpax_02, calculus1_02, calculus2_02]

        if grades_01 < grades_02:
            return [id_01]
        if grades_01 > grades_02:
            return [id_02]
        return [id_01, id_02]

    if is_qualified_01:
        return [id_01]

    if is_qualified_02:
        return [id_02]

    return []


# Execute the input string as code
exec(input())
