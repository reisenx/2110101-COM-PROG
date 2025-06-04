# Unofficial
# Summer 2023 Longest Repeating Characters

# Example
# > Input: AAABBCCCXXXXXAAAAYYZZZ
# > Output: X 5

# Input a text
text = input().strip()

# Setup initial value
# Setup 'letter' as the first character in a 'text'
letter = text[0]
count = 1
letter_count = []

# Consider the remaining character in a 'text'
# Example:
# > text = "AAABBCCCXXXXXAAAAYYZZZ"
# > letter_count = [[3, 'A'], [2, 'B'], [3, 'C'], [5, 'X'], [4, 'A'], [2, 'Y'], [3, 'Z']]
for char in text[1:]:
    # Case 1: Current character is not matching with the 'letter'
    # Put a data in letter_count and reset 'letter' and 'count' value
    if(char != letter):
        letter_count.append([count, letter])
        letter = char
        count = 1
    
    # Case 2: Current character is matching with the 'letter'
    # Just add the 'count' value by 1
    else:
        count += 1
# Don't forget to append the last one
letter_count.append([count, letter])

# Sorting 'letter_count'
# Example: [[2, 'B'], [2, 'Y'], [3, 'A'], [3, 'C'], [3, 'Z'], [4, 'A'], [5, 'X']]
letter_count.sort()

# Output
# The answer is the last sublist of 'letter_count'
letter, count = letter_count[-1][1], letter_count[-1][0]
print(letter, count)

# -- Testcase --
# Input  1: AAABBCCCXXXXXAAAAYYZZZ
# Output 1: X 5
# Input  2: RRRRRRYYZZZABCRRRP
# Output 2: R 6
# Input  3: QWILYYAPN
# Output 3: Y 2
# Input  4: TPPMMMD0CCCC
# Output 4: C 4