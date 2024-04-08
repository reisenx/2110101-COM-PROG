telephone = str(input())
mobile_num = ["06","08","09"]

if(telephone[0:2] in mobile_num and len(telephone)==10):
    print("Mobile number")
else:
    print("Not a mobile number")