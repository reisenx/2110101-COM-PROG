import pandas as pd
import util

# Input generate files
print("----------TABLE GENERATOR----------")
start, end = util.welcome()

# Loop generate each file
for unit in range(start, end):
    # Read CSV file
    file = util.FILENAME[unit]
    input_path = f"PL-Problem-List/database/csv/{file}.csv"
    df = pd.read_csv(input_path)
    
    # Construct a markdown file
    markdown = []
    # Table Header
    markdown.append('| No. | Problem Code | Name | Difficulty | Solution |')
    markdown.append('| :---: | :--- | :--- | :--- | :--- |')
    # Iterate through CSV file
    for row in df.itertuples():
        # Construct each part of each line
        no = str(row.Index + 1)
        problem = f"[`{row.code}`]({row.link})"
        name = f"**{row.name}**"
        stars = util.get_stars(row.level)
        sol = f"[`Solution`]({util.get_problem_path(unit, row.code)})"
        # Add line to markdown list
        markdown.append(f"| {no} | {problem} | {name} | {stars} | {sol} |")
    
    # Write markdown to a text file
    markdown = '\n'.join(markdown)
    output_path = f"PL-Problem-List/database/txt/table/{file}.txt"
    with open(output_path, 'w', encoding = 'utf-8') as f:
        f.write(markdown)
    
    # Update Log
    print(f"{file}.txt successfully generated from {file}.csv")