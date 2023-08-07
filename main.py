import pdfkit
from jinja2 import Environment, FileSystemLoader
import pandas as pd
import os
import webbrowser

def create_pdf(data, template_path="report.html", output="report.pdf"):
    # Load your Jinja2 template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_path)

    # Render the template with your data
    rendered_html = template.render(data=data)

    # Create the pdf
    pdfkit.from_string(rendered_html, output, options={'enable-local-file-access': ''})

    # Open the pdf
    webbrowser.open_new_tab(output)

# Read the CSV data
df = pd.read_csv('data/table.csv')
tb_summary = pd.read_csv('data/summary.csv')
tb_variants = pd.read_csv('data/variants.csv')
tb_variant_details = pd.read_csv('data/variant_details.csv')
tb_drug_summary = pd.read_csv('data/drug_summary.csv')

# Convert the DataFrame into a list of dictionaries
table_data = df.to_dict('records')
table_summary = tb_summary.to_dict('records')
table_variants = tb_variants.to_dict('records')
table_variant_details = tb_variant_details.to_dict('records')
table_drug_summary = tb_drug_summary.to_dict('records')

# Ask for user input, with default values
# name = input("Enter name: ") or "John Doe"
# id = input("Enter ID: ") or "A123456"
# gender = input("Enter gender: ") or "Male"
# age = input("Enter age: ") or 25
# dob = input("Enter date-of-birth: ") or "01/11/1990"

name = "John Doe"
id = "A123456"
gender = "Male"
age = 25
dob = "01/11/1990"

logo_path = "templates/test.png"

# Data from your .csv, .json, .txt, etc.
data = {
    "name": name,
    "age": age,
    "id": id,
    "gender": gender,
    "dob": dob,
    "logo_path": os.path.abspath(logo_path),
    "table": table_data,
    "table_summary": table_summary,
    "table_variants": table_variants,
    "table_variant_details": table_variant_details,
    "table_drug_summary": table_drug_summary,
}

create_pdf(data)