<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Text Formatting ★★★ (
      <a href="https://drive.google.com/file/d/1QGJZXr-JWt5Q5TsxwuGSbMgivmjtX_z_/view?usp=drive_link">
        <code>P3_03_Text</code>
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
# File Name : P3_03_Text.py
# Problem   : Part-III Text Formatting
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------


# Print a ruler with dashes and numbers
def print_ruler(limit):
    line = ""
    for i in range(limit // 10):
        line += f"{'-' * 9}{i + 1}"
    line += "-" * (limit % 10)
    print(line)


# Extract words from a file and return them as a list
def extract_words_from_file(filename):
    words = []
    with open(filename) as file:
        for line in file:
            words += line.strip().split(".")
    return words


# Input the filename and limit
filename = input().strip()
limit = int(input())

# Output the ruler
print_ruler(limit)
# Extract words from the file
words = extract_words_from_file(filename)

# Initialize start and end indices for word processing
start, end = 0, 0
# Process until all words are processed
while start < len(words):
    # Construct the line from words[start:end]
    line = ".".join(words[start:end]).strip(".")

    # Check if the end index exceeds the length of words
    if end > len(words):
        print(line)
        break

    # If the line exceeds the limit, print the current line and reset start
    if len(line) > limit:
        # Output the line without the last word to fit the limit
        if end - start > 1:
            print(".".join(words[start : end - 1]).strip("."))
            start = end - 1
        # The length of only one word exceeds the limit
        else:
            print(line)
            start = end
    # If the line does not exceed the limit, increment end
    else:
        end += 1
```
