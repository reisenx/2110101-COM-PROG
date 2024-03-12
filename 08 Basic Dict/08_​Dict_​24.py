# In the past, a mobile phone has the keypad like this
# 1        | 2 [abc] | 3 [def]
# 4 [ghi]  | 5 [jkl] | 6 [mno]
# 7 [pqrs] | 8 [tuv] | 9 [wxyz]
# To type a letter 'a', you need to press '2' one time
# To type a letter 'b', you need to press '2' two times
# To type a letter 'c', you need to press '2' three times
# To type a spacebar, you need to press '0' one time

# Create a dictionary that convert text <--> str
keys_to_text = {'2':'a', '22':'b', '222':'c',
               '3':'d', '33':'e', '333':'f',
               '4':'g', '44':'h', '444':'i',
               '5':'j', '55':'k', '555':'l',
               '6':'m', '66':'n', '666':'o',
               '7':'p', '77':'q', '777':'r', '7777':'s',
               '8':'t', '88':'u', '888':'v',
               '9':'w', '99':'x', '999':'y', '9999':'z', '0':' '}
text_to_keys = {'a':'2', 'b':'22', 'c':'222',
               'd':'3', 'e':'33', 'f':'333',
               'g':'4', 'h':'44', 'i':'444',
               'j':'5', 'k':'55', 'l':'555',
               'm':'6', 'n':'66', 'o':'666',
               'p':'7', 'q':'77', 'r':'777', 's':'7777',
               't':'8', 'u':'88', 'v':'888',
               'w':'9', 'x':'99', 'y':'999', 'z':'9999', ' ':'0'}
# Create a string that contains all lowercase alphabet and spacebar
alphabet = "abcdefghijklmnopqrstuvwxyz "

# This function can convert text to keys
# Assume that the uppercase is the same as lowercase and ignore all symbol (except spacebar)
# Example: "I am busy." --> "444 0 2 6 0 22 88 7777 999"
def text2keys(text):
    text = text.lower()
    keys = ""
    for char in text:
        if(char in alphabet):
            keys += text_to_keys[char] + " "
    keys = keys.strip()
    return keys

# This function can convert keys to text
# Example: "444 0 2 6 0 22 88 7777 999" --> "i am busy"
def keys2text(keys):
    keys_list = keys.split()
    text = ""
    for key in keys_list:
        text += keys_to_text[key]
    return text

# Execute an input string
exec(input().strip())