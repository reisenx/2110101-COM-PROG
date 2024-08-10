# Solution 2: Sliding Window Technique

# Input number of input data and pattern
pattern = str(input())
n = int(input())

# Create an empty list that collect number of repeated pattern
repeat_list = []

# Input text and find how many repeated pattern in that input text
# The repetition occurs in 1 place
# The repetition must occurs more than once, otherwise put 0 in the repeat_list
# Example: data = "TGACACACGG"; pattern = "AC"
# data = "TG[ACACAC]GG", there're 3 repetition of 'AC' in the data
# Put 3 in the repeat_list
for i in range(n):
    # Input text of each testcases
    text = str(input())
    # Create a variable to count a repeated pattern
    count = 0
    max_count = 0
    index = 0
    # For a text that shorter than the length of pattern x 2
    # It's impossible that repetition occurs more than once
    if(len(text) < 2*len(pattern)):
        repeat_list.append(0)

    # Sliding Window Technique
    # Example: text = "ABCABCABCSINCOSTANABCDX" pattern = "ABC"
    # So we start by slice a string into 3 letters and process like this
    # Loop 1: text[0:3] = "ABC" and pattern = "ABC" | count = 1 | max_count = 0
    # Loop 2: text[3:6] = "ABC" and pattern = "ABC" | count = 2 | max_count = 0
    # Loop 3: text[6:9] = "ABC" and pattern = "ABC" | count = 3 | max_count = 0
    # Loop 4: text[9:12] = "SIN" and pattern = "ABC" | count = 0 | max_count = 3
    # Loop 5: text[10:13] = "ISC" and pattern = "ABC" | count = 0 | max_count = 3
    # Loop 6: text[11:14] = "SCO" and pattern = "ABC" | count = 0 | max_count = 3
    # Loop 7: text[12:15] = "COS" and pattern = "ABC" | count = 0 | max_count = 3
    # Loop 8: text[13:16] = "OST" and pattern = "ABC" | count = 0 | max_count = 3
    # Loop 9: text[14:17] = "STA" and pattern = "ABC" | count = 0 | max_count = 3
    # Loop 10: text[15:18] = "TAN" and pattern = "ABC" | count = 0 | max_count = 3
    # Loop 11: text[16:19] = "ANA" and pattern = "ABC" | count = 0 | max_count = 3
    # Loop 12: text[17:20] = "NAB" and pattern = "ABC" | count = 0 | max_count = 3
    # Loop 13: text[18:21] = "ABC" and pattern = "ABC" | count = 1 | max_count = 3
    else:
        while(index <= len(text)-len(pattern)):
            if(text[index : index + len(pattern)] != pattern):
                if(count > max_count):
                    max_count = count
                count = 0
                index += 1
            elif(text[index : index + len(pattern)] == pattern):
                count += 1
                index += len(pattern)
        # Don't forget to check the max_count after the loop done
        if(count > max_count):
            max_count = count
        
        if(max_count < 2):
            repeat_list.append(0)
        else:
            repeat_list.append(max_count)

# Output
for item in repeat_list:
    print(item)