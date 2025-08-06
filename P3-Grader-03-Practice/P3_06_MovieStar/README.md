<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Movie Stars ★★ (
      <a href="https://drive.google.com/file/d/1DK_DCEgW6pIdlKQ9rGdqh4aLln2Cs7Lr/view?usp=drive_link">
        <code>P3_06_MovieStar</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**Solution**](#solution)

---

<div align="center">
  <h2>เฉลยอย่างละเอียดจะตามมาทีหลัง</h2>
</div>

---

# Solution

```python
# --------------------------------------------------
# File Name : P3_06_MovieStar.py
# Problem   : Part-III Movie Stars
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# Initialize a dictionary to store actor names and their movies
actor_to_movies = {}

# Input the number of movies
n = int(input())
for _ in range(n):
    data = input().strip().split(", ")
    movie = data[0].strip()
    actors = data[1:]

    for actor in actors:
        if actor not in actor_to_movies:
            actor_to_movies[actor] = []
        actor_to_movies[actor].append(movie)

# Input query
query_actors = input().strip().split(", ")
# Find and print the movies for each queried actor
for actor in query_actors:
    if actor in actor_to_movies:
        movies = ", ".join(actor_to_movies[actor])
        print(f"{actor} -> {movies}")
    else:
        print(f"{actor} -> Not found")
```
