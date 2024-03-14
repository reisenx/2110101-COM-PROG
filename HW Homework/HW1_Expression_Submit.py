# HW1_Expression
# Student ID: 6632200221
# Problem: Find 7-th root of 127 without loop, Output n that makes the difference less than 10E-6 (Given x0 = 100)

# Newton's method
# x_(n+1) = x_n + f(x_n)/f'(x_n))
# Example: x1 = x0 - f(x0)/f'(x0)

# Estimate 7-th root of 127 using Newton's method
# f(x) = x**7 - a
# f'(x) = 7*(x**6)
# Example: x1 = x0 - f(x0)/f'(x0)
#          x1 = x0 - ((x0**7) - a)/(7*(x0**6))

# Difference = |(x_n)**7 - a|
# Example: x27 = 2.002995624189019
#          Difference = |(2.002995624189019**7) - 127| = 2.3480850827803295

# Create the function
def x_n(x0,a):
    return x0 - ((x0**7) - a)/(7*(x0**6))
def diff(xn,a):
    return abs(xn**7 - a)

# Setup Initial value
a, x0 = 127, 100

# Calulate until n = 30
x1 = x_n(x0,a)
diff1 = diff(x1,a)
print("x1 =",x1)
print("diff1 =",diff1,"\n")

x2 = x_n(x1,a)
diff2 = diff(x2,a)
print("x2 =",x2)
print("diff2 =",diff2,"\n")

x3 = x_n(x2,a)
diff3 = diff(x3,a)
print("x3 =",x3)
print("diff3 =",diff3,"\n")

x4 = x_n(x3,a)
diff4 = diff(x4,a)
print("x4 =",x4)
print("diff4 =",diff4,"\n")

x5 = x_n(x4,a)
diff5 = diff(x5,a)
print("x5 =",x5)
print("diff5 =",diff5,"\n")

x6 = x_n(x5,a)
diff6 = diff(x6,a)
print("x2 =",x6)
print("diff2 =",diff6,"\n")

x7 = x_n(x6,a)
diff7 = diff(x7,a)
print("x7 =",x7)
print("diff7 =",diff7,"\n")

x8 = x_n(x7,a)
diff8 = diff(x8,a)
print("x8 =",x8)
print("diff8 =",diff8,"\n")

x9 = x_n(x8,a)
diff9 = diff(x9,a)
print("x9 =",x9)
print("diff9 =",diff9,"\n")

x10 = x_n(x9,a)
diff10 = diff(x10,a)
print("x10 =",x10)
print("diff10 =",diff10,"\n")

x11 = x_n(x10,a)
diff11 = diff(x11,a)
print("x11 =",x11)
print("diff11 =",diff11,"\n")

x12 = x_n(x11,a)
diff12 = diff(x12,a)
print("x12 =",x12)
print("diff12 =",diff12,"\n")

x13 = x_n(x12,a)
diff13 = diff(x13,a)
print("x13 =",x13)
print("diff13 =",diff13,"\n")

x14 = x_n(x13,a)
diff14 = diff(x14,a)
print("x14 =",x14)
print("diff14 =",diff14,"\n")

x15 = x_n(x14,a)
diff15 = diff(x15,a)
print("x15 =",x15)
print("diff15 =",diff15,"\n")

x16 = x_n(x15,a)
diff16 = diff(x16,a)
print("x16 =",x16)
print("diff16 =",diff16,"\n")

x17 = x_n(x16,a)
diff17 = diff(x17,a)
print("x17 =",x17)
print("diff17 =",diff17,"\n")

x18 = x_n(x17,a)
diff18 = diff(x18,a)
print("x18 =",x18)
print("diff18 =",diff18,"\n")

x19 = x_n(x18,a)
diff19 = diff(x19,a)
print("x19 =",x19)
print("diff19 =",diff19,"\n")

x20 = x_n(x19,a)
diff20 = diff(x20,a)
print("x20 =",x20)
print("diff20 =",diff20,"\n")

x21 = x_n(x20,a)
diff21 = diff(x21,a)
print("x21 =",x21)
print("diff21 =",diff21,"\n")

x22 = x_n(x21,a)
diff22 = diff(x22,a)
print("x22 =",x22)
print("diff22 =",diff22,"\n")

x23 = x_n(x22,a)
diff23 = diff(x23,a)
print("x23 =",x23)
print("diff23 =",diff23,"\n")

x24 = x_n(x23,a)
diff24 = diff(x24,a)
print("x24 =",x24)
print("diff24 =",diff24,"\n")

x25 = x_n(x24,a)
diff25 = diff(x25,a)
print("x25 =",x25)
print("diff25 =",diff25,"\n")

x26 = x_n(x25,a)
diff26 = diff(x26,a)
print("x26 =",x26)
print("diff26 =",diff26,"\n")

x27 = x_n(x26,a)
diff27 = diff(x27,a)
print("x27 =",x27)
print("diff27 =",diff27,"\n")

x28 = x_n(x27,a)
diff28 = diff(x28,a)
print("x28 =",x28)
print("diff28 =",diff28,"\n")

x29 = x_n(x28,a)
diff29 = diff(x29,a)
print("x29 =",x29)
print("diff29 =",diff29,"\n")

x30 = x_n(x29,a)
diff30 = diff(x30,a)
print("x30 =",x30)
print("diff30 =",diff30,"\n")

# Output n=30
print(30)