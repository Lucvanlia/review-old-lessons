import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load the combined stream text
with open("c:/Users/DELL/Downloads/ontap_html/scratch/combined_next_f.txt", "r", encoding="utf-8") as f:
    payload = f.read()

# Let's locate "questions":[{"id":
start_idx = payload.find('"questions":[')
if start_idx == -1:
    print("Could not find questions list in payload.")
    sys.exit()

# Extract from start_idx to matching bracket
# Since it is a nested JSON, let's parse it carefully.
# We will find the start of the questions list and extract everything until we find a valid JSON list or use regex.
# Actually, the payload is part of a larger Next.js string. Let's find a valid JSON chunk.
# Let's search for the pattern '"questions":\s*\[(.*?)\]\s*,\s*"[^"]+":' or similar, or count brackets.

bracket_count = 0
chars = []
started = False

for i in range(start_idx, len(payload)):
    char = payload[i]
    if char == '[':
        bracket_count += 1
        started = True
    elif char == ']':
        bracket_count -= 1
    
    if started:
        chars.append(char)
        if bracket_count == 0:
            break

questions_str = "".join(chars)
# Let's wrap it in a dictionary to make it valid JSON: {"questions": ...}
try:
    data = json.loads("{" + questions_str + "}")
    questions_list = data["questions"]
    print("Successfully parsed questions list JSON!")
    print("Total questions found:", len(questions_list))
    
    # Print the first question JSON
    first_q = questions_list[0]
    print("\nFirst Question Structure:")
    for k, v in first_q.items():
        if k != "answers" and k != "name" and k != "explain_answer":
            print(f"  {k}: {repr(v)}")
        elif k == "answers":
            print("  answers (first 2):")
            for ans in v[:2]:
                print("    ", ans)
        else:
            print(f"  {k}: {repr(v)[:100]}...")
            
except Exception as e:
    print("Error parsing JSON:", e)
    # Print first 500 chars of questions_str
    print("\nRaw slice:")
    print(questions_str[:1000])
