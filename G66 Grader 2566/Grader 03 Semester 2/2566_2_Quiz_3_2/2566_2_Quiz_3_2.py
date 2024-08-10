def read_friends():
    dat = []
    N = int(input())
    for i in range(N):
        dat.append(tuple(input().strip().split()))
    return dat

# [('A', 'B'), ('C', 'D')]
# Convert it to {'A':{'B'}, B:{'A'}, ...}
def tuple_to_dict(data):
    friends = {}
    for name01,name02 in data:
        if(name01 not in friends):
            friends[name01] = {name02}
        else:
            friends[name01].add(name02)
        if(name02 not in friends):
            friends[name02] = {name01}
        else:
            friends[name02].add(name01)
    return friends
                
def count_friends(data, names):
    friends = tuple_to_dict(data)
    count = []
    for item in names:
        if(item in friends):
            count.append((item, len(friends[item])))
        else:
            count.append((item, 0))
    count.sort()
    return count

exec(input().strip())