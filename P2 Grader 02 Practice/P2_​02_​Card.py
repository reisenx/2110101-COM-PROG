# Input a set of cards as a string and find how many cards are in the input
# Example: "AS2C4STCTDJS2S2S" is a set of 8 cards contains ["AS","2C","4S","TC","TD","JS","2S","2S"] 
cards = str(input())
c_number = len(cards)//2

# Convert cards into a number with the following citeria
# "Card Value" is the first letter of a card
# A 2 3 4 5 6 7 8 9 T  J  Q  K
# 1 2 3 4 5 6 7 8 9 10 11 12 13
# "Card Set" is the second letter of a card
# C D H S
# 1 2 3 4
c_value = []
c_set = []
for i in range(c_number):
    # Convert a string into "Card Value"
    if(cards[2*i] in "23456789"):
        c_value.append(int(cards[2*i]))
    elif(cards[2*i] == "A"):
        c_value.append(1)
    elif(cards[2*i] == "T"):
        c_value.append(10)
    elif(cards[2*i] == "J"):
        c_value.append(11)
    elif(cards[2*i] == "Q"):
        c_value.append(12)
    elif(cards[2*i] == "K"):
        c_value.append(13)
    # Convert a string into "Card Set"
    if(cards[2*i + 1] == "C"):
        c_set.append(1)
    elif(cards[2*i + 1] == "D"):
        c_set.append(2)
    elif(cards[2*i + 1] == "H"):
        c_set.append(3)
    elif(cards[2*i + 1] == "S"):
        c_set.append(4)

# Compare (i)th card with (i+1)th card
# - Compare the "Card Value"
# - If the "Card Value" are the same, then compare "Card Set"
# - If the "Card Set" are still the same, then put 0 in to a string
# Example: ASKSKC5H5HTD
# Loop 1: Compare "AS" and "KS"
# Compare A = 1 and K = 13 --> score = "[-12]"
# Loop 2: Compare "KS" and "KC"
# Compare S = 4 and C = 1 --> score = "-12[+3]"
# Loop 3: Compare "KC" and "5H"
# Compare K = 13 and 5 --> score = "-12+3[+8]"
# Loop 4: Compare "5H" and "5H"
# Both cards are the same --> score = "-12+3+8[0]"
# Loop 5: Compare "5H" and "TD"
# Compare 5 and T = 10 --> score = "-12+3+80[-5]"
# Output: "-12+3+80-5"
score = ""
for i in range(c_number-1):
    if(c_value[i] == c_value[i+1]):
        if(c_set[i] == c_set[i+1]):
            score += "0"
        elif(c_set[i] > c_set[i+1]):
            score += "+" + str(c_set[i] - c_set[i+1])
        elif(c_set[i] < c_set[i+1]):
            score += "-" + str(c_set[i+1] - c_set[i])
    elif(c_value[i] > c_value[i+1]):
        score += "+" + str(c_value[i] - c_value[i+1])
    elif(c_value[i] < c_value[i+1]):
        score += "-" + str(c_value[i+1] - c_value[i])

# Output
print(score)