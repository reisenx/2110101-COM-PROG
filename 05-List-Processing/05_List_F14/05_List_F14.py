def peaks(number):
    # Check if the index i are both greater than index i-1 and i+1
    # If yes, considered it as a peak and put an index to a list
    peak = []
    for i in range(1,len(number)-1):
        if(number[i] > number[i-1] and number[i] > number[i+1]):
            peak.append(i)
    
    # Output the number of peaks
    return peak

# Execute a input string
exec(input())