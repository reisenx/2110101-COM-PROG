# Input variable txt as a string variable
txt = str(input())
# Input variable N as a integer variable
N = int(input())

# Calculuate the length of the text
M = len(txt)

# Output the text in the specific format
# If M >= N, just output txt
# Example: txt = "123", M = 3, N = 2 --> Output: "123"
# If M < N, output N-M digits '0' before txt string
# Example: txt = "123", M = 3, N = 5 --> Output:00123
print('0'*(max(M,N)-M) + txt)