# Create a function is_prime(n)
# This function can check if the input number is a prime number
def is_prime(n):
    if n<=1:
        return False
    for k in range(2,int(n**0.5)+1):
        if(n%k == 0):
            return False
    return True    

# Create a function next_prime(N)
# This function returns a minimum prime number that greater than N
def next_prime(N):
    # Set an initial number that greater than N
    N += 1
    # Increase a value by 1 until N is a prime number
    while(is_prime(N) == False):
        N += 1
    return N

# Create a function next_twin_prime(N)
# This function return a minimum twin prime that greater than N
# Twin prime is 2 prime numbers that differ by 2
def next_twin_prime(N):
    while(next_prime(next_prime(N)) - next_prime(N) != 2):
        N = next_prime(N)
    return (next_prime(N), next_prime(next_prime(N)))

# Execute a input string
exec(input().strip())