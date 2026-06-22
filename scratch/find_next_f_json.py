import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'c:/Users/DELL/Downloads/ontap_html/scratch/de1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Match self.__next_f.push([1,"..."])
matches = re.finditer(r'self\.__next_f\.push\(\[(?:\d+),\s*\"(.*?)\"\s*\]\)', content)
full_str = ""
for m in matches:
    # Decode escape characters
    val = m.group(1)
    # Next.js streams escape quotes as \"
    val = val.replace('\\"', '"').replace('\\\\', '\\')
    full_str += val

print("Combined NextJS string length:", len(full_str))

# Let's save the combined string to check it
with open("c:/Users/DELL/Downloads/ontap_html/scratch/combined_next_f.txt", "w", encoding="utf-8") as out:
    out.write(full_str)

# Search for any question patterns
print("\nSearching for question IDs or tags in combined string:")
# Let's see if we find "questions" or option list or "correct"
for kw in ["questions", "correct", "answer", "761606"]:
    pos = full_str.find(kw)
    if pos != -1:
        print(f"Keyword '{kw}' found at position {pos}")
        print("Context:", full_str[max(0, pos-100):min(len(full_str), pos+200)])
