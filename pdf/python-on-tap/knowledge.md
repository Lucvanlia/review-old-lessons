# TỔNG HỢP KIẾN THỨC ÔN TẬP PYTHON (BẢN CHI TIẾT)

# Khái niệm cơ bản & Nhập xuất dữ liệu

## Tóm tắt
Python là ngôn ngữ lập trình cấp cao, thông dịch (interpreted), hướng đối tượng (OOP) và có kiểu dữ liệu động (dynamically typed). 1. KHAI BÁO BIẾN VÀ QUY TẮC ĐẶT TÊN:

## Khái niệm
Python là ngôn ngữ lập trình cấp cao, thông dịch (interpreted), hướng đối tượng (OOP) và có kiểu dữ liệu động (dynamically typed).

1. KHAI BÁO BIẾN VÀ QUY TẮC ĐẶT TÊN:
• Khai báo biến: Không cần khai báo kiểu dữ liệu trước, kiểu của biến được quyết định tự động lúc gán giá trị.
• Quy tắc đặt tên biến hợp lệ:
  - Bắt đầu bằng chữ cái (a-z, A-Z) hoặc dấu gạch dưới `_`.
  - KHÔNG được bắt đầu bằng chữ số (Ví dụ: `2my_var` là KHÔNG hợp lệ).
  - Không chứa ký tự đặc biệt như @, #, $, %, khoảng trắng.
  - Phân biệt chữ hoa và chữ thường (ví dụ `myVar` khác `myvar`).
  - Không trùng các từ khóa (keywords) của Python.
• Phép gán đồng thời:
  - Gán cùng một giá trị cho nhiều biến: `a = b = c = 10`.
  - Gán các giá trị khác nhau: `a, b, c = 1, 2, 3`. (Lưu ý: Viết `a = 6, b = 8` không dùng dấu phẩy gán đồng thời sẽ gây ra lỗi cú pháp Syntax Error).

2. KIỂU DỮ LIỆU SỐ (NUMBERS):
• `int` (Số nguyên): Không giới hạn độ dài.
• `float` (Số thực): Ví dụ `3.14`, `2.0`.
• `complex` (Số phức): Có dạng `a + bj` (ví dụ `2 + 3j`).
• `bool` (Luận lý): Gồm `True` (tương đương 1) và `False` (tương đương 0). Trong Python, kiểu bool được coi là một tập con của kiểu số nguyên.

3. TOÁN TỬ SỐ HỌC CẦN LƯU Ý:
• Phép chia lấy nguyên (`//`): Trả về phần nguyên của phép chia (Ví dụ `22 // 3` trả về `7`).
• Phép chia lấy dư (`%`): Trả về số dư. 
  - Lưu ý đặc biệt: Nếu có bất kỳ toán hạng nào là số thực (`float`), kết quả của phép toán cũng được tự động ép kiểu thành số thực. Ví dụ biểu thức `22 % 3.0` sẽ trả về giá trị thực là `1.0` chứ không phải là số nguyên `1`.
• Phép lũy thừa (`**`): Ví dụ `2 ** 3` trả về `8`.

4. NHẬP XUẤT DỮ LIỆU:
• `print()`: Hàm xuất dữ liệu ra console. Mặc định tự động thêm ký tự xuống dòng `\n` ở cuối kết quả in ra. Để in không xuống dòng, ta phải tùy chỉnh tham số `end` (ví dụ: `print("H", end="")`). Tham số `sep` dùng để định nghĩa ký tự ngăn cách giữa các giá trị in ra.
• `input()`: Nhập dữ liệu từ bàn phím. Mặc định LUÔN TRẢ VỀ kiểu dữ liệu chuỗi (`str`). Muốn tính toán số học, ta bắt buộc phải ép kiểu thủ công (ví dụ: `int(input())`).
• Định nghĩa chuỗi hợp lệ: Phải được bao quanh bởi cặp nháy đơn `'...'` hoặc nháy kép `"..."`, hoặc ba nháy `'''...'''` / `"""..."""` cho chuỗi nhiều dòng. Viết chuỗi thiếu cặp nháy (ví dụ chỉ ghi `python` mà không có nháy) sẽ được Python hiểu là một biến và ném ra NameError nếu biến đó chưa khai báo.

## Ví dụ
```python
# Minh họa nhập xuất và toán tử cơ bản
a = 22
b = 3.0

print("Phép chia lấy nguyên:", a // 3)   # Output: 7 (int)
print("Phép chia lấy dư thực:", a % b)   # Output: 1.0 (float vì số chia là 3.0)
print("Phép lũy thừa:", 2 ** 3)          # Output: 8

# Nhập xuất không xuống dòng và tùy chỉnh ngăn cách
print("Hello", "World", sep="-", end="! ") # Output: Hello-World!
print("Tiếp tục trên cùng dòng.")

# Khai báo xâu kí tự hợp lệ
s1 = "123_@##" # Hợp lệ
# s2 = python  # Lỗi NameError vì thiếu nháy bao quanh
```

## Ghi nhớ
- Hãy làm quen với cú pháp và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Cấu trúc rẽ nhánh & Kiểu dữ liệu tập hợp

