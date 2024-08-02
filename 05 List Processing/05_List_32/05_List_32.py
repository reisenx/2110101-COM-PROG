# Input number of command lines
n = int(input())

# Create empty lists and variable
tickets = []
new_time = []
order_time = []
queue_time = []
order_count = 0

# Input command lines
for i in range(n):
    command = input().split()
    
    # Command: 'reset'
    # Set initial ticket number
    # Example: reset 301 --> 'initial_ticket' = 301
    # No output in this command
    if(command[0] == "reset"):
        initial_ticket = int(command[1])
    
    # Command: 'new'
    # Create new ticket
    # Example:
    # > "new 1100" --> tickets = [301]      | new_time = [1100]
    # > "new 1120" --> tickets = [301,302]  | new_time = [1100, 1120]
    # NOTE: 1100 is a time when the ticket is created (time is an integer, not a HHMM format)
    
    # Output "ticket [number]" after create a ticket
    # Example:
    # > Input: "new 1100" --> Output: "ticket 301"
    # > Input: "new 1120" --> Output: "ticket 302"
    elif(command[0] == "new"):
        if(len(tickets) == 0):
            tickets.append(initial_ticket)
        else:
            tickets.append(tickets[-1] + 1)
        new_time.append(int(command[1]))
        print("ticket", tickets[-1])
    
    # Command: 'next'
    # Call next queue
    # Example:
    # > Input: "next" --> Output: "call 301"  | tickets = [301,302]
    elif(command[0] == "next"):
        print("call", tickets[order_count])
        order_count += 1
    
    # Command: 'order'
    # Get time when calling a customer and calculate queue time
    # Example: 
    # > Input: "order 1130" --> Output: "qtime 301 30"
    elif(command[0] == "order"):
        order_count -= 1
        order_time.append(int(command[1]))
        queue_time.append(order_time[-1] - new_time[order_count])
        print("qtime", tickets[order_count], queue_time[-1])
        order_count += 1
    
    # Command: 'avg_qtime'
    # Calculate average queue time up to the current customer
    # Example:
    # > Input: "avq_qtime" --> Output: "avq_qtime 25.0"
    elif(command[0] == "avg_qtime"):
        print("avg_qtime", float(sum(queue_time)/len(queue_time)))