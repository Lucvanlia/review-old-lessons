import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

try:
    doc = fitz.open("C:/Users/DELL/Downloads/ontap_html/pdf/python-on-tap/Numpy.pdf")
    print(f"NumPy.pdf total pages: {len(doc)}")
    if len(doc) > 0:
        print("\n--- Page 1 text: ---")
        print(doc[0].get_text())
except Exception as e:
    print(f"Error: {e}")
