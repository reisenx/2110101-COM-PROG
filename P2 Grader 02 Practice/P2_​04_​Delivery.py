# Create important dictionary and list
common_year = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
delivery_type = {'E':1, 'Q':3, 'N':7, 'F':14}
success = []

# Check leap year (Don't forget to convert from B.E. to A.D.)
def IsLeapYear(year):
    return ((year-543)%400 == 0) or ((year-543)%100 != 0 and (year-543)%4 == 0)

# This function can check if the order is error or not
# 'order' contains [ID] [Type] [Day] [Month] [Year]
# 1.) Invalid year: Year less than 2558
# 2.) Invaid month: Month doesn't exist
# 3.) Invalid date: Date doesn't exist
# 4.) Invalid delivery type: Type is not in ['E','Q','N','F']
def IsError(order):
    # Get value from parameter
    ID, type, day, month, year = order.strip().split()
    day, month, year = int(day), int(month), int(year)
    
    # 1.) Invalid year
    if(year < 2558):
        print("Error:", ID, type, day, month, year, "--> Invalid year")
        return True
    
    # 2.) Invalid month
    if(month < 1 or month > 12):
        print("Error:", ID, type, day, month, year, "--> Invalid month")
        return True
    
    # 3.) Invalid date
    # 3.1) Leap year
    if(IsLeapYear(year)):
        if(day < 1 or day > leap_year[month-1]):
            print("Error:", ID, type, day, month, year, "--> Invalid date")
            return True
    # 3.2) Common year
    else:
        if(day < 1 or day > common_year[month-1]):
            print("Error:", ID, type, day, month, year, "--> Invalid date")
            return True
    
    # 4.) Invalid delivery type
    if(type not in delivery_type):
        print("Error:", ID, type, day, month, year, "--> Invalid delivery type")
        return True
    
    # If the order is not error, it will return this
    return False

# This function can add date by delivery type
# Example: Add(28,12,2560,'F') returns (11,1,2561)
def AddDate(day,month,year,type):
    # Calculate days from 1/1/year to day/month/year
    # Case 1: Leap year
    if(IsLeapYear(year)):
        days = sum(leap_year[0 : month-1]) + day
    # Case 2: Common year
    else:
        days = sum(common_year[0 : month-1]) + day
    
    # Add days by delivery type
    days += delivery_type[type]

    # Convert back day,month,year value
    # Case 1: Leap year
    if(IsLeapYear(year)):
        # In case of 'days' exceed 366
        if(days > 366):
            days -= 366
            year += 1
        # Find new 'day' and 'month'
        for m in range(13):
            if(days <= sum(leap_year[0:m])):
                month = m
                day = days - sum(leap_year[0:m-1])
                break
    # Case 2: Common year
    else:
        # In case of 'days' exceed 365
        if(days > 365):
            days -= 365
            year += 1
        # Find new 'day' and 'month'
        for m in range(13):
            if(days <= sum(common_year[0:m])):
                month = m
                day = days - sum(common_year[0:m-1])
                break
    
    # Returns new day,month,year value
    return day,month,year

# This function can convert day,month,year to DD/MM/YYYY format
def DateFormat(day,month,year):
    return str(day) + "/" + str(month) + "/" + str(year)

# Input orders
while(True):
    order = input().strip()
    if(order != "END"):
        # Input order that is not error in 'success' list in the format
        # success = [[Year, Month, Date, ID], ...]
        if(not IsError(order)):
            # Get value from input
            ID, type, day, month, year = order.strip().split()
            day, month, year = int(day), int(month), int(year)
            
            # Add date by delivery type
            day,month,year = AddDate(day,month,year,type)

            # Store a data in 'success' list
            success.append([year,month,day,ID])
    
    # Break the loop if input = "END"
    else:
        break

# Sort 'success' by year, month, day then ID
# Example: [[2561,5,11,'10008'], [2559,12,31,'10005'], [2560,1,1,'10010']]
# After sorting: [[2559,12,31,'10005'], [2560,1,1,'10010'], [2561,5,11,'10008']]
success.sort()

# Output
for year,month,day,ID in success:
    print(ID + ": delivered on " + DateFormat(day,month,year))