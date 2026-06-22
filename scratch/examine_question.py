import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'C:/Users/DELL/.gemini/antigravity-ide/brain/e5a3d042-d1d1-4b3f-8822-f02aacf878f5/.system_generated/steps/116/content.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find question-name of Question 25
q_match = re.search(r'id="question-[^"]+"', content)
matches = re.finditer(r'<div id="question-[^"]+">', content)
for m in matches:
    start = m.start()
    snippet = content[start:start+4000]
    if "Câu 25:" in snippet:
        print("--- QUESTION 25 HTML ---")
        print(snippet[:2000])
        break