## Tóm tắt
Python cung cấp cấu trúc rẽ nhánh điều kiện linh hoạt cùng các kiểu dữ liệu tập hợp phong phú để lưu trữ nhóm dữ liệu. 1. PHÂN LOẠI MUTABLE VS IMMUTABLE (RẤT QUAN TRỌNG):

## Khái niệm
Python cung cấp cấu trúc rẽ nhánh điều kiện linh hoạt cùng các kiểu dữ liệu tập hợp phong phú để lưu trữ nhóm dữ liệu.

1. PHÂN LOẠI MUTABLE VS IMMUTABLE (RẤT QUAN TRỌNG):
• Mutable (Có thể sửa đổi phần tử trực tiếp trên vùng nhớ cũ):
  - Gồm: List (`[1, 2]`), Dictionary (`{'key': 'value'}`), Set (`{1, 2}`).
• Immutable (Bất biến, không thể sửa đổi phần tử sau khi tạo. Mọi thao tác chỉnh sửa đều tạo ra đối tượng mới ở vùng nhớ mới):
  - Gồm: String (`"hello"`), Tuple (`(1, 2)`), Int, Float, Bool.

2. CÁC KIỂU DỮ LIỆU TẬP HỢP:
• List: Danh sách có thứ tự, cho phép phần tử trùng lặp, dùng ngoặc vuông `[]`.
• Tuple: Tương tự List nhưng là bất biến (immutable), dùng ngoặc đơn `()`.
• Set: Tập hợp các phần tử duy nhất, không có thứ tự, dùng ngoặc nhọn `{}`.
• Dictionary: Tập hợp key-value không có thứ tự, dùng `{key: value}`.
  - Lưu ý về Dictionary Key: Khóa (key) của dictionary bắt buộc phải thuộc kiểu dữ liệu bất biến (immutable/hashable) như int, float, string, tuple. Kiểu mutable như List KHÔNG thể làm key.
  - Phương thức: `d.keys()` trả về danh sách các key, `d.values()` trả về danh sách các value, `d.items()` trả về cặp (key, value).

3. PHÉP GÁN THAM CHIẾU:
• Với kiểu mutable như List, phép gán `y = x` không tạo ra bản sao mới mà chỉ tạo thêm một tham chiếu cùng trỏ vào một vùng nhớ. Khi gọi `y.append(4)`, danh sách gốc `x` cũng sẽ tự động bị thay đổi thành `[1, 2, 3, 4]`.

4. CẤU TRÚC RẼ NHÁNH VÀ CHÂN TRỊ (TRUTHY/FALSY):
• Python sử dụng thụt lề (indentation - mặc định 4 khoảng trắng) thay cho ngoặc nhọn `{}` để gom khối lệnh điều kiện.
• Các toán tử logic: `and` (và), `or` (hoặc), `not` (phủ định).
• Chân trị (Truthiness): Trong Python, các giá trị sau tương đương với `False` trong biểu thức điều kiện: số `0` (hoặc `0.0`), đối tượng `None`, chuỗi rỗng `""`, danh sách rỗng `[]`, tuple rỗng `()`, dict rỗng `{}`. Các giá trị khác (bao gồm số âm như `-3`) đều tương đương với `True`.
• Toán tử rẽ nhánh inline (Ternary Operator): Cú pháp `val_true if condition else val_false` (Ví dụ: `'pq' if '12'.isdigit() else 'rs'`).

5. XỬ LÝ NGOẠI LỆ (TRY-EXCEPT-FINALLY):
• Sử dụng cấu trúc `try...except...` để bắt và xử lý các lỗi runtime (chia cho 0, sai kiểu dữ liệu, thiếu file) để chương trình không bị crash đột ngột.
• Khối `finally` luôn luôn được thực thi bất kể có lỗi xảy ra hay không, thường dùng để giải phóng tài nguyên hệ thống.

## Ví dụ
```python
# Minh họa phép gán tham chiếu list
x = [1, 2, 3]
y = x
y.append(4)
print("x sau khi sửa y:", x) # Output: [1, 2, 3, 4]

# Minh họa ternary operator và truthy
a = -3
result = "True" if a else "False" # -3 khác 0 nên là True
print("Kết quả chân trị:", result) # Output: True

# Dictionary key là tuple (hợp lệ) nhưng không thể là list
d = {(1, 2): "TupleKey"} # Hợp lệ
# d = {[1, 2]: "ListKey"}  # Lỗi TypeError: unhashable type: 'list'

# Try-except-finally
try:
    val = 10 / 0
except ZeroDivisionError:
    print("Lỗi chia cho 0!")
finally:
    print("Khối này luôn chạy.") # Luôn chạy sau try/except
```

## Ghi nhớ
- Hãy làm quen với cú pháp và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Cấu trúc lặp (Loops)

## Tóm tắt
Python hỗ trợ hai cấu trúc vòng lặp chính để lặp đi lặp lại khối lệnh: `while` (lặp kiểm tra điều kiện) và `for` (lặp duyệt qua tập hợp). 1. VÒNG LẶP WHILE:

## Khái niệm
Python hỗ trợ hai cấu trúc vòng lặp chính để lặp đi lặp lại khối lệnh: `while` (lặp kiểm tra điều kiện) và `for` (lặp duyệt qua tập hợp).

