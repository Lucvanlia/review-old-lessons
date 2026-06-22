import json
import os

path = 'c:/Users/DELL/Downloads/ontap_html/data/java/knowledge.json'
with open(path, 'r', encoding='utf-8') as f:
    knowledge = json.load(f)

# Check if java_core already exists
exists = any(t['topicId'] == 'java_core' for t in knowledge)
if not exists:
    new_topic = {
        'topicId': 'java_core',
        'title': 'Kiến Thức Lập Trình Java Cơ Bản',
        'content': 'Tổng hợp kiến thức nền tảng của ngôn ngữ lập trình Java (Java Core):\n1. Khái niệm cơ bản: Cú pháp, các kiểu dữ liệu nguyên thủy (primitive) và kiểu đối tượng (reference), biến, toán tử, cấu trúc điều kiện (if-else, switch-case) và vòng lặp (for, while, do-while).\n2. Lập trình hướng đối tượng (OOP): Lớp (Class), đối tượng (Object), kế thừa (Inheritance), đa hình (Polymorphism), đóng gói (Encapsulation) và trừu tượng (Abstraction - Abstract Class & Interface).\n3. Xử lý ngoại lệ (Exception Handling): Cơ chế try-catch-finally, checked exception (phải khai báo/xử lý) vs unchecked exception (RuntimeException), từ khóa throw và throws.\n4. Đa luồng (Multithreading): Lớp Thread và interface Runnable, vòng đời luồng, đồng bộ hóa (synchronized) tránh xung đột tranh chấp (Race Condition).\n5. Java Collections Framework: Danh sách (List - ArrayList, LinkedList), Tập hợp (Set - HashSet), Bản đồ (Map - HashMap), cơ chế Generic giúp kiểm soát an toàn kiểu dữ liệu.',
        'example': '// Ví dụ về kế thừa và đa hình trong Java\nabstract class Animal {\n    abstract void makeSound();\n}\n\nclass Cat extends Animal {\n    @Override\n    void makeSound() {\n        System.out.println("Meo meo");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Animal myCat = new Cat();\n        myCat.makeSound(); // In ra: Meo meo\n    }\n}'
    }
    # Add to the beginning of the list as it is Java Core
    knowledge.insert(0, new_topic)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(knowledge, f, ensure_ascii=False, indent=2)
    print('Successfully appended java_core topic to knowledge.json!')
else:
    print('java_core topic already exists.')
