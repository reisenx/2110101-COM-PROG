# This function can replace some letters in word to '*'
# Example: hide_vowel("Bitch") returns "B*t*h"
def hide_vowel(word):
    censor = ""
    for i in range(len(word)):
        if(i%2 == 0):
            censor += word[i]
        else:
            censor += '*'
    return censor

# ---------- Algorithm ----------
# Create a new string 'censor'
# Check if t[start:end] is 'offensive' until the end of the string 't'
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
# ------------------------------
offensive = input().strip()
t = input().strip()
start,end = 0, len(offensive) 
censor = ""
while(start < len(t)):
    if(t[start:end].lower() == offensive.lower()):
        censor += hide_vowel(t[start:end])
        start += len(offensive)
        end += len(offensive)
    else:
        censor += t[start]
        start += 1
        end += 1
print(censor)