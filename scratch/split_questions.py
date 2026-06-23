# -*- coding: utf-8 -*-
import json
import os
import math

root_dir = "C:/Users/DELL/Downloads/ontap_html"

def split_large_topic(subject_id, large_topic_id, prefix_title):
    data_dir = os.path.join(root_dir, f"data/{subject_id}")
    questions_path = os.path.join(data_dir, "questions.json")
    knowledge_path = os.path.join(data_dir, "knowledge.json")
    
    with open(questions_path, "r", encoding="utf-8") as f:
        questions = json.load(f)
        
    with open(knowledge_path, "r", encoding="utf-8") as f:
        knowledge = json.load(f)
        
    # Find the large topic in knowledge
    large_topic = next((t for t in knowledge if t["topicId"] == large_topic_id), None)
    if not large_topic:
        return
        
    # Extract questions belonging to the large topic
    large_qs = [q for q in questions if q["topicId"] == large_topic_id]
    other_qs = [q for q in questions if q["topicId"] != large_topic_id]
    
    if len(large_qs) <= 50:
        return # No need to split
        
    chunk_size = 50
    num_chunks = math.ceil(len(large_qs) / chunk_size)
    
    new_knowledge = [t for t in knowledge if t["topicId"] != large_topic_id]
    
    for i in range(num_chunks):
        chunk = large_qs[i*chunk_size : (i+1)*chunk_size]
        new_topic_id = f"{large_topic_id}_part{i+1}"
        
        # Update question topicIds
        for q in chunk:
            q["topicId"] = new_topic_id
            other_qs.append(q)
            
        # Create new knowledge entry
        new_knowledge.append({
            "topicId": new_topic_id,
            "title": f"{prefix_title} - Phần {i+1} ({len(chunk)} câu)",
            "keywords": large_topic["keywords"],
            "summary": f"{large_topic['summary']} (Phần {i+1})",
            "content": large_topic["content"],
            "example": ""
        })
        
    # Write back
    with open(questions_path, "w", encoding="utf-8") as f:
        json.dump(other_qs, f, ensure_ascii=False, indent=2)
        
    with open(knowledge_path, "w", encoding="utf-8") as f:
        json.dump(new_knowledge, f, ensure_ascii=False, indent=2)
        
    print(f"Split {subject_id} '{large_topic_id}' into {num_chunks} parts.")

split_large_topic("quocphong_hp1", "hp1_other_topics", "Ngân hàng Câu hỏi Tổng hợp")
split_large_topic("quocphong_hp2", "hp2_other_topics", "Ngân hàng Câu hỏi Tổng hợp")
