# This function can replace all vowels ('a','e','i','o','u') to '*'
# Example: hide_vowel("FuCk sHiT") returns "F*Ck sH*T"
def hide_vowel(w):
    h = ""
    for c in w:
        if c.lower() in 'aeiou':
            c = '*'
        h += c
    return h

# This function can censor 'oword' that appears in 't'
# Example: less_offensive("He's so full of crap.","Crap") returns "He's so full of cr*p."

# Algorithm
# Create a new string 'censor'
# Check if t[start:end] is 'oword' until the end of the string 't' 
# - If yes, add censored t[start:end] to 'censor' and increase start and end by len(oword)
# - If no, add t[start] to 'censor' and increase start and end by 1

# Example: less_offensive("He's so full of crap.","Crap")
# Loop 1: t[0:4] = "[He's] so full of crap." --> censor = "H"
# Loop 2: t[1:5] = "H[e's ]so full of crap." --> censor = "He"       
# Loop 3: t[2:6] = "He['s s]o full of crap." --> censor = "He'"      
# ...
# Loop 16: t[15:19] = "He's so full of[ cra]p." --> censor = "He's so full of "
# Loop 17: t[16:20] = "He's so full of [crap]." --> censor = "He's so full of cr*p" (Added 'cr*p' to censor)
# Loop 18: t[20:24] = "He's so full of crap[.]" --> censor = "He's so full of cr*p."
# Loop 19: t[21:25] --> break (start = 21 and len(t) = 21)
def less_offensive(t,oword):
    start = 0
    end = len(oword)
    censor = ""
    while(start < len(t)):
        if(t[start:end].lower() == oword.lower()):
            censor += hide_vowel(t[start:end])
            start += len(oword)
            end += len(oword)
        else:
            censor += t[start]
            start += 1
            end += 1
    return censor

# Input offensive words and split them to a list
Owords = input().split()
# Input a text that need to be censored
text = input()
# Censor each word in a 'Owords' list
# Example: Owords = ['crap', 'DAMN'] and censor = "!!!CrapDAMNcRAPdamn_crab_darn!!!"
# 1.) less_offensive(censor, 'crap') returns censor = "!!!Cr*pDAMNcR*Pdamn_crab_darn!!!"
# 2.) less_offensive(censor, 'DAMN') returns censor = "!!!Cr*pD*MNcR*Pd*mn_crab_darn!!!"
censor = text
for word in Owords:
    censor = less_offensive(censor,word)
# Output
print(censor)