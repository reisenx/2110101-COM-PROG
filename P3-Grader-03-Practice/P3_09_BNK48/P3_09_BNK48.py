# --------------------------------------------------
# File Name : P3_09_BNK48.py
# Problem   : Part-III BNK48
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# Initialize dictionaries to store otaku and idol data
otakus = {}
idols = {}


# Function to handle voting by otakus for idols
def vote(otaku: str, idol: str, score: int) -> None:
    # If the otaku or idol does not exist, initialize them
    if otaku not in otakus:
        otakus[otaku] = {"vote": [], "kamioshi": ""}
    if idol not in idols:
        idols[idol] = {"total_score": 0, "otakus": set(), "kamioshi_count": 0}
    # Update the otaku's vote for the idol and idol's total score
    otakus[otaku]["vote"].append([idol, score])
    idols[idol]["total_score"] += score
    idols[idol]["otakus"].add(otaku)


# Function to determine the kamioshi (favorite idol) for an otaku
def get_kamioshi(otaku: str) -> str:
    # Sort the votes of the otaku by score (descending) and idol name (ascending)
    idol_ranks = []
    for idol, score in otakus[otaku]["vote"]:
        idol_ranks.append([-score, idol])
    idol_ranks.sort()
    # Return the idol with the highest score (kamioshi)
    return idol_ranks[0][1]


# Function to update all otakus' kamioshi and idols' kamioshi counts
def update_all_kamioshi() -> None:
    # Iterate through each otaku and determine their kamioshi
    for otaku, details in otakus.items():
        # Get the kamioshi for the otaku
        kamioshi = get_kamioshi(otaku)
        # Update the otaku's kamioshi
        details["kamioshi"] = kamioshi
        idols[kamioshi]["kamioshi_count"] += 1


# Function to get the top 3 idols based on total votes
def get_top_total_votes() -> list[str]:
    # Sort idols by total score (descending) and idol name (ascending)
    idol_ranks = []
    for idol, details in idols.items():
        idol_ranks.append([-details["total_score"], idol])
    idol_ranks.sort()
    # Return the top 3 idols
    results = []
    for _, idol in idol_ranks[:3]:
        results.append(idol)
    return results


# Function to get the top 3 idols based on the number of otakus
def get_top_otaku_count() -> list[str]:
    # Sort idols by the number of otakus (descending) and idol name (ascending)
    idol_ranks = []
    for idol, details in idols.items():
        idol_ranks.append([-len(details["otakus"]), idol])
    idol_ranks.sort()
    # Return the top 3 idols
    results = []
    for _, idol in idol_ranks[:3]:
        results.append(idol)
    return results


# Function to get the top 3 idols based on kamioshi counts
def get_top_kamioshi_count() -> list[str]:
    # Sort idols by kamioshi count (descending) and idol name (ascending)
    idol_ranks = []
    for idol, details in idols.items():
        idol_ranks.append([-details["kamioshi_count"], idol])
    idol_ranks.sort()
    # Return the top 3 idols
    results = []
    for _, idol in idol_ranks[:3]:
        results.append(idol)
    return results


# Main function
def main() -> None:
    # Read votes from otakus to idols
    while True:
        data = input().strip().split()
        # Stop if the input is a command
        if len(data) == 1:
            cmd = int(data[0]) - 1
            break
        # Update the vote for the idol by the otaku
        otaku, idol, score = data[0], data[1], int(data[2])
        vote(otaku, idol, score)
    # Update kamioshi for all otakus and kamioshi counts for idols
    update_all_kamioshi()
    # Output the results based on the command
    results = [get_top_total_votes(), get_top_otaku_count(), get_top_kamioshi_count()]
    print(", ".join(results[cmd]))


# Call the main function to start the program
main()