1. VÒNG LẶP WHILE:
• Thực thi khối lệnh chừng nào biểu thức điều kiện còn thỏa mãn chân trị `True`.
• Cần đảm bảo cập nhật biến điều kiện trong thân vòng lặp để tránh vòng lặp vô hạn.

2. VÒNG LẶP FOR:
• Dùng để duyệt qua lần lượt các phần tử của một tập hợp tuần tự (như List, Tuple, String, Dictionary) hoặc một dãy số sinh ra từ range().
• Cú pháp hợp lệ bắt buộc phải kết thúc bằng dấu hai chấm `:`. Ví dụ: `for i in range(5):`.

3. HÀM RANGE(START, STOP, STEP):
• Hàm range sinh ra một dãy số nguyên. Có 3 tham số:
  - `start` (mặc định là 0): Giá trị bắt đầu.
  - `stop`: Giá trị dừng (dãy số sinh ra dừng ngay trước `stop`, không bao gồm `stop`).
  - `step` (mặc định là 1): Bước nhảy tăng/giảm giữa các số.
• LƯU Ý BƯỚC NHẢY ÂM: 
  - Nếu `step` là số âm, `start` phải lớn hơn `stop`. Dãy số sẽ đếm lùi.
  - Ví dụ: `range(5, 0, -2)` sinh ra dãy số: `5, 3, 1` (không bao gồm 0).
  - Ví dụ: `range(6, 0, -2)` sinh ra dãy: `6, 4, 2`.

4. LỆNH ĐIỀU KHIỂN VÒNG LẶP:
• `break`: Thoát hoàn toàn và lập tức ra khỏi vòng lặp chứa nó.
• `continue`: Bỏ qua toàn bộ các câu lệnh còn lại trong thân vòng lặp của lượt lặp hiện tại, và lập tức nhảy sang lượt lặp tiếp theo.
• `pass`: Lệnh giữ chỗ rỗng, không làm gì cả, dùng để đảm bảo đúng cú pháp khi khối lệnh chưa được viết.

5. VÒNG LẶP KẾT HỢP KHỐI ELSE (FOR...ELSE / WHILE...ELSE):
• Khối `else` viết thẳng hàng với `for`/`while` sẽ ĐƯỢC thực thi khi vòng lặp hoàn thành bình thường mà KHÔNG gặp lệnh `break` giữa chừng.
• Nếu vòng lặp bị ngắt quãng bởi lệnh `break`, khối `else` sẽ BỊ BỎ QUA.

## Ví dụ
```python
# Vòng lặp for-else và break
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
else:
    print("Vòng lặp hoàn thành!") # Không được in ra vì bị break ở i=3
# Output: 0 1 2

print()

# range bước nhảy âm đếm lùi
for x in range(5, 0, -2):
    print(x, end=" ") # Output: 5 3 1
```

## Ghi nhớ
- Hãy làm quen với cú pháp và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Hàm & Phạm vi biến (Functions)

## Tóm tắt
Hàm là khối lệnh được định nghĩa một lần để thực hiện một tác vụ cụ thể, giúp tái sử dụng mã nguồn và tăng tính module cho chương trình. 1. KHAI BÁO HÀM VÀ GIÁ TRỊ TRẢ VỀ:

## Khái niệm
Hàm là khối lệnh được định nghĩa một lần để thực hiện một tác vụ cụ thể, giúp tái sử dụng mã nguồn và tăng tính module cho chương trình.

1. KHAI BÁO HÀM VÀ GIÁ TRỊ TRẢ VỀ:
• Hàm được định nghĩa bằng từ khóa `def`, theo sau là tên hàm, danh sách tham số trong ngoặc đơn và kết thúc bằng dấu `:`.
• Sử dụng từ khóa `return` để trả kết quả về cho nơi gọi. Nếu hàm không có lệnh `return`, hoặc chỉ ghi `return` không tham số, hàm mặc định trả về đối tượng `None`.

2. CÁC LOẠI THAM SỐ (PARAMETERS) VÀ ĐỐI SỐ:
• Tham số mặc định (Default Parameters):
  - Cho phép gán giá trị mặc định cho tham số (ví dụ: `def func(a, b=10):`).
  - LƯU Ý QUAN TRỌNG: Các tham số mặc định bắt buộc phải được khai báo sau các tham số không có giá trị mặc định. Viết `def func(a=10, b):` sẽ gây lỗi cú pháp.
  - SỰ CỐ BIẾN MUTABLE LÀM GIÁ TRỊ MẶC ĐỊNH: Giá trị mặc định của đối số chỉ được khởi tạo MỘT LẦN DUY NHẤT khi hàm được định nghĩa. Nếu ta dùng một kiểu dữ liệu mutable làm mặc định (ví dụ `li=[]`), danh sách này sẽ được dùng chung giữa các lần gọi hàm, dẫn đến dữ liệu của các lần gọi trước bị tích lũy sang các lần gọi sau.
