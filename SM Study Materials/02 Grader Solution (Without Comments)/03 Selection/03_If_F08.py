common_year = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
leap_year = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]

def day_of_year(D,M,Y):
    Y = Y-543
    if(M != 1):
        if(Y%400 == 0):
            return leap_year[M-2]+D
        elif(Y%4 == 0 and Y%100!=0):
            return leap_year[M-2]+D
        else:
            return common_year[M-2]+D
    else:
        return D

exec(input())