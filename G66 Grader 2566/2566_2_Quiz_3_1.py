def read_data():
    dat = []
    R = int(input())
    for r in range(R):
        dat.append([int(e) for e in input().strip().split()])
    return dat

def count_peak(data):
    count = 0
    nrow = len(data)
    ncol = len(data[0])
    for i in range(1,nrow-1):
        for j in range(1,ncol-1):
            if(data[i][j] > data[i-1][j] and data[i][j] > data[i+1][j] and data[i][j] > data[i][j-1] and data[i][j] > data[i][j+1]):
                count += 1
    return count

exec(input().strip())