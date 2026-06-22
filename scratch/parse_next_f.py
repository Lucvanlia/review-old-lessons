import re
import html
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'C:/Users/DELL/.gemini/antigravity-ide/brain/e5a3d042-d1d1-4b3f-8822-f02aacf878f5/.system_generated/steps/116/content.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find all script tags that call self.__next_f.push
chunks = re.findall(r'self\.__next_f\.push\(\[(.*?)\].*?\)', content)
print(f"Found {len(chunks)} next_f chunks.")

full_payload = ""
for idx, chunk in enumerate(chunks):
    # Parse the chunk args (usually 0, "string" or 1, "string")
    # For simplicity, let's extract strings
    str_matches = re.findall(r'\"(.*?)\"', chunk)
    for s in str_matches:
        decoded = s.encode().decode('unicode-escape', errors='ignore')
        full_payload += decoded

# Let's search for keywords in the full payload
print("Payload length:", len(full_payload))
if "correctAnswer" in full_payload or "correct" in full_payload:
    print("Found 'correctAnswer' or 'correct' keyword in payload!")
    # Print occurrences
    for m in re.finditer(r'correct[a-zA-Z]*', full_payload):
        start = max(0, m.start() - 100)
        end = min(len(full_payload), m.end() + 100)
        print(f"Match context: ... {full_payload[start:end]} ...")
else:
    print("Did not find 'correct' keyword in next_f payload.")
    
# Let's search the regular html text for "correct" or "đáp án"
print("--- Search for correct in text ---")
matches = re.finditer(r'(đáp án|đúng|correct|answer)', content, re.IGNORECASE)
for i, m in enumerate(matches):
    if i < 15:
        start = max(0, m.start() - 60)
        end = min(len(content), m.end() + 60)
        print(f"HTML Context: ... {content[start:end]} ...")
