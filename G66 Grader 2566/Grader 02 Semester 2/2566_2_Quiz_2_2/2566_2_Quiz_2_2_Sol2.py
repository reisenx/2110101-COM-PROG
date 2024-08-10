# Solution 2: Dictionary

# Input number of coupons
n = int(input())

# Create an important variables
# 'coupons' is a dictionary contains {Score:Name, ...}
# 'use' is a dictionary contains {Score:Usage, ...}
# 'scores' is a list of scores in input order
# NOTE: It is guaruntee that there are no coupons that have the same score
coupons = {}
use = {}
scores = []
# Exaple Input:
# 4
# a_1 100
# a_2 150
# b_1 200
# b_2 250

# Variables:
# coupons = {100:'a_1', 150:'a_2', 200:'b_1', 250:'b_2'}
# use = {100:0, 150:0, 200:0, 250:0}
# scores = [100,150,200,250]
for i in range(n):
    temp = input().strip().split()
    name, score = temp[0], int(temp[1])
    coupons[score] = name
    use[score] = 0
    scores.append(score)

# Input initial score
initial_score = int(input())
remain = initial_score
# Calculate usage of each coupon by consider the score of the coupon in descending order
# Initial Variables:
# coupons = {100:'a_1', 150:'a_2', 200:'b_1', 250:'b_2'}
# use = {100:0, 150:0, 200:0, 250:0}
# scores_sorted = [250,200,150,100]

# Process:
# Loop 1: Consider coupon with score = 250 ('b_2' coupon)
# > use[250] = min(1500//250, 3) = 3 --> remain = 1500-(250*3) = 750
# Loop 2: Consider coupon with score = 250 ('b_1' coupon)
# > use[200] = min(750//200, 3) = 3 --> remain = 750-(200*3) = 150
# Loop 3: Consider coupon with score = 250 ('a_2' coupon)
# > use[150] = min(150//150, 3) = 1 --> remain = 150-(150*1) = 0
# Loop 4: Do nothing because 'remain' = 0
# NOTE: We use min() because each coupon has maximum usage = 3
# After the process, use = {100:0, 150:1, 200:3, 250:3}
scores_sorted = sorted(scores)[::-1]
for score in scores_sorted:
    if(remain > 0):
        use[score] = min(remain//score, 3)
        remain -= score*use[score]

# Output
# In the first line, we output initial score, used score, remaining score
print(">", initial_score, initial_score - remain, remain)
IsPrintCoupon = False
# Output the coupon that can be used and its number of usage (Sorting key by 'scores')
for score in scores:
    if(use[score] > 0):
        print(coupons[score], use[score])
        IsPrintCoupon = True
# If there are no coupon that can be used
if(not IsPrintCoupon):
    print("No coupon")