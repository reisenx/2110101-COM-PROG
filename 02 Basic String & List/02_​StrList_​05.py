#Input a string into sales variable
sales=str(input())

#Split a price from sales variable
price=sales.split()

#Output the weekly sales
print(int(price[0])+int(price[1])+int(price[2])+int(price[3])+int(price[4])+int(price[5])+int(price[6]))