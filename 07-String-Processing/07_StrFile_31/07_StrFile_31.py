# --------------------------------------------------
# File Name : 07_StrFile_31.py
# Problem   : DNA
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input DNA sequence
DNA = input().strip().upper()
NUCLEOTIDE = "AGTC"

# Validate the DNA sequence
is_dna = True
for char in DNA:
    if char not in NUCLEOTIDE:
        is_dna = False
        break

# Input command
cmd = input().strip().upper()

# Process commands if the sequence is valid
if is_dna:
    # Reverse the DNA sequence
    # Change A to T, T to A, C to G, and G to C
    # Then reverse the string
    if cmd == "R":
        new_DNA = ""
        for char in DNA:
            idx = NUCLEOTIDE.index(char)
            new_DNA += NUCLEOTIDE[(idx + 2) % 4]
        print(new_DNA[::-1])

    # Count the occurrences of each nucleotide
    elif cmd == "F":
        counts = [0] * 4
        for char in DNA:
            idx = NUCLEOTIDE.index(char)
            counts[idx] += 1
        # Output
        A, G, T, C = counts
        print(f"A={A}, T={T}, G={G}, C={C}")

    # Count the occurrences of a specific nucleotide pair
    elif cmd == "D":
        pair = input().strip().upper()
        pair_count = 0
        for i in range(len(DNA) - 1):
            if DNA[i : i + 2] == pair:
                pair_count += 1
        print(pair_count)

# Invalid DNA sequence
else:
    print("Invalid DNA")
