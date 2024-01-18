# Import string
number = str(input())

# List of digits that need to round up
roundup_list = ["5","6","7","8","9"]

# Round up a number
# Case 1: 4,5 or 7,8 or 10,11 digits
# Look at index 2 then round a number on index 1
# Example: 8456 --> 8500 or 84566 --> 85000
case1_list = [4,5,7,8,10,11]
case2_list = [6,9,12]

if(len(number) in case1_list):
    if(number[2] in roundup_list):
        number = str(int(number[0:2])+1) + (len(number)-2)*"0"
    else:
        number = str(int(number[0:2])) + (len(number)-2)*"0"

# Case 2: 6,9 or 12 digits
# Look at index 3 then round a number on index 2
# Example: 108283 --> 108000
elif(len(number) in case2_list):
    if(number[3] in roundup_list):
        number = str(int(number[0:3])+1) + (len(number)-3)*"0"
    else:
        number = str(int(number[0:3])) + (len(number)-3)*"0"

# Case 3: More than 12 digits
# Look at index -9 then round a number on index -10
# Example: 2555555555555 --> 2556000000000
elif(len(number)>12):
    if(number[-9] in roundup_list):
        number = str(int(number[0:-9])+1) + 9*"0"
    else:
        number = str(int(number[0:-9])) + 9*"0"

# Output the number in the specific form
# Case 1: 1-3 digits
# Do nothing
if(len(number)>=1 and len(number)<=3):
    print(number)

# Case 2: 4 digits
# 8456 --> 8500 --> 8.5K
elif(len(number)==4):
    print(number[0] + "." + number[1] + "K")

# Case 3: 5 digits
# 84560 --> 85000 --> 85K
elif(len(number)==5):
    print(number[0:2] + "K")

# Case 4: 6 digits
# 108283 --> 108000 --> 108K
elif(len(number)==6):
    print(number[0:3] + "K")

# Case 5: 7 digits
# 2293910 --> 2300000 --> 2.3M
elif(len(number)==7):
    print(number[0] + "." + number[1] + "M")

# Case 6: 8 digits
# 12999995 --> 13000000 --> 13M
elif(len(number)==8):
    print(number[0:2] + "M")

# Case 7: 9 digits
# 580912391 --> 581000000 --> 851M
elif(len(number)==9):
    print(number[0:3] + "M")

# Case 8: 10 digits
# 1301008191 --> 1300000000 --> 1.3B
elif(len(number)==10):
    print(number[0] + "." + number[1] + "B")

# Case 9: 11 digits
# 25555555555 --> 26000000000 --> 26B
elif(len(number)==11):
    print(number[0:2] + "B")

# Case 10: 12 digits
# 255555555555 --> 256000000000 --> 256B
elif(len(number)==12):
    print(number[0:3] + "B")

# Case 11: More than 12 digits
# 2555555555555 --> 2556000000000 --> 2556B
elif(len(number)>12):
    print(number[0:-9] + "B")