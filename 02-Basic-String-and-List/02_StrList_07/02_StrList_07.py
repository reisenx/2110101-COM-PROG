# --------------------------------------------------
# File Name : 02_StrList_07.py
# Problem   : Decryption
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input a string of numbers
num = input().strip()

# Step 1: Concatenate the numbers at indices 3, 10, 17, 24, and 31
#         and convert them to an integer.
step1 = num[3] + num[10] + num[17] + num[24] + num[31]
step1 = int(step1)

# Step 2: Concatenate the numbers at indices 7, 12, 17, 22, and 27
#         and convert them to an integer.
step2 = num[7] + num[12] + num[17] + num[22] + num[27]
step2 = int(step2)

# Step 3: Add the results from Step 1 and Step 2, then add 10000
#         and convert the result to a string.
step3 = step1 + step2 + 10000
step3 = str(step3)

# Step 4: Take the middle three digits from the result of Step 3
step4 = step3[-4:-1]

# Step 5: Calculate the sum of the digits in Step 4,
#         choose the last digit, and add 1.
step5 = int(step4[0]) + int(step4[1]) + int(step4[2])
step5 = step5 % 10 + 1

# Step 6: Use the result from Step 5 to select a letter from the alphabet
ALPHABET = "ABCDEFGHIJ"
step6 = ALPHABET[step5 - 1]

# Step 7: Output the final result by concatenating Step 4 and Step 6
print(step4 + step6)
