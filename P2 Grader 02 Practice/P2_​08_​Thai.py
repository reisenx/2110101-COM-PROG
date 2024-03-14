# Create a dictionary that contains number in Thai
thai_num = {'1':'neung', '2':'song', '3':'sam', '4':'si', '5':'ha', '6':'hok', '7':'chet', '8':'paet', '9':'kao', '0':'soon'}

# Create a function that able to read number (0-9999) in Thai
def to_Thai(N):
    N = str(N)
    num_read = ""
    # Case 1: 0-9
    if(len(N) == 1):
        return thai_num[N]
    
    # Case 2: 10-99
    # 1.) If ones is 0, don't read '0' (Example: '60' -> 'hok sip')
    # 2.) If ones is 1, read '1' as 'et' instead (Example: '31' --> sam sip et)
    # 3.) If tens is 1, don't read '1' (Example: '15' --> 'sip ha')
    # 4.) If tens is 2, read '2' as 'yi' instead (Example: '27' --> 'yi sip chet')
    elif(len(N) == 2):
        # Read tens
        if(N[0] == '1'):
            pass
        elif(N[0] == '2'):
            num_read += "yi "
        else:
            num_read += thai_num[N[0]] + " "
        num_read += "sip "

        # Read ones
        if(N[1] == '0'):
            pass
        elif(N[1] == '1'):
            num_read += "et"
        else:
            num_read += thai_num[N[1]]
    
    # Case 3: 100-999
    # 5.) If tens is 0, don't read '0' and 'sip' (Example: '208' --> 'song roi paet')
    elif(len(N) == 3):
        # Read hundreds
        num_read += thai_num[N[0]] + " roi "

        # Read tens
        if(N[1] == '0' or N[1] == '1'):
            pass
        elif(N[1] == '2'):
            num_read += "yi "
        else:
            num_read += thai_num[N[1]] + " "
        if(N[1] != '0'):
            num_read += "sip "

        # Read ones
        if(N[2] == '0'):
            pass
        elif(N[2] == '1'):
            num_read += "et"
        else:
            num_read += thai_num[N[2]]
    
    # Case 4: 1000-9999
    # 6.) If hundreds is 0, don't read '0' and 'roi' (Example: '1024' --> 'neung pun yi sip si')
    elif(len(N) == 4):
        # Read thousands
        num_read += thai_num[N[0]] + " pun "

        # Read hundreds
        if(N[1] != '0'):
            num_read += thai_num[N[1]] + " roi "

        # Read tens
        if(N[2] == '0' or N[2] == '1'):
            pass
        elif(N[2] == '2'):
            num_read += "yi "
        else:
            num_read += thai_num[N[2]] + " "
        if(N[2] != '0'):
            num_read += "sip "

        # Read ones
        if(N[3] == '0'):
            pass
        elif(N[3] == '1'):
            num_read += "et"
        else:
            num_read += thai_num[N[3]]
    
    # Return "num_read"
    return num_read

# Execute an input string
exec(input().strip())