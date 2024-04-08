code = str(input())
RLE = ""
for i in range(0,len(code)):
    if(i == 0):
        character = code[0]
        count = 1

    elif(code[i] != character):
        RLE += character + " " + str(count) + " "
        character = code[i]
        count = 1

    elif(code[i] == character):
        count += 1

RLE += character + " " + str(count) + " "
print(RLE)