• Số lượng đối số biến đổi (*args và **kwargs):
  - `*args`: Nhận tất cả các đối số vị trí tùy chọn truyền thêm dưới dạng một tập hợp dạng **Tuple**.
  - `**kwargs`: Nhận tất cả các đối số từ khóa (keyword arguments) truyền thêm dưới dạng một **Dictionary**.

3. PHẠM VI BIẾN (SCOPE):
• Biến cục bộ (Local Variable): Khai báo bên trong hàm, chỉ có hiệu lực và sử dụng được bên trong hàm đó.
• Biến toàn cục (Global Variable): Khai báo ngoài hàm.
• Từ khóa `global`: Nếu muốn chỉnh sửa trực tiếp giá trị của một biến toàn cục ngay bên trong hàm, ta phải khai báo biến đó kèm từ khóa `global` ở đầu hàm (ví dụ: `global x`). Nếu không khai báo, việc gán `x = 10` trong hàm chỉ tạo ra một biến cục bộ trùng tên và không làm đổi giá trị biến toàn cục bên ngoài.

4. HÀM NẶC DANH (LAMBDA):
• Hàm nặc danh ngắn gọn, được định nghĩa trên một dòng bằng từ khóa `lambda`.
• Cú pháp: `lambda arguments: expression` (Ví dụ: `lambda x: x**2` trả về bình phương của x). Tự động trả về giá trị của biểu thức mà không cần từ khóa `return`.

## Ví dụ
```python
# Sự cố mutable default argument
def add_to_list(val, li=[]):
    li.append(val)
    return li

print(add_to_list(1)) # Output: [1]
print(add_to_list(2)) # Output: [1, 2] (Dùng lại danh sách cũ!)

# Khắc phục sự cố trên:
def safe_add(val, li=None):
    if li is None:
        li = []
    li.append(val)
    return li

# Biến global
x = 5
def update_global():
    global x
    x = 10
update_global()
print("x global:", x) # Output: 10

# Lambda function
square = lambda n: n**2
print("Bình phương 5:", square(5)) # Output: 25
```

## Ghi nhớ
- Hãy làm quen với cú pháp và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Xử lý chuỗi ký tự (Strings)

## Tóm tắt
Chuỗi ký tự trong Python là một dãy các ký tự bất biến (immutable), đại diện bằng kiểu dữ liệu `str`. 1. CHỈ MỤC (INDEXING) VÀ CẮT CHUỖI (SLICING):

## Khái niệm
Chuỗi ký tự trong Python là một dãy các ký tự bất biến (immutable), đại diện bằng kiểu dữ liệu `str`.

1. CHỈ MỤC (INDEXING) VÀ CẮT CHUỖI (SLICING):
• Chỉ mục:
  - Chỉ mục dương: Bắt đầu từ `0` (ký tự đầu tiên) tăng dần đến `len-1` (ký tự cuối).
  - Chỉ mục âm: Bắt đầu từ `-1` (ký tự cuối cùng) giảm dần về phía trước.
• Cắt chuỗi (Slicing):
  - Cú pháp: `s[start:stop:step]`
  - Trích xuất chuỗi con từ chỉ mục `start` và dừng ngay trước chỉ mục `stop`, khoảng cách bước nhảy là `step`.
  - Đảo ngược chuỗi: Sử dụng cú pháp `s[::-1]`.
  - Độ dài chuỗi: Sử dụng hàm `len(s)` trả về tổng số ký tự trong chuỗi (kể cả chữ, số, ký tự đặc biệt và khoảng trắng).

2. CÁC PHƯƠNG THỨC THAO TÁC CHUỖI PHỔ BIẾN:
• `s.lower()`, `s.upper()`: Chuyển đổi toàn bộ chuỗi thành chữ thường / chữ hoa.
• `s.strip()`: Loại bỏ toàn bộ khoảng trắng thừa ở hai đầu chuỗi (không loại bỏ khoảng trắng ở giữa).
• `s.split(delimiter)`: Tách chuỗi thành một **Danh sách** (List) các chuỗi con dựa trên ký tự phân tách `delimiter`.
• `s.join(list)`: Gộp một danh sách các chuỗi thành một chuỗi duy nhất bằng cách chèn ký tự nối `s` vào giữa các phần tử.
• `s.replace(old, new)`: Tìm kiếm và thay thế toàn bộ chuỗi con `old` bằng chuỗi con mới `new`.
• `s.find(sub)`: Tìm vị trí xuất hiện đầu tiên của chuỗi con `sub`. Trả về chỉ mục của ký tự bắt đầu, hoặc trả về `-1` nếu không tìm thấy.
• `s.isdigit()`: Kiểm tra xem toàn bộ các ký tự trong chuỗi có phải là chữ số hay không. Trả về `True` hoặc `False`.

## Ví dụ
```python
# Minh họa slicing và methods
s = "  Python Programming  "

# Loại bỏ khoảng trắng 2 đầu và cắt chuỗi
s_clean = s.strip() # "Python Programming"
print("Độ dài:", len(s_clean)) # Output: 18

print("Chuỗi đảo ngược:", s_clean[::-1]) # Output: gnimmargorP nohtyP
print("Cắt chuỗi con:", s_clean[0:6])     # Output: Python

# Tách chuỗi và gộp chuỗi
words = "Táo,Chuối,Cam".split(",")
print("List words:", words) # Output: ['Táo', 'Chuối', 'Cam']
joined_str = "-".join(words)
print("Chuỗi gộp:", joined_str) # Output: Táo-Chuối-Cam

# find và isdigit
print("Vị trí chữ Prog:", s_clean.find("Prog")) # Output: 7
print("Vị trí không có:", s_clean.find("Java")) # Output: -1
print("Kiểm tra số '123':", "123".isdigit())    # Output: True
```

