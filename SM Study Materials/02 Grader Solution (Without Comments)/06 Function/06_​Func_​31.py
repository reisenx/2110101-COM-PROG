def read_date():
    month_list = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    date = input().split()
    date = [int(date[0]), month_list.index(date[1]) + 1, int(date[2])]
    return date

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

def days_in_feb(y):
    if((y%400 == 0) or (y%4 == 0 and y%100 != 0)):
        return 29
    else:
        return 28

def days_in_month(m,y):
    month_day = [31, days_in_feb(y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_day[m-1]

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

def main():
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    print(zodiac(d1,m1), zodiac(d2,m2))
    print(days_in_between(d1,m1,y1,d2,m2,y2))

exec(input().strip())