# Import math library
import math

# Input a string
bd,bm,by,d,m,y = [int(e) for e in input().split()]
day = 0

# Convert year from BE to AD
by = by-543
y = y-543

# Create a list with a sum of the day in each month
# Common year is 365-day year
# Leap year is 366-day year
common_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Find duration between bd/bm/by and 31/12/by (Leap year considered)
# Leap year
if((by%400 == 0) or (by%4 == 0 and by%100 != 0)):
    day += sum(leap_year[bm:12]) + (leap_year[bm-1] - bd)
# Common year
else:
    day += sum(common_year[bm:12]) + (common_year[bm-1] - bd)

# Find duration between 01/01/(by+1) and 31/12/(y-1) (Leap year not considered)
day += (y-by-1) * 365

# Find duration between 01/01/y and d/m/y (Leap year considered)
# Leap year
if((y%400 == 0) or (y%4 == 0 and y%100 != 0)):
    day += sum(leap_year[0:m-1]) + d
# Common year
else:
    day += sum(common_year[0:m-1]) + d

# Calculate Biorhythm
physical = math.sin((2*math.pi*day)/23)
emotional = math.sin((2*math.pi*day)/28)
intellectual = math.sin((2*math.pi*day)/33)

# Output in the specific format
print(day, "{:.2f}".format(physical), "{:.2f}".format(emotional), "{:.2f}".format(intellectual))