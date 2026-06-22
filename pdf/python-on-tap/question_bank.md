# NGÂN HÀNG CÂU HỎI ÔN TẬP PYTHON

Tổng số câu hỏi: 144

## Chương 1: Khái niệm cơ bản & Nhập xuất dữ liệu (12 câu)

### Câu 1 [Đọc code]
Output của đoạn code sau là gì?: print('Hello, world!'); print("H")

- A. Hello world! H
- B. H
- C. Hello world! H (H được in ở hàng mới)
- D. Error

* **Đáp án đúng:** C
* **Giải thích:** Hàm print() trong Python tự động thêm ký tự xuống dòng '\n' ở cuối kết quả in ra trừ khi được tùy chỉnh tham số end.

### Câu 2 [Lý thuyết]
Đâu là kiểu dữ liệu số trong Python?

- A. Integer
- B. Complex
- C. Boolean
- D. Tất cả các phương án trên.

* **Đáp án đúng:** D
* **Giải thích:** Trong Python, Integer và Complex là các kiểu dữ liệu số. Kiểu Boolean cũng được coi là kiểu số vì True đại diện cho 1 và False đại diện cho 0.

### Câu 3 [Lý thuyết]
Trong số các phép gán sau đây, phép gán nào sẽ gây ra lỗi?

- A. a = b = c = 89
- B. a = 6, b = 8
- C. a, b, c = 1, 2, 3
- D. Không có phép gán nào trên đúng.

* **Đáp án đúng:** B
* **Giải thích:** Trong Python, cú pháp gán đồng thời cho hai biến riêng biệt phải dùng dấu phẩy như a, b = 6, 8. Biểu thức a = 6, b = 8 không hợp lệ và gây ra Syntax Error.

### Câu 5 [Tính toán]
Giá trị của biểu thức này là gì? 22% 3.0

- A. 7
- B. 1
- C. 1.0
- D. 7.0

* **Đáp án đúng:** C
* **Giải thích:** Phép chia dư 22 % 3 bằng 1. Vì số chia là số thực (3.0), kết quả của phép toán cũng được ép kiểu tự động thành số thực (1.0).

### Câu 7 [Đọc code]
Đoạn mã sau in ra gì trên console? print("lion" == "cat" or 99 != 88)

- A. False
- B. True
- C. ValueError xảy ra
- D. TypeError xảy ra

* **Đáp án đúng:** B
* **Giải thích:** Vế 1 'lion' == 'cat' là False. Vế 2 99 != 88 là True. False or True trả về kết quả True.

### Câu 31 [Lý thuyết]
Biến nào sau đây có tên đặt KHÔNG hợp lệ trong Python?

- A. _my_var
- B. myVar2
- C. 2my_var
- D. my_var_name

* **Đáp án đúng:** C
* **Giải thích:** Tên biến trong Python không được bắt đầu bằng chữ số.

### Câu 32 [Tính toán]
Kết quả của phép chia lấy phần nguyên 22 // 3 là gì?

- A. 7
- B. 7.33
- C. 1
- D. 7.0

* **Đáp án đúng:** A
* **Giải thích:** Toán tử // thực hiện phép chia lấy phần nguyên, kết quả là 7.

### Câu 33 [Lý thuyết]
Hàm input() trong Python mặc định trả về dữ liệu kiểu nào?

- A. int
- B. float
- C. str
- D. list

* **Đáp án đúng:** C
* **Giải thích:** Hàm input() luôn trả về dữ liệu kiểu chuỗi (string/str). Muốn dùng kiểu khác phải ép kiểu.

### Câu 34 [Lý thuyết]
Để in ra màn hình mà không tự động xuống dòng, ta cần gán tham số nào của hàm print()?

- A. newline=''
- B. end=''
- C. sep=''
- D. flush=True

* **Đáp án đúng:** B
* **Giải thích:** Tham số end quyết định ký tự in ra cuối chuỗi, gán end='' để không xuống dòng.

### Câu 35 [Lý thuyết]
Toán tử nào được dùng để tính lũy thừa trong Python?

- A. ^
- B. **
- C. pow
- D. exp

* **Đáp án đúng:** B
* **Giải thích:** Trong Python, toán tử ** biểu thị phép lũy thừa (ví dụ 2 ** 3 = 8).

### Câu 107 [Lý thuyết]
Có bao nhiêu khai báo xâu kí tự hợp lệ trong số các khai báo sau?
1) “123_@##”
2) “hoa hau”
3) “346h7g84jd”
4) python
5) “01028475”
6) 123456

- A. 5
- B. 6
- C. 4
- D. 3

* **Đáp án đúng:** C
* **Giải thích:** Các khai báo 1, 2, 3, 5 là các xâu kí tự hợp lệ vì chúng được bao quanh bởi cặp nháy kép. Khai báo 4 (python) được hiểu là một biến, còn 6 (123456) là một số nguyên.

### Câu 108 [Tính toán]
Chuỗi “1234%^^%TFRESDRG” trong Python có độ dài bằng bao nhiêu?

- A. 16
- B. 17
- C. 18
- D. 15

* **Đáp án đúng:** A
* **Giải thích:** Chuỗi '1234%^^%TFRESDRG' có đúng 16 ký tự kể cả chữ, số và ký tự đặc biệt.

---

## Chương 2: Cấu trúc rẽ nhánh & Kiểu dữ liệu tập hợp (19 câu)

### Câu 4 [Lý thuyết]
Đâu là kiểu dữ liệu mutable (có thể sửa đổi phần tử)?

- A. String
- B. Tuple
- C. List
- D. Tất cả các phương án trên.

* **Đáp án đúng:** C
* **Giải thích:** Kiểu List là mutable. String và Tuple là các kiểu dữ liệu immutable (bất biến), không thể thay đổi giá trị của phần tử sau khi đã tạo.

### Câu 6 [Lý thuyết]
D = [1, 23, 'hello', 1] thuộc kiểu dữ liệu nào?

- A. List
- B. Dictionary
- C. Array
- D. Tuple

* **Đáp án đúng:** A
* **Giải thích:** Dãy giá trị được khai báo trong cặp ngoặc vuông [] đại diện cho kiểu dữ liệu List trong Python.

### Câu 8 [Đọc code]
Kết quả của biểu thức này sẽ là gì: print('p' + 'q' if '12'.isdigit() else 'r' + 's')

- A. pq
- B. rs
- C. pqrs
- D. pq12
- E. lỗi

* **Đáp án đúng:** A
* **Giải thích:** '12'.isdigit() trả về True, do đó biểu thức rẽ nhánh inline sẽ trả về 'p' + 'q' = 'pq'.

### Câu 9 [Đọc code]
Đọc đoạn code sau và cho biết kết quả in ra:
a = True
b = False
c = True
if not a or b:
    print ("a")
elif not a or not b and c:
    print ("b")
elif not a or b or not b and a:
    print ("c")
else:
    print ("d")

- A. a
- B. b
- C. c
- D. d

* **Đáp án đúng:** B
* **Giải thích:** - not a or b = not True or False = False.
- not a or not b and c = False or True and True = False or True = True. Nhánh elif thứ nhất thỏa mãn nên in ra 'b'.

### Câu 36 [Lý thuyết]
Phát biểu nào sau đây là ĐÚNG về kiểu dữ liệu Tuple trong Python?

- A. Tuple có thể thay đổi phần tử sau khi tạo.
- B. Tuple sử dụng ngoặc vuông [] để khai báo.
- C. Tuple là kiểu dữ liệu bất biến (immutable).
- D. Tuple không cho phép chứa các kiểu dữ liệu khác nhau.

* **Đáp án đúng:** C
* **Giải thích:** Tuple là một dãy phần tử bất biến (immutable) và được định nghĩa bằng cặp ngoặc đơn ().

### Câu 37 [Lý thuyết]
Phương thức nào dùng để thêm một phần tử vào cuối một List trong Python?

- A. add()
- B. append()
- C. insert()
- D. push()

* **Đáp án đúng:** B
* **Giải thích:** Hàm append() thêm phần tử vào vị trí cuối cùng của List.

### Câu 38 [Lý thuyết]
Khóa (key) của một Dictionary trong Python bắt buộc phải thuộc kiểu dữ liệu nào?

- A. Chỉ được là số nguyên
- B. Phải thuộc kiểu mutable
- C. Phải thuộc kiểu bất biến (immutable)
- D. Bất kỳ kiểu dữ liệu nào

* **Đáp án đúng:** C
* **Giải thích:** Key của Dictionary phải băm được (hashable), nghĩa là phải thuộc kiểu bất biến (immutable) như int, float, string, tuple.

### Câu 39 [Lý thuyết]
Để khai báo một tập hợp Set chứa các phần tử duy nhất, ta sử dụng cặp ngoặc nào?

- A. []
- B. ()
- C. {}
- D. <>

* **Đáp án đúng:** C
* **Giải thích:** Set sử dụng ngoặc nhọn {} tương tự Dictionary nhưng không có các cặp key-value.

