# HW4_Social_Media_Data

# Input CSV file and return all data in CSV file as a dict
# Key: Post_ID
# Value: [Text, Platform, Retweets, Likes, Country, Year]
# From social_media_data.csv header, we have
# Post_ID,Text,Sentiment,Timestamp,User,Platform,Retweets,Likes,Country,Year,Month,Day,Hour
# Since the first line of the CSV file is the header, we need to skip it.
# After skip it, we need to split data with comma (,) and input an a data in index 1,5,6,7,8,9
# Don't forget to convert Retweets and Likes to integer.
def social_media_data(file_in):
    f = open(file_in, encoding="utf-8")
    social_dict = {}
    IsFirstLine = True
    for line in f:
        # Skip first line (Header)
        if(not IsFirstLine):
            data = line.strip().split(',')
            social_dict[data[0]] = [data[1].strip(), data[5].strip(),
                                    int(data[6]), int(data[7]),
                                    data[8].strip(), data[9].strip()]
        else:
            IsFirstLine = False
    return social_dict

# Check if a parameter 'word' is in the file stopwords.txt
# Consider lowercase and uppercase as a same character
def is_stopword(word):
    f = open("stopwords.txt", "r")
    # Get a list of stopwords from stopwords.txt
    stopwords = f.readline().strip().split(", ")
    for i in range(len(stopwords)):
        stopwords[i] = stopwords[i].strip()
    # Check if the word is stopword
    if(word.lower() in stopwords):
        return True
    else:
        return False    

# Count a word (except stopwords) in text and update them in word_count_dict
# - Consider lowercase and uppercase as a same character
# - Consider singular and plural word as different word
# - Consider hashtag word as different word (Example: #Enjoy and enjoy is not the same)
#   and guaruntee that there are no single '#' in a text
# - Consider a word like "can't" --> cant, "soul-stirring" --> "soulstirring" and "Jay-Z" --> "jayz"
# - Beware of ".,:;?()[]"'{}-/|_!"
# - No need to order keys in word_count_dict
def count_words_from_text(word_count_dict, text):
    # Split a string into a list of words
    words = text.split()
    # Convert all words in a list into lowercase and remove all symbols
    for i in range(len(words)):
        words[i] = words[i].lower()
        temp = ""
        for char in words[i]:
            if(char not in ".,:;?()[]\"\'{}-/|_!"):
                temp += char
        words[i] = temp
    # Count words
    for word in words:
        if(not is_stopword(word)):
            if(word not in word_count_dict):
                word_count_dict[word] = 1
            else:
                word_count_dict[word] += 1
    return word_count_dict
        
# This function filter a data by year, country and platform and returns as a word count dict
# Parameter 'data_dict' keys is 'Post_ID' and value is [Text, Platform, Retweets, Likes, Country, Year]
# Count words in 'Text' in each value in data_dict
# If year = 'all', output data in all year from a data_dict
# If country = 'all', output data in all country from data_dict
# If platform = 'all', output data in all platform from
# Uppercase and lowercase are not the same
def count_words_from_data_dict(data_dict, year, country, platform):
    words_count = {}
    for key in data_dict:
        # All year, country and platform
        if(year == 'all' and country == 'all' and platform == 'all'):
            words_count = count_words_from_text(words_count,data_dict[key][0])
        # All year and country. Filter only platform
        elif(year == 'all' and country == 'all'):
            if(data_dict[key][1] == platform):
                words_count = count_words_from_text(words_count,data_dict[key][0])
        # All year and platform. Filter only country
        elif(year == 'all' and platform == 'all'):
            if(data_dict[key][4] == country):
                words_count = count_words_from_text(words_count,data_dict[key][0])
        # All country and platform. Filter only year
        elif(country == 'all' and platform == 'all'):
            if(data_dict[key][5] == year):
                words_count = count_words_from_text(words_count,data_dict[key][0])
        # All year. Filter country and platform
        elif(year == 'all'):
            if(data_dict[key][4] == country and data_dict[key][5] == platform):
                words_count = count_words_from_text(words_count,data_dict[key][0])
        # All country. Filter year and platform
        elif(country == 'all'):
            if(data_dict[key][5] == year and data_dict[key][1] == platform):
                words_count = count_words_from_text(words_count,data_dict[key][0])
        # All platform. Filter year and country
        elif(platform == 'all'):
            if(data_dict[key][5] == year and data_dict[key][4] == country):
                words_count = count_words_from_text(words_count,data_dict[key][0])
        # Filter year, country and platform
        else:
            if(data_dict[key][5] == year and data_dict[key][4] == country and data_dict[key][1] == platform):
                words_count = count_words_from_text(words_count,data_dict[key][0])
    return words_count

# This function returns top 'k' highest word count. Returns as a list with words
# If the words have the same count, then sort them in alphabetical order
# In case of k is greater than len(unique_count), returns all words but in order
# In case of length of list 'words' is already greater than k, break the loop
def top_k_words(word_count_dict, k):
    # Find unique_count from word_count_dict
    # Example: word_count_dict = {'dreams':15,,'day':9,'like':10,'feeling':10,'challenges':9}
    # unique_count = [15,10,9]
    unique_count = []
    for key in word_count_dict:
        if(word_count_dict[key] not in unique_count):
            unique_count.append(word_count_dict[key])
    unique_count.sort(reverse = True)
    # Find and return a list of top 'k' highest word count
    words = []
    # Use min(k, len(unique_count) in case of k is greater than len(unique_count)
    for i in range(min(k, len(unique_count))):
        temp = []
        if(len(words) < k):
            for key in word_count_dict:
                if(word_count_dict[key] == unique_count[i]):
                    temp.append(key)
            temp.sort()
            for item in temp:
                words.append(item)
        # Break the loop in case of length of list 'words' is already greater than k
        else:
            break
    return words

# Use all previous function to solve this
# - file_in = social_media_data.csv
# - file_out = top 'k' word count (.txt)
# - year = if 'all', then consider all year
# - country = if 'all', then consider all country
# - platform = if 'all', then consider all platform
# - This function does not return anything but edit/create file in parameter 'file_out'
# - If there is no data, then edit text in 'file_out' as 'No data'
def count_word_summary(file_in, file_out, k, year, country, platform):
    social_dict = social_media_data(file_in)
    count_words = count_words_from_data_dict(social_dict, year, country, platform)
    top_k = top_k_words(count_words, k)
    f = open(file_out, 'w')
    text = ""
    for word in top_k:
        text += word + ":" + str(count_words[word]) + "\n"
    if(text == ""):
        f.write("No data")
    else:
        f.write(text)
    f.close()