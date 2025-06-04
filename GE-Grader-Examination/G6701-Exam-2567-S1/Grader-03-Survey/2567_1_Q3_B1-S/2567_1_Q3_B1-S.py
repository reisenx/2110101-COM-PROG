# Input amount of data, start time and data
dataCount, time = [int(e) for e in input().split()]
data = [float(e) for e in input().split()]

# Create a function to find mean of a list (round to 2 decimal places)
def mean(data):
    return round(sum(data)/len(data), 2)
print(data)

# Input amount of sub-data
n, mode = input().split()
n = int(n)
# Calculate the sub-data amount
if(dataCount % n > 0):
    count = (dataCount//n) + 1
else:
    count = dataCount//n

# Find sub-data and output a value
# Example: [1,2,3,2,4,5,3,4,2,3,4,6,4,3,1,3,5], time = 10 and n = 3
# > time = 10 | subData = data[0:3]   = [1,2,3]
# > time = 13 | subData = data[3:6]   = [2,4,5]
# > time = 16 | subData = data[6:9]   = [3,4,2]
# > time = 19 | subData = data[9:12]  = [3,4,6]
# > time = 22 | subData = data[12:15] = [4,3,1]
# > time = 25 | subData = data[15:18] = [3,5]
start,end = 0,n
for i in range(count):
    subData = data[start:end]
    # Output
    if(mode == "max"):
        print(time, max(subData))
    if(mode == "mean"):
        print(time, mean(subData))
    # Increase time, start and end by n
    time += n
    start += n
    end += n