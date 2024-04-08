word = str(input())
sentence = str(input())

symbol = ["\"", "(", ")", ",", ".", "\'"]
for item in symbol:
    sentence = sentence.replace(item," ")
words_list = sentence.split()

count = 0
for item in words_list:
    if(item == word):
        count += 1

print(count)