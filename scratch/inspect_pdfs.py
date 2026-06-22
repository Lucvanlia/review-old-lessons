import os
import fitz # PyMuPDF
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir = "C:/Users/DELL/Downloads/ontap_html/pdf/python-on-tap"
pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]

print(f"Found {len(pdf_files)} PDF files in {pdf_dir}:")
for f in sorted(pdf_files):
    path = os.path.join(pdf_dir, f)
    try:
        doc = fitz.open(path)
        num_pages = len(doc)
        first_page_text = ""
        if num_pages > 0:
            first_page_text = doc[0].get_text()[:400].replace('\n', ' | ')
        print(f"\n--- {f} ({num_pages} pages) ---")
        print(f"Snippet: {first_page_text}")
    except Exception as e:
        print(f"Error reading {f}: {e}")
