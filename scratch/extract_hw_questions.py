import os
import fitz
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir = "C:/Users/DELL/Downloads/ontap_html/pdf/python-on-tap"
hw_files = [f for f in os.listdir(pdf_dir) if "_HW" in f and f.lower().endswith(".pdf")]

print(f"Found {len(hw_files)} homework files:")
for f in sorted(hw_files):
    path = os.path.join(pdf_dir, f)
    try:
        doc = fitz.open(path)
        print(f"\n=========================================")
        print(f"FILE: {f} ({len(doc)} pages)")
        print(f"=========================================")
        
        # Look for questions or exercises across pages
        for page_num in range(len(doc)):
            text = doc[page_num].get_text()
            lines = text.split("\n")
            
            # Print lines that look like questions or headings
            for line in lines:
                line_strip = line.strip()
                if not line_strip:
                    continue
                # Match lines starting with "Câu ", "Bài ", "Bài tập ", "Yêu cầu", or ending with "?"
                if re.match(r'^(Câu|Bài|Yêu cầu|Bài tập)\s+\d+', line_strip, re.IGNORECASE) or line_strip.endswith("?"):
                    if len(line_strip) > 5:
                        print(f"  Page {page_num+1}: {line_strip}")
    except Exception as e:
        print(f"Error reading {f}: {e}")