## Ghi nhớ
- Hãy làm quen với cú pháp và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Xử lý tệp tin (File Handling)

## Tóm tắt
Python cung cấp các hàm dựng sẵn mạnh mẽ để làm việc với các tệp tin (đọc và ghi file) trên đĩa cứng hệ thống. 1. HÀM OPEN() VÀ CÁC CHẾ ĐỘ MỞ FILE (MODES):

## Khái niệm
Python cung cấp các hàm dựng sẵn mạnh mẽ để làm việc với các tệp tin (đọc và ghi file) trên đĩa cứng hệ thống.

1. HÀM OPEN() VÀ CÁC CHẾ ĐỘ MỞ FILE (MODES):
• Cú pháp: `open(file_path, mode, encoding)`
• Các chế độ mở file (`mode`) chính:
  - `'r'` (Read): Mở để đọc dữ liệu (Chế độ mặc định). Ném ra lỗi `FileNotFoundError` nếu file không tồn tại trên đĩa.
  - `'w'` (Write): Mở để ghi dữ liệu. Nếu file chưa tồn tại, tự tạo file mới. Nếu file đã tồn tại, nó sẽ XÓA SẠCH toàn bộ nội dung cũ của file trước khi ghi đè dữ liệu mới.
  - `'a'` (Append): Mở để ghi tiếp vào cuối file. Nếu file đã tồn tại, dữ liệu mới sẽ được nối tiếp vào cuối file mà không làm mất nội dung cũ.
  - `'+'` (Update): Mở file để vừa đọc vừa ghi kết hợp (ví dụ `'r+'`, `'w+'`).
  - `'b'` (Binary): Mở file dưới dạng dữ liệu nhị phân (dùng cho file ảnh, file âm thanh, ví dụ `'rb'`, `'wb'`).
• Khuyến nghị: Luôn khai báo `encoding='utf-8'` khi đọc ghi file text chứa tiếng Việt có dấu để tránh lỗi hiển thị font.

2. CÁC PHƯƠNG THỨC ĐỌC FILE:
• `f.read()`: Đọc toàn bộ nội dung của file và trả về dưới dạng một chuỗi văn bản duy nhất (`str`).
• `f.readline()`: Đọc duy nhất 1 dòng tiếp theo của file kể từ vị trí con trỏ hiện tại và trả về dạng chuỗi.
• `f.readlines()`: Đọc toàn bộ tất cả các dòng của file và trả về dưới dạng một **Danh sách** (List) các chuỗi, mỗi chuỗi đại diện cho một dòng (bao gồm cả ký tự xuống dòng `\n`).

3. QUẢN LÝ TÀI NGUYÊN BẰNG CẤU TRÚC 'WITH' (CONTEXT MANAGER):
• Trong lập trình tệp tin, sau khi mở file, ta bắt buộc phải gọi `f.close()` để đóng file giải phóng tài nguyên. Nếu quên đóng, file bị khóa và rò rỉ bộ nhớ.
• Cách viết an toàn nhất là sử dụng từ khóa `with`. Cấu trúc này hoạt động như một Context Manager, đảm bảo file sẽ tự động được đóng an toàn khi khối lệnh kết thúc, ngay cả khi có ngoại lệ xảy ra đột ngột trong thân block.

## Ví dụ
```python
# Ghi dữ liệu vào file
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Dòng thứ nhất\n")
    f.write("Dòng thứ hai\n")

# Đọc dữ liệu an toàn với with
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        print(f"Dòng {idx+1}: {line.strip()}") 
        # dùng strip() để loại bỏ ký tự \n ở cuối dòng khi in

# File tự động đóng khi thoát khỏi block with
```

## Ghi nhớ
- Hãy làm quen với cú pháp và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Sử dụng Modules & Thư viện

## Tóm tắt
Module trong Python là một file chứa các định nghĩa hàm, lớp, biến và mã nguồn Python, giúp phân tách mã nguồn thành các phần nhỏ để dễ quản lý và tái sử dụng. 1. CÁC CÚ PHÁP IMPORT MODULES:

## Khái niệm
Module trong Python là một file chứa các định nghĩa hàm, lớp, biến và mã nguồn Python, giúp phân tách mã nguồn thành các phần nhỏ để dễ quản lý và tái sử dụng.

1. CÁC CÚ PHÁP IMPORT MODULES:
• `import math`: Nhập toàn bộ module. Khi gọi hàm phải đi kèm tiền tố tên module (Ví dụ: `math.ceil()`).
• `from math import sqrt, pi`: Chỉ nhập các thành phần cụ thể cần sử dụng. Khi gọi sẽ dùng trực tiếp tên hàm mà không cần tiền tố (Ví dụ: `sqrt()`).
• `import math as m`: Nhập module và đặt tên đại diện ngắn gọn (alias). Gọi qua tiền tố mới (Ví dụ: `m.ceil()`).

