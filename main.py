from jinja2 import Environment, FileSystemLoader
import pandas as pd
import os
from weasyprint import HTML
import webbrowser

# def df_to_html_merging_cells(df):
#     html = '<table>\n'
    
#     # Track previous values for vertical merging
#     prev_values = [None for _ in df.columns]
#     row_spans = [1 for _ in df.columns]
#     last_non_empty_cell = ['' for _ in df.columns]

#     for i, row in df.iterrows():
#         html += '<tr>\n'

#         for j, item in enumerate(row):
#             if item == '':
#                 # Increase rowspan
#                 row_spans[j] += 1
#             else:
#                 # New cell: reset rowspan and update prev_values
#                 if row_spans[j] > 1:
#                     # Replace the rowspan of the last non-empty cell
#                     html = html.replace(
#                         last_non_empty_cell[j], 
#                         '<td rowspan="{}">{}</td>\n'.format(row_spans[j], prev_values[j])
#                     )
#                     row_spans[j] = 1

#                 last_non_empty_cell[j] = '<td>{}</td>\n'.format(item)
#                 html += last_non_empty_cell[j]
#                 prev_values[j] = item

#         html += '</tr>\n'
        
#     # handle the last row's rowspan
#     for j, rowspan in enumerate(row_spans):
#         if rowspan > 1:
#             html = html.replace(
#                 last_non_empty_cell[j], 
#                 '<td rowspan="{}">{}</td>\n'.format(rowspan, prev_values[j])
#             )

#     html += '</table>'
#     return html

# # Read the CSV data
# df = pd.read_csv('data/test.csv', keep_default_na=False)

# # Fill NaNs with empty strings
# df.fillna("", inplace=True)


# # Convert DataFrame to HTML with merged cells
# table_merged = df_to_html_merging_cells(df)



import pandas as pd

def df_to_html_merging_cells(df):
    # Track previous values for vertical merging
    prev_values = [None for _ in df.columns]
    row_spans = [1 for _ in df.columns]
    last_non_empty_cell = ['' for _ in df.columns]
    headers = list(df.columns)
    table = []

    for i, row in df.iterrows():
        html_row = []
        for j, item in enumerate(row):
            if item == '':
                # Increase rowspan
                row_spans[j] += 1
            else:
                # New cell: reset rowspan and update prev_values
                if row_spans[j] > 1:
                    # Replace the rowspan of the last non-empty cell
                    table[-row_spans[j]][j] = {'value': prev_values[j], 'rowspan': row_spans[j]}
                    row_spans[j] = 1

                html_row.append({'value': item})
                prev_values[j] = item
        table.append(html_row)
        
    # handle the last row's rowspan
    for j, rowspan in enumerate(row_spans):
        if rowspan > 1:
            table[-rowspan][j] = {'value': prev_values[j], 'rowspan': rowspan}

    return headers, table

# Read the CSV data
df = pd.read_csv('data/test.csv', keep_default_na=False)

# Fill NaNs with empty strings
df.fillna("", inplace=True)

# Convert DataFrame to HTML with merged cells
headers, table = df_to_html_merging_cells(df)







def create_pdf(data, template_path="template.html", output="report.pdf"):
    # Load your Jinja2 template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_path)

    # Render the template with your data
    rendered_html = template.render(data=data)

    # Create the pdf
    HTML(string=rendered_html).write_pdf(output)

    # Open the pdf
    webbrowser.open_new_tab(output)

# Read the CSV data
tb_summary = pd.read_csv('data/summary.csv').fillna('NA')
tb_variants = pd.read_csv('data/variants.csv').fillna('NA')
tb_drug_summary = pd.read_csv('data/drug_summary.csv').fillna('NA')
tb_drug = pd.read_csv('data/drug.csv').fillna('NA')
tb_recommendation = pd.read_csv('data/recommendation.csv').fillna('NA')
tb_var_details = pd.read_csv('data/var_details.csv').fillna('NA')

# Get the column names
columns = tb_var_details.columns.tolist()
# Get the last column name
last_col = columns[-1]
# Remove the last column name from the list
columns.remove(last_col)

# Convert the DataFrame into a list of dictionaries
table_summary = tb_summary.to_dict('records')
table_variants = tb_variants.to_dict('records')
table_drug_summary = tb_drug_summary.to_dict('records')
table_drug = tb_drug.to_dict('records')
table_recommendation = tb_recommendation.to_dict('records')
table_var_details = tb_var_details.to_dict('records')

name = "John Doe"
id = "A123456"
gender = "Male"
dob = "01/11/1990"

# name = input("Enter name: ") or "John Doe"
# id = input("Enter ID: ") or "A123456"
# gender = input("Enter gender: ") or "Male"
# dob = input("Enter date-of-birth: ") or "01/11/1990"

sample_type = "Whole Blood"
collection_date = "01/01/2023"
accession = "4316546"
report_date = "07/08/2023"


logo_path = os.path.abspath("src/img/logo.png")


# Data from your .csv, .json, .txt, etc.
data = {
    "name": name,
    "id": id,
    "gender": gender,
    "dob": dob,
    "sample_type": sample_type,
    "collection_date": collection_date,
    "accession": accession,
    "report_date": report_date,
    "logo_path": "file:///" + logo_path.replace("\\", "/"),
    "table_summary": table_summary,
    "table_variants": table_variants,
    "table_drug_summary": table_drug_summary,
    "table_drug": table_drug,
    "table_recommendation": table_recommendation,
    "table_var_details": table_var_details,
    "last_column": last_col,
    "columns": columns,
    "headers": headers,
    "table": table,
    # "table_merged": table_merged,
}

print(table)

create_pdf(data)