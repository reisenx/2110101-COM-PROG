# Create a function RLE(code)
# This function can convert a string into RLE Code
def RLE(code):
    # Create empty RLE list
    RLE = []

    # If not an empty string
    if(code != ""):
        # Convert string into RLE
        # Example: ABBA --> A 1 B 2 A 1
        for i in range(0,len(code)):
            # Setup a matching character = character in index 0 and starts counting
            if(i==0):
                character = code[0]
                count = 1
            # If the current character doesn't match anymore
            # Note it in to RLE, setup a new character then reset the variable
            elif(code[i] != character):
                character_count = [character,count]
                RLE.append(character_count)
                character = code[i]
                count = 1
            # If the current character matches, then count them
            elif(code[i] == character):
                count = count + 1
        # Don't forget note the last one into RLE
        character_count = [character,count]
        RLE.append(character_count)

    # Return a list
    return RLE

#Execute the input string
exec(input())