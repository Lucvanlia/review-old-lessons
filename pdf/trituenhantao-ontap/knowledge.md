# TỔNG HỢP KIẾN THỨC ÔN TẬP TRÍ TUỆ NHÂN TẠO

# Chương 1: Giới thiệu chung về AI (Introduction to AI)

## Tóm tắt
Trí tuệ nhân tạo (AI) là lĩnh vực khoa học máy tính nghiên cứu cách tạo ra các hệ thống có khả năng thực hiện các tác vụ đòi hỏi trí thông minh của con người. 1. ĐỊNH NGHĨA VÀ CÁC HƯỚNG TIẾP CẬN AI:

## Khái niệm
Trí tuệ nhân tạo (AI) là lĩnh vực khoa học máy tính nghiên cứu cách tạo ra các hệ thống có khả năng thực hiện các tác vụ đòi hỏi trí thông minh của con người.

1. ĐỊNH NGHĨA VÀ CÁC HƯỚNG TIẾP CẬN AI:
AI được chia làm 4 hướng tiếp cận chính dựa trên suy nghĩ và hành động:
• Suy nghĩ như con người (Thinking Humanly): Tiếp cận nhận thức (Cognitive modeling).
• Hành động như con người (Acting Humanly): Phép thử Turing (Turing Test).
• Suy nghĩ hợp lý (Thinking Rationally): Các quy luật tư duy (Laws of Thought - Logic học).
• Hành động hợp lý (Acting Rationally): Tiếp cận Agent hợp lý (Rational Agent).

2. CÁC PHÂN LOẠI AI CHÍNH:
• ANI (Artificial Narrow Intelligence): AI hẹp/yếu, thiết kế để giải quyết một tác vụ cụ thể (như bộ lọc spam, nhận diện khuôn mặt, chơi cờ).
• AGI (Artificial General Intelligence): AI tổng quát/mạnh, có khả năng học tập, suy luận và thực hiện bất kỳ tác vụ trí tuệ nào như con người.
• ASI (Artificial Super Intelligence): Siêu trí tuệ nhân tạo, vượt trội hơn trí tuệ con người ở mọi khía cạnh.

3. BA YẾU TỐ CỐT LÕI THÚC ĐẨY AI:
• Thuật toán (Algorithms): Đặc biệt là Deep Learning và Reinforcement Learning.
• Dữ liệu lớn (Big Data): Các đặc trưng như Volume, Velocity, Variety, Veracity.
• Năng lực tính toán (Computing Power): Sự phát triển của các phần cứng chuyên biệt như GPU, TPU hỗ trợ xử lý song song cực tốt.

## Ví dụ
```python
# Ví dụ về phân biệt lập trình truyền thống và AI học máy (Machine Learning)
# Lập trình truyền thống: Quy tắc (Rules) + Dữ liệu (Data) -> Kết quả (Answers)
def traditional_classify(email):
    if "mua ngay" in email.lower() or "khuyến mãi" in email.lower():
        return "Spam"
    return "Inbox"

# AI/Machine Learning: Dữ liệu (Data) + Kết quả (Answers) -> Quy tắc (Rules)
# Mô hình học máy tự tìm ra các trọng số và từ khóa đặc trưng từ hàng triệu email huấn luyện.
```

## Ghi nhớ
- Hãy làm quen với các khái niệm và ví dụ minh họa trên.
- Chú ý ôn luyện các dạng thuật toán tìm kiếm và bài toán CSP có trong ngân hàng câu hỏi.

---

# Chương 2: Lập trình Python và Thư viện NumPy

## Tóm tắt
Python là ngôn ngữ lập trình phổ biến nhất trong AI nhờ cú pháp đơn giản, dễ đọc và hệ sinh thái thư viện phong phú. NumPy là thư viện nền tảng cho tính toán khoa học và xử lý mảng nhiều chiều trong Python. 1. KIỂU DỮ LIỆU VÀ CẤU TRÚC ĐIỀU KHIỂN:

## Khái niệm
Python là ngôn ngữ lập trình phổ biến nhất trong AI nhờ cú pháp đơn giản, dễ đọc và hệ sinh thái thư viện phong phú. NumPy là thư viện nền tảng cho tính toán khoa học và xử lý mảng nhiều chiều trong Python.