### Câu 40 [Lý thuyết]
Làm thế nào để lấy ra danh sách tất cả các key của dictionary `d`?

- A. d.keys()
- B. d.values()
- C. d.items()
- D. d.get_keys()

* **Đáp án đúng:** A
* **Giải thích:** Phương thức d.keys() trả về một view object chứa danh sách các key của dictionary.

### Câu 41 [Đọc code]
Đoạn code sau xuất ra màn hình kết quả gì?
x = [1, 2, 3]
y = x
y.append(4)
print(x)

- A. [1, 2, 3]
- B. [1, 2, 3, 4]
- C. Lỗi TypeError
- D. [4]

* **Đáp án đúng:** B
* **Giải thích:** Vì List là kiểu mutable, phép gán y = x tạo ra một tham chiếu cùng trỏ tới một vùng nhớ. Thay đổi y sẽ trực tiếp thay đổi x.

### Câu 109 [Đọc code]
Cho biết giá trị của x sau khi thực hiện đoạn lệnh sau:
x, a, b = 0, 5, 5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2

- A. 3
- B. 5
- C. 4
- D. 2

* **Đáp án đúng:** A
* **Giải thích:** Vì a = 5 > 0 là True, chương trình đi vào khối if bên trong. Ở đây, b = 5 < 0 là False, và a > 5 cũng là False, do đó nhánh else cuối cùng của khối trong được thực thi: x = x + 3 = 3.

### Câu 110 [Đọc code]
Cho biết kết quả sau khi thực hiện đoạn lệnh sau:
a, b = 12, 5
print('True') if b // a else print('False')

- A. False
- B. Lỗi
- C. True
- D. Tất cả đều sai

* **Đáp án đúng:** A
* **Giải thích:** Phép chia lấy nguyên b // a = 5 // 12 = 0. Trong cấu trúc điều kiện của Python, số 0 tương đương với False, nên câu lệnh rẽ nhánh inline sẽ chạy nhánh else và in ra 'False'.

### Câu 111 [Đọc code]
Cho biết kết quả sau khi thực hiện đoạn lệnh sau:
print('False') if -3 else print('True')

- A. False
- B. Lỗi
- C. True
- D. Tất cả đều sai

* **Đáp án đúng:** A
* **Giải thích:** Bất kỳ số nguyên nào khác 0 (bao gồm cả số âm như -3) đều tương đương với giá trị chân trị True trong Python. Do đó biểu thức 'False' if -3 được chạy và in ra 'False'.

### Câu 112 [Đọc code]
Cho biết kết quả sau khi thực hiện đoạn lệnh sau:
print('False') if None else print('True')

- A. False
- B. Lỗi
- C. True
- D. Tất cả đều sai

* **Đáp án đúng:** C
* **Giải thích:** Đối tượng None đại diện cho giá trị rỗng/không tồn tại và tương đương với False trong biểu thức điều kiện. Do đó câu lệnh rẽ nhánh in ra nhánh else là 'True'.

### Câu 113 [Lý thuyết]
Đoạn lệnh nào dùng để kiểm tra một số tự nhiên n là chẵn hay lẻ?

- A. print('Lẻ') if n % 2 != 0 else print('Chẵn')
- B. print('Lẻ') if n // 2 != 0 else print('Chẵn')
- C. print('Lẻ') if n % 2 == 0 else print('Chẵn')
- D. print('Lẻ') if n // 2 == 0 else print('Chẵn')

* **Đáp án đúng:** A
* **Giải thích:** Số n lẻ khi n % 2 != 0 (số dư khác 0), ngược lại là số chẵn.

### Câu 114 [Lý thuyết]
Phát biểu nào sau đây là ĐÚNG với khối lệnh finally trong cấu trúc try/except/finally?

- A. Chỉ được thực hiện khi không phát sinh lỗi
- B. Luôn được thực hiện bất kể có lỗi xảy ra hay không
- C. Chỉ được thực hiện khi có lỗi xảy ra
- D. Chỉ được thực hiện khi có lỗi ZeroDivisionError

* **Đáp án đúng:** B
* **Giải thích:** Khối lệnh đặt trong finally luôn được thực thi sau khi chạy xong các khối try và except, dùng để giải phóng tài nguyên.

### Câu 115 [Lý thuyết]
Trong Python, cấu trúc try … except … được dùng để làm gì?

- A. Xử lý các ngoại lệ (errors) tránh chương trình bị crash/dừng đột ngột
- B. Kiểm tra cú pháp của chương trình xem có chạy đúng nghiệp vụ không
- C. Để bắt lấy các giá trị đang xử lý trong khối lệnh
- D. Để tối ưu tốc độ thực thi của vòng lặp

* **Đáp án đúng:** A
* **Giải thích:** try ... except giúp bắt lấy các ngoại lệ phát sinh lúc runtime và định nghĩa cách xử lý, tránh dừng ứng dụng đột ngột.

### Câu 116 [Đọc code]
Cho biết kết quả của đoạn chương trình sau:
try:
    print("throw")
except:
    print("except")
finally:
    print("finally")

- A. finally – throw
- B. finally – except
- C. except – finally
- D. throw – finally

* **Đáp án đúng:** D
* **Giải thích:** Khối try thực hiện thành công và in ra 'throw'. Không có lỗi nên khối except bị bỏ qua. Cuối cùng khối finally luôn chạy nên in tiếp 'finally'.

### Câu 117 [Đọc code]
Cho biết kết quả của đoạn chương trình sau:
number = 5.0
try:
    r = 10/number
    print(r)
except:
    print("Oops! Error occurred.")

- A. Oops! Error occurred.
- B. 2.0
- C. 2.0 Oops! Error occurred.
- D. 5.0

* **Đáp án đúng:** B
* **Giải thích:** Phép chia 10 / 5.0 bằng số thực 2.0 và diễn ra thành công không gây lỗi, do đó in ra 2.0.

---

## Chương 3: Cấu trúc lặp (Loops) (18 câu)

### Câu 10 [Lý thuyết]
Câu nào sau đây là vòng lặp for hợp lệ trong Python?

- A. for(i=0; i<n; i++)
- B. for i in range(0,5):
- C. for i in range(0,5)
- D. for i in range(5)

* **Đáp án đúng:** B
* **Giải thích:** Vòng lặp for hợp lệ trong Python phải có từ khóa in, sử dụng range() hoặc tập hợp, và phải kết thúc bằng dấu hai chấm ':'. Phương án D thiếu dấu hai chấm ở cuối.

### Câu 11 [Tính toán]
Trong dãy mã dưới đây, dãy nào sẽ được tạo ra từ dòng mã đã cho? range(5, 0, -2)

- A. 5 4 3 2 1 0 -1
- B. 5 4 3 2 1 0
- C. 5 3 1
- D. Không có trong các lựa chọn trên

* **Đáp án đúng:** C
* **Giải thích:** range(5, 0, -2) sinh ra dãy bắt đầu từ 5, giảm đi 2 mỗi bước và dừng trước 0. Dãy gồm các phần tử: 5, 3, 1.

### Câu 12 [Đọc code]
Đọc đoạn code sau và cho biết kết quả:
output = ""
x = -5
while x < 0:
    x = x + 1
    output = output + str(x) + " "
print(output)

- A. 5 4 3 2 1
- B. -4 -3 -2 -1 0
- C. -5 -4 -3 -2 -1
- D. Đây là vòng lặp vô hạn

* **Đáp án đúng:** B
* **Giải thích:** Mỗi bước lặp tăng x trước: x=-4, output='-4 '. Cứ thế đến khi x=0, output='-4 -3 -2 -1 0 '. Vòng lặp dừng vì 0 < 0 là False.

### Câu 13 [Đọc code]
Output của đoạn chương trình sau:
sum = 0
values = [1,3,5,7]
for number in values:
    sum = sum + number
print(sum)

- A. 4
- B. 0
- C. 7
- D. 16

* **Đáp án đúng:** D
* **Giải thích:** Vòng lặp tính tổng các số trong danh sách values. Sum = 1 + 3 + 5 + 7 = 16.

### Câu 14 [Lý thuyết]
Một câu lệnh ______________ bỏ qua phần còn lại của vòng lặp và nhảy tới câu lệnh ngay sau vòng lặp.

- A. break
- B. continue
- C. if else
- D. pass

* **Đáp án đúng:** A
* **Giải thích:** Câu lệnh break dùng để thoát ngay lập tức khỏi vòng lặp đang chạy và chuyển quyền thực thi sang câu lệnh tiếp sau vòng lặp.

### Câu 42 [Lý thuyết]
Lệnh continue trong vòng lặp có tác dụng gì?

- A. Dừng và thoát hoàn toàn khỏi vòng lặp.
- B. Bỏ qua các câu lệnh còn lại của lượt lặp này và nhảy sang lượt lặp tiếp theo.
- C. Bỏ qua toàn bộ vòng lặp.
- D. Khởi động lại vòng lặp từ đầu.

