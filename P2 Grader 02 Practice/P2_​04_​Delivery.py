# Create a important dictionary
delivery_type = {'E':1, 'Q':3, 'N':7, 'F':14}
date = [31,28,31,30,31,30,31,31,30,31,30,31]
date_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
common_year = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
leap_year = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
success = {}

# Create a function that check if the year is leap year
def is_leap_year(year):
    if((year-543)%400 == 0):
        return True
    elif((year-543)%4 == 0 and (year-543)%100 != 0):
        return True
    else:
        return False

# Create a function that can find date after the specified day
# Guarantee that 'add' parameter won't be more than 14
def add_date(d,m,y,add):
    new_date = ""
    # Calculate how many days from 1/1/y to d/m/y
    # Case 1: Leap year (29-day Febuary and 366-day year)
    if(is_leap_year(y)):
        total_day = leap_year[m-2] + d + add
        # Convert total_day to DD/MM/YYYY format
        if(total_day > 366):
            new_date = str(total_day-366) + "/1/" + str(y+1)
        else:
            for i in range(0,12):
                if(leap_year[i] >= total_day):
                    new_month = i+1
                    break
            new_day = total_day - leap_year[new_month-2]
            new_date = str(new_day) + "/" + str(new_month) + "/" + str(year)
            
    # Case 2: Common year (28-day Febuary and 365-day year)
    else:
        total_day = common_year[m-2] + d + add
        # Convert total_day to DD/MM/YYYY format
        if(total_day > 365):
            new_date = str(total_day-365) + "/1/" + str(y+1)
        else:
            for i in range(0,12):
                if(common_year[i] >= total_day):
                    new_month = i+1
                    break
            new_day = total_day - common_year[new_month-2]
            new_date = str(new_day) + "/" + str(new_month) + "/" + str(year)

    # Return date in DD/MM/YYYY form
    return new_date

# Create a function that can sort date in ascending order
# Example input:["5/6/2560", "13/4/2559", "11/1/2561", "2/1/2559"]
# Example output: ["2/1/2559", "13/4/2559", "5/6/2560", "11/1/2561"]
def date_sort(d_list):
    # Convert date into a sublist [y,m,d]
    # Example: "11/11/2561" --> [2561,11,11]
    ymd_list = []
    for item in d_list:
        d,m,y = item.split('/')
        ymd_list.append([int(y),int(m),int(d)])
    # Sort the list
    ymd_list.sort()
    # Convert back to DD/MM/YYYY format
    sorted_d_list = []
    for y,m,d in ymd_list:
        sorted_d_list.append(str(d) + "/" + str(m) + "/" + str(y))
    # Return a new date list
    return sorted_d_list

# Input and read delivery order
while True:
    order = input().strip()
    if(order == "END"):
        break
    else:
        ID, order_type, day, month, year = order.split()
        day, month, year = int(day), int(month), int(year)
        IsError = False
        # Check year error (year less than 2558)
        if(year < 2558):
            error = "Invalid year"
            IsError = True
        # Check month error (month less than 1 or month more than 12)
        elif(month < 1 or month > 12):
            error = "Invalid month"
            IsError = True
        # Check date error (Invalid date, Example: 31/4/2567)
        else:
            if(is_leap_year(year)):
                if(day <= 0 or day > date_leap[month-1]):
                    error = "Invalid date"
                    IsError = True
            else:
                if(day <= 0 or day > date[month-1]):
                    error = "Invalid date"
                    IsError = True
        # Check delivery type error (Example: 'X')
        if(not IsError):
            if(order_type not in delivery_type):
                error = "Invalid delivery type"
                IsError = True
        
        # Output Error orders here because it is possible that there're orders with the same ID
        if(IsError):
            print("Error:", ID, order_type, day,month, year, "-->", error)
        
        # If not error, calcalate the delivery date of successful orders 
        if(not IsError):
            success[ID] = add_date(day, month, year, delivery_type[order_type])

# Output the sucessful order
# Find unique delivery date and put them in the list
delivery_date = []
for ID in success:
    if(success[ID] not in delivery_date):
        delivery_date.append(success[ID])
# Sort the date list
delivery_date = date_sort(delivery_date)
# Output by using delevery date list
temp_ID = []
for day in delivery_date:
    # Find ID in each date
    for ID in success:
        if(success[ID] == day):
            temp_ID.append(ID)
    # Sort ID in the same date
    temp_ID.sort()
    # Ouput order delivered in that date
    for ID in temp_ID:
        print(ID + ":", "delivered on", success[ID])
    # Reset the 'temp_ID' list
    temp_ID = []