import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

subject_id = "python"
data_dir = f"C:/Users/DELL/Downloads/ontap_html/data/{subject_id}"

files = {
    "knowledge.json": os.path.join(data_dir, "knowledge.json"),
    "questions.json": os.path.join(data_dir, "questions.json"),
    "preset_exams.json": os.path.join(data_dir, "preset_exams.json")
}

errors = []

# Validate subjects.json first
subjects_path = "C:/Users/DELL/Downloads/ontap_html/data/subjects.json"
try:
    with open(subjects_path, "r", encoding="utf-8") as f:
        subjects = json.load(f)
    print("subjects.json parsed successfully.")
    py_subj = [s for s in subjects if s["id"] == subject_id]
    if not py_subj:
        errors.append("Python subject is not registered in subjects.json")
    else:
        print("Python subject registration found.")
except Exception as e:
    errors.append(f"Failed to parse subjects.json: {e}")

# Validate generated files
loaded_data = {}
for name, path in files.items():
    if not os.path.exists(path):
        errors.append(f"Missing file: {path}")
        continue
    try:
        with open(path, "r", encoding="utf-8") as f:
            loaded_data[name] = json.load(f)
        print(f"{name} parsed successfully. Number of records: {len(loaded_data[name])}")
    except Exception as e:
        errors.append(f"Failed to parse {name}: {e}")

# Detailed checks if all parsed successfully
if len(loaded_data) == 3:
    knowledge = loaded_data["knowledge.json"]
    questions = loaded_data["questions.json"]
    preset_exams = loaded_data["preset_exams.json"]

    # Topic IDs check
    topic_ids = {t["topicId"] for t in knowledge}
    print(f"Total topics: {len(topic_ids)}")
    print(f"Topics: {sorted(list(topic_ids))}")

    # Check that each topic has at least 10 questions
    topic_counts = {}
    for q in questions:
        t_id = q.get("topicId")
        if not t_id:
            errors.append(f"Question ID {q.get('id')} has no topicId.")
            continue
        if t_id not in topic_ids:
            errors.append(f"Question ID {q.get('id')} has invalid topicId '{t_id}'.")
        topic_counts[t_id] = topic_counts.get(t_id, 0) + 1

    for t_id in topic_ids:
        cnt = topic_counts.get(t_id, 0)
        print(f"  Topic '{t_id}': {cnt} questions")
        if cnt < 10:
            errors.append(f"Topic '{t_id}' has only {cnt} questions (minimum required is 10).")

    # Options and correct answers check
    for q in questions:
        opts = q.get("options", [])
        if len(opts) < 4:
            errors.append(f"Question ID {q.get('id')} has less than 4 options.")
        ans = q.get("correctAnswer")
        if not ans or ans not in ["A", "B", "C", "D", "E"]:
            errors.append(f"Question ID {q.get('id')} has invalid correctAnswer '{ans}'.")

    # Preset exams validation
    for idx, exam in enumerate(preset_exams):
        exam_id = exam.get("id")
        exam_name = exam.get("name")
        exam_qs = exam.get("questions", [])
        print(f"Preset Exam '{exam_name}' ({exam_id}): {len(exam_qs)} questions")
        if not exam_id or not exam_name:
            errors.append(f"Preset exam at index {idx} missing id/name.")
        if len(exam_qs) == 0:
            errors.append(f"Preset exam '{exam_id}' has no questions.")
        for q in exam_qs:
            if q.get("id") not in {o["id"] for o in questions}:
                errors.append(f"Preset exam '{exam_id}' references question ID {q.get('id')} which does not exist in master questions list.")

if errors:
    print("\n--- VALIDATION ERRORS FOUND ---")
    for err in errors:
        print(f"Error: {err}")
else:
    print("\nAll data files validated successfully! Integrity checks PASSED.")