* **Đáp án đúng:** B
* **Giải thích:** continue kết thúc lượt lặp hiện tại và nhảy tới biểu thức điều kiện (while) hoặc phần tử tiếp theo (for).

### Câu 43 [Lý thuyết]
Câu lệnh pass trong Python được dùng để làm gì?

- A. Thoát khỏi chương trình.
- B. Bỏ qua một lượt lặp.
- C. Làm câu lệnh giữ chỗ trống (placeholder) không thực hiện hành động nào.
- D. Trả về kết quả cho hàm.

* **Đáp án đúng:** C
* **Giải thích:** pass là một null statement, được dùng làm placeholder khi cú pháp yêu cầu phải có lệnh nhưng chưa cần viết logic.

### Câu 44 [Tính toán]
Dãy số nào được tạo ra bởi lệnh `range(1, 10, 3)`?

- A. 1 4 7 10
- B. 1 4 7
- C. 3 6 9
- D. 1 3 5 7 9

* **Đáp án đúng:** B
* **Giải thích:** Dãy số bắt đầu từ 1, tăng 3 đơn vị mỗi bước và kết thúc trước 10, gồm các số 1, 4, 7.

### Câu 45 [Đọc code]
Đoạn code sau chạy bao nhiêu vòng lặp?
i = 0
while i < 5:
    print(i)
    i += 2

- A. 5
- B. 3
- C. 2
- D. Vô hạn

* **Đáp án đúng:** B
* **Giải thích:** Các giá trị của i được in ra lần lượt là 0, 2, 4. Khi i = 6 thì điều kiện 6 < 5 là False, vòng lặp chạy đúng 3 lần.

### Câu 46 [Đọc code]
Đoạn code sau in ra kết quả gì?
for i in range(3):
    if i == 1:
        break
    print(i, end=' ')

- A. 0 1 2
- B. 0 2
- C. 0
- D. 0 1

* **Đáp án đúng:** C
* **Giải thích:** Vòng lặp chạy với i=0, in ra 0. Sau đó i=1, gặp lệnh break nên lập tức thoát khỏi vòng lặp, chỉ in ra số 0.

### Câu 118 [Phân tích]
Đoạn chương trình sau dùng để giải quyết bài toán gì?
t = 0
for i in range(1, 101):
    if(i % 3 == 0 and i % 5 == 0):
        t = t + i
print(t)

- A. Tính tổng các số chia hết cho 3 hoặc 5 trong khoảng từ 1 đến 100
- B. Tính tổng các số chia hết cho 3 hoặc 5 trong khoảng từ 1 đến 101
- C. Tính tổng các số chia hết cho 3 và 5 trong khoảng từ 1 đến 101
- D. Tính tổng các số chia hết cho 3 và 5 trong khoảng từ 1 đến 100

* **Đáp án đúng:** D
* **Giải thích:** range(1, 101) sinh dãy số từ 1 đến 100. Điều kiện i % 3 == 0 and i % 5 == 0 lọc các số đồng thời chia hết cho 3 và 5.

### Câu 119 [Lý thuyết]
Trong các phát biểu sau về cấu trúc lặp, phát biểu nào chưa chính xác?

- A. while là lệnh lặp với số lần lặp chưa biết trước
- B. for là lệnh lặp với số lần xác định trước
- C. Khối lệnh lặp while được thực hiện cho đến khi điều kiện có giá trị >= False
- D. Số lần lặp của lệnh lặp for thường được xác định bởi vùng giá trị hoặc tập hợp được duyệt

* **Đáp án đúng:** C
* **Giải thích:** Trong Python, điều kiện của while được kiểm tra tính chân trị (True/False). Vòng lặp chạy chừng nào điều kiện còn là True (hoặc tương đương True), và dừng khi điều kiện bằng False (hoặc tương đương False), không dùng phép toán so sánh `>= False`.

### Câu 120 [Phân tích]
Cho biết ý nghĩa của biến k sau khi chạy đoạn chương trình sau:
n = int(input('Nhập n <= 1000: '))
k = 0; n = abs(n)
while n != 0:
    n //= 10
    k += 1

- A. k là số chữ số của n
- B. k là chữ số hàng đơn vị của n
- C. k là chữ số lớn nhất của n
- D. k là số chữ số khác 0 của n

* **Đáp án đúng:** A
* **Giải thích:** Vòng lặp thực hiện chia lấy nguyên n cho 10 ở mỗi bước lặp cho đến khi n bằng 0. Mỗi lượt chia tương ứng với việc bớt đi 1 chữ số của n, do đó k ghi nhận số chữ số của n.

### Câu 121 [Đọc code]
Cho biết kết quả của biến x sau khi thực hiện đoạn chương trình sau:
i = 0; x = 0
while i < 10:
    if i % 2 == 0:
        x += 1
    i += 1

- A. 2
- B. 3
- C. 4
- D. 5

* **Đáp án đúng:** D
* **Giải thích:** Vòng lặp duyệt i từ 0 đến 9. Biến x được tăng lên khi i là số chẵn (0, 2, 4, 6, 8). Có đúng 5 số chẵn nên x = 5.

### Câu 122 [Phân tích]
Câu lệnh dưới đây dùng để giải bài toán nào?
while m != n:
    if m > n:
        m = m - n
    else:
        n = n - m

- A. Tìm ước chung lớn nhất UCLN của m và n
- B. Tìm bội chung nhỏ nhất BCNN của m và n
- C. Tìm hiệu nhỏ nhất của m và n
- D. Tìm số dư lớn nhất

* **Đáp án đúng:** A
* **Giải thích:** Đây là thuật toán trừ liên tiếp (thuật toán Euclid) để tìm ước chung lớn nhất của hai số nguyên dương m và n.

### Câu 123 [Đọc code]
Cho biết kết quả của đoạn chương trình sau:
for i in range(20): 
    if i == 10: 
        break
    else: 
        print(i, end = "") 
else: 
    print("*")

- A. 0123456789*
- B. 123456789
- C. 0123456789
- D. 123456789*

* **Đáp án đúng:** C
* **Giải thích:** Vòng lặp in các số từ 0 đến 9. Khi i = 10, lệnh break thực thi và kết thúc vòng lặp ngay lập tức. Khối else của cấu trúc for chỉ chạy khi vòng lặp hoàn thành bình thường (không bị break chặn), nên ký tự '*' không được in ra.

### Câu 124 [Đọc code]
Cho biết kết quả của đoạn chương trình sau:
for i in range(5, 7):
    print(str(i) * 3)

- A. 555 và 666 (in trên hai dòng riêng biệt)
- B. 15 và 18 (in trên hai dòng riêng biệt)
- C. 555 666 777
- D. Lỗi

* **Đáp án đúng:** A
* **Giải thích:** range(5, 7) sinh ra 5 và 6. Lệnh `str(i) * 3` thực hiện lặp lại chuỗi ký tự đó 3 lần, lần lượt in ra '555' và '666' trên các dòng.

### Câu 125 [Tính toán]
Điền vào dấu … để được kết quả in ra là 66 và 44 trên các dòng:
for i in range(6, 0, … ):
    print(str(i) * 2)

- A. 0
- B. None
- C. -2
- D. -1

* **Đáp án đúng:** C
* **Giải thích:** Để tạo ra dãy số bắt đầu từ 6, giảm dần về phía 0 và chỉ chứa các số chẵn (6, 4, dừng trước 0), bước nhảy (step) của range phải là -2.

---

## Chương 4: Hàm & Phạm vi biến (Functions) (18 câu)

### Câu 47 [Lý thuyết]
Từ khóa nào được dùng để định nghĩa một hàm trong Python?

- A. function
- B. func
- C. def
- D. define

* **Đáp án đúng:** C
* **Giải thích:** Python sử dụng từ khóa def để bắt đầu định nghĩa một hàm.

### Câu 48 [Lý thuyết]
Hàm không có câu lệnh return hoặc chỉ gọi return không có tham số thì trả về giá trị gì?

- A. 0
- B. False
- C. None
- D. Rỗng

* **Đáp án đúng:** C
* **Giải thích:** Mặc định nếu không chỉ định giá trị trả về, hàm trong Python sẽ trả về đối tượng None.

### Câu 49 [Lý thuyết]
Làm thế nào để thay đổi giá trị của một biến toàn cục (global variable) ngay trong một hàm?

- A. Khai báo biến đó với từ khóa global ở đầu hàm.
- B. Sử dụng toán tử gán toàn cục := .
- C. Truyền biến đó làm đối số tham chiếu.
- D. Không thể thay đổi được.

* **Đáp án đúng:** A
* **Giải thích:** Từ khóa global báo cho Python biết biến trong hàm là biến toàn cục ngoài phạm vi hàm, cho phép ghi đè.

### Câu 50 [Lý thuyết]
Khai báo `def func(a, b=10):` có ý nghĩa gì?

- A. Tham số b bắt buộc phải truyền giá trị 10.
- B. Tham số b có giá trị mặc định là 10.
- C. Hàm trả về giá trị b là 10.
- D. Lỗi cú pháp.

