num = str(input())
odd_digit = ['1','3','5','7','9']
even_digit = ['0','2','4','6','8']

if(num == "0"):
    print("zero")
elif(num[0] == '-'):
    print("negative")
else:
    print("positive")

if(num[-1] in even_digit):
    print("even")
elif(num[-1] in odd_digit):
    print("odd")