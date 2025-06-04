# Input
total_distance = float(input())
jump_factor = float(input())
end_gap = float(input())
pit_start = float(input())
pit_end = float(input())

# Setup initial value of current_distance, remain_distance and jump_count
current_distance = 0
remain_distance = total_distance
jump_count = 0
# Loop jump until remain_distance is equal or less than end_gap
while(remain_distance > end_gap):
    # If the bug is in a pit, the bug needs to walk to the pit_end before jumping
    if(pit_start <= current_distance <= pit_end):
        current_distance = pit_end
        remain_distance = total_distance - pit_end
    # Recheck if the bug has reached end_gap
    if(remain_distance <= end_gap):
        break
    # Calculate jump_distance of each jump
    jump_distance = jump_factor * remain_distance
    # Calculate current_distance
    current_distance += jump_distance
    # Calculate remain_distance
    remain_distance -= jump_distance
    # Count how many time that the bug jumps
    jump_count += 1
print(jump_count)