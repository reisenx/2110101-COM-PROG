# Solution 1: Repetition Cases Checking

# Input number of input data and pattern
pattern = str(input())
n = int(input())

# Create an empty list that collect number of repeated pattern
repeat_list = []

# Input text and find how many repeated pattern in that input text
# The repetition occurs in 1 place
# The repetition must occurs more than once, otherwise put 0 in the repeat_list
# Example: data = "TGACACACGG"; pattern = "AC"
# data = "TG[ACACAC]GG", there're 3 repetition of 'AC' in the data
# Put 3 in the repeat_list
for i in range(n):
    text = str(input())
    repeat = len(text)//len(pattern)
    # Loop the process by [length of the string divided by 2] - 1 times
    # Example: data = TGACACACGG; pattern = "AC"
    # The length of the string = 10 so the loop process 4 times
    # Loop 1: Start at checking "ACACACACAC" is in "TGACACACGG"
    # Loop 2: Start at checking "ACACACAC" is in "TGACACACGG"
    # Loop 3: Start at checking "ACACAC" is in "TGACACACGG"
    # Stops at Loop 3 and Put 3 in the repeat_list
    while(repeat >= 2):
        if(pattern*repeat in text):
            repeat_list.append(repeat)
            break
        else:
            repeat -= 1
    if(repeat < 2):
        repeat_list.append(0)

# Output
for item in repeat_list:
    print(item)