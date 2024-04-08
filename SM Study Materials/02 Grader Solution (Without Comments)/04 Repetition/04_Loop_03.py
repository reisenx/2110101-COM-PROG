key = str(input())
answer = str(input())
score = 0

if(len(key) != len(answer)):
    print("Incomplete answer")

else:
    for i in range(0,len(key)):
        if(answer[i] == key[i]):
            score += 1
    print(score)