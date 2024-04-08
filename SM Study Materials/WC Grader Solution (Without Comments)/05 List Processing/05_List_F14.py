def peaks(number):
    peak = []
    for i in range(1,len(number)-1):
        if(number[i] > number[i-1] and number[i] > number[i+1]):
            peak.append(i)
    return peak

exec(input())