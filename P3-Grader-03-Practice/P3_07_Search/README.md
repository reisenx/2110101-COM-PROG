<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Search Engine ★★ (
      <a href="https://drive.google.com/file/d/1QUqzKH_17u-sY_sTCGyMRoe2W_uh2dC9/view?usp=drive_link">
        <code>P3_07_Search</code>
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
# File Name : P3_07_Search.py
# Problem   : Part-III Search Engine
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------


# Calculate relatable scores for a list of words.
def calculate_relatable_scores(words):
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

    total_words = len(words)
    total_unique_words = len(word_counts)

    relatable_scores = {}
    for word, count in word_counts.items():
        relatable_scores[word] = (count / total_words) * (1 / total_unique_words)
    return relatable_scores


# Initialize a list of documents.
documents = {}

# Input amount of documents and calculate relatable scores for each document.
n = int(input())
for _ in range(n):
    name = input().strip()
    words = input().strip().split()
    documents[name] = calculate_relatable_scores(words)

# Query for a word and find the most relatable document.
while True:
    query = input().strip()
    if query == "-1":
        break

    max_score = 0
    best_document = ""

    for name, scores in documents.items():
        if query in scores and scores[query] > max_score:
            max_score = scores[query]
            best_document = name

    if max_score > 0:
        print(best_document)
    else:
        print("NOT FOUND")
```
