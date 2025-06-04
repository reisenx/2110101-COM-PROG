# Algorithm
# 1.) split() the text with comma (,) first
# 2.) strip() each item in the list to delete the excess spacebar
# 3.) Modify each item in the list. Make the first letter as uppercase and the rest are lower case
# 4.) output using .join()
# Example: text = "Tom, aNN,      TONY,jOe"
# 1.) text.split(',') = ['Tom',' aNN','      TONY','jOe']
# 2.) strip() each item in the list --> ['Tom','aNN','TONY','jOe']
# 3.) Modify each item in the list --> ['Tom','Ann','Tony','Joe']
# 4.) Output using " ".join(list) --> "Tom Ann Tony Joe"
text = str(input())
text_list = text.split(',')
for i in range(len(text_list)):
    text_list[i] = text_list[i].strip()
    text_list[i] = text_list[i][0].upper() + text_list[i][1:].lower()
print(" ".join(text_list))