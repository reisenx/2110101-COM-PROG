# Flowchart

# Input a string in DD MM YYYY format 
# Then split into 3 part and contain them in d,m,y variable
d,m,y = [int(e) for e in input().split()]

# Create a list of 30-day month
m30list = [4,6,9,11]

# Change the value of y to y-543
y = y-543

# Set the value of n=31
n = 31

# Condition: input month (m) is the 30-day month
# If true, change the value of n to 30
# If false, check the following condition
if(m in m30list):
    n = 30
else:
    # Condition: m = 2
    # If true, change the value of n to 28 then check the following condition
    # If false, do nothing
    if(m == 2):
        n = 28
        # Condition: y mod 400 = 0
        # If true, change the value of n to 29
        # If false, do nothing
        if(y%400 == 0):
            n = 29
        # Condition: y mod 4 = 0 and y mod 100 != 0
        # If true, change the value of n to 29
        # If false, do nothing
        if(y%4 == 0 and y%100 != 0):
            n = 29

# Change the value of d to d+15
d += 15

# Condition: d > n
# If true, Change the value of d to d-n and the value of m to m+1
# If false, do nothing
if(d > n):
    d = d-n
    m += 1

# Condition: m > 12
# If true, Change the value of m to m-12 and the value of y to y+1
# If false, do nothing
if(m > 12):
    m -= 12
    y += 1

# Change the value of y to y+543
y += 543

# Output the date in specific form
print(str(d) + "/" + str(m) + "/" + str(y))