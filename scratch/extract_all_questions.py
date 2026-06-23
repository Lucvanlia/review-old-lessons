# -*- coding: utf-8 -*-
import json
import os
import re
import shutil

# Base paths
root_dir = "C:/Users/DELL/Downloads/ontap_html"
data_hp1_dir = os.path.join(root_dir, "data/quocphong_hp1")
data_hp2_dir = os.path.join(root_dir, "data/quocphong_hp2")
os.makedirs(data_hp1_dir, exist_ok=True)
os.makedirs(data_hp2_dir, exist_ok=True)

# 1. Prepare High Quality Data (HP1)
topics_hp1 = [
    {
        "topicId": "hp1_bai2_chien_tranh_quan_doi",
        "title": "Quan điểm Mác-Lênin, TT Hồ Chí Minh về Chiến tranh & Quân đội",
        "keywords": ["Chiến tranh", "Giai cấp", "Bạo lực cách mạng", "Quân đội kiểu mới", "Đảng lãnh đạo"],
        "summary": "Nghiên cứu quan điểm của chủ nghĩa Mác-Lênin và Tư tưởng Hồ Chí Minh về nguồn gốc, bản chất của chiến tranh và quân đội, từ đó rút ra bài học cho việc xây dựng quân đội nhân dân Việt Nam.",
        "content": """
        <h3>Nội dung trọng tâm</h3>
        <ul>
            <li>Chiến tranh bắt nguồn từ chế độ tư hữu, có giai cấp và đối kháng giai cấp.</li>
            <li>Bản chất chiến tranh: Kế tục chính trị bằng thủ đoạn bạo lực.</li>
            <li>Nguyên tắc xây dựng quân đội kiểu mới của Lênin: Đảng Cộng sản lãnh đạo là quan trọng nhất.</li>
            <li>Quân đội nhân dân Việt Nam mang bản chất giai cấp công nhân, có tính nhân dân và tính dân tộc sâu sắc.</li>
        </ul>
        <h3>Những ý dễ nhầm</h3>
        <ul>
            <li>Nhầm lẫn nguồn gốc của chiến tranh: Nhiều sinh viên cho rằng chiến tranh có từ khi xuất hiện loài người (SAI), thực tế chiến tranh chỉ xuất hiện khi có chế độ tư hữu và giai cấp (ĐÚNG).</li>
            <li>Phân biệt giữa chức năng và nhiệm vụ của quân đội.</li>
        </ul>
        <div style="padding: 10px; background-color: #e6f7ff; border-left: 4px solid #1890ff;">
            <strong>Ghi nhớ nhanh:</strong> Chiến tranh = Tư hữu + Giai cấp. Bản chất quân đội = Bản chất của giai cấp lãnh đạo.
        </div>
        """,
        "example": ""
    },
    {
        "topicId": "hp1_bai3_duong_loi_quoc_phong",
        "title": "Đường lối Quốc phòng và An ninh của Đảng",
        "keywords": ["Toàn dân", "Toàn diện", "Tiềm lực kinh tế", "Tiềm lực chính trị", "Thế trận"],
        "summary": "Nội dung đường lối quốc phòng, an ninh của Đảng ta nhằm bảo vệ vững chắc Tổ quốc xã hội chủ nghĩa trong tình hình mới.",
        "content": """
        <h3>Nội dung trọng tâm</h3>
        <ul>
            <li>Hai nhiệm vụ chiến lược: Xây dựng CNXH và Bảo vệ Tổ quốc XHCN (luôn gắn bó chặt chẽ).</li>
            <li>Đặc trưng của nền quốc phòng: Nền quốc phòng vì dân, do dân, của dân.</li>
            <li>Mục đích: Tạo ra môi trường hòa bình, ổn định để phát triển kinh tế xã hội.</li>
            <li>Tiềm lực quốc phòng an ninh: Tiềm lực chính trị tinh thần là nhân tố cơ bản, tiềm lực kinh tế là nền tảng vật chất.</li>
        </ul>
        <h3>Những ý dễ nhầm</h3>
        <ul>
            <li>Nhầm lẫn giữa 'Tiềm lực chính trị' và 'Tiềm lực quân sự'. Tiềm lực chính trị tinh thần mới là yếu tố quyết định.</li>
        </ul>
        <div style="padding: 10px; background-color: #e6f7ff; border-left: 4px solid #1890ff;">
            <strong>Ghi nhớ nhanh:</strong> Quốc phòng toàn dân = Bảo vệ hòa bình. Kinh tế là nền tảng, Chính trị tinh thần là quyết định.
        </div>
        """,
        "example": ""
    },
    {
        "topicId": "hp1_bai4_chien_tranh_nhan_dan",
        "title": "Chiến tranh Nhân dân Bảo vệ Tổ quốc",
        "keywords": ["Lực lượng vũ trang 3 thứ quân", "Toàn dân đánh giặc", "Thế trận", "Chính nghĩa"],
        "summary": "Nghệ thuật chiến tranh nhân dân của Việt Nam, phát huy sức mạnh của toàn dân tộc đánh giặc ngoại xâm.",
        "content": """
        <h3>Nội dung trọng tâm</h3>
        <ul>
            <li>Tính chất: Là cuộc chiến tranh chính nghĩa, tự vệ, mạng tính toàn dân, toàn diện.</li>
            <li>Lực lượng: Toàn dân tham gia, trong đó lực lượng vũ trang 3 thứ quân làm nòng cốt.</li>
        </ul>
        <h3>Những ý dễ nhầm</h3>
        <ul>
            <li>Thường nhầm lực lượng nòng cốt của chiến tranh nhân dân chỉ là Bộ đội chủ lực. Thực tế là LLVT 3 thứ quân.</li>
        </ul>
        <div style="padding: 10px; background-color: #e6f7ff; border-left: 4px solid #1890ff;">
            <strong>Ghi nhớ nhanh:</strong> Chiến tranh nhân dân = Toàn dân đánh giặc + LLVT 3 thứ quân làm nòng cốt.
        </div>
        """,
        "example": ""
    },
    {
        "topicId": "hp1_other_topics",
        "title": "Ngân hàng Câu hỏi Tổng hợp - Học Phần 1",
        "keywords": ["Lịch sử quân sự", "Nghệ thuật quân sự", "Dân quân tự vệ", "Biển đảo", "An ninh Tổ quốc"],
        "summary": "Tổng hợp hơn hàng trăm câu hỏi trắc nghiệm từ ngân hàng đề của Học phần 1, hỗ trợ ôn luyện thi hết học phần.",
        "content": """
        <h3>Lưu ý về bộ đề tự động</h3>
        <p>Đây là bộ câu hỏi được trích xuất tự động từ ngân hàng đề thi môn Giáo dục Quốc phòng (Học phần 1).</p>
        <ul>
            <li>Các câu hỏi chưa có đáp án chính thức sẽ được tạm gắn mặc định là đáp án A.</li>
            <li>Sinh viên nên tự đối chiếu với giáo trình để tìm ra đáp án chính xác nhất.</li>
            <li>Phần thi thử sẽ tự động trộn các câu hỏi này.</li>
        </ul>
        """,
        "example": ""
    }
]

