import json

questions_path = "c:/Users/DELL/Downloads/ontap_html/data/java/questions.json"
with open(questions_path, "r", encoding="utf-8") as f:
    questions = json.load(f)

syllabus_qs = [q for q in questions if q.get("id", 0) < 200]

# Write details to a scratch file so it's easy to read
out_path = "c:/Users/DELL/Downloads/ontap_html/scratch/java_questions_detail.txt"
with open(out_path, "w", encoding="utf-8") as f:
    for q in syllabus_qs:
        f.write(f"ID: {q.get('id')} | Topic: {q.get('topicId')}\n")
        f.write(f"Q: {q.get('question')}\n")
        f.write(f"Options: {q.get('options')}\n")
        f.write(f"Ans: {q.get('correctAnswer')}\n")
        f.write(f"Explanation: {q.get('explanation')}\n")
        f.write("-" * 50 + "\n")

print(f"Details written to {out_path}")
