def find_P(D):
    P = []
    i = 0
    for num in D[::-1]:
        if(i % 2 == 0):
            P.insert(0,num)
        else:
            P.append(num)
        i += 1
    return P

def rearrange(D):
    P = find_P(D)
    newD = []
    idx = 0
    for i in range(len(P)):
        idx += P[i]
        newD.append(D[idx % len(D)])
        D.pop(idx % len(D))
    return newD

exec(input().strip())