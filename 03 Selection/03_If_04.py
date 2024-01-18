# Input a string
telephone = str(input())

# Create a list that indicate mobile number
mobile_num = ["06","08","09"]

# Mobile number Requirement
# 1.) The first 2 digits must be "06", "08" or "09"
# 2.) Mobile number must be 10-digit long
if(telephone[0:2] in mobile_num and len(telephone)==10):
    print("Mobile number")
else:
    print("Not a mobile number")