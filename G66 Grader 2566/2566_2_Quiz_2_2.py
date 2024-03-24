n = int(input())
temp = []
coupon_name = []
coupon = []
use = []
for i in range(n):
    data = input().strip().split()
    coupon_name.append(data[0])
    temp.append([int(data[1]),data[0]])
for tvalue, tname in sorted(temp)[::-1]:
    coupon.append([tname,tvalue])
    use.append([tname,0])

money = int(input())
remain = money
for i in range(len(coupon)):
    if(remain > 0):
        use[i][1] = min(remain//coupon[i][1], 3)
        remain -= coupon[i][1]*use[i][1]

print(">",money, money-remain, remain)
IsPrintCoupon = False
for name in coupon_name:
    for uname, uvalue in use:
        if(name == uname and uvalue > 0):
            print(uname, uvalue)
            IsPrintCoupon = True
if(not IsPrintCoupon):
    print("No coupon")