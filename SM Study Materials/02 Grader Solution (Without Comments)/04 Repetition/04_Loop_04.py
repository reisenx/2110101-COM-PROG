txt = str(input())
for i in range(0,len(txt)):
    if(txt[i]=='('):
        txt = txt[:i] + '[' + txt[i+1:]
    elif(txt[i]==')'):
        txt = txt[:i] + ']' + txt[i+1:]
    elif(txt[i]=='['):
        txt = txt[:i] + '(' + txt[i+1:]
    elif(txt[i]==']'):
        txt = txt[:i] + ')' + txt[i+1:]

print(txt)