2. MỘT SỐ MODULE TIÊU CHUẨN CỐT LÕI:
• Module `math`: Cung cấp các hàm toán học chuyên sâu.
  - `math.ceil(x)`: Làm tròn lên số nguyên gần nhất (Ví dụ: `math.ceil(4.2)` trả về `5`).
  - `math.floor(x)`: Làm tròn xuống số nguyên gần nhất (Ví dụ: `math.floor(4.8)` trả về `4`).
  - `math.sqrt(x)`: Tính căn bậc hai của x.
  - `math.pi`: Hằng số Pi (khoảng 3.14159).
• Module `random`: Sinh các giá trị ngẫu nhiên.
  - `random.random()`: Trả về số thực ngẫu nhiên từ `0.0` đến dưới `1.0`.
  - `random.randint(a, b)`: Trả về một số nguyên ngẫu nhiên trong đoạn `[a, b]` (bao gồm cả hai điểm mút `a` và `b`).
  - `random.choice(sequence)`: Trả về ngẫu nhiên 1 phần tử từ tập hợp sequence (List, Tuple).
• Module `os` và `sys`: Tương tác với hệ điều hành, đường dẫn file, thư mục và tham số hệ thống.
• Module `datetime`: Thao tác xử lý thông tin ngày tháng năm và thời gian thực.

3. QUẢN LÝ LƯ VIỆN BÊN NGOÀI BẰNG PIP:
• Pip (Python Package Index) là công cụ quản lý package tiêu chuẩn của Python, dùng để cài đặt các thư viện từ cộng đồng như NumPy, Pandas, Matplotlib.

## Ví dụ
```python
import math
from random import randint, choice

# Thao tác làm tròn số
val = 4.2
print("Làm tròn lên (ceil):", math.ceil(val))   # Output: 5
print("Làm tròn xuống (floor):", math.floor(val)) # Output: 4

# Sinh số ngẫu nhiên
rand_num = randint(1, 10) # ngẫu nhiên từ 1 đến 10
print("Số ngẫu nhiên:", rand_num)

items = ["Táo", "Cam", "Banana"]
selected = choice(items)
print("Trái cây ngẫu nhiên:", selected)
```

## Ghi nhớ
- Hãy làm quen với cú pháp và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Thư viện tính toán NumPy (NumPy)

## Tóm tắt
NumPy (Numerical Python) là thư viện nền tảng cho tính toán khoa học, phân tích số liệu và tối ưu hóa các phép toán ma trận đại số tuyến tính trong Python. 1. KIỂU DỮ LIỆU ĐẶC TRƯNG NDARRAY:

## Khái niệm
NumPy (Numerical Python) là thư viện nền tảng cho tính toán khoa học, phân tích số liệu và tối ưu hóa các phép toán ma trận đại số tuyến tính trong Python.

1. KIỂU DỮ LIỆU ĐẶC TRƯNG NDARRAY:
• ndarray (N-dimensional array): Mảng đa chiều của NumPy.
• Đặc điểm:
  - Khác với List của Python có thể chứa nhiều kiểu dữ liệu hỗn hợp, ndarray yêu cầu tất cả phần tử trong mảng bắt buộc phải có CÙNG KIỂU DỮ LIỆU (homogeneous).
  - Tốc độ xử lý tính toán cực nhanh, tốn ít bộ nhớ hơn nhiều so với List vì NumPy được viết trên nền tảng ngôn ngữ C và tối ưu hóa lưu trữ liên tục trên RAM, loại bỏ các vòng lặp for thủ công của Python.
• Thuộc tính quan trọng:
  - `.shape`: Trả về một tuple mô tả kích thước các chiều của mảng (ví dụ: mảng 2 hàng 3 cột có shape là `(2, 3)`).
  - `.ndim`: Trả về số chiều của mảng (mảng 1 chiều ndim = 1, ma trận 2 chiều ndim = 2).
  - `.dtype`: Trả về kiểu dữ liệu của các phần tử trong mảng (ví dụ: `int32`, `float64`).

2. CÁC PHƯƠNG THỨC KHỞI TẠO MẢNG:
• `np.array(object)`: Khởi tạo mảng từ một danh sách List hoặc Tuple của Python.
• `np.zeros(shape)`: Tạo mảng chứa toàn số 0 với kích thước chỉ định.
• `np.ones(shape)`: Tạo mảng chứa toàn số 1.
• `np.arange(start, stop, step)`: Tạo dãy số tăng dần tương tự range() của Python nhưng trả về đối tượng mảng ndarray.
• `np.linspace(start, stop, num)`: Tạo dãy số gồm đúng `num` phần tử phân bố đều nhau trong khoảng từ `start` đến `stop` (bao gồm cả điểm mút stop).

