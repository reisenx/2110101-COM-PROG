# Newton's method
# x_(n+1) = x_n + f(x_n)/f'(x_n))
# Example: x1 = x0 - f(x0)/f'(x0)

# Estimate k-th root of a
# f(x) = x^k - a
# f'(x) = k * x^(k-1)
# Example: x1 = x0 - f(x0)/f'(x0)
#          x1 = x0 - ((x0**k) - a)/(k*(x0**(k-1)))

# Input initial x0, k, a
a = int(input("Input number: "))
k = int(input("Root: "))
x = int(input("x0: "))
print("Find estimated value of", str(k) + "-th root of", a, "with initial value x0 =",x,"\n")

# Output the value of each loop
# Loop until |(x_n)^k - a| < 10^(-6)
n=0
while(abs(x**k - a) >= 10**(-6)):
    n = n+1
    print("Using Newton's method", "(n = "+ str(n) + ")")
    x = x - ((x**k) - a)/(k*(x**(k-1)))
    diff = abs(x**k - a)
    print("Value of x"+str(n), "=", x)
    print("Difference =", diff, "\n")

print("At", str(n)+"-th loop the difference is lower than 10^(-6)")
print("End of the program")