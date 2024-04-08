number = str(input())
roundup_list = ['5','6','7','8','9']

case1_list = [4,5,7,8,10,11]
case2_list = [6,9,12]

if(len(number) in case1_list):
    if(number[2] in roundup_list):
        number = str(int(number[0:2])+1) + (len(number)-2)*"0"
    else:
        number = str(int(number[0:2])) + (len(number)-2)*"0"

elif(len(number) in case2_list):
    if(number[3] in roundup_list):
        number = str(int(number[0:3])+1) + (len(number)-3)*"0"
    else:
        number = str(int(number[0:3])) + (len(number)-3)*"0"

elif(len(number) > 12):
    if(number[-9] in roundup_list):
        number = str(int(number[0:-9])+1) + 9*"0"
    else:
        number = str(int(number[0:-9])) + 9*"0"

if(len(number) >= 1 and len(number) <= 3):
    print(number)

elif(len(number) == 4):
    print(number[0] + "." + number[1] + "K")

elif(len(number) == 5):
    print(number[0:2] + "K")

elif(len(number) == 6):
    print(number[0:3] + "K")

elif(len(number) == 7):
    print(number[0] + "." + number[1] + "M")

elif(len(number) == 8):
    print(number[0:2] + "M")

elif(len(number) == 9):
    print(number[0:3] + "M")

elif(len(number) == 10):
    print(number[0] + "." + number[1] + "B")

elif(len(number) == 11):
    print(number[0:2] + "B")

elif(len(number) == 12):
    print(number[0:3] + "B")

elif(len(number) > 12):
    print(number[0:-9] + "B")