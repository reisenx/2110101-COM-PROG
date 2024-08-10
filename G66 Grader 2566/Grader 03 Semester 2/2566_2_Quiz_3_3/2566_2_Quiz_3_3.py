# Input clip hashtags
hashtags = {}
clips = []
while(True):
    data = input().strip().split()
    if(data[0] != 'q'):
        clips.append(data[0])
        hashtags[data[0]] = set(data[1:])
    else:
        break

max = 0
watch = input().split()
match_set = set()
for item in watch:
    if(item in clips):
        match_set = match_set | hashtags[item]

match_count = {}
max_clips = []
for item in clips:
    if(item not in watch):
        match_count[item] = len(match_set & hashtags[item])
        if(match_count[item] > max):
            max = match_count[item]

if(max != 0):
    for name,count in match_count.items():
        if(count == max):
            max_clips.append(name)
    max_clips.sort()
    print(" ".join(max_clips))
else:
    print("No suggested clip")