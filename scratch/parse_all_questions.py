import re
import os
import json
import html
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_file(file_path):
    print(f"Parsing {file_path}...")
    if not os.path.exists(file_path):
        print("  File does not exist.")
        return []
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Standard regex parser since the structure is highly uniform:
    # 1. Find all question divs
    # <div id="question-(\d+)">
    # 2. Inside it: <div id="question-\d+_question-name">...</div>
    # 3. Followed by options: <label ...>...A. ...</label>
    
    questions = []
    
    # We find all question div matches
    q_matches = re.finditer(r'<div id="question-(\d+)">', content)
    q_positions = [m.start() for m in q_matches]
    
    if not q_positions:
        print("  No questions found via main pattern.")
        return []
        
    for idx, pos in enumerate(q_positions):
        # Slice the content for this question block
        end_pos = q_positions[idx+1] if idx+1 < len(q_positions) else len(content)
        block = content[pos:end_pos]
        
        # Extract question id
        q_id_match = re.search(r'id="question-(\d+)"', block)
        if not q_id_match:
            continue
        q_db_id = q_id_match.group(1)
        
        # Extract question text
        # Look for the question name div
        name_match = re.search(r'id="question-\d+_question-name">(.*?)</div>', block, re.DOTALL)
        if not name_match:
            continue
        
        q_html = name_match.group(1)
        # Clean HTML tags from question name
        q_text = re.sub(r'<[^>]*>', '', q_html)
        q_text = html.unescape(q_text).strip()
        # Clean up question number prefix e.g. "Câu 1:"
        q_text = re.sub(r'^Câu\s+\d+:\s*', '', q_text).strip()
        
        # Extract options (look for labels containing A., B., C., D.)
        # We can extract text inside tags that display A., B., C., D.
        # Options are wrapped in label tags
        labels = re.findall(r'<label[^>]*>(.*?)</label>', block, re.DOTALL)
        options_list = []
        for lbl in labels:
            lbl_text = re.sub(r'<[^>]*>', '', lbl)
            lbl_text = html.unescape(lbl_text).strip()
            # Clean up JSJSESSION or next-specific characters
            lbl_text = re.sub(r'\s+', ' ', lbl_text)
            
            # Match A. B. C. D. at start
            if re.match(r'^[A-D]\.\s*', lbl_text):
                options_list.append(lbl_text)
                
        # If we got exactly 4 options, save it
        if len(options_list) == 4 and q_text:
            questions.append({
                "dbId": q_db_id,
                "question": q_text,
                "options": options_list
            })
            
    print(f"  Extracted {len(questions)} valid questions.")
    return questions

# Test parsing the first file
de1_questions = parse_file("c:/Users/DELL/Downloads/ontap_html/scratch/de1.html")
if de1_questions:
    print("\nSample Question 1:")
    print("Q:", de1_questions[0]["question"])
    print("Opts:", de1_questions[0]["options"])
    
    print("\nSample Question 2:")
    print("Q:", de1_questions[1]["question"])
    print("Opts:", de1_questions[1]["options"])
