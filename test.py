from jinja2 import Environment, FileSystemLoader
import pandas as pd
import os
from weasyprint import HTML
import webbrowser

def create_pdf(data, template_path="test.html", output="report.pdf"):
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
tb_summary = pd.read_csv('data/summary.csv')
tb_variants = pd.read_csv('data/variants.csv')
tb_variant_details = pd.read_csv('data/variant_details.csv')
tb_drug_summary = pd.read_csv('data/drug_summary.csv')
tb_drug = pd.read_csv('data/drug.csv')
tb_recommendation = pd.read_csv('data/recommendation.csv')

# Convert the DataFrame into a list of dictionaries
table_summary = tb_summary.to_dict('records')
table_variants = tb_variants.to_dict('records')
table_variant_details = tb_variant_details.to_dict('records')
table_drug_summary = tb_drug_summary.to_dict('records')
table_drug = tb_drug.to_dict('records')
table_recommendation = tb_recommendation.to_dict('records')

name = "John Doe"
gender = "Male"
dob = "01/11/1990"
sample_type = "Whole Blood"
id = "A123456"
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
    "table_variant_details": table_variant_details,
    "table_drug_summary": table_drug_summary,
    "table_drug": table_drug,
    "table_recommendation": table_recommendation,
}

create_pdf(data)