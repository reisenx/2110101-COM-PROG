txt = str(input())

step1 = txt[3] + txt[10] + txt[17] + txt[24] + txt[31]
step1 = int(step1)

step2 = txt[7] + txt[12] + txt[17] + txt[22] + txt[27]
step2 = int(step2)

step3 = step1 + step2 + 10000
step3 = str(step3)

step4 = step3[-4:-1]

step5 = int(step4[0]) + int(step4[1]) + int(step4[2])
step5 = step5%10 + 1

alphabet = "ABCDEFGHIJ"
step6 = alphabet[step5 - 1]

print(step4 + step6) 