* **Đáp án đúng:** B
* **Giải thích:** b=10 thiết lập giá trị mặc định cho b. Khi gọi func(5), a nhận 5 và b tự động nhận 10.

### Câu 51 [Lý thuyết]
Tham số hình thức *args trong khai báo hàm dùng để làm gì?

- A. Nhận các đối số dưới dạng một Dictionary.
- B. Nhận một số lượng biến đổi các đối số truyền vào dưới dạng một Tuple.
- C. Chỉ định các đối số bắt buộc phải truyền.
- D. Thiết lập giá trị mặc định cho tham số.

* **Đáp án đúng:** B
* **Giải thích:** *args cho phép hàm nhận một danh sách đối số vị trí tùy chọn và lưu trữ chúng dưới dạng một Tuple.

### Câu 52 [Lý thuyết]
Đối số **kwargs trong khai báo hàm dùng để nhận các đối số dưới dạng cấu trúc dữ liệu nào?

- A. List
- B. Tuple
- C. Dictionary
- D. Set

* **Đáp án đúng:** C
* **Giải thích:** **kwargs nhận các đối số có đặt tên (keyword arguments) dưới dạng một Dictionary.

### Câu 53 [Đọc code]
Đoạn code sau in ra giá trị nào?
def add_item(val, li=[]):
    li.append(val)
    return li

print(add_item(1))
print(add_item(2))

- A. [1] sau đó [2]
- B. [1] sau đó [1, 2]
- C. [1, 2] sau đó [1, 2]
- D. Lỗi biên dịch

* **Đáp án đúng:** B
* **Giải thích:** Giá trị mặc định của đối số chỉ được khởi tạo một lần duy nhất khi định nghĩa hàm. Lần gọi thứ hai tiếp tục sử dụng danh sách cũ.

### Câu 54 [Lý thuyết]
Hàm nặc danh (anonymous function) trong Python được định nghĩa bằng từ khóa nào?

- A. def
- B. anonymous
- C. lambda
- D. inline

* **Đáp án đúng:** C
* **Giải thích:** Từ khóa lambda dùng để định nghĩa các hàm ẩn danh ngắn gọn trên một dòng.

### Câu 55 [Đọc code]
Đoạn code sau xuất ra màn hình kết quả gì?
x = 5
def test():
    x = 10
test()
print(x)

- A. 5
- B. 10
- C. Lỗi UnboundLocalError
- D. None

* **Đáp án đúng:** A
* **Giải thích:** x = 10 bên trong hàm chỉ là một biến cục bộ trùng tên, không ảnh hưởng đến biến toàn cục x bên ngoài vì không khai báo global x.

### Câu 56 [Lý thuyết]
Hàm lambda nào sau đây trả về bình phương của một số x?

- A. lambda x -> x*x
- B. lambda x: x**2
- C. lambda x return x*x
- D. def lambda(x): return x**2

* **Đáp án đúng:** B
* **Giải thích:** Cú pháp của lambda: lambda arguments: expression. Do đó lambda x: x**2 là chính xác.

### Câu 126 [Đọc code]
Chương trình sau ra kết quả bao nhiêu?
def get_sum(num):
    tmp = 0
    for i in num:
        tmp += i
    return tmp
result = get_sum((1, 2, 3, 4, 5))
print(result)

- A. 12
- B. 13
- C. 14
- D. 15

* **Đáp án đúng:** D
* **Giải thích:** Đối số truyền vào hàm get_sum là tuple (1, 2, 3, 4, 5). Hàm thực hiện tính tổng và trả về kết quả 1 + 2 + 3 + 4 + 5 = 15.

### Câu 127 [Phân tích]
Chương trình sau bị lỗi ở dòng lệnh thứ bao nhiêu?
(1) a = "Hello World!"
(2) def say(i):
(3)     return a + i
(4) say(13)
(5) print(a)

- A. Dòng (2)
- B. Dòng (3)
- C. Dòng (4)
- D. Dòng (5)

* **Đáp án đúng:** C
* **Giải thích:** Lỗi xảy ra ở dòng (4) khi thực hiện lời gọi hàm say(13). Bên trong hàm thực hiện phép cộng `a + i` (trong đó a là 'Hello World!' kiểu chuỗi, i là 13 kiểu số nguyên), phép cộng chuỗi với số nguyên này gây ra TypeError.

### Câu 128 [Phân tích]
Chương trình sau bị lỗi ở dòng lệnh thứ bao nhiêu?
(1) def add(a, b):
(2)     x = a + b
(3)     return(x)
(4) add(1, 2)
(5) add(5, 6)

- A. Dòng (2)
- B. Dòng (3)
- C. Dòng (4)
- D. Không lỗi

* **Đáp án đúng:** D
* **Giải thích:** Chương trình được định nghĩa và gọi hàm hoàn toàn hợp lệ, không phát sinh lỗi.

### Câu 129 [Phân tích]
Chương trình sau bị lỗi cú pháp ở dòng lệnh thứ bao nhiêu?
(1) def add(a, b)
(2)     sum = a + b
(3)     return sum

- A. Dòng (1)
- B. Dòng (2)
- C. Dòng (3)
- D. Không lỗi

* **Đáp án đúng:** A
* **Giải thích:** Khai báo hàm ở dòng (1) thiếu dấu hai chấm `:` ở cuối định nghĩa để bắt đầu khối lệnh của hàm.

### Câu 130 [Đọc code]
Chương trình sau hiển thị kết quả như thế nào?
def ham():
    print("Hello")
ham("Sweden")
ham("India")

- A. Sweden, India
- B. Sweden
- C. Hello, Hello
- D. Chương trình bị lỗi

* **Đáp án đúng:** D
* **Giải thích:** Hàm ham() được định nghĩa không nhận tham số nào, nhưng khi gọi lại truyền vào đối số dạng chuỗi ('Sweden', 'India') nên phát sinh lỗi TypeError.

### Câu 131 [Lý thuyết]
Chọn phát biểu ĐÚNG trong các phát biểu sau về hàm:

- A. Lời gọi hàm không có lỗi nếu tham số được truyền chưa có giá trị
- B. Số lượng đối số được truyền vào hàm phải khớp với số tham số trong khai báo của hàm (nếu không có tham số mặc định)
- C. Tham số là giá trị cụ thể được truyền vào khi gọi hàm
- D. Tất cả các phát biểu trên đều đúng

* **Đáp án đúng:** B
* **Giải thích:** Đại lượng khi định nghĩa hàm gọi là tham số (parameter), đại lượng thực tế truyền vào khi gọi hàm gọi là đối số (argument). Số lượng đối số truyền vào phải khớp với tham số khai báo.

### Câu 132 [Lý thuyết]
Phát biểu nào sau đây là SAI về hàm và đối số?

- A. Một hàm khi khai báo chỉ có một tham số nhưng khi gọi hàm có thể truyền vào 2 đối số bất kỳ
- B. Tham số được định nghĩa khi khai báo hàm
- C. Tham số và đối số có một số điểm khác biệt về khái niệm
- D. Khi gọi hàm, các tham số sẽ được truyền giá trị thông qua đối số

* **Đáp án đúng:** A
* **Giải thích:** Nếu định nghĩa hàm chỉ có 1 tham số (không dùng *args), việc gọi hàm với 2 đối số sẽ trực tiếp ném ra lỗi TypeError.

### Câu 133 [Tính toán]
Hoàn thành chương trình kiểm tra số nguyên tố (True - là SNT, False - Không là SNT):
def prime(n):
    c = 0; k = 1
    while(k<n):
        if n%k == 0:
            c = c + 1
        k = k+ 1
    if c == 1:
        return (…)
    else:
        return (…)

- A. True, False
- B. True, True
- C. False, False
- D. False, True

* **Đáp án đúng:** A
* **Giải thích:** Vì vòng lặp chạy k từ 1 đến sát n. Số nguyên tố n chỉ có đúng 1 ước số trong đoạn này là số 1, nên biến đếm c = 1. Khi c == 1, ta trả về True, ngược lại trả về False.

---

## Chương 5: Xử lý chuỗi ký tự (Strings) (18 câu)

### Câu 57 [Tính toán]
Với chuỗi s = 'Programming', biểu thức s[3:6] trả về kết quả nào?

- A. gra
- B. rog
- C. rogr
- D. gram

* **Đáp án đúng:** B
* **Giải thích:** Cắt chuỗi từ chỉ mục 3 (chữ 'r') đến sát chỉ mục 6 (chữ 'r' thứ hai), kết quả thu được là 'rog'.

### Câu 58 [Lý thuyết]
Phương thức nào dùng để loại bỏ các khoảng trắng thừa ở cả hai đầu của chuỗi?

- A. clear()
- B. strip()
- C. clean()
- D. replace()

* **Đáp án đúng:** B
* **Giải thích:** s.strip() xóa bỏ khoảng trắng, dấu tab, dấu xuống dòng ở đầu và cuối chuỗi s.

