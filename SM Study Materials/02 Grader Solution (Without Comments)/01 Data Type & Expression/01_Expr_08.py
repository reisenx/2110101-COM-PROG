def sqrt_n_times(x,n):
    return x**(1/(2**n))

def cube_root(y):
    step1 = sqrt_n_times(y,2)
    step2 = sqrt_n_times(step1,2)
    step3 = sqrt_n_times(step1*step2,4)
    step4 = sqrt_n_times(step1*step2*step3,8)
    step5 = sqrt_n_times(step1*step2*step3*step4,16)
    step6 = sqrt_n_times(step1*step2*step3*step4*step5,32)
    return step1*step2*step3*step4*step5*step6

def main():
    q = float(input())
    print(cube_root(q))

exec(input())