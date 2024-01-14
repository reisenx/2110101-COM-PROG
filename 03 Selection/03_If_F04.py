#Create is_mobile_number(number) function
def is_mobile_number(number):
    #Create a list that indicate mobile number
    mobile_num = ["06","08","09"]
    
    #Mobile number Requirement
    #1.) The first 2 digits must be "06", "08" or "09"
    #2.) Mobile number must be 10-digit long
    if(number[0:2] in mobile_num and len(number)==10):
        return True
    else:
        return False

#Execute the input string
exec(input())