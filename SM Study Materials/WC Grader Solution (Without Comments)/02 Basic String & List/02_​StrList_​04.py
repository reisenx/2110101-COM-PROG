txt = str(input())
N = int(input())
M = len(txt)
print('0'*(max(M,N)-M) + txt)