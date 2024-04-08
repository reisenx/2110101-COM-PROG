N = 0
min_01 = 0
max_01 = 0
min_02 = 0
max_02 = 0

while(True):
    txt = str(input())
    if(txt == "Zig-Zag"):
        print(min_01,max_02)
        break
    
    elif(txt == "Zag-Zig"):
        print(min_02,max_01)
        break
    
    elif(N == 0):
        data = [int(e) for e in txt.split()]
        min_01 = data[0]
        max_01 = data[0]
        min_02 = data[1]
        max_02 = data[1]
        N += 1
    
    elif(N >= 1):
        data = [int(e) for e in txt.split()]
        if(N%2 == 1):
            min_01 = min(min_01, data[1])
            max_01 = max(max_01, data[1])
            min_02 = min(min_02, data[0])
            max_02 = max(max_02, data[0])
        elif(N%2 == 0):
            min_01 = min(min_01, data[0])
            max_01 = max(max_01, data[0])
            min_02 = min(min_02, data[1])
            max_02 = max(max_02, data[1])
        N += 1