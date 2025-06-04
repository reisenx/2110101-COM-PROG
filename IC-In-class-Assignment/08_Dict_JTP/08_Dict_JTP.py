# Create a dictionary of the pizza and its calories per 1 slice
calories = {'PZ871':265.25, 'PZ953':246.50, 'Z1983':256.50, 'Z2853':272.50, 'LC673':309.25}
customer = {}

# Input how many orders
n = int(input())

# Input order details
# Order details will be in the format --> "[ID],[Pizza1],[Silces1],[Pizza2],[Slice2],..."
# ID = order[0]
# pizza = order[1], order[3], order[5], ...
# slice = order[2], order[4], order[6], ... 
# Pizza details may be lowercase (Example: 'pZ871')
for i in range(n):
    order = input().strip().split(',')
    ID = order[0]
    pizza_amount = (len(order)-1)//2
    for j in range(1, pizza_amount+1):
        if(ID not in customer):
            customer[ID] = calories[order[2*j - 1].upper()] * int(order[2*j])
        else:
            customer[ID] += calories[order[2*j - 1].upper()] * int(order[2*j])

# Output by customer ID (Ascending order)
ID_list = []
for ID in customer:
    ID_list.append(ID)
# Sort ID list in ascending order
ID_list.sort()
# Output
for ID in ID_list:
    print(ID, "-->", round(customer[ID],2))