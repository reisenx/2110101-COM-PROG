# HW2_Genetics_Analysis

# A function to count how many A,C,G,T in a string
# Return a list with number of A,C,G,T respectively
# Example: AAGAA --> [4, 0, 1, 0]
def get_acgt_count(data):
    # Set initial of count value
    countA, countC, countG, countT = 0,0,0,0
    # Counting how many A,C,G,T in the string
    for i in range(0,len(data)):
        if(data[i] == 'A'):
            countA = countA + 1
        elif(data[i] == 'C'):
            countC = countC + 1
        elif(data[i] == 'G'):
            countG = countG + 1
        elif(data[i] == 'T'):
            countT = countT + 1
    # Return as a list
    return [countA, countC, countG, countT]

# Find number of A+G divided by number of C+T and return as a float
# If C+T = 0 return -1.0
def get_ag_ct_ratio(data):
    # Get a count value using get_acgt_count() fuction
    countA, countC, countG, countT = get_acgt_count(data)
    # Calculate and return the ratio
    # If C+T = 0 then return -1.0
    if(countC + countT == 0):
        return -1.0
    else:
        ratio = float((countA + countG) / (countC + countT))
        return ratio

# Find number of G+C divided by length of the string and return as a float
def get_gc_percentage(data):
    # Get a count value using get_acgt_count() fuction
    countA, countC, countG, countT = get_acgt_count(data)
    # Calculate and return the percentage
    percentage = float((countG + countC)/(countA + countC + countG + countT))
    return percentage

# Find and return the number of pattern
# The repetition occurs in 1 place
# The repetition must occurs more than once, otherwise return 0
# Example: data = "TGACACACGG"; pattern = "AC"
# data = "TG[AC][AC][AC]GG", there're 3 repetition of 'AC' in the data
# return 3
def get_repeat_count(data, pattern):
    # Create a boolean to check if the repetition occurs
    IsRepeat = False
    # Loop the process by [length of the string divided by 2] - 1 times
    # Example: data = TGACACACGG; pattern = "AC"
    # The length of the string = 10 so the loop process 4 times
    # Loop 1: Start at checking "ACACACACAC" is in "TGACACACGG"
    # Loop 2: Start at checking "ACACACAC" is in "TGACACACGG"
    # Loop 3: Start at checking "ACACAC" is in "TGACACACGG"
    # Stops at Loop 3 and return 3
    repetition = int(len(data)//2)
    while(repetition != 1):
        if(pattern*repetition in data):
            IsRepeat = True
            break
        else:
            repetition = repetition - 1
    # If IsRepeat is true then return repetition
    # If IsRepeat is flase then return 0
    if(IsRepeat == True):
        return repetition
    elif(IsRepeat == False):
        return 0