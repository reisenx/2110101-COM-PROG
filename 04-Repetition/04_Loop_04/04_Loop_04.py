# Input a string
txt = str(input())

# Replace the parentheses
# 1. Replace ( with [
# 2. Replace ) with ]
# 3. Replace [ with (
# 4. Replace ] with )
for i in range(0,len(txt)):
    if(txt[i]=='('):
        txt = txt[:i] + '[' + txt[i+1:]
    elif(txt[i]==')'):
        txt = txt[:i] + ']' + txt[i+1:]
    elif(txt[i]=='['):
        txt = txt[:i] + '(' + txt[i+1:]
    elif(txt[i]==']'):
        txt = txt[:i] + ')' + txt[i+1:]

# Output modifided text
print(txt)