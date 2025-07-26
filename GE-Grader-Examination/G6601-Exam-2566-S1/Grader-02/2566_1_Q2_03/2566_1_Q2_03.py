# --------------------------------------------------
# File Name : 2566_1_Q2_03.py
# Problem   : Eavesdrop
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------

# Input the character name queries
queries = []
n = int(input())
for _ in range(n):
    queries.append(input().strip())

# Input the novel dialog as a raw string
raw_dialog = ""
while True:
    line = input().strip()
    if line == "END":
        break
    raw_dialog += line + "\n"

# Parse the raw dialog to extract character names and their dialogs
dialog_list = []
# Initialize the index for searching
query_idx = 0
while True:
    # Find the start index of the character name
    name_start_idx = raw_dialog.find("*", query_idx)
    # Stop if no more names are found
    if name_start_idx == -1:
        break
    # Find the end index of the character name
    name_end_idx = raw_dialog.find(":", name_start_idx + 1)
    # Find the start and end index of the dialog
    dialog_start_idx = raw_dialog.find('"', name_end_idx + 1)
    dialog_end_idx = raw_dialog.find('"', dialog_start_idx + 1)

    # Extract the character name and dialog from the raw dialog
    name = raw_dialog[name_start_idx + 1 : name_end_idx].strip()
    dialog = raw_dialog[dialog_start_idx : dialog_end_idx + 1].strip()
    # Store the character name and dialog in the list
    dialog_list.append([name, dialog])

    # Update the query index to search for the next character name
    query_idx = dialog_end_idx + 1

# Output the dialogs for the queried character names
has_dialog = False
for name, dialog in dialog_list:
    if name in queries:
        print(f"{name}: {dialog}")
        has_dialog = True

if not has_dialog:
    print("Maybe wrong novel")
