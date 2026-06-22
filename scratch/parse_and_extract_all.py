import re
import json
import html
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Helper to clean html
def clean_html(text):
    if not text:
        return ""
    text = re.sub(r'<[^>]*>', ' ', text)
    text = html.unescape(text)
    # replace non-breaking spaces and double spaces
    text = text.replace('\xa0', ' ').replace('\u200b', ' ')
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_questions_from_file(file_path):
    print(f"Extracting questions from {file_path}...")
    if not os.path.exists(file_path):
        print("  File not found.")
        return []
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Combine Next.js stream payload
    matches = re.finditer(r'self\.__next_f\.push\(\[(?:\d+),\s*\"(.*?)\"\s*\]\)', content)
    full_str = ""
    for m in matches:
        val = m.group(1)
        val = val.replace('\\"', '"').replace('\\\\', '\\')
        full_str += val
        
    # Find "questions":[
    start_idx = full_str.find('"questions":[')
    if start_idx == -1:
        print("  Could not find 'questions':[' in payload.")
        return []
        
    # Extract matching brackets
    bracket_count = 0
    chars = []
    started = False
    for i in range(start_idx + len('"questions":'), len(full_str)):
        char = full_str[i]
        if char == '[':
            bracket_count += 1
            started = True
        elif char == ']':
            bracket_count -= 1
            
        if started:
            chars.append(char)
            if bracket_count == 0:
                break
                
    list_str = "".join(chars)
    try:
        raw_questions = json.loads(list_str)
    except Exception as e:
        print(f"  JSON parsing error: {e}")
        # Try a quick fallback using regex to find raw blocks if needed, but it should work if balanced
        return []
        
    extracted = []
    option_badges = ['A', 'B', 'C', 'D']
    
    for q in raw_questions:
        q_text = clean_html(q.get("name", ""))
        # Clean prefix "Câu X:"
        q_text = re.sub(r'^Câu\s+\d+:\s*', '', q_text).strip()
        
        # Options list
        answers = q.get("answers", [])
        options = []
        for a in answers:
            opt_text = clean_html(a.get("name", ""))
            options.append(opt_text)
            
        # Parse Correct Answer & Explanation from "note"
        note = q.get("note", "")
        note_clean = clean_html(note)
        
        # Look for: "Đáp án đúng là: [Correct text] Vì: [Explanation]" or similar
        # E.g. "Đáp án đúng là: Chương trình viết... Vì: Chương trình viết bằng..."
        correct_ans_letter = None
        explanation = ""
        
        # Clean html in note
        # Find correct answer text
        correct_text = ""
        correct_match = re.search(r'Đáp án đúng là:\s*(.*?)(?:\s*Vì:|$)', note_clean, re.IGNORECASE)
        if correct_match:
            correct_text = correct_match.group(1).strip()
            
        # Find explanation text
        explanation_match = re.search(r'Vì:\s*(.*)', note_clean, re.IGNORECASE)
        if explanation_match:
            explanation = explanation_match.group(1).strip()
        else:
            explanation = note_clean.strip() # fallback
            
        # Find which option matches the correct text
        if correct_text:
            cleaned_correct = re.sub(r'^[A-D]\.\s*', '', correct_text).strip().lower()
            # Clean spaces and punctuation for loose matching
            cleaned_correct_norm = re.sub(r'[^\w\s]', '', cleaned_correct).replace(' ', '')
            
            for idx, opt in enumerate(options):
                cleaned_opt = re.sub(r'^[A-D]\.\s*', '', opt).strip().lower()
                cleaned_opt_norm = re.sub(r'[^\w\s]', '', cleaned_opt).replace(' ', '')
                
                # Check for exact or loose match
                if cleaned_opt_norm == cleaned_correct_norm or cleaned_correct_norm in cleaned_opt_norm or cleaned_opt_norm in cleaned_correct_norm:
                    correct_ans_letter = optionBadges = ['A', 'B', 'C', 'D'][idx]
                    break
        
        # Fallback if no matching option was found, check if note clean itself has A., B., C. or D.
        if not correct_ans_letter:
            letter_match = re.search(r'Đáp án đúng là:\s*([A-D])\b', note_clean, re.IGNORECASE)
            if letter_match:
                correct_ans_letter = letter_match.group(1).upper()
            else:
                # Default fallback
                correct_ans_letter = "A"
                
        # Format explanation nicely
        if not explanation:
            explanation = f"Đáp án đúng là: {correct_text if correct_text else options[option_badges.index(correct_ans_letter)]}"
            
        extracted.append({
            "question": q_text,
            "options": options,
            "correctAnswer": correct_ans_letter,
            "explanation": explanation
        })
        
    print(f"  Successfully extracted {len(extracted)} questions.")
    return extracted

# Test run for de1
de1 = extract_questions_from_file("c:/Users/DELL/Downloads/ontap_html/scratch/de1.html")
if de1:
    print("\nParsed Sample 1:")
    print("Q:", de1[0]["question"])
    print("Ans:", de1[0]["correctAnswer"])
    print("Exp:", de1[0]["explanation"])
