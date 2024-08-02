# Input a string and convert it to a float list
number = [float(e) for e in input().split()]

# Check if the index i are both greater than index i-1 and i+1
# If yes, considered it as a peak and count
peak_count = 0
for i in range(1,len(number)-1):
    if(number[i] > number[i-1] and number[i] > number[i+1]):
        peak_count += 1
    
# Output the number of peaks
print(peak_count)