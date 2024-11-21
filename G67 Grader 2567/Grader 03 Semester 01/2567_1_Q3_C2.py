# Input Information
personSales = {}
bossLinks = {}
n = int(input())
for i in range(n):
    minion, boss, sales = input().strip().split(',')
    # Get sales of each minion
    # Big bosses will have 0 sales in this process
    if(boss not in personSales):
        personSales[boss] = 0
    personSales[minion] = int(sales)
    
    # Get boss-minion links
    if(boss not in bossLinks):
        bossLinks[boss] = [minion]
    else:
        bossLinks[boss].append(minion)

# Get all big bosses
bigBosses = []
for people, sales in personSales.items():
    if(sales == 0):
        bigBosses.append(people)

# Create recursive function to calculate total sales of bosses
def totalSales(person):
    # When reach the lowest minion, return their value
    if(person not in bossLinks):
        return personSales[person]
    # For bosses, use recursive function to get all sales of their minions
    # Get the boss sales (for big bosses this will be 0)
    total = personSales[person]
    # Get their minions sales
    for minion in bossLinks[person]:
        total += totalSales(minion)
    return total

# Calculate big bosses sales
bigBossesSales = []
for boss in bigBosses:
    bigBossesSales.append([totalSales(boss), boss])
bigBossesSales.sort(reverse = True)

# Output
for sales, boss in bigBossesSales:
    print("Boss", boss, sales)