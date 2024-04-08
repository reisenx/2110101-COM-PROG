n = int(input())
list_01 = []
for i in range(n):
    number = int(input())
    list_01.append(number)

number = str(input())
if(number == ""):
    list_02 = []
else:
    list_02 = [int(e) for e in number.split()]

list_03 = []
while(True):
    number = int(input())
    if(number == -1):
        break
    else:
        list_03.append(number)

merge_list = list_01 + list_02 + list_03

backfront_list = []
for i in range(len(merge_list)):
    if(i%2 == 0):
        backfront_list.append(merge_list[i])
    else:
        backfront_list.insert(0,merge_list[i])

print(backfront_list)