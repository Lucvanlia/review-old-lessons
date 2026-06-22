import json

questions_path = "c:/Users/DELL/Downloads/ontap_html/data/java/questions.json"
with open(questions_path, "r", encoding="utf-8") as f:
    questions = json.load(f)

syllabus_qs = [q for q in questions if q.get("id", 0) < 200]
print(f"Total syllabus questions (id < 200): {len(syllabus_qs)}")

# Group by topicId
topics = {}
for q in syllabus_qs:
    tid = q.get("topicId")
    topics[tid] = topics.get(tid, 0) + 1

for tid, count in topics.items():
    print(f"  Topic '{tid}': {count} questions")
