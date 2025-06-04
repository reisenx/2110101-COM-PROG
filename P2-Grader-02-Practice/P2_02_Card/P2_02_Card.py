# Input a set of cards as a string and find how many cards are in the input
# Example: "AS2C4STCTDJS2S2S" is a set of 8 cards contains ["AS","2C","4S","TC","TD","JS","2S","2S"] 
text = str(input())
num = len(text)//2

# "Card Value" is the first letter of a card
# A 2 3 4 5 6 7 8 9 T  J  Q  K
# 1 2 3 4 5 6 7 8 9 10 11 12 13
# "Card Set" is the second letter of a card
# C D H S
# 1 2 3 4
value_score = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13}
set_score = {'C':1, 'D':2, 'H':3, 'S':4}

# Convert cards into a score and put it in a 'cards' list in the format
# [[Value01, Set01], [Value02, Set02], ...]
# Example: "AS2C4STCTDJS2S2S" --> [[1,4],[2,1],[4,4],[10,1],[10,2],[11,4],[2,4],[2,4]]
cards = []
for i in range(num):
    value = value_score[text[2*i]]
    set = set_score[text[2*i + 1]]
    cards.append([value,set])

# Compare (i)th card with (i+1)th card
# - Compare the "Card Value"
# - If the "Card Value" are the same, then compare "Card Set"
# - If the "Card Set" are still the same, then put 0 in to a string
# Example: "ASKSKC5H5HTD"
# > Loop 1: Compare "AS" and "KS"
#   Compare A = 1 and K = 13 --> score = "[-12]"
# > Loop 2: Compare "KS" and "KC"
#   Compare S = 4 and C = 1 --> score = "-12[+3]"
# > Loop 3: Compare "KC" and "5H"
#   Compare K = 13 and 5 --> score = "-12+3[+8]"
# > Loop 4: Compare "5H" and "5H"
#   Both cards are the same --> score = "-12+3+8[0]"
# > Loop 5: Compare "5H" and "TD"
#   Compare 5 and T = 10 --> score = "-12+3+80[-5]"
# Output: "-12+3+80-5"
score = ""
for i in range(num-1):
    value01, set01 = cards[i]
    value02, set02 = cards[i+1]
    # Compare value
    if(value01 > value02):
        score += '+' + str(value01 - value02)
    elif(value01 < value02):
        score += str(value01 - value02)
    else:
        # Compare set
        if(set01 > set02):
            score += '+' + str(set01 - set02)
        elif(set01 < set02):
            score += str(set01 - set02)
        else:
            score += '0'

# Output
print(score)