import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = "C:/Users/DELL/Downloads/ontap_html/pdf/python-on-tap/[IPPA233277] w02.3-c02_cau-truc-lap_HW (done).pdf"
try:
    doc = fitz.open(path)
    for p in [4, 5, 6]: # pages 5 to 7 (0-indexed: 4 to 6)
        if p < len(doc):
            print(f"\n--- PAGE {p+1} ---")
            print(doc[p].get_text())
except Exception as e:
    print(f"Error: {e}")
