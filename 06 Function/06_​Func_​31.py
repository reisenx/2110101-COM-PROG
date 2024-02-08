# Create a function read_date()
# This function can convert a date string a list with [D,M,Y]
# Example: "1 Jan 2017" --> [1,1,2017]
def read_date():
    month_list = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    date = input().split()
    date = [int(date[0]), month_list.index(date[1]) + 1, int(date[2])]
    return date

# Create a function zodiac(d,m)
# This function can return a zodiac of input day and month
def zodiac(d,m):
    if d >= 22 and m==3 or d <=21 and m==4 : zodiac = "Aries"
    elif d >= 22 and m==4 or d <=21 and m==5 : zodiac = "Taurus"
    elif d >= 22 and m==5 or d <=21 and m==6 : zodiac = "Gemini"
    elif d >= 22 and m==6 or d <=21 and m==7 : zodiac = "Cancer"
    elif d >= 22 and m==7 or d <=21 and m==8 : zodiac = "Leo"
    elif d >= 22 and m==8 or d <=21 and m==9 : zodiac = "Virgo"
    elif d >= 22 and m==9 or d <=21 and m==10 : zodiac = "Libra"
    elif d >= 22 and m==10 or d <=21 and m==11 : zodiac = "Scorpio"
    elif d >= 22 and m==11 or d <=21 and m==12 : zodiac = "Sagittarius"
    elif d >= 22 and m==12 or d <=20 and m==1 : zodiac = "Capricorn"
    elif d >= 21 and m==1 or d <=20 and m==2 : zodiac = "Aquarius"
    elif d >= 21 and m==2 or d <=21 and m==3 : zodiac = "Pisces"
    return zodiac


# Create a function days_in_feb(y)
# This function can check if there's 28 days or 29 days in Febuary in that year
# Leap year condition (A year with 366 days)
# 1.) That year must be divisible by 400
# 2.) If not, That year must be divisible by 4 and must not divisble by 100
# 3.) Else, it is a common year (365 days)
# Example: days_in_feb(2016) = 29
def days_in_feb(y):
    if(y%400 == 0):
        return 29
    elif(y%4 == 0 and y%100 != 0):
        return 29
    else:
        return 28

# Create a function days_in_month(m,y)
# This function can return number of days in input month and year
# Example: days_in_month(2,2017) = 28
def days_in_month(m,y):
    month_day = [31, days_in_feb(y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_day[m-1]

# Create a function days_in_between(d1,m1,y1,d2,m2,y2)
# This function can retuen number of days between d1/m1/y1 and d2/m2/y2 
def days_in_between(d1,m1,y1,d2,m2,y2):
    days = 0
    for month in range(2,13):
        if(m1 < month):
            days += days_in_month(month,y1)
    for month in range(1,12):
        if(m2 > month):
            days += days_in_month(month,y2)
    days += (days_in_month(m1,y1) - d1 + 1) + int((y2 - y1 - 1)*365.25) + (d2 - 1)
    return days

# Create a main() function
# This function can return a zodiac of 2 dates and number of day between 2 dates
def main():
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    print(zodiac(d1,m1), zodiac(d2,m2))
    print(days_in_between(d1,m1,y1,d2,m2,y2))

# Execute the input string
exec(input().strip())