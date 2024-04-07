# Input date
date = str(input())

# Split a split using '/' and put it in variable d,m,y
# DD/MM/YYYY --> d,m,y
d,m,y = date.split('/')

# Create a list that "January" is in index 0, "February" is in index 1 and so on
month_name = ["January","February","March","April","May","June","July","August","September","October","November","December"]

# Output a date in the specific format
print(month_name[int(m)-1] + " " + d + ", " + y)