1. KIỂU DỮ LIỆU VÀ CẤU TRÚC ĐIỀU KHIỂN:
• Python hỗ trợ các kiểu dữ liệu tích hợp mạnh mẽ: List, Tuple, Dictionary, Set.
• range(n) trả về một generator tiết kiệm bộ nhớ, trong khi np.arange(n) tạo ra một đối tượng mảng NumPy (ndarray) trong bộ nhớ.

2. THƯ VIỆN NUMPY VÀ PHÉP TOÁN VECTOR:
• Mảng ndarray của NumPy yêu cầu tất cả các phần tử phải cùng kiểu dữ liệu (homogenous), giúp tối ưu hóa bộ nhớ và tăng tốc độ tính toán nhờ xử lý ở tầng C.
• Vectorization: Cho phép thực hiện các phép toán trên toàn bộ mảng mà không cần sử dụng vòng lặp for chậm chạp của Python.
• Broadcasting: Cơ chế tự động mở rộng kích thước mảng nhỏ hơn để thực hiện phép toán với mảng lớn hơn khi có các chiều tương thích.
• Các hàm thông dụng: np.array(), np.zeros(), np.ones(), np.dot(), np.reshape(), np.transpose().

## Ví dụ
```python
import numpy as np

# Tạo mảng 2 chiều đại diện cho ma trận trọng số
weights = np.array([[0.2, 0.8], [0.5, 0.1]])
inputs = np.array([1.0, 2.0])

# Thực hiện phép nhân ma trận (Matrix Multiplication / Dot Product)
output = np.dot(weights, inputs)
print("Output vector:", output) # Kết quả: [1.8, 0.7]

# Ví dụ Broadcasting: Cộng một vector hàng vào tất cả các hàng của ma trận
matrix = np.array([[1, 2], [3, 4]])
vector = np.array([10, 20])
result = matrix + vector
print("Result of broadcasting:\n", result) # [[11, 22], [13, 24]]
```

## Ghi nhớ
- Hãy làm quen với các khái niệm và ví dụ minh họa trên.
- Chú ý ôn luyện các dạng thuật toán tìm kiếm và bài toán CSP có trong ngân hàng câu hỏi.

---

# Chương 3: Đạo đức và Pháp luật trong AI

## Tóm tắt
Việc phát triển AI đi đôi với trách nhiệm xã hội, đảm bảo các giá trị nhân văn và an toàn pháp lý. 1. CÁC VẤN ĐỀ ĐẠO ĐỨC CHÍNH TRONG AI:

## Khái niệm
Việc phát triển AI đi đôi với trách nhiệm xã hội, đảm bảo các giá trị nhân văn và an toàn pháp lý.

1. CÁC VẤN ĐỀ ĐẠO ĐỨC CHÍNH TRONG AI:
• Thiên vị và Định kiến (Bias & Discrimination): Dữ liệu huấn luyện bị lệch có thể dẫn đến việc AI đưa ra quyết định phân biệt đối xử (chủng tộc, giới tính).
• Tính minh bạch và giải thích được (Explainable AI - XAI): Các mô hình hộp đen (Black box) cần được làm rõ cách đưa ra quyết định để con người tin cậy.
• Quyền riêng tư (Privacy): Bảo vệ dữ liệu cá nhân của người dùng không bị khai thác trái phép khi huấn luyện AI.

2. CÁC QUY ĐỊNH PHÁP LUẬT VỀ AI:
• Đạo luật Trí tuệ Nhân tạo của Liên minh Châu Âu (EU AI Act): Phân loại rủi ro của hệ thống AI thành 4 mức: Rủi ro không thể chấp nhận được, Rủi ro cao, Rủi ro hạn chế, và Rủi ro tối thiểu.
• Trách nhiệm pháp lý: Khi AI tự hành (như xe tự lái) gây tai nạn, việc xác định trách nhiệm thuộc về nhà phát triển phần mềm, nhà sản xuất phần cứng, hay người dùng là bài toán pháp lý phức tạp.

