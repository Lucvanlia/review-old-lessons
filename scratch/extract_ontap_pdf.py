import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

try:
    doc = fitz.open("C:/Users/DELL/Downloads/ontap_html/pdf/ontap.pdf")
    print(f"Total pages: {len(doc)}")
    full_text = ""
    for idx, page in enumerate(doc):
        full_text += f"\n--- PAGE {idx+1} ---\n"
        full_text += page.get_text()
    
    with open("C:/Users/DELL/Downloads/ontap_html/scratch/ontap_pdf_text.txt", "w", encoding="utf-8") as f:
        f.write(full_text)
    print("Done! Extracted text saved to scratch/ontap_pdf_text.txt")
except Exception as e:
    print(f"Error: {e}")
