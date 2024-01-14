#Input variable txt as a string variable
txt=str(input())
#Input variable N as a integer variable
N=int(input())

#Calculuate the length of the text
M=len(txt)

#Output the text in the specific format
#if M>=N, it will output only txt string
#Example: txt="123", M=3, N=2 --> Output:123
#else, it will output a N-M digits "0" then txt string
#Example: txt="123", M=3, N=5 --> Output:00123
print("0"*(max(M,N)-M)+txt)