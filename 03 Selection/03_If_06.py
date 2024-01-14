#Input weight as an integer
weight = int(input())

#Transportation fee
# 1.) no more than 100 g = 18 baht
# 2.) more than 100 g but no more than 250 g = 22 baht
# 3.) more than 250 g but no more than 500 g = 28 baht
# 4.) more than 500 g but no more than 1000 g = 38 baht
# 5.) more than 1,000 g but no more than 2000 g = 58 baht
# 6.) more than 2,000 g = Reject
if(weight<=100):
    print(18)
elif(weight>100 and weight<=250):
    print(22)
elif(weight>250 and weight<=500):
    print(28)
elif(weight>500 and weight<=1000):
    print(38)
elif(weight>1000 and weight<=2000):
    print(58)
else:
    print("Reject")