### Câu 59 [Lý thuyết]
Làm thế nào để kiểm tra một chuỗi con 'sub' có tồn tại trong chuỗi 's' hay không?

- A. s.contains('sub')
- B. 'sub' in s
- C. s.has('sub')
- D. in(s, 'sub')

* **Đáp án đúng:** B
* **Giải thích:** Toán tử in kiểm tra xem một chuỗi con có nằm trong chuỗi lớn hơn hay không, trả về True/False.

### Câu 60 [Lý thuyết]
Phương thức nào dùng để tách một chuỗi thành một danh sách các chuỗi con dựa trên một ký tự phân cách?

- A. split()
- B. join()
- C. divide()
- D. break()

* **Đáp án đúng:** A
* **Giải thích:** s.split() chia chuỗi thành các phần dựa vào ký tự phân tách và trả về một List.

### Câu 61 [Lý thuyết]
Để đảo ngược một chuỗi s trong Python, ta dùng cú pháp lát cắt (slicing) nào?

- A. s[0:-1]
- B. s[::-1]
- C. s[-1:0]
- D. s[reverse]

* **Đáp án đúng:** B
* **Giải thích:** s[::-1] nghĩa là cắt toàn bộ chuỗi với bước nhảy là -1, giúp đảo ngược chuỗi nhanh chóng.

### Câu 62 [Lý thuyết]
Phương thức nào dùng để thay thế tất cả các chuỗi con 'A' bằng 'B' trong chuỗi s?

- A. s.replace('A', 'B')
- B. s.sub('A', 'B')
- C. s.change('A', 'B')
- D. s.swap('A', 'B')

* **Đáp án đúng:** A
* **Giải thích:** replace('old', 'new') trả về một chuỗi mới với các phần cũ được thay thế.

### Câu 63 [Phân tích]
Điều gì xảy ra khi thực thi lệnh: s = 'Hello'; s[0] = 'h'?

- A. Chuỗi s trở thành 'hello'.
- B. Xảy ra lỗi TypeError.
- C. Ký tự 'H' được chuyển thành 'h' nhưng giá trị không đổi.
- D. Lỗi IndexException.

* **Đáp án đúng:** B
* **Giải thích:** Chuỗi trong Python là bất biến (immutable), không cho phép gán lại phần tử qua chỉ mục.

### Câu 64 [Lý thuyết]
Phương thức nào trả về True nếu chuỗi chỉ chứa toàn bộ các ký tự là chữ số?

- A. isalpha()
- B. isdigit()
- C. isnumeric()
- D. Cả B và C đều đúng

* **Đáp án đúng:** D
* **Giải thích:** Cả isdigit() và isnumeric() đều kiểm tra tính chất chữ số của chuỗi, trả về True nếu chuỗi chỉ gồm chữ số.

### Câu 65 [Tính toán]
Kết quả của phép nối chuỗi `'a' * 3` là gì?

- A. 'a3'
- B. 'aaa'
- C. Lỗi TypeError
- D. ['a', 'a', 'a']

* **Đáp án đúng:** B
* **Giải thích:** Toán tử * dùng giữa chuỗi và số nguyên thực hiện phép nhân bản chuỗi đó.

### Câu 66 [Lý thuyết]
Phương thức nào dùng để tìm kiếm vị trí xuất hiện đầu tiên của một chuỗi con và trả về -1 nếu không tìm thấy?

- A. index()
- B. find()
- C. search()
- D. locate()

* **Đáp án đúng:** B
* **Giải thích:** s.find() trả về chỉ mục xuất hiện đầu tiên hoặc -1 nếu không tìm thấy. index() tương tự nhưng ném ra lỗi ValueError.

### Câu 134 [Lý thuyết]
Câu lệnh nào dùng để tính độ dài (số ký tự) của chuỗi s?

- A. len(s)
- B. length(s)
- C. s.len()
- D. s.length()

* **Đáp án đúng:** A
* **Giải thích:** Hàm built-in len() trong Python nhận đối tượng chuỗi và trả về số lượng ký tự của chuỗi đó.

### Câu 135 [Lý thuyết]
Phát biểu nào sau đây là SAI khi nói về chuỗi ký tự trong Python?

- A. Có thể truy cập từng kí tự của chuỗi thông qua chỉ số chỉ mục
- B. Chỉ số chỉ mục bắt đầu từ số 0
- C. Có thể gán để thay đổi trực tiếp từng kí tự của một chuỗi đang có
- D. Python không có kiểu dữ liệu ký tự riêng biệt (chỉ có kiểu chuỗi)

* **Đáp án đúng:** C
* **Giải thích:** Chuỗi ký tự trong Python là bất biến (immutable), không cho phép gán trực tiếp để thay đổi ký tự qua chỉ mục (ví dụ s[0] = 'a' sẽ gây lỗi).

### Câu 136 [Đọc code]
Sau khi thực hiện lệnh sau, biến s2 sẽ có kết quả là gì?
s1 ="3986443"
s2 = ""
for ch in s1:
    if int(ch) % 2 == 0:
        s2 = s2 + ch
print(s2)

- A. 3986443
- B. 8644
- C. 39864
- D. 443

* **Đáp án đúng:** B
* **Giải thích:** Vòng lặp duyệt qua các ký tự của s1, ép kiểu sang số nguyên và chỉ nối các ký tự số chẵn (8, 6, 4, 4) vào s2.

### Câu 137 [Đọc code]
Chương trình sau cho kết quả là bao nhiêu?
name = "Codelearn"; print(name[0])

- A. C
- B. o
- C. c
- D. Lỗi

* **Đáp án đúng:** A
* **Giải thích:** Ký tự đầu tiên của chuỗi 'Codelearn' ở chỉ số index = 0 là ký tự viết hoa 'C'.

### Câu 138 [Đọc code]
Kết quả của chương trình sau là bao nhiêu?
s = "0123145"; s[0] = '8'; print(s[0])

- A. 8
- B. 0
- C. 1
- D. Lỗi

* **Đáp án đúng:** D
* **Giải thích:** Dòng lệnh `s[0] = '8'` báo lỗi TypeError vì chuỗi là immutable, không hỗ trợ phép gán sửa đổi phần tử.

### Câu 139 [Đọc code]
Kết quả của các câu lệnh sau là gì?
s = "12 34 56 ab cd de "
print(s.find(" "))
print(s.find("12"))
print(s.find("34"))

- A. 2, 0, 3
- B. 2, 1, 3
- C. 3, 5, 2
- D. 1, 4, 5

* **Đáp án đúng:** A
* **Giải thích:** find() trả về vị trí xuất hiện đầu tiên của chuỗi con. Khoảng trắng đầu tiên ở vị trí chỉ mục 2. Chuỗi '12' bắt đầu ở vị trí 0. Chuỗi '34' bắt đầu ở vị trí 3.

### Câu 140 [Đọc code]
Lệnh sau trả lại giá trị gì?
print("abcdabcd".find("cd"))
print("abcdabcd".find("cd", 4))

- A. 2, 6
- B. 3, 3
- C. 2, 2
- D. 2, 7

* **Đáp án đúng:** A
* **Giải thích:** - find('cd') tìm kiếm từ đầu, thấy 'cd' tại index 2.
- find('cd', 4) bắt đầu tìm từ vị trí index 4 trở đi, tìm thấy 'cd' tiếp theo ở index 6.

### Câu 141 [Lý thuyết]
Lệnh nào sau đây dùng để tách xâu ký tự thành một danh sách?

- A. split()
- B. join()
- C. remove()
- D. copy()

* **Đáp án đúng:** A
* **Giải thích:** Phương thức split() tách chuỗi thành danh sách các chuỗi con dựa trên ký tự phân cách (mặc định là khoảng trắng).

---

## Chương 6: Xử lý tệp tin (File Handling) (10 câu)

### Câu 67 [Lý thuyết]
Chế độ mở tệp nào sau đây ghi đè lên nội dung cũ nếu tệp đã tồn tại?

- A. 'r'
- B. 'w'
- C. 'a'
- D. 'x'

* **Đáp án đúng:** B
* **Giải thích:** Chế độ 'w' (write) mở tệp để ghi, xóa sạch nội dung cũ của tệp hoặc tạo tệp mới.

### Câu 68 [Lý thuyết]
Để mở một tệp tin văn bản và ghi thêm nội dung vào cuối tệp, ta dùng chế độ mở tệp nào?

- A. 'r'
- B. 'w'
- C. 'a'
- D. 'w+'

* **Đáp án đúng:** C
* **Giải thích:** Chế độ 'a' (append) cho phép ghi dữ liệu nối tiếp vào cuối tệp tin hiện tại.

### Câu 69 [Lý thuyết]
Tại sao việc sử dụng khối lệnh 'with' lại được khuyến khích khi thao tác với tệp tin?

