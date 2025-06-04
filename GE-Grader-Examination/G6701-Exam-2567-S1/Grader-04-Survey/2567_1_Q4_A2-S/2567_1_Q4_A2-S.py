# Input percentage of each type
type1 = float(input())
type2 = float(input())
type3 = float(input())
type4 = float(input())

# Input sales
N = int(input())
benefit = 0
for i in range(N):
    date, product, sales = input().strip().split()
    product, sales = int(product), float(sales)
    if(product == 1):
        benefit += sales*(type1/100)
    if(product == 2):
        benefit += sales*(type2/100)
    if(product == 3):
        benefit += sales*(type3/100)
    if(product == 4):
        benefit += sales*(type4/100)

# Output
print(round(benefit, 2))