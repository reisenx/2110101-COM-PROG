<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Location Analysis ★★ (
      <a href="https://drive.google.com/file/d/1q6ZCJdDag9yIrOAhdH0dGYcXHTZxTHKG/view?usp=drive_link">
        <code>10_TSD_26</code>
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
# File Name : 10_TSD_26.py
# Problem   : Location Analysis
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Initialize a dictionary to store locations and their users.
locations_to_users = {}
users_to_locations = {}
location_order = []

# Input number of locations
n = int(input())

# Read each location and its users
for _ in range(n):
    line = input().strip().split(": ")
    location = line[0]
    users_list = line[1].split(", ")

    # Update locations set
    location_order.append(location)

    # Store the location and its users in the dictionary
    locations_to_users[location] = set(users_list)

    # Update the users dictionary
    for user in users_list:
        if user not in users_to_locations:
            users_to_locations[user] = set()
        users_to_locations[user].add(location)

# Input analysis location
analysis_location = input().strip()

# Find all locations visited by users of the analysis location
visited_locations = set()
for user in locations_to_users[analysis_location]:
    visited_locations |= users_to_locations[user]

# Exclude the analysis location itself
visited_locations -= {analysis_location}

# Output the result
if len(visited_locations) > 0:
    for location in location_order:
        if location in visited_locations:
            print(location)
else:
    print("Not Found")
```
