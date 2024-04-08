text = str(input())
count = [0,0,0,0,0,0,0,0,0,0]

for character in text:
    if("0" <= character <= "9"):
        count[int(character)] += 1

missing = ""
for i in range(0,10):
    if(count[i] == 0):
        missing = missing + str(i) + ","

if(missing != ""):
    missing = missing[:-1]

if(missing == ""):
    print("None")
else:
    print(missing)