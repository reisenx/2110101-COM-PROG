import pandas as pd
import util

# Input generate files
print("----------HEADER GENERATOR----------")
start, end = util.welcome()

# Loop generate each file
for unit in range(start, end):
    # Read CSV file
    file = util.FILENAME[unit]
    input_path = f"PL-Problem-List/database/csv/{file}.csv"
    df = pd.read_csv(input_path)
    
    # Construct a markdown file
    markdown = []
    # Iterate through CSV file
    for row in df.itertuples():
        # Problem Header in HTML
        HTML = []
        HTML.append('<div align=\"center\">')
        HTML.append('  <h1>')
        HTML.append(f"    {row.name} {util.get_stars(row.level)} (")
        HTML.append(f"      <a href=\"{row.link}\">")
        HTML.append(f"        <code>{row.code}</code>")
        HTML.append('      </a>')
        HTML.append('    )')
        HTML.append('  </h1>')
        HTML.append('</div>\n')
        # Add line to markdown list
        markdown.append('\n'.join(HTML))
    
    # Write markdown to a text file
    markdown = '\n'.join(markdown)
    output_path = f"PL-Problem-List/database/txt/header/{file}.txt"
    with open(output_path, 'w', encoding = 'utf-8') as f:
        f.write(markdown)
    
    # Update Log
    print(f"{file}.txt successfully generated from {file}.csv")