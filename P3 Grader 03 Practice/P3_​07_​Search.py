# Calculate frequency of a word in text
# It is guaruntee that all parameters will be all uppercase
def frequency(text, word):
    # Create a list of words
    words_list = text.strip().split()
    # Count times that a specified word appears in text
    appears_count = words_list.count(word)
    # Count all words in a text
    words_count = len(words_list)
    # Calculate frequency
    freq = appears_count/words_count
    return freq

# Calculate specified value of a word in text
# It is guaruntee that all parameters will be all uppercase
def specified(text, word):
    # Create a list of words, then convert it to set to delete duplicates
    words_list = text.strip().split()
    words_set = set(words_list)
    # Count all unique words in a set
    unique_count = len(words_set)
    # Calculate specified value
    spec = 1/unique_count
    return spec

# Calculate relateable value of a word in text
# It is guaruntee that all parameters will be all uppercase
def relateable(text, word):
    return frequency(text, word) * specified(text, word)

# Input number of documents
n = int(input())

# Input documents and store them in dictionary and list
doc_name = []
documents = {}
for i in range(n):
    name = input()
    text = input()
    doc_name.append(name)
    documents[name] = text

# Input searching words until -1
# Contains all searching words in a list
search_words = []
while(True):
    temp = input()
    if(temp == "-1"):
        break
    else:
        search_words.append(temp)

# Output a document that is the most relateable to each serching words
# If the maximum relateable value = 0, then output "NOT FOUND"
for word in search_words:
    # Find document with maximum relateable value and its name
    maximum = 0
    max_name = "NOT FOUND"
    for name, text in documents.items():
        if(relateable(text,word) > maximum):
            max_name = name
            maximum = relateable(text,word)
    # Output a name of document with maximum relateable value
    print(max_name)