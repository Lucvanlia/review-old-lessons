import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = "C:/Users/DELL/Downloads/ontap_html/pdf/python-on-tap/[IPPA233277] w02.2-c02_kieu-du-lieu_cau-truc-re-nhanh_HW (done).pdf"
try:
    doc = fitz.open(path)
    for p in [2, 3, 4, 5]: # pages 3 to 6 (0-indexed: 2 to 5)
        if p < len(doc):
            print(f"\n--- PAGE {p+1} ---")
            print(doc[p].get_text())
except Exception as e:
    print(f"Error: {e}")
