def missing_digits(text):
    count = [0,0,0,0,0,0,0,0,0,0]

    for character in text:
        if("0" <= character <= "9"):
            count[int(character)] += 1

    missing = []
    for i in range(0,10):
        if(count[i] == 0):
            missing.append(i)
    return missing

exec(input())