## Ví dụ
```python
# Ví dụ minh họa về bias trong dữ liệu huấn luyện tuyển dụng
# Nếu tập dữ liệu lịch sử chứa 90% hồ sơ nam giới được tuyển dụng, mô hình AI sẽ tự động học quy tắc ngầm:
# "Giới tính nam là một điểm cộng". Điều này dẫn đến sự thiên vị giới tính bất công.
# Giải pháp: Cân bằng dữ liệu (Data balancing) và loại bỏ thông tin nhạy cảm trước khi huấn luyện.
```

## Ghi nhớ
- Hãy làm quen với các khái niệm và ví dụ minh họa trên.
- Chú ý ôn luyện các dạng thuật toán tìm kiếm và bài toán CSP có trong ngân hàng câu hỏi.

---

# Chương 4: Hệ thống thông minh và Môi trường (Agent)

## Tóm tắt
Một Agent là bất kỳ thực thể nào có thể nhận thức môi trường của nó thông qua các cảm biến (Sensors) và tác động lên môi trường đó thông qua các bộ chấp hành (Actuators). 1. MÔ HÌNH PEAS:

## Khái niệm
Một Agent là bất kỳ thực thể nào có thể nhận thức môi trường của nó thông qua các cảm biến (Sensors) và tác động lên môi trường đó thông qua các bộ chấp hành (Actuators).

1. MÔ HÌNH PEAS:
Để thiết kế một Agent thông minh, ta phải xác định rõ cấu trúc PEAS của bài toán:
• Performance Measure (Độ đo hiệu năng): Các tiêu chí đánh giá mức độ thành công của Agent.
• Environment (Môi trường): Môi trường hoạt động của Agent.
• Actuators (Bộ chấp hành): Các cơ cấu tác động giúp Agent thực hiện hành động.
• Sensors (Cảm biến): Các thiết bị giúp Agent thu thập thông tin từ môi trường.

2. PHÂN LOẠI MÔI TRƯỜNG:
• Quan sát được toàn bộ (Fully observable) vs. Một phần (Partially observable).
• Đơn tác nhân (Single agent) vs. Đa tác nhân (Multiagent).
• Xác định (Deterministic) vs. Không xác định/Ngẫu nhiên (Stochastic).
• Theo chuỗi (Episodic) vs. Theo tuần tự (Sequential).
• Tĩnh (Static) vs. Động (Dynamic).
• Rời rạc (Discrete) vs. Liên tục (Continuous).
• Đã biết (Known) vs. Chưa biết (Unknown).

3. CÁC LOẠI AGENT CHÍNH:
• Simple reflex agent (Agent phản xạ đơn giản).
• Model-based reflex agent (Agent phản xạ dựa trên mô hình).
• Goal-based agent (Agent dựa trên mục tiêu).
• Utility-based agent (Agent dựa trên hữu dụng/tiện ích).
• Learning agent (Agent học tập).

## Ví dụ
```python
# Ví dụ thiết kế PEAS cho xe tự hành (Automated taxi driver)
taxi_peas = {
    "Performance": ["Đến đích an toàn", "Nhanh chóng", "Hợp luật giao thông", "Tiết kiệm nhiên liệu", "Khách hàng hài lòng"],
    "Environment": ["Đường phố", "Người đi bộ", "Các phương tiện giao thông khác", "Thời tiết", "Biển báo giao thông"],
    "Actuators": ["Vô lăng (Bẻ lái)", "Chân ga (Tăng tốc)", "Chân phanh (Dừng xe)", "Đèn tín hiệu", "Còi"],
    "Sensors": ["Cameras", "LiDAR", "GPS", "Cảm biến khoảng cách", "Tốc độ kế"]
}
```

## Ghi nhớ
- Hãy làm quen với các khái niệm và ví dụ minh họa trên.
- Chú ý ôn luyện các dạng thuật toán tìm kiếm và bài toán CSP có trong ngân hàng câu hỏi.

---

# Chương 5: Giải quyết vấn đề bằng Tìm kiếm (Search Problems)

## Tóm tắt
Tìm kiếm là phương pháp cơ bản để tìm ra chuỗi hành động dẫn tới mục tiêu mong muốn khi Agent không biết trước lời giải trực tiếp. 1. CẤU TRÚC BÀI TOÁN TÌM KIẾM:

