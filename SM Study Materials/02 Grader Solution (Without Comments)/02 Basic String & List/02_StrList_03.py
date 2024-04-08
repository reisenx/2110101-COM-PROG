date = str(input())
d,m,y = date.split('/')
month_name = ["January","February","March","April","May","June","July","August","September","October","November","December"]
print(month_name[int(m)-1] + " " + d + ", " + y)