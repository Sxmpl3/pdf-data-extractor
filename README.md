# PDF Data Extractor

This project automates the process of downloading PDF files from an IMAP server, extracting text, analyzing it with OpenAI to extract key data, and storing the information in a database for later use.

## Features
- Automatically downloads PDF files from an email server (IMAP).
- Extracts text content from PDFs.
- Uses OpenAI to process and extract relevant data from the extracted text.
- Stores the extracted data in a database for future use.

## Requirements
- Python 3.x
- Required Python libraries:
  - `imaplib`
  - `PyMuPDF`
  - `openai==0.28.0`
  - `mysql-connector-python`
  
Install the dependencies with:

```bash
pip install -r requirements.txt