topics_hp2 = [
    {
        "topicId": "hp2_bai1_dien_bien_hoa_binh",
        "title": "Phòng chống Diễn biến hòa bình, Bạo loạn lật đổ",
        "keywords": ["DBHB", "Bạo loạn lật đổ", "Phi chính trị hóa", "Đa nguyên đa đảng"],
        "summary": "Nhận diện âm mưu, thủ đoạn của các thế lực thù địch trong chiến lược DBHB và biện pháp phòng chống của ta.",
        "content": """
        <h3>Nội dung trọng tâm</h3>
        <ul>
            <li>Khái niệm: DBHB là chiến lược cơ bản nhằm lật đổ chế độ chính trị xã hội từ bên trong bằng biện pháp phi quân sự.</li>
            <li>Bạo loạn lật đổ là hành động bạo lực có tổ chức để lật đổ chính quyền.</li>
            <li>Thủ đoạn: Phá hoại kinh tế, đòi đa nguyên đa đảng, xóa bỏ CN Mác-Lênin.</li>
        </ul>
        <h3>Những ý dễ nhầm</h3>
        <ul>
            <li>Sinh viên hay nhầm lẫn giữa thủ đoạn về chính trị (đòi đa đảng) và thủ đoạn về tư tưởng văn hóa (bôi nhọ lãnh tụ).</li>
        </ul>
        <div style="padding: 10px; background-color: #e6f7ff; border-left: 4px solid #1890ff;">
            <strong>Ghi nhớ nhanh:</strong> DBHB = Đánh từ bên trong (Không dùng súng).
        </div>
        """,
        "example": ""
    },
    {
        "topicId": "hp2_bai3_bao_ve_moi_truong",
        "title": "Phòng chống vi phạm pháp luật về bảo vệ môi trường",
        "keywords": ["Ô nhiễm", "Tội phạm môi trường", "Mặt khách quan", "Mặt chủ quan"],
        "summary": "Nắm vững các quy định pháp luật và biện pháp đấu tranh phòng chống tội phạm và vi phạm pháp luật về bảo vệ môi trường.",
        "content": """
        <h3>Nội dung trọng tâm</h3>
        <ul>
            <li>Các yếu tố cấu thành tội phạm: Khách thể, Mặt khách quan, Chủ thể, Mặt chủ quan.</li>
            <li>Chủ thể của tội phạm môi trường theo BLHS hiện hành bao gồm cả Pháp nhân thương mại.</li>
        </ul>
        <h3>Những ý dễ nhầm</h3>
        <ul>
            <li>Nhầm lẫn giữa 'Khách thể' và 'Đối tượng tác động'. Khách thể là quan hệ xã hội được pháp luật bảo vệ.</li>
        </ul>
        <div style="padding: 10px; background-color: #e6f7ff; border-left: 4px solid #1890ff;">
            <strong>Ghi nhớ nhanh:</strong> Khách thể (Cái bị hại) - Mặt khách quan (Hành vi) - Chủ thể (Kẻ làm) - Mặt chủ quan (Lỗi).
        </div>
        """,
        "example": ""
    },
    {
        "topicId": "hp2_other_topics",
        "title": "Ngân hàng Câu hỏi Tổng hợp - Học Phần 2",
        "keywords": ["Tội phạm công nghệ cao", "An ninh phi truyền thống", "Vi phạm pháp luật"],
        "summary": "Tổng hợp hơn hàng trăm câu hỏi trắc nghiệm từ ngân hàng đề của Học phần 2, hỗ trợ ôn luyện thi hết học phần.",
        "content": """
        <h3>Lưu ý về bộ đề tự động</h3>
        <p>Đây là bộ câu hỏi được trích xuất tự động từ ngân hàng đề thi môn Giáo dục Quốc phòng (Học phần 2).</p>
        <ul>
            <li>Các câu hỏi chưa có đáp án chính thức sẽ được tạm gắn mặc định là đáp án A.</li>
            <li>Sinh viên nên tự đối chiếu với giáo trình để tìm ra đáp án chính xác nhất.</li>
            <li>Phần thi thử sẽ tự động trộn các câu hỏi này.</li>
        </ul>
        """,
        "example": ""
    }
]

