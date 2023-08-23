import json

# Provided JSON data
json_data = ''
# Parse JSON data
data = json.loads(json_data)


# Extract column headers dynamically from the keys in the JSON objects
column_headers = list(data[0].keys())

# Create an HTML table
html_table = "<table border='1'><tr>"
html_table += "".join(f"<th>{header}</th>" for header in column_headers)
html_table += "</tr>"

# Populate the table with data
for obj in data:
    html_table += "<tr>"
    for header in column_headers:
        html_table += f"<td>{obj.get(header, '')}</td>"
    html_table += "</tr>"

html_table += "</table>"


# Save the HTML table to a file or print it
with open("output_table.html", "w") as f:
    f.write(html_table)

print("HTML table generated and saved to 'output_table.html'")