## Khái niệm
Tìm kiếm là phương pháp cơ bản để tìm ra chuỗi hành động dẫn tới mục tiêu mong muốn khi Agent không biết trước lời giải trực tiếp.

1. CẤU TRÚC BÀI TOÁN TÌM KIẾM:
Gồm 5 thành phần: Trạng thái bắt đầu (Initial state), Tập hành động (Actions), Mô hình chuyển trạng thái (Transition model), Kiểm tra mục tiêu (Goal test), và Chi phí đường đi (Path cost).

2. THUẬT TOÁN TÌM KIẾM KHÔNG THÔNG TIN (Uninformed Search):
Duyệt đồ thị không có tri thức bổ trợ (chỉ biết trạng thái hiện tại là đích hay chưa):
• Breadth-First Search (BFS): Duyệt theo chiều rộng bằng hàng đợi FIFO.
  - Completeness: Có (nếu b hữu hạn). Optimal: Có (nếu chi phí mọi bước bằng nhau).
  - Độ phức tạp thời gian và không gian: O(b^d), tốn rất nhiều bộ nhớ.
• Depth-First Search (DFS): Duyệt theo chiều sâu bằng ngăn xếp LIFO (hoặc đệ quy).
  - Completeness: Không (tránh vòng lặp vô hạn). Optimal: Không.
  - Độ phức tạp không gian: O(bm), cực kỳ tiết kiệm bộ nhớ so với BFS.
• Uniform Cost Search (UCS): Duyệt dựa trên chi phí đường đi g(n) tích lũy nhỏ nhất bằng hàng đợi ưu tiên (Priority Queue). Bản chất là thuật toán Dijkstra.
  - Completeness: Có. Optimal: Có (nếu chi phí bước > 0).

3. THUẬT TOÁN TÌM KIẾM CÓ THÔNG TIN (Informed / Heuristic Search):
Sử dụng hàm Heuristic h(n) để ước lượng chi phí từ nút n tới đích:
• Greedy Best-First Search (GBFS): Chọn nút có h(n) nhỏ nhất để mở rộng. Không tối ưu nhưng tốc độ nhanh.
• A* Search: Chọn nút có f(n) = g(n) + h(n) nhỏ nhất.
  - Điều kiện tối ưu của A* trên cây: h(n) phải admissible (h(n) <= h*(n)).
  - Điều kiện tối ưu của A* trên đồ thị: h(n) phải consistent (h(n) <= c(n, a, n') + h(n')).

## Ví dụ
```python
# Minh họa thuật toán A* cơ bản
# Giả sử cấu trúc đồ thị dạng Dictionary
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1)],
    'C': [], 'D': []
}
heuristics = {'S': 6, 'A': 5, 'B': 2, 'C': 3, 'D': 0} # h(n) ước lượng tới D

# f(n) cho các nút lân cận của S:
# f(A) = g(A) + h(A) = 1 + 5 = 6
# f(B) = g(B) + h(B) = 4 + 2 = 6
# Cả hai bằng nhau, thuật toán mở rộng một trong hai. Nếu mở rộng A trước:
# f(C) = g(C) + h(C) = (1+2) + 3 = 6
# f(D) = g(D) + h(D) = (1+5) + 0 = 6
```

## Ghi nhớ
- Hãy làm quen với các khái niệm và ví dụ minh họa trên.
- Chú ý ôn luyện các dạng thuật toán tìm kiếm và bài toán CSP có trong ngân hàng câu hỏi.

---

# Chương 6: Tìm kiếm cục bộ và Tối ưu hóa (Local Search)

## Tóm tắt
Tìm kiếm cục bộ (Local Search) chỉ quan tâm đến trạng thái hiện tại thay vì tìm kiếm toàn bộ đường đi từ điểm bắt đầu. Thích hợp cho bài toán có không gian trạng thái cực lớn nơi đường đi không quan trọng (như bài toán xếp lịch, N-Queens). 1. THUẬT TOÁN LEO ĐỒI (Hill Climbing):

## Khái niệm
Tìm kiếm cục bộ (Local Search) chỉ quan tâm đến trạng thái hiện tại thay vì tìm kiếm toàn bộ đường đi từ điểm bắt đầu. Thích hợp cho bài toán có không gian trạng thái cực lớn nơi đường đi không quan trọng (như bài toán xếp lịch, N-Queens).

