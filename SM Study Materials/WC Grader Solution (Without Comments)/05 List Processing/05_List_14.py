number = [float(e) for e in input().split()]

peak_count = 0
for i in range(1,len(number)-1):
    if(number[i] > number[i-1] and number[i] > number[i+1]):
        peak_count += 1
    
print(peak_count)