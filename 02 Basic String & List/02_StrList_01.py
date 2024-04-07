#Input ID
id=input()

#Calculate the last digits then put it at the end of the list
#Don't forget to convert to int before calcululating
last_digit=(11-(13*int(id[0]) + 12*int(id[1]) + 11*int(id[2]) + 10*int(id[3]) + 9*int(id[4]) + 8*int(id[5]) + 7*int(id[6]) + 6*int(id[7]) + 5*int(id[8]) + 4*int(id[9]) + 3*int(id[10]) + 2*int(id[11]))%11)%10

#Output the ID in specific format
print(id[0],id[1:5],id[5:10],id[10:12],last_digit)