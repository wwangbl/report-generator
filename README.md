# Automated Clinical Report Generator

This application is designed to generate clinical reports in PDF format. The reports are generated automatically based on the input data provided in formats like .json, .csv, .txt. Each report is generated according to a standardized template, with the only differences being the input data (the clinical information of different customers).

## Setup and Installation

1. Clone this repo to your local machine.

2. Install the required Python libraries by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

You also need to install wkhtmltopdf which is an open source tool that pdfkit uses under the hood:

For Ubuntu/Debian: sudo apt-get install wkhtmltopdf

For Windows and other systems, download a packaged installer at wkhtmltopdf's downloads page: https://wkhtmltopdf.org/downloads.html