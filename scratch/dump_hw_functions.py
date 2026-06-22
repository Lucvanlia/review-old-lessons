import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = "C:/Users/DELL/Downloads/ontap_html/pdf/python-on-tap/[IPPA233277] w05-c04_ham_HW (done) (1).pdf"
try:
    doc = fitz.open(path)
    for p in [4, 5, 6, 7]: # pages 5 to 8 (0-indexed: 4 to 7)
        if p < len(doc):
            print(f"\n--- PAGE {p+1} ---")
            print(doc[p].get_text())
except Exception as e:
    print(f"Error: {e}")
