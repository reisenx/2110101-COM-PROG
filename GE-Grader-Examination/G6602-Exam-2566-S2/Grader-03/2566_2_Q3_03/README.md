<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Hashtag Recommendation ★★ (
      <a href="https://drive.google.com/file/d/1Rcox7hJg5OtCnwYM4SuiiLp4fweragxh/view?usp=sharing">
        <code>2566_2_Q3_03</code>
      </a>
    )
  </h1>
</div>

# Contents

- [**แนวคิด**](#แนวคิด)
- [**ขั้นตอนการแก้ปัญหา**](#ขั้นตอนการแก้ปัญหา)
- [**การเรียงลำดับคำแนะนำ**](#การเรียงลำดับคำแนะนำ)
- [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
- [**รูปแบบข้อมูลนำเข้าและส่งออก**](#รูปแบบข้อมูลนำเข้าและส่งออก)
- [**ข้อควรระวัง**](#ข้อควรระวัง)
- [**Solution**](#solution)

---

# แนวคิด

แต่ละคลิปมี `clip_id` และกลุ่มแฮชแท็ก โปรแกรมจึงเก็บข้อมูลด้วย dictionary โดยใช้ `clip_id` เป็นคีย์ และใช้ `set` เป็นค่าของแฮชแท็ก เช่น

```python
{
    "clip01": {"labubu", "popmart"},
    "clip03": {"unbox", "molly", "popmart"},
}
```

`set` เหมาะกับข้อนี้เพราะแฮชแท็กเดียวกันต้องนับเพียงครั้งเดียว แม้จะปรากฏในคลิปที่ผู้ใช้เคยมีส่วนร่วมหลายคลิป

ให้ $H(v)$ เป็นเซตแฮชแท็กของคลิป $v$ และให้ $V_{\text{known}}$ เป็นคลิปที่ผู้ใช้เคยมีส่วนร่วมและมีข้อมูลอยู่ใน dictionary เซตแฮชแท็กที่ผู้ใช้สนใจทั้งหมดคือ

$$
U = \bigcup_{v \in V_{\text{known}}} H(v)
$$

ใน Python การรวมเซตทำได้ด้วย

```python
visited_hashtags |= video_hashtags[video]
```

สำหรับคลิปที่ยังไม่เคยมีส่วนร่วม คะแนนคือจำนวนแฮชแท็กที่อยู่ทั้งในคลิปนั้นและใน `visited_hashtags`

$$
\operatorname{score}(v) = |H(v) \cap U|
$$

ซึ่งตรงกับ Python ว่า

```python
mutual_count = len(hashtags & visited_hashtags)
```

# ขั้นตอนการแก้ปัญหา

1. อ่านข้อมูลแต่ละคลิปจนพบ `q` แล้วเก็บ `video_name` กับ `set` ของแฮชแท็กใน `video_hashtags`
2. อ่านลิสต์ `visited_videos`
3. วนผ่านคลิปที่เคยมีส่วนร่วม ถ้ามีข้อมูลของคลิปนั้น ให้รวมแฮชแท็กเข้า `visited_hashtags` ถ้าไม่มีข้อมูลให้ข้าม
4. วนผ่านคลิปทั้งหมดอีกครั้ง โดยไม่พิจารณาคลิปที่อยู่ใน `visited_videos`
5. หาจำนวนแฮชแท็กร่วมด้วย set intersection `&` และติดตามค่าสูงสุดใน `max_mutual_count`
6. เก็บคะแนนและชื่อคลิปลงใน `mutual_hashtags_count`
7. เรียงข้อมูล เลือกทุกคลิปที่ได้คะแนนสูงสุด แล้วแสดงชื่อคั่นด้วยช่องว่าง
8. ถ้าคะแนนสูงสุดเป็น `0` ให้แสดง `No suggested clip`

# การเรียงลำดับคำแนะนำ

โจทย์ต้องการให้คะแนนมากอยู่ก่อน แต่ถ้าคะแนนเท่ากันให้ชื่อคลิปเรียงตามลำดับพจนานุกรม โค้ดจึงเก็บทูเปิลเป็น

```python
(-mutual_count, video)
```

เมื่อเรียก `.sort()` ทูเปิลจะเรียงจากสมาชิกตัวแรกก่อน

- คะแนน `3` ถูกเก็บเป็น `-3` และจะมาก่อนคะแนน `2` ที่ถูกเก็บเป็น `-2`
- ถ้าคะแนนที่ติดลบเท่ากัน Python จะเปรียบเทียบ `video` ต่อ ทำให้ชื่อเรียงจากน้อยไปมาก

หลังเรียงแล้ว คลิปที่ได้คะแนนสูงสุดจะอยู่ติดกันที่ต้นลิสต์ ลูปสุดท้ายจึงเก็บคลิปเหล่านี้และหยุดทันทีเมื่อพบคะแนนที่น้อยกว่า `max_mutual_count`

# ตัวอย่างการทำงาน

สมมติว่าผู้ใช้เคยมีส่วนร่วมกับ `c02` และ `c04`

```text
c05 fold cat irish
c04 cat fold brit
c03 cat scot fold
c02 fold cat
c01 cat fold
```

คลิป `c06` ที่อยู่ในรายชื่อคลิปที่เคยมีส่วนร่วมแต่ไม่มีข้อมูลจะถูกข้าม เซตแฮชแท็กที่สนใจจาก `c02` และ `c04` คือ `{"cat", "fold", "brit"}`

คลิปที่ยังไม่เคยมีส่วนร่วมมีคะแนนดังนี้

| คลิป | แฮชแท็กที่ซ้ำ | คะแนน |
|---|---|---:|
| `c01` | `cat`, `fold` | `2` |
| `c03` | `cat`, `fold` | `2` |
| `c05` | `cat`, `fold` | `2` |

ทุกคลิปได้คะแนนสูงสุดเท่ากัน จึงเรียงชื่อและแสดงผลเป็น

```text
c01 c03 c05
```

# รูปแบบข้อมูลนำเข้าและส่งออก

ลำดับข้อมูลนำเข้าคือ

1. หลายบรรทัดในรูป `clip_id hashtag1 hashtag2 ...`
2. บรรทัด `q` เพื่อจบข้อมูลคลิป
3. หนึ่งบรรทัดที่เป็นรายชื่อคลิปซึ่งผู้ใช้เคยมีส่วนร่วม คั่นด้วยช่องว่าง

โปรแกรมแสดงผลเพียงหนึ่งบรรทัด

- ถ้ามีคะแนนสูงสุดมากกว่า `0` ให้แสดง `clip_id` ทุกตัวที่ได้คะแนนนั้น คั่นด้วยช่องว่าง และเรียงตามลำดับพจนานุกรม
- ถ้าไม่มีแฮชแท็กร่วมเลย ไม่มีคลิปเหลือให้แนะนำ หรือมีแต่รหัสคลิปที่ไม่ทราบข้อมูล ให้แสดงข้อความ `No suggested clip`

# ข้อควรระวัง

- ห้ามแนะนำคลิปที่อยู่ใน `visited_videos`
- คลิปที่เคยมีส่วนร่วมแต่ไม่มีใน `video_hashtags` ต้องถูกข้าม
- การซ้ำของแฮชแท็กทั้งภายในคลิปเดียวและระหว่างหลายคลิปไม่นับเพิ่ม เพราะเก็บด้วย `set`
- ถ้าคลิปที่ยังไม่เคยมีส่วนร่วมทุกคลิปได้คะแนน `0` ต้องแสดง `No suggested clip` ไม่ใช่แสดงชื่อคลิปทั้งหมด
- โจทย์รับประกันว่า `clip_id` ไม่ซ้ำ และทั้ง `clip_id` กับแฮชแท็กเป็นตัวพิมพ์เล็ก โค้ดจึงไม่แปลงรูปแบบข้อมูลเพิ่มเติม

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_2_Q3_03.py
# Problem   : Hashtag Recommendation
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
```
