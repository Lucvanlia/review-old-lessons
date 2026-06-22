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
    text = text.replace('\xa0', ' ').replace('\u200b', ' ')
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def parse_html_file(file_path, base_id):
    if not os.path.exists(file_path):
        print(f"  Error: {file_path} not found.")
        return []
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Match self.__next_f.push([1,"..."])
    matches = re.finditer(r'self\.__next_f\.push\(\[(?:\d+),\s*\"(.*?)\"\s*\]\)', content)
    full_str = ""
    for m in matches:
        val = m.group(1)
        val = val.replace('\\"', '"').replace('\\\\', '\\')
        full_str += val
        
    start_idx = full_str.find('"questions":[')
    if start_idx == -1:
        print(f"  Error: 'questions' list not found in {file_path}")
        return []
        
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
        print(f"  JSON parsing error in {file_path}: {e}")
        return []
        
    extracted = []
    option_badges = ['A', 'B', 'C', 'D']
    
    for idx, q in enumerate(raw_questions):
        q_text = clean_html(q.get("name", ""))
        q_text = re.sub(r'^Câu\s+\d+:\s*', '', q_text).strip()
        
        # Answers options list
        answers = q.get("answers", [])
        options = []
        for a in answers:
            opt_text = clean_html(a.get("name", ""))
            options.append(opt_text)
            
        # Correct answer & explanation
        note = q.get("note", "")
        note_clean = clean_html(note)
        
        correct_text = ""
        correct_match = re.search(r'Đáp án đúng là:\s*(.*?)(?:\s*Vì:|$)', note_clean, re.IGNORECASE)
        if correct_match:
            correct_text = correct_match.group(1).strip()
            
        explanation = ""
        explanation_match = re.search(r'Vì:\s*(.*)', note_clean, re.IGNORECASE)
        if explanation_match:
            explanation = explanation_match.group(1).strip()
        else:
            explanation = note_clean.strip()
            
        # Match option
        correct_ans_letter = None
        if correct_text:
            cleaned_correct = re.sub(r'^[A-D]\.\s*', '', correct_text).strip().lower()
            cleaned_correct_norm = re.sub(r'[^\w\s]', '', cleaned_correct).replace(' ', '')
            
            for o_idx, opt in enumerate(options):
                cleaned_opt = re.sub(r'^[A-D]\.\s*', '', opt).strip().lower()
                cleaned_opt_norm = re.sub(r'[^\w\s]', '', cleaned_opt).replace(' ', '')
                if cleaned_opt_norm == cleaned_correct_norm or cleaned_correct_norm in cleaned_opt_norm or cleaned_opt_norm in cleaned_correct_norm:
                    correct_ans_letter = option_badges[o_idx]
                    break
                    
        if not correct_ans_letter:
            letter_match = re.search(r'Đáp án đúng là:\s*([A-D])\b', note_clean, re.IGNORECASE)
            if letter_match:
                correct_ans_letter = letter_match.group(1).upper()
            else:
                correct_ans_letter = "A" # fallback
                
        if not explanation:
            explanation = f"Đáp án đúng là: {correct_text if correct_text else options[option_badges.index(correct_ans_letter)]}"
            
        extracted.append({
            "id": base_id + idx,
            "topicId": "java_core",
            "question": q_text,
            "options": options,
            "correctAnswer": correct_ans_letter,
            "explanation": explanation
        })
        
    return extracted

# Parse all 4 files
preset_exams = []
all_new_questions = []

for num in range(1, 5):
    file_path = f"c:/Users/DELL/Downloads/ontap_html/scratch/de{num}.html"
    base_id = 200 + (num - 1) * 50 # 200, 250, 300, 350
    questions = parse_html_file(file_path, base_id)
    if questions:
        print(f"Extracted {len(questions)} questions from Đề {num}")
        # Add to preset exams structure
        preset_exams.append({
            "id": f"de_{num}",
            "name": f"Đề thi mẫu số {num} (Java Core)",
            "description": f"Đề thi thử gồm 50 câu hỏi trắc nghiệm Lập trình Java online từ Đề #{num} của website baitaptracnghiem.com.",
            "questions": questions
        })
        all_new_questions.extend(questions)

# Save preset_exams.json
preset_exams_path = "c:/Users/DELL/Downloads/ontap_html/data/java/preset_exams.json"
with open(preset_exams_path, "w", encoding="utf-8") as f:
    json.dump(preset_exams, f, ensure_ascii=False, indent=2)
print(f"Saved preset exams to {preset_exams_path}")

# Load current questions.json and append new ones
questions_path = "c:/Users/DELL/Downloads/ontap_html/data/java/questions.json"
if os.path.exists(questions_path):
    with open(questions_path, "r", encoding="utf-8") as f:
        existing_questions = json.load(f)
else:
    existing_questions = []

# Filter out old questions with id >= 200 to allow overwriting/updating
filtered_existing = [q for q in existing_questions if q.get("id", 0) < 200]
merged_questions = filtered_existing + all_new_questions

with open(questions_path, "w", encoding="utf-8") as f:
    json.dump(merged_questions, f, ensure_ascii=False, indent=2)
print(f"Merged and saved {len(merged_questions)} total questions to {questions_path} (119 outline + {len(all_new_questions)} new).")