3. PHÉP TOÁN TOÁN TỬ VÀ NHÂN MA TRẬN:
• Phép toán cơ bản (+, -, *, /) mặc định được thực thi trên từng phần tử tương ứng (**element-wise operations**). Ví dụ: `arr * 2` sẽ nhân tất cả phần tử trong mảng với 2.
• Nhân hai ma trận thực tế trong đại số tuyến tính: Bắt buộc sử dụng toán tử `@` hoặc hàm `np.dot(m1, m2)`. Sử dụng phép nhân `*` thông thường giữa 2 ma trận chỉ là nhân các phần tử cùng vị trí với nhau (element-wise), không phải nhân ma trận.

## Ví dụ
```python
import numpy as np

# Khởi tạo mảng 2 chiều (ma trận) từ List lồng nhau
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Mảng ndarray:\n", matrix)
print("Số chiều (ndim):", matrix.ndim)    # Output: 2
print("Kích thước (shape):", matrix.shape) # Output: (2, 3)
print("Kiểu dữ liệu (dtype):", matrix.dtype) # Output: int32 hoặc int64

# Phép toán element-wise vs Nhân ma trận đại số
arr = np.array([1, 2, 3])
print("Nhân element-wise arr * 2:", arr * 2) # Output: [2, 4, 6]

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[2, 0], [1, 2]])
print("Nhân ma trận đại số m1 @ m2:\n", m1 @ m2)
# Output: [[4, 4], [10, 8]]
```

## Ghi nhớ
- Hãy làm quen với cú pháp và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Thư viện phân tích dữ liệu Pandas

## Tóm tắt
Pandas là thư viện mã nguồn mở mạnh mẽ chuyên dùng để thao tác, làm sạch, phân tích và xử lý các tập dữ liệu có cấu trúc dưới dạng bảng biểu. 1. HAI CẤU TRÚC DỮ LIỆU CỐT LÕI:

## Khái niệm
Pandas là thư viện mã nguồn mở mạnh mẽ chuyên dùng để thao tác, làm sạch, phân tích và xử lý các tập dữ liệu có cấu trúc dưới dạng bảng biểu.

1. HAI CẤU TRÚC DỮ LIỆU CỐT LÕI:
• Series: Cấu trúc dữ liệu mảng 1 chiều có nhãn chỉ mục (index) đi kèm.
• DataFrame: Bảng dữ liệu 2 chiều (gồm nhiều dòng và cột), tương tự như bảng SQL hoặc trang tính Excel.
  - Các cách khởi tạo DataFrame:
    1. Từ danh sách các từ điển (List of Dictionaries): Mỗi từ điển đại diện cho một dòng dữ liệu. `dicts = [{'a':10, 'b':20}, {'a':5, 'b':10, 'c':20}]`. Pandas tự động quét tất cả các key để tạo danh sách cột chung (gồm 3 cột 'a', 'b', 'c').
    2. Từ từ điển của các danh sách (Dictionary of Lists): Mỗi key là tên cột, value là list dữ liệu của cột đó.
• Thuộc tính chính:
  - `.shape`: Trả về tuple (số dòng, số cột) của DataFrame.
  - `.size`: Trả về tổng số ô dữ liệu (bằng số dòng x số cột).
• Hàm tải dữ liệu:
  - `pd.read_csv('file.csv')`: Đọc file CSV và trả về một DataFrame.

2. CÁC THAO TÁC TRÊN DATAFRAME:
• Truy cập dữ liệu (loc vs iloc):
  - `.loc[label]`: Lọc dòng/cột dựa vào tên nhãn chuỗi.
  - `.iloc[index]`: Lọc dòng/cột dựa vào chỉ mục số nguyên vị trí (integer location).
• Khái niệm Trục (axis):
  - `axis = 0` (hoặc `axis = 'index'`): Đại diện cho các **Hàng** (Rows).
  - `axis = 1` (hoặc `axis = 'columns'`): Đại diện cho các **Cột** (Columns).
• Xóa hàng hoặc cột:
  - Sử dụng phương thức `.drop(labels, axis)`: Không thay đổi dataframe gốc mà trả về bản sao (muốn xóa trực tiếp phải set `inplace=True`). Để xóa các cột, bắt buộc set `axis=1` (Ví dụ: `df.drop(['Name', 'Class'], axis=1)`).
  - Từ khóa `del`: Dùng để xóa trực tiếp một cột ngay trên DataFrame gốc (Ví dụ: `del df['fee']`).
• Chuyển vị (Transpose):
  - Sử dụng `.T` để đổi hàng thành cột và ngược lại.
• Hợp nhất (Merge):
  - Hàm `pd.merge(df1, df2)` dùng để gộp dữ liệu từ 2 dataframe dựa trên các cột khóa chung (tương tự SQL JOIN).
• Biểu đồ (Plotting):
  - Pandas tích hợp trực tiếp với Matplotlib thông qua `.plot()`. Các biểu đồ phổ biến: `line` (biểu đồ đường - xem sự thay đổi theo thời gian), `bar` (biểu đồ cột), `hist` (biểu đồ tần suất), `pie` (biểu đồ tròn).

