# Input a DNA and convert it into a uppercase
DNA = input().strip().upper()
operation = input().strip().upper()

# Check if an input is an valid DNA or not
IsValid = True
DNA_char = "ATGC"
for char in DNA:
    if(char not in DNA_char):
        IsValid = False
        break

# Output
# Process an operation if the DNA is valid DNA
if(not IsValid):
    print("Invalid DNA")
else:
    # Operation R
    # 1.) Change A <--> T and G <--> C
    # 2.) Reverse a new DNA and output it
    # Example: "AAAACCCGGT" --> "TTTTGGGCCA" --> "ACCGGGTTTT"
    if(operation == 'R'):
        new_DNA = ""
        for char in DNA:
            if(char == "A"):
                new_DNA += "T"
            elif(char == "T"):
                new_DNA += "A"
            elif(char == "G"):
                new_DNA += "C"
            elif(char == "C"):
                new_DNA += "G"
        print(new_DNA[::-1])
    
    # Operation F
    # Just count how many A, T, G, C in a DNA
    # Example: "AAAACCCGGT" --> "A=4, T=1, G=2, C=3"
    elif(operation == 'F'):
        A = DNA.count('A')
        T = DNA.count('T')
        G = DNA.count('G')
        C = DNA.count('C')
        print("A=" + str(A) + ", T=" + str(T) + ", G=" + str(G) + ", C=" + str(C))
    
    # Operation D
    # Count a repetition of a pair of letter that occurs in a DNA
    # The repetition must occurs in 1 place
    # Example: The repetition occurs in "AAAACCCGGT" are
    # "[AA]AACCCGGT", "A[AA]ACCCGGT", "AA[AA]CCCGGT"
    elif(operation == "D"):
        pattern = input().strip().upper()
        count = 0
        for index in range(len(DNA)-1):
            if(DNA[index : index + 2] == pattern):
                count += 1
        print(count)