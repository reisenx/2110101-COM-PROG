# --------------------------------------------------
# File Name : 07_StrFile_31.py
# Problem   : DNA
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Initialize the nucleotide characters
NUCLEOTIDE = "AGTC"

# Input DNA sequence
dna = input().strip().upper()

# Validate the DNA sequence
is_dna = True
for char in dna:
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
        modified_dna = ""
        for char in dna:
            idx = NUCLEOTIDE.index(char)
            modified_dna += NUCLEOTIDE[(idx + 2) % 4]
        print(modified_dna[::-1])

    # Count the occurrences of each nucleotide
    elif cmd == "F":
        counts = [0] * 4
        for char in dna:
            idx = NUCLEOTIDE.index(char)
            counts[idx] += 1
        # Output
        A, G, T, C = counts
        print(f"A={A}, T={T}, G={G}, C={C}")

    # Count the occurrences of a specific nucleotide pair
    elif cmd == "D":
        pair = input().strip().upper()
        pair_count = 0
        for i in range(len(dna) - 1):
            if dna[i : i + 2] == pair:
                pair_count += 1
        print(pair_count)

# Invalid DNA sequence
else:
    print("Invalid DNA")