- A. Nó giúp tệp ghi nhanh hơn.
- B. Nó tự động đóng tệp để giải phóng tài nguyên hệ thống khi kết thúc khối lệnh, kể cả khi xảy ra ngoại lệ.
- C. Nó tự động mã hóa tệp tin.
- D. Nó ngăn không cho các chương trình khác đọc tệp.

* **Đáp án đúng:** B
* **Giải thích:** Context manager 'with' tự động gọi phương thức close() giải phóng file khi luồng thực thi đi ra ngoài.

### Câu 70 [Lý thuyết]
Phương thức nào dùng để đọc toàn bộ nội dung của tệp tin thành một chuỗi duy nhất?

- A. read()
- B. readline()
- C. readlines()
- D. readall()

* **Đáp án đúng:** A
* **Giải thích:** f.read() tải toàn bộ nội dung tệp vào một biến kiểu str.

### Câu 71 [Lý thuyết]
Hàm open() mặc định mở tệp ở chế độ nào nếu không truyền tham số mode?

- A. 'w'
- B. 'r'
- C. 'a'
- D. 'rb'

* **Đáp án đúng:** B
* **Giải thích:** Mặc định mode='r' (đọc văn bản) được áp dụng khi gọi hàm open().

### Câu 72 [Lý thuyết]
Phương thức readlines() của tệp tin trả về kiểu dữ liệu nào?

- A. Một chuỗi duy nhất
- B. Một danh sách (List) các chuỗi, mỗi chuỗi là một dòng
- C. Một Iterator
- D. Lỗi

* **Đáp án đúng:** B
* **Giải thích:** readlines() trả về danh sách các dòng văn bản của tệp tin.

### Câu 73 [Lý thuyết]
Muốn ghi một danh sách các chuỗi vào tệp tin mà không cần dùng vòng lặp, ta dùng phương thức nào?

- A. write()
- B. writelines()
- C. writeall()
- D. dump()

* **Đáp án đúng:** B
* **Giải thích:** f.writelines(list_of_strings) nhận một list các chuỗi và ghi chúng tuần tự vào tệp tin.

### Câu 74 [Lý thuyết]
Chế độ mở file 'rb' có ý nghĩa gì?

- A. Đọc tệp văn bản thông thường
- B. Đọc tệp tin ở chế độ nhị phân (binary)
- C. Đọc ghi tệp tin kết hợp
- D. Đọc ngược tệp tin từ dưới lên

* **Đáp án đúng:** B
* **Giải thích:** Ký tự 'b' là binary, 'rb' là đọc tệp tin dưới dạng nhị phân (thường dùng cho ảnh, file nén).

### Câu 75 [Lý thuyết]
Để kiểm tra xem một tệp tin có tồn tại trên đĩa cứng trước khi mở hay không, ta nên dùng module nào?

- A. math
- B. os.path
- C. sys
- D. file

* **Đáp án đúng:** B
* **Giải thích:** Hàm os.path.exists(path) hoặc os.path.isfile(path) kiểm tra sự tồn tại của tệp tin.

### Câu 76 [Lý thuyết]
Phương thức flush() của đối tượng tệp tin dùng để làm gì?

- A. Đóng tệp ngay lập tức.
- B. Ép dữ liệu từ bộ nhớ đệm (buffer) ghi ngay xuống đĩa cứng mà không cần đóng tệp.
- C. Xóa sạch nội dung tệp tin.
- D. Giải phóng bộ nhớ RAM của chương trình.

* **Đáp án đúng:** B
* **Giải thích:** flush() đẩy dữ liệu đang chờ trong buffer ghi trực tiếp xuống file vật lý.

---

## Chương 7: Sử dụng Modules & Thư viện (Modules & Libraries) (13 câu)

### Câu 77 [Lý thuyết]
Lệnh import nào sau đây chỉ nhập hàm sqrt từ module math để gọi trực tiếp?

- A. import math.sqrt
- B. from math import sqrt
- C. import sqrt from math
- D. math.import(sqrt)

* **Đáp án đúng:** B
* **Giải thích:** from module import function cho phép import trực tiếp tên hàm vào global namespace.

### Câu 78 [Lý thuyết]
Hàm nào trong module random dùng để chọn ngẫu nhiên một phần tử từ một danh sách?

- A. random()
- B. choice()
- C. randint()
- D. sample()

* **Đáp án đúng:** B
* **Giải thích:** random.choice(sequence) chọn ngẫu nhiên một phần tử từ chuỗi/danh sách truyền vào.

### Câu 79 [Lý thuyết]
Hàm ceil(x) trong module math dùng để làm gì?

- A. Làm tròn số thực x xuống số nguyên gần nhất.
- B. Làm tròn số thực x lên số nguyên gần nhất.
- C. Tính căn bậc hai của x.
- D. Lấy phần nguyên của số thực x.

* **Đáp án đúng:** B
* **Giải thích:** math.ceil(x) là hàm trần, làm tròn lên số nguyên lớn hơn hoặc bằng x.

### Câu 80 [Lý thuyết]
Hàm random.randint(1, 6) có thể sinh ra các số nguyên nào?

- A. Từ 1 đến 5
- B. Từ 1 đến 6 (bao gồm cả 1 và 6)
- C. Từ 2 đến 5
- D. Các số thực ngẫu nhiên từ 1.0 đến 6.0

* **Đáp án đúng:** B
* **Giải thích:** Hàm randint(a, b) sinh số nguyên ngẫu nhiên trong đoạn [a, b] bao gồm cả hai điểm mút.

### Câu 81 [Lý thuyết]
Để cài đặt một gói thư viện bên thứ ba từ Internet, công cụ dòng lệnh nào được dùng mặc định?

- A. python-install
- B. pip
- C. npm
- D. get-library

* **Đáp án đúng:** B
* **Giải thích:** pip (Python Package Index installer) là trình quản lý gói thư viện chuẩn cho Python.

### Câu 82 [Lý thuyết]
Module nào có sẵn dùng để xử lý dữ liệu ngày tháng và thời gian?

- A. date
- B. datetime
- C. time
- D. calendar

* **Đáp án đúng:** B
* **Giải thích:** datetime là module tiêu chuẩn để làm việc với date, time, timezone.

### Câu 83 [Lý thuyết]
Lệnh `import math as m` có mục đích gì?

- A. Chỉ nhập một phần của module math.
- B. Thiết lập tên đại diện (alias) ngắn gọn cho module math.
- C. Đổi tên module trên đĩa cứng.
- D. Giảm dung lượng RAM khi import.

* **Đáp án đúng:** B
* **Giải thích:** Từ khóa as tạo bí danh để viết code ngắn gọn hơn (m.sqrt() thay vì math.sqrt()).

### Câu 84 [Lý thuyết]
Hàm nào trong module math trả về giá trị tuyệt đối của một số?

- A. abs()
- B. fabs()
- C. absolute()
- D. Cả A và B đều đúng

* **Đáp án đúng:** D
* **Giải thích:** abs() là hàm built-in của Python, còn math.fabs() trả về trị tuyệt đối kiểu số thực float. Cả hai đều dùng được.

### Câu 85 [Lý thuyết]
Làm thế nào để lấy ra danh sách các đối số dòng lệnh truyền vào script Python?

- A. os.argv
- B. sys.argv
- C. sys.args
- D. env.args

* **Đáp án đúng:** B
* **Giải thích:** sys.argv là một danh sách chứa các đối số dòng lệnh truyền vào chương trình Python.

### Câu 86 [Lý thuyết]
Module nào hỗ trợ nén và giải nén các tệp tin lưu trữ định dạng .zip?

- A. compress
- B. zipfile
- C. tarfile
- D. unzip

* **Đáp án đúng:** B
* **Giải thích:** zipfile là module tiêu chuẩn của Python để thao tác tạo và đọc tệp ZIP.

### Câu 142 [Lý thuyết]
Trong một module của Python có thể chứa đựng những thành phần nào?

- A. Các hàm định nghĩa
- B. Các lớp (classes) định nghĩa
- C. Các biến và câu lệnh thực thi
- D. Tất cả các phương án trên

* **Đáp án đúng:** D
* **Giải thích:** Một module đơn giản là tệp tin chứa mã nguồn Python, có thể định nghĩa biến, hàm, class và chạy lệnh.

### Câu 143 [Lý thuyết]
Muốn nạp tất cả thành phần trong module math để sử dụng trực tiếp mà không cần viết tiền tố math., ta dùng cú pháp nào?

- A. from math import *
- B. import math.*
- C. import * from math
- D. from math import all

* **Đáp án đúng:** A
* **Giải thích:** Cú pháp `from math import *` đưa toàn bộ các hàm và biến của module math vào namespace hiện tại để gọi trực tiếp.

### Câu 144 [Lý thuyết]
Thuộc tính tích hợp nào của một module lưu trữ tên của chính module đó?

- A. __name__
- B. __module__
- C. __title__
- D. __class__

* **Đáp án đúng:** A
* **Giải thích:** Thuộc tính __name__ lưu trữ tên của module (ví dụ là '__main__' nếu chạy trực tiếp, hoặc tên module nếu được import).

---

