filename = input().strip()
file = open(filename,"r")

words = []
for line in file:
    line = line.strip()
    if(line != ""):
        temp = line.split("_")
        for item in temp:
            words.append(item)

print("-"*50)
start = 0
end = 0
while(start < len(words)):
    line = "_".join(words[start:end])
    if(len(line) <= 50 and end > len(words)):
        print("_".join(words[start:end-1]))
        break
    elif(len(line) <= 50):
        end += 1
    else:
        print("_".join(words[start:end-1]))
        start = end - 1
        end = end - 1

file.close()