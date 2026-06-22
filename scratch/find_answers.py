import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'C:/Users/DELL/.gemini/antigravity-ide/brain/e5a3d042-d1d1-4b3f-8822-f02aacf878f5/.system_generated/steps/116/content.md'
with open(file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

print("Searching for answer patterns...")
# Search for elements or values that could indicate the correct option
# For example, look at where inputs/radios are declared.
inputs = re.findall(r'<input.*?>', html_content)
print(f"Found {len(inputs)} input tags on page.")
for i in inputs[:10]:
    print("  Input:", i)

# Look for text like "Không đúng" or "Đúng" or check if there are tags with classes like border-green or text-green
print("\nSearching for green/red classes or correctness indicators in HTML:")
matches = re.finditer(r'(green|red|correct|wrong|true|false|success|danger|check)', html_content, re.IGNORECASE)
found = set()
for m in matches:
    start = max(0, m.start() - 30)
    end = min(len(html_content), m.end() + 30)
    snippet = html_content[start:end].strip()
    if snippet not in found:
        found.add(snippet)
        if len(found) < 20:
            print("  Snippet:", snippet)