## Chương 8: Thư viện tính toán NumPy (NumPy) (10 câu)

### Câu 87 [Lý thuyết]
Đặc trưng quan trọng nhất của mảng NumPy ndarray so với List của Python là gì?

- A. ndarray có thể chứa các phần tử có kiểu dữ liệu khác nhau.
- B. ndarray yêu cầu tất cả các phần tử phải cùng kiểu dữ liệu (homogeneous) để tối ưu hiệu năng tính toán.
- C. ndarray không hỗ trợ cắt mảng (slicing).
- D. ndarray chậm hơn List thông thường.

* **Đáp án đúng:** B
* **Giải thích:** Mảng ndarray lưu trữ dữ liệu đồng nhất trên các ô nhớ liên tục để tối ưu hóa tính toán song song.

### Câu 88 [Lý thuyết]
Thuộc tính nào của mảng NumPy cho biết kích thước (số dòng, số cột) của nó?

- A. ndim
- B. shape
- C. size
- D. length

* **Đáp án đúng:** B
* **Giải thích:** shape trả về tuple kích thước mảng. size trả về tổng số phần tử. ndim trả về số chiều.

### Câu 89 [Lý thuyết]
Hàm nào dùng để tạo một mảng NumPy chứa toàn bộ giá trị là số 0?

- A. np.array(0)
- B. np.zeros()
- C. np.empty()
- D. np.nulls()

* **Đáp án đúng:** B
* **Giải thích:** np.zeros(shape) tạo mảng chứa toàn số 0 với kích thước chỉ định.

### Câu 90 [Lý thuyết]
Để nhân hai ma trận NumPy theo đúng quy tắc toán học (Matrix Multiplication), ta dùng toán tử nào?

- A. *
- B. @
- C. **
- D. x

* **Đáp án đúng:** B
* **Giải thích:** Toán tử * nhân từng phần tử tương ứng (element-wise), còn toán tử @ thực hiện nhân ma trận đại số tuyến tính.

### Câu 91 [Tính toán]
Hàm np.arange(1, 10, 2) trả về kết quả nào?

- A. [1, 3, 5, 7, 9]
- B. array([1, 3, 5, 7, 9])
- C. [1, 2, 3, 4, 5, 6, 7, 8, 9]
- D. array([1, 2, 3, 4, 5, 6, 7, 8, 9])

* **Đáp án đúng:** B
* **Giải thích:** np.arange() trả về một đối tượng ndarray chứa các số lẻ từ 1 đến 9.

### Câu 92 [Tính toán]
Hàm np.linspace(0, 10, 5) tạo ra mảng gồm bao nhiêu phần tử phân bố đều?

- A. 10 phần tử
- B. 5 phần tử
- C. 50 phần tử
- D. 2 phần tử

* **Đáp án đúng:** B
* **Giải thích:** Tham số thứ 3 của linspace quyết định số lượng phần tử phân bố đều từ điểm đầu đến điểm cuối.

### Câu 93 [Lý thuyết]
Thuộc tính dtype của ndarray cho biết thông tin gì?

- A. Số chiều của mảng.
- B. Kiểu dữ liệu của các phần tử trong mảng.
- C. Tổng kích thước mảng.
- D. Phương thức lưu trữ dữ liệu.

* **Đáp án đúng:** B
* **Giải thích:** dtype (data type) chỉ định kiểu dữ liệu của các phần tử trong mảng NumPy (ví dụ int64, float32).

### Câu 94 [Phân tích]
Với mảng 2 chiều a có kích thước (3, 4), lệnh `a.reshape(2, 6)` sẽ:

- A. Thay đổi kích thước mảng a thành 2 hàng, 6 cột mà không đổi dữ liệu.
- B. Trả về lỗi vì không tương thích số phần tử.
- C. Xóa bớt phần tử thừa.
- D. Xoay ma trận 90 độ.

* **Đáp án đúng:** A
* **Giải thích:** reshape đổi hình dạng mảng miễn là tổng số phần tử không đổi (3*4 = 2*6 = 12).

### Câu 95 [Lý thuyết]
Làm thế nào để tính tổng tất cả các phần tử của mảng a trong NumPy?

- A. a.sum()
- B. np.sum(a)
- C. sum(a)
- D. Cả A và B đều đúng

* **Đáp án đúng:** D
* **Giải thích:** Cả phương thức thành viên a.sum() và hàm np.sum(a) đều tính tổng tất cả phần tử của mảng ndarray.

### Câu 96 [Tính toán]
Để lấy ra phần tử ở dòng thứ 2, cột thứ 3 của mảng 2 chiều a, ta dùng cú pháp nào?

- A. a[2, 3]
- B. a[1, 2]
- C. a[2][3]
- D. a[1][2]

* **Đáp án đúng:** B
* **Giải thích:** Chỉ mục trong Python bắt đầu từ 0. Dòng thứ 2 ứng với index 1, cột thứ 3 ứng với index 2. Cú pháp a[1, 2] tối ưu hơn a[1][2].

---

## Chương 9: Thư viện phân tích dữ liệu Pandas (16 câu)

### Câu 15 [Lý thuyết]
Chúng ta có thể thêm một hàng mới vào DataFrame bằng cách sử dụng phương thức _____________.

- A. rloc[ ]
- B. loc[ ]
- C. iloc[ ]
- D. Không có trong số các phương thức trên.

* **Đáp án đúng:** B
* **Giải thích:** Phương thức loc[] cho phép truy xuất và gán giá trị cho một dòng mới dựa trên nhãn chỉ mục: df.loc[new_label] = values.

### Câu 16 [Đọc code]
Đoạn mã sau tạo một dataframe có tên là 'D1' với ___________ cột.
import pandas as pd
dicts = [{'a':10, 'b':20}, {'a':5, 'b':10, 'c':20}]
D1 = pd.DataFrame(dicts)

- A. 1
- B. 2
- C. 3
- D. 4

* **Đáp án đúng:** C
* **Giải thích:** Pandas sẽ quét qua các keys của tất cả các dicts để tạo thành danh sách các cột. Các cột gồm 'a', 'b' và 'c'. Tổng cộng 3 cột.

### Câu 17 [Lý thuyết]
Chúng ta có thể tạo DataFrame từ _____?

- A. Mảng Numpy (Numpy arrays)
- B. Danh sách các từ điển (List of Dictionaries)
- C. Từ điển của các danh sách (Dictionary of Lists)
- D. Tất cả các phương án trên

* **Đáp án đúng:** D
* **Giải thích:** Pandas DataFrame cực kỳ linh hoạt, có thể được tạo từ Numpy array, List of Dicts, Dict of Lists hoặc Series.

### Câu 18 [Lý thuyết]
Trong DataFrame, tham số axis=0 đại diện cho:

- A. Các hàng (Rows)
- B. Các cột (Columns)
- C. Cả hai hàng và cột
- D. Không phải trong số các lựa chọn này

* **Đáp án đúng:** A
* **Giải thích:** Trong Pandas, axis=0 dùng để chỉ các hàng (rows), còn axis=1 dùng để chỉ các cột (columns).

### Câu 19 [Lý thuyết]
Hàm nào sau đây được sử dụng để tải dữ liệu từ tệp CSV vào DataFrame?

- A. read.csv( )
- B. readcsv( )
- C. read_csv( )
- D. Read_csv( )

* **Đáp án đúng:** C
* **Giải thích:** read_csv() là hàm tích hợp sẵn của thư viện Pandas để đọc file CSV và lưu vào cấu trúc DataFrame.

### Câu 20 [Lý thuyết]
Để xóa một cột, tham số axis của hàm drop( ) được gán giá trị _____________?

- A. 0
- B. 1
- C. 2
- D. 3

* **Đáp án đúng:** B
* **Giải thích:** Khi gọi hàm drop() để xóa cột, ta cần thiết lập axis=1 để báo cho Pandas biết rằng cần tìm nhãn đó ở trục cột.

### Câu 21 [Lý thuyết]
Phương thức nào được sử dụng để xóa hàng hoặc cột trong DataFrame?

- A. delete( )
- B. del( )
- C. drop( )
- D. Không có trong số các phương án trên

* **Đáp án đúng:** C
* **Giải thích:** drop() là phương thức tiêu chuẩn dùng để xóa hàng hoặc cột của DataFrame mà không thay đổi trực tiếp (trừ khi dùng inplace=True).

### Câu 22 [Lý thuyết]
Viết cú pháp để chuyển vị (transpose) DataFrame.

- A. Df1=Df1.Tranpose()
- B. Df2=Df1.Transpose()
- C. Df1=Df1.T
- D. Df1.T=Df1

* **Đáp án đúng:** C
* **Giải thích:** Thuộc tính .T viết tắt của Transpose, được dùng để chuyển vị dòng thành cột và ngược lại.

### Câu 23 [Phân tích]
df = df.drop(['Name', 'Class', 'Rollno'], axis = 1) #df là một đối tượng DataFrame. Câu lệnh trên sẽ làm gì?

