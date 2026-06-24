# Tóm Tắt Kiến Thức An Toàn Thông Tin

## 1. Hệ Mật Mã RSA
Mật mã RSA là một hệ mã hóa bất đối xứng (asymmetric encryption) sử dụng một cặp khóa: Khóa công khai (Public Key) để mã hóa và Khóa bí mật (Private Key) để giải mã.
- **Tính n:** n = p × q.
- **Tính φ(n):** φ(n) = (p-1) × (q-1).
- **Tìm d:** (e × d) mod φ(n) = 1.
- **Mã hóa:** C = M^e mod n.
- **Giải mã:** M = C^d mod n.

## 2. Phân Quyền Hệ Thống Linux
Hệ thống phân quyền dựa trên 3 nhóm: User (u), Group (g), Others (o).
Mã bát phân (Octal):
- r (Read) = 4
- w (Write) = 2
- x (Execute) = 1
Ví dụ: `chmod 754` cấp quyền rwx (User), r-x (Group), r-- (Others).

## 3. Lỗ Hổng Tràn Bộ Đệm (Buffer Overflow)
Lỗi xảy ra khi dữ liệu nhập vào lớn hơn dung lượng bộ đệm, làm tràn sang các vùng nhớ lân cận.
Mục tiêu là ghi đè lên Thanh ghi địa chỉ trả về (Return Address - EIP/RIP) để điều hướng luồng thực thi sang Shellcode, dẫn đến mất dữ liệu hoặc leo thang đặc quyền.

## 4. Tấn Công Ứng Dụng Web
- **SQL Injection (SQLi):** Tấn công bằng cách ghép ký tự đặc biệt để thao túng câu truy vấn SQL (Ví dụ `admin' OR 1=1 --`). Khắc phục: Parameterized Queries, Server-side validation, Error handling an toàn.
- **Cross-Site Scripting (XSS):** Chèn JavaScript độc hại vào trình duyệt nạn nhân.
- **Command Injection:** Tiêm lệnh hệ điều hành thông qua ứng dụng (ví dụ dùng dấu `;` để nối thêm lệnh như `cd ../../../etc; cat shadow`).

## 5. Khái Niệm Cốt Lõi Khác
- **CIA Triad:** Confidentiality (Bảo mật), Integrity (Toàn vẹn), Availability (Sẵn sàng).
- **Access Control:**
  - MAC (Mandatory Access Control): Theo nhãn bảo mật (Classification level).
  - DAC (Discretionary Access Control): Tự quyết định quyền.
  - Least Privilege: Đặc quyền tối thiểu.
  - Separation of Duties: Phân chia trách nhiệm.
- **Tấn công thường gặp:** Replay Attack, Zero-day exploit, Vishing, Brute force, Backdoor (tạo User ID 0).
