# Jonis PDF Cutter

A lightweight command-line tool to split large PDF files when online tools like iLovePDF fail due to file size. Ideal for handling heavy PDFs locally with efficiency and precision.

---

## 🇬🇧 English

### Description
Jonis PDF Cutter is a terminal-based Python application to extract specific pages from PDF files. It's designed to work offline and handle large files that online services often can't process.

### Features
- Works entirely offline
- Handles large PDF files (>100MB)
- Simple terminal interface
- Fast and reliable

### Requirements
- Python 3.x
- PyPDF2 (install via `pip install PyPDF2`)

### Usage
```bash
python jonis_pdf_cutter.py input.pdf start_page end_page output.pdf
