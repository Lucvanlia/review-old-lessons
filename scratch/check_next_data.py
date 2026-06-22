import re
import html
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'C:/Users/DELL/.gemini/antigravity-ide/brain/e5a3d042-d1d1-4b3f-8822-f02aacf878f5/.system_generated/steps/116/content.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Search for __NEXT_DATA__ script content
match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', content)
if match:
    print("Found __NEXT_DATA__ tag!")
    json_data = json.loads(match.group(1))
    # print keys
    print("Keys in Next.js Page Props:")
    props = json_data.get('props', {})
    page_props = props.get('pageProps', {})
    print(list(page_props.keys()))
    
    # Dump pageProps structure to a file to examine
    with open('C:/Users/DELL/.gemini/antigravity-ide/brain/e5a3d042-d1d1-4b3f-8822-f02aacf878f5/props.json', 'w', encoding='utf-8') as pf:
        json.dump(page_props, pf, ensure_ascii=False, indent=2)
    print("Saved pageProps to props.json")
else:
    print("Could not find __NEXT_DATA__ script.")
    # Search for other script tags
    scripts = re.findall(r'<script.*?>(.*?)</script>', content)
    print(f"Found {len(scripts)} scripts on page.")
