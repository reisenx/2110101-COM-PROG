# --------------------------------------------------
# File Name : 2567_2_Q3_A2.py
# Problem   : Earthquake
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------

import math

# Initialize constants
VELOCITY_PER_SEC = 6
VELOCITY_PER_MIN = VELOCITY_PER_SEC * 60

VISIBLE_DISTANCE = 50
DISPLAY_LIMIT = 5

# Input the initial distance between the two persons
initial_distance = int(input())

# Calculate the sum of distance for both to run to see each other
distance_to_run = max(0, initial_distance - VISIBLE_DISTANCE)

# Calculate the distance between them in each minute until they can see each other
if distance_to_run > 0:
    # Calculate the total time in seconds and minutes required to run
    total_seconds = math.ceil(distance_to_run / VELOCITY_PER_SEC)
    total_minutes = math.ceil(total_seconds / 60)

    # Initialize a list to store the timestamps to display
    timestamps = []
    # Add the minute 1 until the total minutes or DISPLAY_LIMIT
    for time in range(1, min(total_minutes, DISPLAY_LIMIT) + 1):
        timestamps.append(time)
    # Add the total minutes if it exceeds DISPLAY_LIMIT
    if total_minutes > DISPLAY_LIMIT:
        timestamps.append(total_minutes)

    # Calculate the distance between them at each timestamp
    for time in timestamps:
        # Before reaching the final minute, calculate the distance based on minutes
        if time < total_minutes:
            current_distance = initial_distance - (time * VELOCITY_PER_MIN)
        # At the final minute, calculate the distance based on seconds
        else:
            current_distance = initial_distance - (total_seconds * VELOCITY_PER_SEC)
        # Output the current timestamp and distance
        print(time, current_distance)

# No need to run if they can already see each other
else:
    print(0, initial_distance)