## Ví dụ
```python
import pandas as pd

# Khởi tạo DataFrame từ List of Dicts
dicts = [{'a': 10, 'b': 20}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(dicts)
print("DataFrame gốc:\n", df)
print("Kích thước (shape):", df.shape) # Output: (2, 3) - 2 hàng, 3 cột
print("Tổng số ô (size):", df.size)   # Output: 6

# Lọc bằng iloc (dòng đầu tiên, cột đầu tiên)
print("Phần tử ở dòng 0 cột 0:", df.iloc[0, 0]) # Output: 10.0

# Xóa cột bằng del và drop
del df['c'] # Xóa trực tiếp cột 'c'
print("Sau khi del cột c:\n", df)

df_dropped = df.drop(['b'], axis=1) # Trả về DF mới không có cột 'b'
print("Sau khi drop cột b:\n", df_dropped)

# Chuyển vị
print("Ma trận chuyển vị (df.T):\n", df.T)
```

## Ghi nhớ
- Hãy làm quen với cú pháp và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Biểu thức chính quy (Regular Expressions)

## Tóm tắt
Regular Expressions (Regex) là công cụ cực kỳ mạnh mẽ dùng để tìm kiếm, trích xuất và thao tác các chuỗi ký tự dựa trên một khuôn mẫu (pattern) xác định trước. 1. THƯ VIỆN RE TRONG PYTHON VÀ CÁC HÀM CỐT LÕI:

## Khái niệm
Regular Expressions (Regex) là công cụ cực kỳ mạnh mẽ dùng để tìm kiếm, trích xuất và thao tác các chuỗi ký tự dựa trên một khuôn mẫu (pattern) xác định trước.

1. THƯ VIỆN RE TRONG PYTHON VÀ CÁC HÀM CỐT LÕI:
• `re.match(pattern, string)`: 
  - Chỉ kiểm tra xem chuỗi có khớp với mẫu NGAY TỪ ĐẦU chuỗi hay không. Nếu ở giữa hoặc ở cuối khớp nhưng ở đầu không khớp thì vẫn trả về `None`.
• `re.search(pattern, string)`:
  - Quét toàn bộ chuỗi từ trái qua phải và trả về vị trí khớp đầu tiên tìm thấy dưới dạng một đối tượng Match. Trả về `None` nếu không tìm thấy.
• `re.findall(pattern, string)`:
  - Tìm kiếm toàn bộ các chuỗi con khớp với mẫu trong chuỗi và trả về kết quả dưới dạng một **Danh sách** (List) các chuỗi.
• `re.sub(pattern, replacement, string)`:
  - Tìm kiếm các chuỗi con khớp với mẫu và thay thế chúng bằng chuỗi `replacement`.

2. CÁC KÝ TỰ ĐẠI DIỆN VÀ ĐỊNH LƯỢNG THƯỜNG DÙNG:
• Ký tự đặc biệt đại diện:
  - `.` : Khớp với bất kỳ ký tự nào ngoại trừ ký tự xuống dòng `\n`.
  - `^` : Khớp ở điểm bắt đầu của chuỗi.
  - `$` : Khớp ở điểm kết thúc của chuỗi.
  - `\d` : Khớp với chữ số tương đương `[0-9]`.
  - `\D` : Khớp với ký tự không phải chữ số (ngược lại của `\d`).
  - `\w` : Khớp với ký tự chữ và số cùng dấu gạch dưới `_` (tương đương `[a-zA-Z0-9_]`).
  - `\W` : Khớp với ký tự không phải chữ và số (ngược lại của `\w`).
  - `\s` : Khớp với ký tự khoảng trắng (space, tab, newline).
  - `\S` : Khớp với ký tự không phải khoảng trắng.
• Bộ định lượng lặp lại (Quantifiers):
  - `*` : Khớp 0 hoặc nhiều lần của ký tự đứng trước.
  - `+` : Khớp 1 hoặc nhiều lần của ký tự đứng trước.
  - `?` : Khớp 0 hoặc 1 lần (tùy chọn).
  - `{n}` : Khớp đúng `n` lần xuất hiện.
  - `{n,m}` : Khớp từ `n` đến `m` lần xuất hiện.

## Ví dụ
```python
import re

text = "Liên hệ qua: 0912-345-678 hoặc 0987-654-321"

# 1. re.findall để trích xuất toàn bộ số điện thoại
# Định dạng: 4 số - 3 số - 3 số
phone_pattern = r'\d{4}-\d{3}-\d{3}'
phones = re.findall(phone_pattern, text)
print("Danh sách sđt tìm thấy:", phones) 
# Output: ['0912-345-678', '0987-654-321']

# 2. re.sub để thay thế bảo mật thông tin
masked = re.sub(phone_pattern, "XXXX-XXX-XXX", text)
print("Chuỗi bảo mật:", masked)
# Output: Liên hệ qua: XXXX-XXX-XXX hoặc XXXX-XXX-XXX

# 3. re.match vs re.search
text2 = "Chào bạn, hãy gọi 0912-345-678"
# re.match trả về None vì số điện thoại không nằm ở đầu chuỗi
print("match:", re.match(phone_pattern, text2)) # Output: None
# re.search tìm thấy vì nó quét toàn bộ chuỗi
match_obj = re.search(phone_pattern, text2)
if match_obj:
    print("search thấy:", match_obj.group()) # Output: 0912-345-678
```

## Ghi nhớ
- Hãy làm quen với cú pháp và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

