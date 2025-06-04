# Function bin(x)
# Return a binary number from integer x with "0b" in the front
# Example: bin(36) = 0b100100

# Function int(x, base)
# Return a integer from a string x in the specified base (default = 10)
# Example: int("69") = 69
# Example: int("0b100100",2) = 36

# Input 2 binary numbers
number = input().split()

# Find a sum of 2 binary numbers
# 1.) Covert binary numbers to integers
# 2.) Find a sum
# 3.) Convert it back to binary number
sum = int(number[0],2) + int(number[1],2)
sum = bin(sum)

# Output but not show the "0b" prefix
# Example: "0b100100" --> "100100"
print(sum[2:])