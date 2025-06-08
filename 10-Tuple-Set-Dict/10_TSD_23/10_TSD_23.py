# Input number of songs
n = int(input())

# Create a function that can convert time in MM:SS format to seconds
# Exmaple: "1:39" --> 99
def time2sec(time):
    min,sec = [int(num) for num in time.split(":")]
    seconds = (min*60) + sec
    return seconds

# Create a function that can convert seconds to time in MM:SS format
# Example: 99 --> "1:39"
def sec2time(seconds):
    min = seconds//60
    sec = seconds%60
    sec = '0' + str(sec)
    time = str(min) + ":" + sec[-2:]
    return time

# Input song details. Each song detail contains 
# [Name], [Artist], [Genre], [Duration]
# Contains the detials in a dictionary 'genres'
# genres = {Genre:[Duration1, Duration2, ...], ...}
# Example: {Pop:['3:39', '3:48', '3:36', '3:42'], ...}
genres = {}
for i in range(n):
    name, artist, type, duration = input().strip().split(", ")
    if(type not in genres):
        genres[type] = [duration]
    else:
        genres[type].append(duration)

# Find duration of each genres and sort them in descending order
# Contains the data in a 'duration_list'
# duration_list = [[Seconds, Time, Genre], ...]
# Example: duration_list = [[924,'15:24','Rock'], [885,'14:45','Pop'], [242, '4:02', 'Country']]
duration_list = []
for genre, durations in genres.items():
    seconds = 0
    for duration in durations:
        seconds += time2sec(duration)
    time = sec2time(seconds)
    duration_list.append([seconds, time, genre])
duration_list.sort(reverse = True)

# Output top 3 longest duration genres
output = duration_list[0:3]
for seconds, time, genre in output:
    print(genre, "-->", time)