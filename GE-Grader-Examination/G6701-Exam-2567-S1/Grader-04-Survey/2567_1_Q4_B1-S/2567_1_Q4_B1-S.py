# Input scores and subject
scores = [float(e) for e in input().split()]
subject = input().strip()

# Calculate mean
mean = sum(scores) / len(scores)
# Calculate Standard Deviation
sd = 0
for score in scores:
    sd += (score - mean)**2
sd = (sd / len(scores))**(0.5)

# Calculate T-Score for TGAT and TPAT
tScores = []
if(subject in ["TGAT", "TPAT"]):
    for score in scores:
        tScore = 50 + 8.69031*((score - mean)/sd)
        tScore = round(tScore, 2)
        tScores.append(str(tScore))
# Calculate T-Score for A-Level
if(subject == "A-LEVEL"):
    for score in scores:
        tScore = 50 + 5.21299*((score - mean)/sd)
        tScore = round(tScore, 2)
        tScores.append(str(tScore))

# Output
print(" ".join(tScores))