def RLE(code):
    RLE = []
    if(code != ""):
        for i in range(0,len(code)):
            if(i == 0):
                character = code[0]
                count = 1

            elif(code[i] != character):
                character_count = [character,count]
                RLE.append(character_count)
                character = code[i]
                count = 1

            elif(code[i] == character):
                count += 1

        character_count = [character,count]
        RLE.append(character_count)
    return RLE

exec(input())