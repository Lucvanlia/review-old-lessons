# Các phát hiện (Findings)

1. **Kiến trúc App.js**: Dựa trên các JSON mẫu trong `data/python`, file `app.js` được thiết kế để tự động fetch các file JSON tương ứng (knowledge, questions, preset_exams) từ thư mục `data/<subject_id>/` khi người dùng click vào thẻ môn học.
2. **Loại câu hỏi (Multiple Answers)**: Các câu như Q22, Q23, Q24 yêu cầu chọn 2 đáp án (Select two), do đó trong `questions.json`, mảng `correctAnswer` đã được thiết lập dưới dạng mảng (ví dụ `["C", "E"]`) thay vì một ký tự string duy nhất, đảm bảo tính năng Multiple Select hoạt động chính xác nếu logic JavaScript có hỗ trợ.
3. **Phân loại**: Toàn bộ nội dung lý thuyết đã bám sát chính xác các lỗ hổng thực tế đề cập trong đề, như SQLi Error Handling, RSA cryptography, File permissions.
