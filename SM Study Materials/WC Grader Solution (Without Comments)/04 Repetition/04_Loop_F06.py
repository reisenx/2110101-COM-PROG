def print_triangle(n):
    for i in range (1,n):
        if(i==1):
            print((n-i)*"." + "*")
        elif(i!=1):
            print((n-i)*"." + "*" + (2*(i-1)-1)*"." + "*")
    print((2*n-1)*"*")

exec(input())