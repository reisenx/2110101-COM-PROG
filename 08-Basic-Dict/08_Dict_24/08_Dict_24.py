# --------------------------------------------------
# File Name : 08_Dict_24.py
# Problem   : Texting
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Initialize dictionaries for conversion between keys and text
TEXT_TO_KEYS = {
    " ": "0",
    "a": "2",
    "b": "22",
    "c": "222",
    "d": "3",
    "e": "33",
    "f": "333",
    "g": "4",
    "h": "44",
    "i": "444",
    "j": "5",
    "k": "55",
    "l": "555",
    "m": "6",
    "n": "66",
    "o": "666",
    "p": "7",
    "q": "77",
    "r": "777",
    "s": "7777",
    "t": "8",
    "u": "88",
    "v": "888",
    "w": "9",
    "x": "99",
    "y": "999",
    "z": "9999",
}
KEYS_TO_TEXT = {
    "0": " ",
    "2": "a",
    "22": "b",
    "222": "c",
    "3": "d",
    "33": "e",
    "333": "f",
    "4": "g",
    "44": "h",
    "444": "i",
    "5": "j",
    "55": "k",
    "555": "l",
    "6": "m",
    "66": "n",
    "666": "o",
    "7": "p",
    "77": "q",
    "777": "r",
    "7777": "s",
    "8": "t",
    "88": "u",
    "888": "v",
    "9": "w",
    "99": "x",
    "999": "y",
    "9999": "z",
}


# Function to convert text to keys
def text2keys(text):
    result = []
    for char in text.lower():
        if char in TEXT_TO_KEYS:
            result.append(TEXT_TO_KEYS[char])
    return " ".join(result)


# Function to convert keys to text
def keys2text(keys):
    result = ""
    for key in keys.split():
        if key in KEYS_TO_TEXT:
            result += KEYS_TO_TEXT[key]
    return result


# Execute the input string as code
exec(input().strip())
