# Create function sqrt_n_times(x,n)
# Square root of x is equal to x^(1/2)
# Square root of x n times is equal to x^(1/(2^n))
def sqrt_n_times(x,n):
    return x**(1/(2**n))

# Create function cuberoot(y)
# Cube root of y can be estimated as
# y^[(1/2^2)(1 + 1/2^2)(1 + 1/2^4)(1 + 1/2^8)(1 + 1/2^16)(1 + 1/2^32)]
def cube_root(y):
    step1 = sqrt_n_times(y,2)
    step2 = sqrt_n_times(step1,2)
    step3 = sqrt_n_times(step1*step2,4)
    step4 = sqrt_n_times(step1*step2*step3,8)
    step5 = sqrt_n_times(step1*step2*step3*step4,16)
    step6 = sqrt_n_times(step1*step2*step3*step4*step5,32)
    return step1*step2*step3*step4*step5*step6

# Create main() function
# main() function can output the estimated cube root value of the input number
def main():
    q = float(input())
    print(cube_root(q))

# Execute the input string
exec(input())