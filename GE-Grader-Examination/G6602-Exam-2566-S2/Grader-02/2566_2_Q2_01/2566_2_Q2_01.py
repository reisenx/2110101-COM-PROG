# --------------------------------------------------
# File Name : 2566_2_Q2_01.py
# Problem   : Offensive Words
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------


# Replace vowels in offensive words with '*'
def hide_vowels(word: str) -> str:
    result = ""
    for char in word:
        if char.lower() in "aeiou":
            char = "*"
        result += char
    return result


# Censor the text by replacing offensive word with their vowel-hidden versions
def censor_text(text: str, target: str) -> str:
    # Initialize the result with the original text and search index
    result = text
    search_idx = 0
    # Loop to find and replace all occurrences of the target word
    while True:
        # Find the next occurrence of the target word
        start_idx = result.lower().find(target.lower(), search_idx)
        end_idx = start_idx + len(target)
        # If no more occurrences are found, break the loop
        if start_idx == -1:
            break
        # Replace the target word with its vowel-hidden version
        before_target = result[:start_idx]
        censored_target = hide_vowels(result[start_idx:end_idx])
        after_target = result[end_idx:]
        result = before_target + censored_target + after_target
        # Update the search index to continue searching after the replaced word
        search_idx = end_idx
    # Return the censored text
    return result


# Read the list of offensive words and the text to censor
offensive_words = input().strip().split()
text = input().strip()
# Censor the text for each offensive word
for word in offensive_words:
    text = censor_text(text, word)
# Output the final censored text
print(text)
