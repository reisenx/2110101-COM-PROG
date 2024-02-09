# Input integer n 
n = int(input())

# Create empty lists and variable
tickets = []
new_time = []
order_time = []
queue_time = []
order_count = 0

# Input an output using a command n times
for i in range(0,n):
    command = input().split()
    
    # Create a "reset" command
    # This command is used to set a initial ticket number as a following integers
    # Example: reset 301 --> initial = 301
    # No output in this command
    if(command[0] == "reset"):
        initial_ticket = int(command[1])
    
    # Create a "new" command
    # This command is used to create a new ticket
    # Input:
    # new 1100 --> tickets = [301] | new_time = [1100]
    # new 1120 --> tickets = [301,302] | new_time = [1100, 1120]
    # 1100 is a time when the ticket is created (time is an integer, not a HHMM format)
    
    # Output in "ticket n" format when "n" is a a ticket the just has created
    # Input: new 1100 --> Output: ticket 301
    # Input: new 1120 --> Output: ticket 302
    elif(command[0] == "new"):
        if(len(tickets) == 0):
            tickets.append(initial_ticket)
        else:
            tickets.append(tickets[-1]+1)
        new_time.append(int(command[1]))
        print("ticket", tickets[-1])
    
    # Create a "next" command
    # This command is used to call the next queue
    # Input: next
    # tickets = [301,302]
    # Output: call 301
    elif(command[0] == "next"):
        print("call", tickets[order_count])
        order_count += 1
    
    # Create order command
    # This command is used to specify time when calling a customer
    # Input: order 1130
    # Output: qtime 301 30
    elif(command[0] == "order"):
        order_count -= 1
        order_time.append(int(command[1]))
        queue_time.append(order_time[-1] - new_time[order_count])
        print("qtime", tickets[order_count], queue_time[-1])
        order_count += 1

    # Create avg_qtime command
    # This command is used to show an average queue time upto the current customer
    # Input: avq_qtime
    # Output: avq_qtime 25.0
    elif(command[0] == "avg_qtime"):
        print("avg_qtime", float(sum(queue_time)/len(queue_time)))