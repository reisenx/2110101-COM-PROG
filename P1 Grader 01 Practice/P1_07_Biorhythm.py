# Import math library
import math

# Input a string
bd,bm,by,d,m,y = [int(e) for e in input().split()]
day = 0

# Convert year from BE to AD
by = by-543
y = y-543

# Create a list with a sum of the day in each month
# Normal list: index 1 is 59 which is the day in January + February (31+28)
# Reversed list: index 1 is 61 which is the day in December + November (31+30)
# Common year is 365-day year
# Leap year is 366-day year
common_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
common_year_sum = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
leap_year_sum = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
reversed_common_year_sum = [31, 61, 92, 122, 153, 184, 214, 245, 275, 306, 334, 365]
reversed_leap_year_sum = [31, 61, 92, 122, 153, 184, 214, 245, 275, 306, 335, 366]

# Find duration between bd/bm/by and 31/12/by (Leap year considered)
# Leap year
if(by%400 == 0):
    if(bm!=12):
        day = day + reversed_leap_year_sum[12-bm-1] + leap_year[bm-1] - bd
    else:
        day = day + leap_year[bm-1] - bd
# Leap year
elif(by%4 == 0 and by%100 != 0):
    if(bm!=12):
        day = day + reversed_leap_year_sum[12-bm-1] + leap_year[bm-1] - bd
    else:
        day = day + leap_year[bm-1] - bd
# Common year
else:
    if(bm!=12):
        day = day + reversed_common_year_sum[12-bm-1] + common_year[bm-1] - bd
    else:
        day = day + common_year[bm-1] - bd

# Find duration between 01/01/(by+1) and 31/12/(y-1) (Leap year not considered)
day = day + ((y-by-1)*365)

# Find duration between 01/01/y and d/m/y (Leap year considered)
# Leap year
if(y%400 == 0):
    if(m!=1):
        day = day + leap_year_sum[m-2] + d
    else:
        day = day + d
# Leap year
elif(y%4 == 0 and y%100 != 0):
    if(m!=1):
        day = day + leap_year_sum[m-2] + d
    else:
        day = day + d
# Common year
else:
    if(m!=1):
        day = day + common_year_sum[m-2] + d
    else:
        day = day + d

# Calculate Biorhythm
physical = math.sin((2*math.pi*day)/23)
emotional = math.sin((2*math.pi*day)/28)
intellectual = math.sin((2*math.pi*day)/33)

# Output in the specific
print(day, "{:.2f}".format(physical), "{:.2f}".format(emotional), "{:.2f}".format(intellectual))