# --------------------------------------------------
# File Name : 2566_2_Q3_03.py
# Problem   : Video Recommendation from Hashtag
# Author    : Worralop Srichainont
# Date      : 2025-07-15
# --------------------------------------------------

# Read input and store hashtags set of each video in a dictionary.
video_hashtags = {}
while True:
    data = input().strip().split()
    # Stop if the input is "q".
    if data == ["q"]:
        break
    # Extract video name and hashtags
    video_name = data[0]
    hashtags = set(data[1:])
    # Update the dictionary with the video name and its hashtags.
    video_hashtags[video_name] = hashtags

# Read the list of visited videos
visited_videos = input().strip().split()
# Initialize a set to store hashtags from visited videos.
visited_hashtags = set()
# Iterate through the visited videos and collect their hashtags.
for video in visited_videos:
    if video in video_hashtags:
        # If the video exists in the dictionary, add its hashtags to the set.
        visited_hashtags |= video_hashtags[video]

# Initialize variables to track the maximum mutual hashtags count
max_mutual_count = 0
# Initialize a list to store videos with their mutual hashtags count.
mutual_hashtags_count = []
# Iterate through the video_hashtags dictionary excluding visited videos.
for video, hashtags in video_hashtags.items():
    if video not in visited_videos:
        # Count the mutual hashtags between the current video and visited videos.
        mutual_count = len(hashtags & visited_hashtags)
        # Update the maximum mutual count
        max_mutual_count = max(max_mutual_count, mutual_count)
        # Store the mutual hashtags count and video name in the list.
        mutual_hashtags_count.append((-mutual_count, video))
# Sort the mutual hashtags count in descending order then video name in ascending order.
mutual_hashtags_count.sort()

# Initialize a list to store suggested videos based on mutual hashtags.
suggested_videos = []
# Iterate through the sorted mutual hashtags count
for count, video in mutual_hashtags_count:
    if -count < max_mutual_count:
        break
    # Collect only videos with the maximum mutual hashtags count.
    suggested_videos.append(video)

# Output
if max_mutual_count == 0:
    print("No suggested clip")
else:
    print(" ".join(suggested_videos))
