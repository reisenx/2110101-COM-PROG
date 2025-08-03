# --------------------------------------------------
# File Name : 2567_1_Q3_A2.py
# Problem   : Jumping Bug
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input information of the ground and the bug
total_distance = float(input())
jump_factor = float(input())
end_gap = float(input())

# Input information of the pit on the ground
pit_start = float(input())
pit_end = float(input())

# Initialize variables
current_distance = 0
remaining_distance = total_distance
jumps = 0

# Loop until the bug reaches the end gap of the ground
while remaining_distance > end_gap:
    # Check if the bug is in the pit
    if pit_start <= current_distance <= pit_end:
        # Set the current position to the end of the pit
        current_distance = pit_end
        remaining_distance = total_distance - pit_end

    # Stop if the bug is at or beyond the end gap
    if remaining_distance <= end_gap:
        break
    # Calculate the jump distance of the bug
    jump_distance = jump_factor * remaining_distance

    # Update the current distance and remaining distance
    current_distance += jump_distance
    remaining_distance -= jump_distance

    # Increment the jump count
    jumps += 1

# Output the number of jumps made by the bug
print(jumps)
