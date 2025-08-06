<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Queue Ticket ★★★ (
      <a href="https://drive.google.com/file/d/1Zr5xve0MFhFOFmckERHE27i3tcze1mQO/view?usp=drive_link">
        <code>05_List_32</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**Solution**](#solution)

---

<div align="center">
  <h2>เฉลยอย่างละเอียดจะตามมาทีหลัง</h2>
</div>

---

# Solution

```python
# --------------------------------------------------
# File Name : 05_List_32.py
# Problem   : Queue Ticket
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input commands amount
n = int(input())

# Initialize variable
queue = []
queue_time = []
ticket = 0
customer = 0

# Process each command
for _ in range(n):
    # Input command
    cmd = input().strip().split()

    # Command: reset
    # Initialize ticket number
    if cmd[0] == "reset":
        ticket = int(cmd[1])

    # Command: new
    # Add a new customer to the queue
    if cmd[0] == "new":
        new_time = int(cmd[1])
        queue.append([ticket, new_time])

        print("ticket", ticket)
        ticket += 1

    # Command: next
    # Process the next customer in the queue
    if cmd[0] == "next":
        current_ticket = queue[customer][0]
        print("call", current_ticket)
        customer += 1

    # Command: order
    # Update the order time for the current customer
    if cmd[0] == "order":
        current_ticket, new_time = queue[customer - 1]
        order_time = int(cmd[1])

        duration = order_time - new_time
        queue_time.append(duration)
        print("qtime", current_ticket, duration)

    # Command: avg_qtime
    # Calculate the average queue time
    if cmd[0] == "avg_qtime":
        avg = 0.0
        if len(queue_time) > 0:
            avg = sum(queue_time) / len(queue_time)
        print("avg_qtime", round(avg, 4))
```
