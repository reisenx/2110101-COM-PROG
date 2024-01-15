#Create a list with a sum of the day in each month
#Example in index 1 is 59 which is the day in January + February (31+28)
#Common year is 365-day year
#Leap year is 366-day year
common_year = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
leap_year = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]

#Create day_of_year(D,M,Y) funbction
def day_of_year(D,M,Y):
    #Convert from BE to AD
    Y = Y-543
    
    #Check if the year is the leap year or not
    #if M=1, Output the D
    #else, Calculate by add sum of days in the previous month (in the list) + days in the current month 
    if(M!=1):
        #Case 1: Leap year (Y mod 400 = 0)
        if(Y%400 == 0):
            return leap_year[M-2]+D
        #Case 2: Leap year (Y mod 4 = 0 but Y mod 100 != 0)
        elif(Y%4 == 0 and Y%100!=0):
           return leap_year[M-2]+D
        #Case 3: Common year
        else:
            return common_year[M-2]+D
    else:
        return D

#Execute the input string
exec(input())