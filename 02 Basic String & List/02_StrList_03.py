#Input date
date = str(input())

#split a split using '/' and put it in variable t
#DD/MM/YYYY --> t[0],t[1],t[2]
t=date.split('/')

#Create a list that "January" is in index 0, "February" is in index 1 and so on
month=["January","February","March","April","May","June","July","August","September","October","November","December"]

#Output a date in the specific format
print(month[int(t[1])-1] + " " + str(t[0]) + ", " + str(t[2]))