# Write knowledge.json
json.dump(topics_hp1, open(os.path.join(data_hp1_dir, "knowledge.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
json.dump(topics_hp2, open(os.path.join(data_hp2_dir, "knowledge.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)

json.dump([], open(os.path.join(data_hp1_dir, "preset_exams.json"), "w", encoding="utf-8"))
json.dump([], open(os.path.join(data_hp2_dir, "preset_exams.json"), "w", encoding="utf-8"))


# 2. Extract Questions from PDFs text
def extract_questions_from_text(file_path, default_topic_id):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
    except Exception:
        return []
        
    questions = []
    
    # Split text by "Câu X:"
    chunks = re.split(r'(?m)^Câu \d+[:.]?', text)
    
    seen_questions = set()
    global_id = 1
    
    for chunk in chunks[1:]:  # skip first empty chunk
        lines = [line.strip() for line in chunk.split('\n') if line.strip()]
        if not lines: continue
        
        question_text = ""
        options = []
        
        # Extract question text and options
        for line in lines:
            if re.match(r'^[A-E][.\)]', line):
                options.append(line)
            else:
                if not options:
                    question_text += " " + line
                else:
                    # Append to last option if it wrapped
                    options[-1] += " " + line
                    
        question_text = question_text.strip()
        
        if not question_text or len(options) < 2:
            continue
            
        # Deduplication
        norm_q = re.sub(r'\s+', '', question_text).lower()
        if norm_q in seen_questions:
            continue
        seen_questions.add(norm_q)
        
        questions.append({
            "id": global_id,
            "topicId": default_topic_id,
            "question": question_text,
            "options": options,
            "correctAnswer": "A",
            "explanation": "Câu hỏi được tự động trích xuất từ ngân hàng đề (chưa có đáp án chính thức).",
            "type": "Lý thuyết"
        })
        global_id += 1
        
    return questions

hp1_questions = extract_questions_from_text(os.path.join(root_dir, "scratch/hp1_text.txt"), "hp1_other_topics")
hp2_questions = extract_questions_from_text(os.path.join(root_dir, "scratch/hp2_text.txt"), "hp2_other_topics")

# Fetch high-quality questions from the old JSON if it exists
try:
    with open(os.path.join(root_dir, "data/quocphong/quocphong.json"), "r", encoding="utf-8") as f:
        old_data = json.load(f)
        old_qs = old_data.get("questions", [])
        for q in old_qs:
            tid = q.get("topicId", "")
            if tid.startswith("hp1_"):
                # Ensure no ID conflict
                q["id"] = "hq_" + str(q["id"])
                hp1_questions.insert(0, q)
            elif tid.startswith("hp2_"):
                q["id"] = "hq_" + str(q["id"])
                hp2_questions.insert(0, q)
except Exception as e:
    print("Warning: Could not load old high-quality questions:", e)

# Write questions.json
json.dump(hp1_questions, open(os.path.join(data_hp1_dir, "questions.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
json.dump(hp2_questions, open(os.path.join(data_hp2_dir, "questions.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)

print(f"Extracted {len(hp1_questions)} questions for HP1.")
print(f"Extracted {len(hp2_questions)} questions for HP2.")

# Remove old quocphong dir to avoid confusion
quocphong_dir = os.path.join(root_dir, "data/quocphong")
if os.path.exists(quocphong_dir):
    shutil.rmtree(quocphong_dir)
    print(f"Removed old {quocphong_dir}")
