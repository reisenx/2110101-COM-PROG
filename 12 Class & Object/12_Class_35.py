class roman:
    # __init__ method
    # Create 'roman' object
    def __init__(self, r):
        self.roman = r
    
    # == Roman numerals ==
    # I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
    # 1-9:       I,II,III,IV,V,VI,VII,VIII,IX
    # 10-90:     X,XX,XXX,XL,L,LX,LXX,LXXX,XC
    # 100-900:   C,CC,CCC,CD,D,DC,DCC,DCCC,CM
    # 1000-4000: M,MM,MMM,MMMM

    # __lt__ method
    # This method can compare 2 'roman' object
    def __lt__(self, rhs):
        return int(self) < int(rhs)

    # __str__ method
    # Return roman number string
    def __str__(self):
        return self.roman
    
    # __int__ method
    # Convert roman number to arabic number 
    def __int__(self):
        # Dictionary contains all roman number
        # 'roman_to_num' can convert roman number to arabic number
        # 'roman_name' is a roman number that start with I,V,X,L,C,D,M and the tuple sorted by its length then its value 
        roman_to_num = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5, 'VI':6, 'VII':7, 'VIII':8, 'IX':9,
                        'X':10, 'XX':20, 'XXX':30, 'XL':40, 'L':50, 'LX':60, 'LXX':70, 'LXXX':80, 'XC':90,
                        'C':100, 'CC':200, 'CCC':300, 'CD':400, 'D':500, 'DC':600, 'DCC':700, 'DCCC':800, 'CM':900,
                        'M':1000, 'MM':2000, 'MMM':3000, 'MMMM':4000}
        roman_name = {'I':('III','IX','IV','II','I'), 'V':('VIII','VII','VI','V'),
                      'X':('XXX','XC','XL','XX','X'), 'L': ('LXXX','LXX','LX','L'),
                      'C':('CCC','CM','CD','CC','C'), 'D': ('DCCC','DCC','DC','D'), 
                      'M':('MMMM','MMM','MM','M')}
        
        # == Algorithm ==
        # Convert Roman number to arabic number
        # 1.) Setup initial variables
        # 2.) Finding a substring using 'roman_name' dictionary.
        # Example: string = 'MMMCMXCIX'
        # > Loop 1: string = 'MMMCMXCIX' starts with 'M' --> Go to roman_name['M']
        #   - Loop 1.1: 'MMMCMXCIX'.find('MMMM') = -1
        #   - Loop 1.2: 'MMMCMXCIX'.find('MMM') = 0 --> break the loop and add value to 'number'
        #   Remove 'MMM' from 'MMMCMXCIX' --> string = 'CMXCIX'
        # > Loop 2: string = 'CMXCIX'
        #   - Loop 2.1: 'CMXCIX'.find('CCC') = -1
        #   - Loop 2.2: 'CMXCIX'.find('CM') = 0 --> break the loop and add value to 'number'
        #   Remove 'CM' from 'CMXCIX' --> string = 'XCIX'
        # > Loop 3: string = 'XCIX'
        #   - Loop 3.1: 'XCIX'.find('XXX') = -1
        #   - Loop 3.2: 'XCIX'.find('XC') = 0 --> break the loop and add value to 'number'
        #   Remove 'XC' from 'XCIX' --> string = 'IX'
        # > Loop 4: string = 'IX'
        #   - Loop 4.1: 'IX'.find('III') = -1
        #   - Loop 4.2: 'IX'.find('IX') = 0 --> break the loop and add value to 'number'
        #   Remove 'IX' from 'IX' --> string = ''
        # > Loop 5: string = '' <-- break the loop
        number = 0
        string = self.roman
        # Loop until string is an empty string
        while(string != ""):
            # Finding a substring using 'roman_name' dictionary.
            for item in roman_name[string[0]]:
                # Found a substring
                if(string.find(item) == 0):
                    # Add a value to a number
                    number += roman_to_num[item]
                    # Remove that substring
                    string = string[len(item):]
                    break
        
        # Return a number
        return number

    # to_roman method
    # Convert arabic number to roman number
    def to_roman(number):
        # Dictionary contains all roman number
        num_to_roman = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX',
                        10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC', 
                        100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM',
                        1000:'M', 2000:'MM', 3000:'MMM', 4000:'MMMM', 0:''}
        
        # Expand a number
        # Example: 2548 --> [2000,500,40,80]
        temp = number
        expand_num = []
        expand_num.append((temp//1000)*1000)
        temp -= expand_num[0]
        expand_num.append((temp//100)*100)
        temp -= expand_num[1]
        expand_num.append((temp//10)*10)
        temp -= expand_num[2]
        expand_num.append(temp)

        # Convert to roman number and return a value
        Roman = ""
        for num in expand_num:
            Roman += num_to_roman[num]
        return Roman
    
    # __add__ method
    # This method can calculate sum of 2 'roman' object and returns as a new 'roman' object
    def __add__(self, rhs):
        # Convert to arabic number, find a sum, and convert back to roman number string
        sum = int(self) + int(rhs)
        sum = roman.to_roman(sum)

        # Returns as a new object
        return roman(sum)

# Output
t, r1, r2 = input().split() 
a = roman(r1); b = roman(r2) 
if t == '1' : print(a < b) 
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b)) 
else : print(str(a + b))