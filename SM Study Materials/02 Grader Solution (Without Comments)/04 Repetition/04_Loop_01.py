sum = 0
num_list = []
while(True):
    num_input = str(input())
    if(num_input == "q"):
        break
    else:
        num_list.append(float(num_input)) 
        sum += float(num_input)

if(len(num_list) > 0):
    print(round(sum/len(num_list), 2))
else:
    print("No Data")