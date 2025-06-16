# --------------------------------------------------
# File Name : 10_TSD_23.py
# Problem   : Genre Total Playtime
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------


# Convert time string in MM:SS format to total seconds.
def to_seconds(time: str) -> int:
    m, s = [int(num) for num in time.split(":")]
    return (m * 60) + s


# Convert total seconds to time string in MM:SS format.
def to_time(seconds: int) -> str:
    m = str(seconds // 60)
    s = "0" + str(seconds % 60)
    return f"{m}:{s[-2:]}"


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
    if genre in genre_playtime:
        genre_playtime[genre] += time
    else:
        genre_playtime[genre] = time

# Sort genres by total playtime in descending order.
sorted_genres = []
for genre, total_time in genre_playtime.items():
    sorted_genres.append([-total_time, genre])
sorted_genres.sort()

# Output the top 3 genres with the longest total playtime.
for total_time, genre in sorted_genres[:3]:
    print(f"{genre} --> {to_time(-total_time)}")
