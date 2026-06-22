# PROJECT_RULES - PDF KNOWLEDGE SOURCE RULE

## Thư mục nguồn

Mặc định mọi tài liệu học tập nằm trong:
`C:\Users\DELL\Downloads\ontap_html\pdf` hoặc các thư mục con bên trong.

Ví dụ:
```
pdf/
├── python-on-tap/
├── java-on-tap/
├── xstk/
├── physics/
└── ...
```

---

## Quy tắc xử lý

Khi người dùng yêu cầu:
* Tạo website ôn tập
* Tạo ngân hàng câu hỏi
* Tạo dữ liệu JSON
* Tạo flashcard
* Tạo đề thi thử

Agent phải tự động thực hiện các bước sau:

### Bước 1: Quét nguồn tài liệu
Quét toàn bộ các file tài liệu định dạng:
* PDF (`.pdf`)
* PPTX (`.pptx`)
* DOCX (`.docx`)
trong thư mục môn học tương ứng (ví dụ: `pdf/python-on-tap/`).

### Bước 2: Tự động trích xuất
Trích xuất tự động các nội dung chính từ tài liệu:
* Tên chương / Chủ đề
* Mục kiến thức chính
* Ví dụ minh họa (code mẫu, ví dụ thực tế)
* Bài tập / Câu hỏi ôn tập

### Bước 3: Sinh file knowledge.md
Sinh file `knowledge.md` trong thư mục của môn học đó (ví dụ: `pdf/python-on-tap/knowledge.md`) với cấu trúc:
```markdown
# [Tên Chương / Chủ đề]

## Tóm tắt
[Nội dung tóm tắt ngắn gọn]

## Khái niệm
[Các định nghĩa, khái niệm cốt lõi]

## Ví dụ
[Các ví dụ code, bài tập mẫu có lời giải]

## Ghi nhớ
[Các điểm quan trọng cần lưu ý]
```

### Bước 4: Sinh file question_bank.md
Sinh file `question_bank.md` trong thư mục môn học (ví dụ: `pdf/python-on-tap/question_bank.md`).
Yêu cầu số lượng câu hỏi cho mỗi chương:
* Tối thiểu: 10 câu hỏi / chương.
* Tối đa: Không giới hạn.

### Bước 5: Phân loại câu hỏi
Mỗi câu hỏi trong ngân hàng câu hỏi phải được phân loại rõ ràng thuộc một trong các nhóm:
* Lý thuyết
* Tình huống
* Đọc hiểu
* Phân tích
* Tính toán
* Đọc code (nếu là môn học lập trình)

### Bước 6: Sinh dữ liệu JSON phục vụ website
Tạo/cập nhật dữ liệu JSON tương ứng trong thư mục `/data/<subject_id>/` (ví dụ: `/data/python-on-tap/` hoặc `/data/python/` dựa trên ID môn học trong `subjects.json`) để phục vụ website.
- Cập nhật `/data/subjects.json` để đăng ký môn học mới (nếu chưa có).
- Sinh file `knowledge.json`, `questions.json` và `preset_exams.json` có cấu trúc tương ứng để website hiển thị.

---

## Quy tắc cập nhật

Nếu thư mục xuất hiện tài liệu học tập mới (PDF, PPTX, DOCX):
Agent phải **tự động**:
1. Đọc và phân tích tài liệu mới đó.
2. Cập nhật nội dung vào file `knowledge.md` tương ứng.
3. Cập nhật thêm câu hỏi vào file `question_bank.md` tương ứng.
4. Cập nhật lại các file JSON trong thư mục `/data/<subject_id>/`.
**Tuyệt đối không hỏi lại hoặc xin xác nhận từ người dùng trước khi cập nhật.**

---

## Quy tắc ưu tiên nguồn dữ liệu

1. Tài liệu PDF (`.pdf`) là ưu tiên cao nhất.
2. Tài liệu PPTX (`.pptx`) là ưu tiên tiếp theo.
3. Tài liệu DOCX (`.docx`) là ưu tiên cuối cùng.

Nếu có nhiều tài liệu trùng lắp hoặc giao thoa nội dung:
- Agent phải tự động hợp nhất (merge) thông tin một cách thông minh để tránh trùng lặp kiến thức và câu hỏi.

---

## Quy tắc website

Website ôn tập phải luôn đáp ứng đầy đủ các tính năng sau:
1. **Tổng quan kiến thức:** Giao diện trực quan xem tài liệu học tập theo chương/chủ đề. Lý thuyết phải cực kỳ đầy đủ, bao gồm cả phần cơ bản và các phần nhỏ nâng cao (chuyên sâu), không được rút gọn quá mức. Lý thuyết phải bao quát toàn bộ nội dung xuất hiện trong các câu hỏi ôn tập để người học tránh bị hoang mang khi tra cứu.
2. **Ghi chú cá nhân:** Cho phép người dùng ghi chú trực tiếp và lưu trữ theo từng môn học/chương.
3. **Ôn tập theo chương:** Cho phép ôn tập lý thuyết và làm trắc nghiệm riêng theo từng chương/chủ đề được chọn.
4. **Thi thử ngẫu nhiên:** Chức năng thi thử với số lượng câu hỏi tự chọn (hoặc đề thi mẫu cố định), tự động trộn câu hỏi và đáp án, đếm ngược thời gian, nộp bài tính điểm. Chú trọng thi thử dựa trên các tài liệu PDF giới hạn của đề thi, không sử dụng các nguồn thi thử Java Core bên ngoài.
5. **Thống kê kết quả / Phân tích học tập:** Hiển thị biểu đồ độ chính xác và gợi ý các chủ đề làm tốt/cần cải thiện.
6. **Lưu LocalStorage:** Mọi tiến trình học tập, lịch sử thi thử, ghi chú cá nhân và cấu hình của người dùng phải được lưu và khôi phục từ `localStorage`.

Các quy tắc trên được áp dụng bắt buộc cho tất cả các môn học được đưa vào ôn tập.

