# Create a function print_triangle(n)
def print_triangle(n):
    # Output the triangle
    # A triangle height is n
    # Output the first n-1 lines
    for i in range (1,n):
        # Part 1: Print "." outside the triangle
        # Part 2: Print "*" (egde of the triangle)
        # Part 3: Print "." inside the triangle
        # Part 4: Print "*" (another edge of triangle)
        if(i==1):
            print((n-i)*"." + "*")
        elif(i!=1):
            print((n-i)*"." + "*" + (2*(i-1)-1)*"." + "*")
    # Output the last line
    print((2*n-1)*"*")

# Execute input string
exec(input())