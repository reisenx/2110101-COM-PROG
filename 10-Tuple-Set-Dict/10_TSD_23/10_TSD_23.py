# --------------------------------------------------
# File Name : 10_TSD_23.py
# Problem   : Genre Total Playtime
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

SECONDS_IN_MIN = 60
DISPLAY_LIMIT = 3


# Convert time string in MM:SS format to total seconds.
def to_seconds(time):
    m, s = [int(num) for num in time.split(":")]
    return (m * SECONDS_IN_MIN) + s


# Convert total seconds to time string in MM:SS format.
def to_time(seconds):
    m = str(seconds // SECONDS_IN_MIN)
    s = f"0{str(seconds % SECONDS_IN_MIN)}"[-2:]
    return f"{m}:{s}"


# Initialize a dictionary to store total playtime for each genre.
genre_playtime = {}

# Input number of entries.
n = int(input())

# Process each entry.
for _ in range(n):
    data = input().strip().split(", ")
    genre = data[-2]
    time = to_seconds(data[-1])

    # Add the playtime to the corresponding genre.
    if genre not in genre_playtime:
        genre_playtime[genre] = 0
    genre_playtime[genre] += time

# Sort genres by total playtime in descending order.
sorted_genre_playtime = []
for genre, total_time in genre_playtime.items():
    sorted_genre_playtime.append((-total_time, genre))
sorted_genre_playtime.sort()

# Output the top 3 genres with the longest total playtime.
for total_time, genre in sorted_genre_playtime[:DISPLAY_LIMIT]:
    print(f"{genre} --> {to_time(-total_time)}")
