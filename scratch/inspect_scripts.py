import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'c:/Users/DELL/Downloads/ontap_html/scratch/de1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find all script tags
scripts = re.findall(r'<script([^>]*)>(.*?)</script>', content, re.DOTALL)
print(f"Total script tags: {len(scripts)}")

for idx, (attrs, body) in enumerate(scripts):
    body_clean = body.strip()
    if not body_clean:
        continue
    # Search for questions data keywords
    if "761606" in body_clean or "761607" in body_clean or "questions" in body_clean:
        print(f"\n--- Script {idx} with attributes: {attrs} ---")
        print(body_clean[:1000])
