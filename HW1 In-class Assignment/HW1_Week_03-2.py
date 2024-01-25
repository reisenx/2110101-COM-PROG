# Input a string
txt1 = str(input())
txt2 = str(input())

# Spilt data to get data
# 1.) Use split() to split data into name and date
# Example: Jane 23/3/2543 --> ["Jane", "23/3/2543"]
split1_1 = txt1.split()
split2_1 = txt2.split()
name1 = split1_1[0]
name2 = split2_1[0]
# 2.) Use split("/") to split date into day, month and year
# Example: 23/3/2543 --> ["23","3","2543"]
split1_2 = split1_1[1].split("/")
split2_2 = split2_1[1].split("/")
day1, month1, year1 = int(split1_2[0]), int(split1_2[1]), int(split1_2[2])
day2, month2, year2 = int(split2_2[0]), int(split2_2[1]), int(split2_2[2])

# Compare and Output who is older
# Check the year of brithday
if(year1 == year2):
    # If in the same year, check the month of birthday
    if(month1 == month2):
        # If in the same month, check the day of birthday
        # If both birthday is the same, print both
        if(day1 == day2):
            print(name1, name2)
        elif(day1 < day2):
            print(name1)
        elif(day2 < day1):
            print(name2)
    elif(month1 < month2):
        print(name1)
    elif(month2 < month1):
        print(name2)
elif(year1 < year2):
    print(name1)
elif(year2 < year1):
    print(name2)