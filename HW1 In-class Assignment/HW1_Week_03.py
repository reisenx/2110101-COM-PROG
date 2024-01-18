# Create a list that contains zodiac years
# Create a list that contains months
zodiac_years = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"]

# Input month and year as a string then split it and change them to integers
month, year = [int(e) for e in input().split()]

# Month
# We minus the month by 1 to make it easier
# In case of month = 1, change month to 12 and year = year-1
# Monkey     2/2004 to 1/2005 --> 1/2004 to 12/2004
# Rooster    2/2005 to 1/2006 --> 1/2005 to 12/2005
# Dog        2/2006 to 1/2007 --> 1/2006 to 12/2006
# Pig        2/2007 to 1/2008 --> 1/2007 to 12/2007
# Rat        2/2008 to 1/2009 --> 1/2008 to 12/2008
# Ox         2/2009 to 1/2010 --> 1/2009 to 12/2009
# Tiger      2/2010 to 1/2011 --> 1/2010 to 12/2010
# Rabbit     2/2011 to 1/2012 --> 1/2011 to 12/2011
# Dragon     2/2012 to 1/2013 --> 1/2012 to 12/2012
# Snake      2/2013 to 1/2014 --> 1/2013 to 12/2013
# Horse      2/2014 to 1/2015 --> 1/2014 to 12/2014
# Goat       2/2015 to 1/2016 --> 1/2015 to 12/2015
if(month == 1):
    month = 12
    year = year-1
else:
    month = month-1

# Year
# Monkey     mod 12 = 0  (Ex: 2004 mod 12 = 0)
# Rooster    mod 12 = 1  (Ex: 2005 mod 12 = 1)
# Dog        mod 12 = 2  (Ex: 2006 mod 12 = 2)
# Pig        mod 12 = 3  (Ex: 2007 mod 12 = 3)
# Rat        mod 12 = 4  (Ex: 2008 mod 12 = 4)
# Ox         mod 12 = 5  (Ex: 2009 mod 12 = 5)
# Tiger      mod 12 = 6  (Ex: 2010 mod 12 = 6)
# Rabbit     mod 12 = 7  (Ex: 2011 mod 12 = 7)
# Dragon     mod 12 = 8  (Ex: 2012 mod 12 = 8)
# Snake      mod 12 = 9  (Ex: 2013 mod 12 = 9)
# Horse      mod 12 = 10 (Ex: 2014 mod 12 = 10)
# Goat       mod 12 = 11 (Ex: 2015 mod 12 = 11)
print(zodiac_years[year%12])