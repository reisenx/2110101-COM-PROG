def hide_vowel(w):
    h = ""
    for c in w:
        if c.lower() in 'aeiou':
            c = '*'
        h += c
    return h

def less_offensive(t,oword):
    index = 0
    end = len(oword)
    censor = ""
    while(index<len(t)):
        if(t[index:end].lower() == oword.lower()):
            censor += hide_vowel(t[index:end])
            index += len(oword)
            end += len(oword)
        else:
            censor += t[index]
            index += 1
            end +=1
    return censor

Owords = input().split()
text = input()
censor = text
for word in Owords:
    censor = less_offensive(censor,word)
print(censor)
