# Input a string
text = str(input())

# Create a list to count how many of each number in a string
# Example: count[1] is used to count how many "1" in the srting
count = [0,0,0,0,0,0,0,0,0,0]

# Count a number in a string
for character in text:
    if("0" <= character <= "9"):
        count[int(character)] += 1

# Create a new string that contains number that missing
# Example: count = [5,0,0,0,0,9,12,3,1,7] --> missing = "1,2,3,4"
missing = ""
for i in range(0,10):
    if(count[i] == 0):
        missing = missing + str(i) + ","
# Delete the excess comma
# Example: "1,2,3,4," --> "1,2,3,4"
if(missing != ""):
    missing = missing[:-1]

# Output the missing number
# If there are no missing number, output "None"
if(missing == ""):
    print("None")
else:
    print(missing)