# Solution 1: List Processing

# Input number of coupons
n = int(input())

# Create an important variables
# 'temp' is used for temporary purposes
# 'coupon_name' contains all coupon names in input order
# 'coupon' contains a sublist [Name,Score] of each coupon in descending order (Sort by coupon score)
# 'use' contains a sublist [Name,Usage] of each coupon in descending order (Sort by coupon score)
temp = []
coupon_name = []
coupon = []
use = []
# Exaple Input:
# 4
# a_1 100
# a_2 150
# b_1 200
# b_2 250

# Variables:
# coupon_name = ['a_1', 'a_2', 'b_1', 'b_2']
# coupon = [['b_2',250], ['b_1',200], ['a_2',150], ['a_1',100]]
# use = [['b_2',0], ['b_1',0], ['a_2',0], ['a_1',0]]
for i in range(n):
    data = input().strip().split()
    coupon_name.append(data[0])
    temp.append([int(data[1]),data[0]])
for tvalue, tname in sorted(temp)[::-1]:
    coupon.append([tname,tvalue])
    use.append([tname,0])

# Input initial score
score = int(input())
# Example:
# Initial Variables:
# score = remain = 1500
# coupon = [['b_2',250], ['b_1',200], ['a_2',150], ['a_1',100]]
# use = [['b_2',0], ['b_1',0], ['a_2',0], ['a_1',0]]

# Process:
# Loop 1: Consider 'b_2' coupon
# > use[0][1] = min(1500//250, 3) = 3 --> remain = 1500-(250*3) = 750
# Loop 2: Consider 'b_1' coupon
# > use[1][1] = min(750//200, 3) = 3 --> remain = 750-(200*3) = 150
# Loop 3: Consider 'b_1' coupon
# > use[2][1] = min(150//150, 3) = 1 --> remain = 150-(150*1) = 0
# Loop 4: Do nothing because 'remain' = 0
# NOTE: We use min() because each coupon has maximum usage = 3
# After the process, use = [['b_2',3], ['b_1',3], ['a_2',1], ['a_1',0]]
remain = score
for i in range(len(coupon)):
    if(remain > 0):
        use[i][1] = min(remain//coupon[i][1], 3)
        remain -= coupon[i][1]*use[i][1]

# Output
# In the first line, we output initial score, used score, remaining score
print(">",score, score-remain, remain)
IsPrintCoupon = False
# Output the coupon that can be used and its number of usage (Sorting by 'coupon_name')
for name in coupon_name:
    for uname, uvalue in use:
        if(name == uname and uvalue > 0):
            print(uname, uvalue)
            IsPrintCoupon = True
# If there are no coupon that can be used
if(not IsPrintCoupon):
    print("No coupon")