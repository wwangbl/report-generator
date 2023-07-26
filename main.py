import pdfkit
from jinja2 import Environment, FileSystemLoader

def create_pdf(data, template_path="templates/report.html", output="report.pdf"):
    # Load your Jinja2 template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)

    # Render the template with your data
    rendered_html = template.render(data=data)

    # Create the pdf
    pdfkit.from_string(rendered_html, output)

# Data from your .csv, .json, .txt, etc.
data = {
    "name": "John Doe",
    "age": 25,
    # Add more data here...
}

create_pdf(data)