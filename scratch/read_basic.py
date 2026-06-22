import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

try:
    doc = fitz.open("C:/Users/DELL/Downloads/ontap_html/pdf/python-on-tap/[IPPA233277] w02.1-c02_cac-khai-niem-co-ban (done).pdf")
    print(f"Total pages: {len(doc)}")
    if len(doc) > 0:
        print("\n--- Page 1 text: ---")
        print(doc[0].get_text())
        print("\n--- Page 5 text: ---")
        print(doc[4].get_text())
except Exception as e:
    print(f"Error: {e}")
