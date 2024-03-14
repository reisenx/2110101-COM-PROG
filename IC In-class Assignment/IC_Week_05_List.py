# Input a string and convert it to a list of float
# Example: "20 50 90 90" --> [20.0, 50.0, 90.0, 90.0]
number = [float(e) for e in input().split()]

# Create a new list to insert an average of number i and i+1
# Example: [1.0, 3.0, 5.0, 7.0, 8.0] 
# Loop 1: (1.0 + 3.0)/2 = 2.0, insert 1.0 and 2.0 into a new list
# Loop 2: (3.0 + 5.0)/2 = 4.0, insert 3.0 and 4.0 into a new list
# Loop 3: (5.0 + 7.0)/2 = 6.0, insert 5.0 and 6.0 into a new list
# Loop 4: (7.0 + 8.0)/2 = 7.5, insert 7.0 and 7.5 into a new list
# After for loop, insert 8.0 into a list
# Output: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 7.5, 8.0]
interpolation = []
for i in range (0,len(number)-1):
    interpolation.append(number[i])
    interpolation.append((number[i] + number[i+1]) / 2)
# Insert a last number
interpolation.append(number[-1])

# Output
print(interpolation)