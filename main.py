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

# Convert the DataFrame into a list of dictionaries
table_data = df.to_dict('records')

# Data from your .csv, .json, .txt, etc.
data = {
    "name": "John Doe",
    "age": 25,
    "logo_path": os.path.abspath("templates/test.png"),
    "table": table_data
}

create_pdf(data)