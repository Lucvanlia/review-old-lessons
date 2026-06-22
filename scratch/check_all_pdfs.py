import os
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir = "C:/Users/DELL/Downloads/ontap_html/pdf/python-on-tap"
for f in sorted(os.listdir(pdf_dir)):
    if not f.lower().endswith('.pdf'):
        continue
    path = os.path.join(pdf_dir, f)
    try:
        doc = fitz.open(path)
        # Check first page
        t = doc[0].get_text()[:200].replace('\n', ' ')
        # Check if text is mostly garbled (very high non-ascii or strange characters)
        # Simple heuristic: if we have some normal Vietnamese or English words, it's fine.
        print(f"{f}: {len(t)} chars. Snippet: {t[:100]}")
    except Exception as e:
        print(f"Error on {f}: {e}")
