# EduPrep AI - Hệ Thống Ôn Tập & Trắc Nghiệm Trực Tuyến

EduPrep AI là một trang web ứng dụng đơn trang (SPA) viết bằng HTML, CSS, và JavaScript thuần (Vanilla JS), giúp người học ôn tập lý thuyết chi tiết và thi thử các môn học lập trình (Java Web và Python) bám sát đề cương ôn tập.

---

## 🚀 Hướng Dẫn Cách Chạy Dự Án

Do ứng dụng tải dữ liệu lý thuyết và câu hỏi thông qua các tệp tin JSON cục bộ bằng API `fetch`, trình duyệt sẽ chặn yêu cầu nếu bạn mở trực tiếp tệp `index.html` (lỗi CORS do giao thức `file://`). Vì vậy, **bắt buộc** phải chạy dự án thông qua một máy chủ HTTP cục bộ (Local Web Server).

Dưới đây là các cách chạy đơn giản nhất:

### Cách 1: Sử dụng Python (Đơn giản và có sẵn)
Nếu máy tính của bạn đã cài đặt Python, hãy mở Terminal/Command Prompt, di chuyển đến thư mục của dự án và chạy lệnh sau:

```bash
python -m http.server 8000
```

Sau đó, mở trình duyệt web và truy cập địa chỉ:
👉 **[http://localhost:8000](http://localhost:8000)**

---

### Cách 2: Sử dụng VS Code Extension "Live Server"
Nếu bạn sử dụng trình soạn thảo VS Code:
1. Cài đặt extension **Live Server** (do Ritwick Dey phát triển).
2. Mở thư mục dự án `ontap_html` bằng VS Code.
3. Nhìn xuống góc dưới cùng bên phải màn hình và nhấn vào nút **Go Live**.
4. Ứng dụng sẽ tự động mở trên trình duyệt mặc định (thường là cổng `5500`).

---

### Cách 3: Sử dụng Node.js (`npx`)
Nếu bạn đã cài đặt Node.js trên máy tính, chạy lệnh sau trong thư mục dự án:

```bash
npx http-server -p 8000
```

Sau đó, truy cập địa chỉ:
👉 **[http://localhost:8000](http://localhost:8000)**

---

## 📁 Cấu Trúc Thư Mục Dự Án

```text
ontap_html/
├── data/                    # Thư mục chứa cơ sở dữ liệu dạng JSON
│   ├── java/                # Dữ liệu lý thuyết, câu hỏi và đề thi của môn Java
│   │   ├── knowledge.json   # 17 chủ đề lý thuyết nâng cao
│   │   ├── questions.json   # Ngân hàng 119 câu hỏi đề cương
│   │   └── preset_exams.json# 4 đề thi thử phân loại (Servlet, Spring, JPA, Tổng hợp)
│   ├── python/              # Dữ liệu lý thuyết, câu hỏi và đề thi của môn Python
│   │   ├── knowledge.json   # 10 chủ đề lý thuyết chi tiết
│   │   ├── questions.json   # Ngân hàng 144 câu hỏi trắc nghiệm
│   │   └── preset_exams.json# 4 đề thi thử phân loại & tổng hợp Python
│   └── subjects.json        # Danh mục các môn học đăng ký hiển thị trên website
│
├── pdf/                     # Tài liệu học tập nguồn dạng PDF & Markdown
│   ├── java-on-tap/         # File tổng hợp lý thuyết và ngân hàng câu hỏi Java dạng Markdown
│   │   ├── knowledge.md
│   │   └── question_bank.md
│   ├── python-on-tap/       # File tổng hợp lý thuyết và ngân hàng câu hỏi Python dạng Markdown
│   │   ├── knowledge.md
│   │   └── question_bank.md
│   └── ontap.pdf            # File PDF gốc đề cương ôn thi Java Web
│
├── index.html               # Giao diện chính của website (SPA)
├── style.css                # Tệp tin định dạng giao diện (Glassmorphism & Sleek Dark theme)
├── app.js                   # Logic xử lý hoạt động của website (State, Routing, Quiz, LocalStorage)
├── PROJECT_RULES.md         # Quy định và hướng dẫn tự động cập nhật tài liệu của hệ thống
└── README.md                # File hướng dẫn chạy và quản lý dự án (tệp này)
```

---

## 🛠️ Hướng Dẫn Cập Nhật Dữ Liệu Học Tập

Để cập nhật lý thuyết hoặc thêm câu hỏi mới vào ứng dụng, bạn chỉ cần thực hiện theo 2 bước:

1. **Cập nhật File Markdown nguồn:**
   * Sửa đổi các file `.md` tương ứng trong thư mục `pdf/java-on-tap/` hoặc `pdf/python-on-tap/`.
2. **Đồng bộ hóa sang JSON:**
   * Chạy script Python `scratch/update_all_data.py` để hệ thống tự động biên dịch dữ liệu từ mã nguồn Python cập nhật vào các file JSON trong thư mục `data/` và tự động phân bổ câu hỏi thành các đề thi thử cân đối.
   * Chạy lệnh:
     ```bash
     python scratch/update_all_data.py
     ```
   * Sau đó chạy script kiểm định để đảm bảo không có lỗi định dạng:
     ```bash
     python scratch/validate_java_data.py
     python scratch/validate_python_data.py
     ```

## ✨ Các Tính Năng Nổi Bật của Website

1. **Học tập đa phương thức:** Xem lý thuyết có cấu trúc, kèm ví dụ code sinh động. Có chức năng lưu ghi chú cá nhân tự động lưu vào trình duyệt (`localStorage`).
2. **Đánh dấu tiến độ:** Người học có thể nhấn "Đánh dấu đã học" để theo dõi phần trăm hoàn thành môn học trực quan trên thanh tiến độ.
3. **Luyện tập theo chương:** Chọn học và làm các câu hỏi trắc nghiệm của riêng một hoặc nhiều chủ đề mà mình mong muốn.
4. **Thi thử có tính giờ:** Làm các đề thi mẫu được chuẩn bị sẵn hoặc tự sinh đề ngẫu nhiên từ ngân hàng câu hỏi. Có đếm ngược thời gian, chấm điểm và xem lời giải thích chi tiết cho từng câu hỏi khi hoàn thành.
5. **Thống kê học tập:** Phân tích độ chính xác theo từng chương học để biết phần nào mình đang yếu và cần ôn tập lại.
