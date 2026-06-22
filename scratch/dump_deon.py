import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open("C:/Users/DELL/Downloads/ontap_html/pdf/python-on-tap/deon.pdf")
print(f"Total pages: {len(doc)}")
for i, page in enumerate(doc):
    print(f"\n--- PAGE {i+1} ---")
    print(page.get_text())
