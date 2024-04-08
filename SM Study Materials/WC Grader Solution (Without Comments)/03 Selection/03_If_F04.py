def is_mobile_number(number):
    mobile_num = ["06","08","09"]
    if(number[0:2] in mobile_num and len(number)==10):
        return True
    else:
        return False

exec(input())