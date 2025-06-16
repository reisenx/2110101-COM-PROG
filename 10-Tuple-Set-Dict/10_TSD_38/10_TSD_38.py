# --------------------------------------------------
# File Name : 10_TSD_38.py
# Problem   : Sky Train
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Initialize a dictionary for adjacent stations
adjacent_stations = {}
start_station = ""

while True:
    # Read the input line
    data = input().strip().split()
    # Stop input if has only one station
    if len(data) == 1:
        start_station = data[0]
        break

    # Update the adjacent stations dictionary
    station, adjacent = data
    if station not in adjacent_stations:
        adjacent_stations[station] = set()
    adjacent_stations[station].add(adjacent)

    if adjacent not in adjacent_stations:
        adjacent_stations[adjacent] = set()
    adjacent_stations[adjacent].add(station)

# Find reachable stations from the start station in range of 2 stations
reachable_stations = {start_station}
if start_station in adjacent_stations:
    reachable_stations |= adjacent_stations[start_station]
    for station in adjacent_stations[start_station]:
        reachable_stations |= adjacent_stations[station]

# Output all reachable stations in sorted order
for station in sorted(reachable_stations):
    print(station)
