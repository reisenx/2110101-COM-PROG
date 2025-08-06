<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Cartoon ★★ (
      <a href="https://drive.google.com/file/d/1-d45vrVJgudHhNZWBcjlpOO7604YnSpC/view?usp=drive_link">
        <code>10_TSD_24</code>
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
# File Name : 10_TSD_24.py
# Problem   : Cartoon
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Initialize a dictionary to store cartoon characters.
characters = {}

# Input cartoon character names and animal types.
while True:
    # Input a line of data.
    data = input().strip()
    # If the input is "q", break the loop.
    if data == "q":
        break

    # Split the input data into name and animal type.
    name, animal = data.split(", ")

    # Update the characters dictionary.
    if animal not in characters:
        characters[animal] = []
    characters[animal].append(name)

# Output the animal types and their corresponding characters.
for animal, names in characters.items():
    print(f"{animal}: {', '.join(names)}")
```