1. THUẬT TOÁN LEO ĐỒI (Hill Climbing):
• Hoạt động như việc leo núi trong sương mù: liên tục di chuyển về phía trạng thái hàng xóm có giá trị hàm mục tiêu tốt hơn trạng thái hiện tại.
• Hạn chế: Dễ bị kẹt ở Cực đại địa phương (Local Maxima), Sườn dốc phẳng (Plateaux), hoặc Rặng núi (Ridges).

2. THUẬT TOÁN LUYỆN KIM (Simulated Annealing):
• Lấy ý tưởng từ quá trình tôi thép trong luyện kim: ban đầu cho phép chấp nhận các bước đi xấu với xác suất cao để thoát khỏi cực tiểu/cực đại địa phương, sau đó giảm dần nhiệt độ T để thuật toán hội tụ về nghiệm tối ưu toàn cục.
• Xác suất chấp nhận bước đi xấu delta_E < 0 là P = exp(delta_E / T).

3. THUẬT TOÁN DI TRUYỀN (Genetic Algorithm):
• Mô phỏng quá trình tiến hóa tự nhiên của Darwin.
• Quy trình: Khởi tạo quần thể cá thể -> Đánh giá độ thích nghi (Fitness function) -> Chọn lọc tự nhiên (Selection) -> Lai ghép (Crossover) -> Đột biến (Mutation).

## Ví dụ
```python
# Hàm chấp nhận bước đi xấu trong Simulated Annealing
import math
import random

def accept_worse_state(delta_E, temperature):
    if temperature == 0:
        return False
    probability = math.exp(delta_E / temperature)
    return random.random() < probability

# Ví dụ: delta_E = -5 (giảm chất lượng), T = 100
# P = exp(-5/100) = exp(-0.05) ~ 0.95 (khả năng chấp nhận cực kỳ cao ở nhiệt độ cao)
```

## Ghi nhớ
- Hãy làm quen với các khái niệm và ví dụ minh họa trên.
- Chú ý ôn luyện các dạng thuật toán tìm kiếm và bài toán CSP có trong ngân hàng câu hỏi.

---

# Chương 7: Tìm kiếm trong môi trường phức hợp (AND-OR Search)

## Tóm tắt
Khi môi trường không xác định (nondeterministic) hoặc quan sát được một phần, hành động của Agent có thể dẫn tới nhiều kết quả trạng thái khác nhau. Do đó, lời giải không còn là một chuỗi hành động cố định mà là một Kế hoạch có điều kiện (Conditional Plan / Contingency Plan). 1. ĐỒ THỊ AND-OR (AND-OR Graph):

## Khái niệm
Khi môi trường không xác định (nondeterministic) hoặc quan sát được một phần, hành động của Agent có thể dẫn tới nhiều kết quả trạng thái khác nhau. Do đó, lời giải không còn là một chuỗi hành động cố định mà là một Kế hoạch có điều kiện (Conditional Plan / Contingency Plan).

1. ĐỒ THỊ AND-OR (AND-OR Graph):
• Nút OR đại diện cho các lựa chọn hành động của Agent tại một trạng thái.
• Nút AND đại diện cho các kết quả có thể xảy ra của một hành động do môi trường ngẫu nhiên quyết định. Tất cả các nhánh con của nút AND đều phải thành công thì hành động đó mới dẫn tới đích thành công.
• Một bài toán tìm kiếm AND-OR là solvable (khả thi) nếu tồn tại một cây con giải pháp (solution subtree) xuất phát từ nút gốc dẫn tới các nút đích ở tất cả các nhánh lá.

2. TÌM KIẾM KHÔNG CẢM BIẾN (Sensorless / Blind Search):
• Agent hoàn toàn không có cảm biến để biết mình đang ở trạng thái nào.
• Khái niệm Trạng thái niềm tin (Belief State): Tập hợp tất cả các trạng thái thực tế mà Agent có thể đang đứng ở đó.

