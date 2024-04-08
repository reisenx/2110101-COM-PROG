n = int(input())
tickets = []
new_time = []
order_time = []
queue_time = []
order_count = 0

for i in range(n):
    command = input().split()
    if(command[0] == "reset"):
        initial_ticket = int(command[1])

    elif(command[0] == "new"):
        if(len(tickets) == 0):
            tickets.append(initial_ticket)
        else:
            tickets.append(tickets[-1] + 1)
        new_time.append(int(command[1]))
        print("ticket", tickets[-1])

    elif(command[0] == "next"):
        print("call", tickets[order_count])
        order_count += 1
    
    elif(command[0] == "order"):
        order_count -= 1
        order_time.append(int(command[1]))
        queue_time.append(order_time[-1] - new_time[order_count])
        print("qtime", tickets[order_count], queue_time[-1])
        order_count += 1
    
    elif(command[0] == "avg_qtime"):
        print("avg_qtime", float(sum(queue_time)/len(queue_time)))