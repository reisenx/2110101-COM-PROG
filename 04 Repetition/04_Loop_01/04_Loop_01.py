# Input data, put them in the list and add it to sum
# Input data until the input = "q"
sum = 0
num_list = []
while(True):
    num_input = str(input())
    if(num_input == "q"):
        break
    else:
        num_list.append(float(num_input)) 
        sum += float(num_input)

# Calculate and output the average by divide sum by the length of the list
# Don't forget to round the decimal to 2 digits
# If there's no data in the list, output "No Data"
if(len(num_list) > 0):
    print(round(sum/len(num_list), 2))
else:
    print("No Data")