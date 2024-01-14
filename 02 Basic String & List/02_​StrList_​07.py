#Input a string
txt = str(input())

#Step 1: Pick number in index 3, 10, 17, 24, 31 (index starts at 0)
#Then put them together to be a 5-digit number
step1 = txt[3] + txt[10] + txt[17] + txt[24] + txt[31]
step1 = int(step1)

#Step 2: Pick number in index 7, 12, 17, 22, 27 (index starts at 0)
#Then put them together to be a 5-digit number
step2 = txt[7] + txt[12] + txt[17] + txt[22] + txt[27]
step2 = int(step2)

#Step 3: Add number from Step 1 + Step 2 + 10,000
step3 = step1 + step2 + 10000
step3 = str(step3)

#Step 4: Pick only a number from thousands, hundreds and tens from a number from Step 3
#then put them together to be a 3-digit number
step4 = step3[-4:-1:1]

#Step 5: Pick ones from a sum of digits of 3-digit number then add 1
#Example: 813 --> 8 + 1 + 3 --> 12 --> 2 --> 2 + 1 --> 3
step5 = int(step4[0]) + int(step4[1]) + int(step4[2])
step5 = step5%10 + 1

#Step 6: Convert a number from step 5 to an alphabet
#Example: 1-->A, 2-->B, 3-->C and so on
alphabet = ["A","B","C","D","E","F","G","H","I","J"]
step6 = alphabet[step5-1]

#Step 7: Output a number from Step 4 with an alphabet from Step 6 together
print(step4+step6) 