- A. xóa ba cột có nhãn ‘Name’, ‘Class’ và ‘Rollno’
- B. xóa ba hàng có nhãn ‘Name’, ‘Class’ và ‘Rollno’
- C. xóa bất kỳ ba cột nào
- D. trả về lỗi

* **Đáp án đúng:** A
* **Giải thích:** Lệnh drop với một danh sách các nhãn và axis=1 sẽ tìm và xóa các cột có tên tương ứng.

### Câu 24 [Lý thuyết]
Trong số các thuộc tính sau của DataFrame, thuộc tính nào hiển thị kích thước dạng tuple (số dòng, số cột)?

- A. shape
- B. size
- C. dimension
- D. values

* **Đáp án đúng:** A
* **Giải thích:** Thuộc tính shape trả về một tuple chứa (số dòng, số cột) của DataFrame. size trả về tổng số phần tử.

### Câu 25 [Lý thuyết]
Chúng ta có thể sử dụng phương thức ______ để hợp nhất hai DataFrame?

- A. merge( )
- B. join( )
- C. append( )
- D. drop( )

* **Đáp án đúng:** A
* **Giải thích:** merge() là phương thức chính được dùng để gộp dữ liệu từ hai DataFrame dựa trên các điều kiện khoá tương tự như SQL JOIN.

### Câu 26 [Lý thuyết]
Viết mã Python để xóa cột 'fee' trực tiếp trên khung dữ liệu Df1.

- A. delete Df1[‘fee']
- B. drop Df1Col[‘Fee']
- C. del Df1[Col.‘fee']
- D. del Df1[‘fee']

* **Đáp án đúng:** D
* **Giải thích:** Từ khóa del trong Python có thể dùng để xóa phần tử của dictionary hoặc xóa cột của DataFrame: del Df1['fee'].

### Câu 27 [Lý thuyết]
Hàm/Thuộc tính nào được sử dụng để tìm các giá trị từ DataFrame D sử dụng số chỉ mục nguyên?

- A. D.loc
- B. D.iloc
- C. D.index
- D. Không có trong số các lựa chọn này

* **Đáp án đúng:** B
* **Giải thích:** iloc dùng cho việc truy cập dòng/cột thông qua chỉ mục số nguyên (integer location), còn loc dùng nhãn chuỗi.

### Câu 28 [Lý thuyết]
Trong Pandas, hàm được sử dụng để xóa một cột hoặc hàng trong DataFrame là:

- A. Remove
- B. del
- C. Drop
- D. cancel

* **Đáp án đúng:** C
* **Giải thích:** Hàm drop() (hoặc phương thức .drop()) là cách phổ thông nhất để xóa các hàng hoặc các cột trong DataFrame.

### Câu 29 [Đọc code]
Viết một câu lệnh để xóa hai cột có nhãn là 2017 và 2016 trong DataFrame 'DF'.

- A. print(DF.drop([2017, 2016], axis=1))
- B. print(DF.drop((2017, 2016), axis=1))
- C. Cả hai câu trên đều đúng
- D. print(DF.drop([2017,2016],axis=0))

* **Đáp án đúng:** A
* **Giải thích:** Câu lệnh đúng cần truyền list nhãn [2017, 2016] và gán axis=1 để xóa ở cột.

### Câu 30 [Lý thuyết]
Để xem sự thay đổi trong dữ liệu qua một khoảng thời gian chúng ta có thể sử dụng biểu đồ _________?

- A. Line (Biểu đồ đường)
- B. Bar (Biểu đồ cột)
- C. Histogram (Biểu đồ tần suất)
- D. Pie (Biểu đồ tròn)

* **Đáp án đúng:** A
* **Giải thích:** Biểu đồ đường (Line chart) là lựa chọn tốt nhất để trực quan hóa sự thay đổi liên tục của dữ liệu theo thời gian.

---

## Chương 10: Biểu thức chính quy (Regular Expressions) (10 câu)

### Câu 97 [Lý thuyết]
Module nào trong thư viện tiêu chuẩn của Python được dùng để làm việc với biểu thức chính quy (Regex)?

- A. regex
- B. re
- C. expression
- D. pattern

* **Đáp án đúng:** B
* **Giải thích:** Module re cung cấp các hàm tìm kiếm, so khớp mẫu chuỗi bằng Regex trong Python.

### Câu 98 [Lý thuyết]
Hàm nào trong module re dùng để tìm TẤT CẢ các chuỗi con khớp với mẫu và trả về dưới dạng danh sách?

- A. search()
- B. match()
- C. findall()
- D. find()

* **Đáp án đúng:** C
* **Giải thích:** re.findall() quét qua chuỗi và trả về list tất cả các đoạn khớp mẫu.

### Câu 99 [Lý thuyết]
Ký tự đại diện `\d` trong Regex đại diện cho nhóm ký tự nào?

- A. Bất kỳ ký tự chữ cái nào.
- B. Bất kỳ chữ số nào từ 0 đến 9.
- C. Ký tự khoảng trắng.
- D. Điểm bắt đầu của chuỗi.

* **Đáp án đúng:** B
* **Giải thích:** \d tương đương với tập ký tự [0-9], đại diện cho chữ số.

### Câu 100 [Lý thuyết]
Trong Regex, ký tự neo `^` được dùng để làm gì?

- A. Khớp ở vị trí kết thúc chuỗi.
- B. Khớp ở vị trí bắt đầu chuỗi.
- C. Đại diện cho bất kỳ ký tự nào.
- D. Lặp lại 1 hoặc nhiều lần.

* **Đáp án đúng:** B
* **Giải thích:** ^ là ký tự neo đại diện cho điểm bắt đầu của dòng/chuỗi.

### Câu 101 [Lý thuyết]
Bộ định lượng `+` trong Regex chỉ định sự lặp lại của ký tự đứng trước bao nhiêu lần?

- A. Từ 0 hoặc nhiều lần.
- B. Từ 1 hoặc nhiều lần.
- C. Đúng 1 lần.
- D. Từ 0 hoặc 1 lần.

* **Đáp án đúng:** B
* **Giải thích:** + đại diện cho lặp lại ít nhất 1 lần (1 hoặc nhiều lần). * đại diện cho 0 hoặc nhiều lần.

### Câu 102 [Lý thuyết]
Hàm re.sub(pattern, replacement, string) thực hiện chức năng gì?

- A. Tách chuỗi thành danh sách.
- B. Tìm kiếm và thay thế tất cả các chuỗi con khớp với mẫu bằng chuỗi thay thế.
- C. Kiểm tra xem chuỗi có khớp mẫu không.
- D. Đếm số lượng kết quả trùng khớp.

* **Đáp án đúng:** B
* **Giải thích:** sub (substitute) thay thế các chuỗi con khớp mẫu bằng replacement.

### Câu 103 [Lý thuyết]
Sự khác biệt chính giữa re.match() và re.search() là gì?

- A. re.match() tìm kiếm ở bất kỳ vị trí nào, re.search() chỉ khớp từ đầu chuỗi.
- B. re.match() chỉ khớp mẫu ngay ở đầu chuỗi, còn re.search() tìm kiếm mẫu ở bất kỳ vị trí nào trong toàn bộ chuỗi.
- C. re.match() trả về chuỗi, re.search() trả về số nguyên.
- D. Không có sự khác biệt.

* **Đáp án đúng:** B
* **Giải thích:** match() bắt buộc phải khớp ngay ký tự đầu tiên của chuỗi, nếu không sẽ trả về None. search() quét toàn chuỗi.

### Câu 104 [Lý thuyết]
Ký tự đại diện `\w` trong Regex tương đương với nhóm ký tự nào?

- A. [a-zA-Z0-9_] (chữ, số và dấu gạch dưới)
- B. [0-9] (chữ số)
- C. [a-z] (chữ thường)
- D. Không phải chữ và số

* **Đáp án đúng:** A
* **Giải thích:** \w đại diện cho ký tự cấu thành từ (word character), gồm chữ cái, chữ số và dấu gạch dưới.

### Câu 105 [Phân tích]
Mẫu Regex nào sau đây khớp với định dạng một email đơn giản (dạng text@domain.com)?

- A. \d+@\d+\.\d+
- B. [\w.-]+@[\w.-]+\.[a-zA-Z]{2,4}
- C. ^email$
- D. .*@.*

* **Đáp án đúng:** B
* **Giải thích:** [\w.-]+ khớp với tên hộp thư, @ là bắt buộc, sau đó đến domain, và đuôi tên miền .com/.vn dài từ 2 đến 4 ký tự.

### Câu 106 [Phân tích]
Để tìm các từ bắt đầu bằng chữ 'P' trong chuỗi, mẫu Regex nào sau đây là phù hợp?

- A. \bP\w*
- B. ^P
- C. P$
- D. [^P]

* **Đáp án đúng:** A
* **Giải thích:** \b chỉ định ranh giới từ (word boundary), P là chữ cái bắt đầu, \w* khớp các ký tự tiếp theo của từ đó.

---