## Ví dụ
```python
# Ví dụ về Cây Giải pháp có điều kiện (Conditional Plan)
# Cho bài toán AND-OR có:
# R1: S -> A, B (AND connector)
# R2: S -> C (OR connector)
# R3: A -> D, E (AND)
# R4: C -> F (OR)
# Với Goal = {B, D, E}, Cây giải pháp hợp lệ là:
# [R1, if state == A then R3 else []]
# Giải thích: R1 chuyển S thành {A, B}. 
# Tại B: B là goal (xong).
# Tại A: áp dụng R3 chuyển A thành {D, E}. Cả D và E đều là goal (xong).
# Tất cả các nhánh đều dẫn tới đích thành công.
```

## Ghi nhớ
- Hãy làm quen với các khái niệm và ví dụ minh họa trên.
- Chú ý ôn luyện các dạng thuật toán tìm kiếm và bài toán CSP có trong ngân hàng câu hỏi.

---

# Chương 8: Bài toán thỏa mãn ràng buộc (CSP)

## Tóm tắt
Bài toán thỏa mãn ràng buộc (Constraint Satisfaction Problem - CSP) biểu diễn trạng thái bằng các biến có miền giá trị cụ thể và ràng buộc giữa chúng, giúp thuật toán giải quyết thông minh hơn tìm kiếm thông thường. 1. BA THÀNH PHẦN CỦA CSP:

## Khái niệm
Bài toán thỏa mãn ràng buộc (Constraint Satisfaction Problem - CSP) biểu diễn trạng thái bằng các biến có miền giá trị cụ thể và ràng buộc giữa chúng, giúp thuật toán giải quyết thông minh hơn tìm kiếm thông thường.

1. BA THÀNH PHẦN CỦA CSP:
• Tập hợp các biến (Variables): X = {X1, X2, ..., Xn}.
• Miền giá trị (Domains): D = {D1, D2, ..., Dn} chứa các giá trị có thể gán cho biến.
• Tập các ràng buộc (Constraints): C ràng buộc các giá trị mà các biến có thể nhận đồng thời.

2. CÁC THUẬT TOÁN VÀ KỸ THUẬT GIẢI CSP:
• Backtracking Search: Thuật toán quay lui duyệt cây trạng thái để tìm phép gán hoàn chỉnh hợp lệ.
• Các Heuristics lựa chọn:
  - MRV (Minimum Remaining Values): Chọn biến có ít giá trị hợp lệ nhất trong miền giá trị trước (Fail-first để sớm phát hiện nhánh rỗng).
  - LCV (Least Constraining Value): Chọn giá trị ít ràng buộc nhất cho biến được chọn để chừa nhiều không gian gán cho các biến khác.
• Lan truyền ràng buộc (Constraint Propagation) giúp thu hẹp miền giá trị sớm:
  - Nhất quán nút (Node Consistency).
  - Nhất quán cung (Arc Consistency - thuật toán AC-3): Đảm bảo với mọi giá trị x thuộc miền của X, luôn tồn tại y thuộc miền của Y thỏa mãn ràng buộc nhị phân giữa X và Y.
  - Forward Checking: Kiểm tra trước miền giá trị của các biến chưa gán kề với biến vừa gán để loại bỏ các giá trị vi phạm ràng buộc.

## Ví dụ
```python
# Ví dụ bài toán tô màu bản đồ Úc (Map Coloring) làm CSP
# Các biến đại diện cho các vùng bang: WA, NT, Q, NSW, V, SA, T
variables = ["WA", "NT", "Q", "NSW", "V", "SA", "T"]
domains = {v: ["Red", "Green", "Blue"] for v in variables}

# Ràng buộc nhị phân: các vùng kề nhau không được trùng màu
# Ví dụ: WA != NT, WA != SA, NT != SA, NT != Q, Q != SA, Q != NSW, NSW != SA, NSW != V, V != SA
constraints = [
    ("WA", "NT"), ("WA", "SA"),
    ("NT", "SA"), ("NT", "Q"),
    ("Q", "SA"), ("Q", "NSW"),
    ("NSW", "SA"), ("NSW", "V"),
    ("V", "SA")
]
```

## Ghi nhớ
- Hãy làm quen với các khái niệm và ví dụ minh họa trên.
- Chú ý ôn luyện các dạng thuật toán tìm kiếm và bài toán CSP có trong ngân hàng câu hỏi.

---

