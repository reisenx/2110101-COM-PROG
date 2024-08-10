# Chulalongkorn Univerity student ID
# 1.) The ID has 10 digits
# 2.) Consider 3rd digit of the student ID
# 2.1.) 0,3 or 4 is undergraduate student
# 2.2.) 1,7 or 8 is graduate student
# 3.) Consider the 9th and 10th digits
# 3.1.) 21 is Engineering student (ENG)
# 3.2.) 22 is Arts student (ART)
# 3.3.) 23 is Science student (SCI)

# This function can check if the student ID is undergraduate or not
def is_undergrad(sid):
    sid = str(sid)
    if(sid[2] in "034"):
        return True
    else:
        return False

# This function can check the faculty by student ID
# Assume that the input student ID always exists
def get_faculty(sid):
    sid = str(sid)
    if(sid[8:10] == '21'):
        return "ENG"
    elif(sid[8:10] == '22'):
        return "ART"
    elif(sid[8:10] == '23'):
        return "SCI"
    else:
        return "OTHER"

# This function can check if the student is undergraduate (U) or graduate (G) and their faculty
# Assume that the input student ID always exists
def get_status(sid):
    sid = str(sid)
    if(is_undergrad(sid)):
        return ['U', get_faculty(sid)]
    else:
        return ['G', get_faculty(sid)]

# Execute an input string
exec(input().strip())