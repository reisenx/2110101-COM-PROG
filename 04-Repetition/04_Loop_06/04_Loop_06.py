# Input an integer
n = int(input())

# Output the triangle
# A triangle height is n
# Output the first n-1 lines
for i in range (1,n):
    # Part 1: Print "." outside the triangle
    # Part 2: Print "*" (left edge of the triangle)
    # Part 3: Print "." inside the triangle
    # Part 4: Print "*" (right edge of triangle)
    if(i==1):
        print((n-i)*"." + "*")
    elif(i!=1):
        print((n-i)*"." + "*" + (2*(i-1)-1)*"." + "*")
# Output the bottom of a triangle
print((2*n-1)*"*")


# See the pattern in the line 1-7
# n=8                   n
# .......*              1|  7   1   0   0   (Don't print Part 3 and 4 if n=1)
# ......*.*             2|  6   1   1   1
# .....*...*            3|  5   1   3   1
# ....*.....*           4|  4   1   5   1
# ...*.......*          5|  3   1   7   1
# ..*.........*         6|  2   1   9   1
# .*...........*        7|  1   1   11  1
# ***************       8|  0   15  0   0   (Just print "*" 2(8)-1 times)