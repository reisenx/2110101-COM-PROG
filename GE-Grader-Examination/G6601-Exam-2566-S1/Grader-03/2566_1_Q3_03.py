# --------------------------------------------------
# File Name : 2566_1_Q3_03.py
# Problem   : One Piece
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------

# Initialize a dictionary to store the routes between islands
goto_next_island = {}


# Function to input the island routes
def input_island_route() -> None:
    n = int(input())
    for _ in range(n):
        # Extract the current island, next island, and duration from input
        current_island, next_island, duration = input().strip().split()
        # Store the route in the dictionary
        goto_next_island[current_island] = (next_island, int(duration))


# Function to calculate the total duration of the route from start to end island
# If the route is not found, return -1
def find_route(start_island: str, end_island: str) -> int:
    # Initialize total duration, current island and a set to track visited islands
    total_duration = 0
    current_island = start_island
    visited_island = set()

    # Traverse the islands until reaching the end island
    while current_island != end_island:
        # Add the current island to the visited set
        visited_island.add(current_island)
        # If the current island has no outgoing route, the route is not exist
        if current_island not in goto_next_island:
            return -1

        # Get the next island and duration from the current island
        next_island, duration = goto_next_island[current_island]
        # Calculate the total duration
        total_duration += duration

        # Set the current island to the next island
        current_island = next_island
        # Check if the current island has been visited before
        if current_island in visited_island:
            return -1
    # Return the total duration if the route is found
    return total_duration


# Main function
def main() -> None:
    # Input the island routes
    input_island_route()

    # Input queries
    n = int(input())
    for _ in range(n):
        start_island, end_island = input().strip().split()
        # Calculate the total duration of the route from start to end island
        total_duration = find_route(start_island, end_island)
        # Output the total duration
        if total_duration == -1:
            print("Route not found")
        else:
            print(total_duration)


# Run the main function
main()
