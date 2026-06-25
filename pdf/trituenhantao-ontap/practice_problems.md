# BÀI TẬP THỰC HÀNH TỰ LUẬN TRÍ TUỆ NHÂN TẠO

## Practical Problems

### Tree Search vs. Graph Search
Các bài toán tìm kiếm trên cây (Tree Search) không kiểm tra trạng thái trùng lặp, dễ rơi vào lặp vô tận trên các đồ thị có chu trình. Graph Search duy trì một Closed Set (hoặc Explored Set) lưu trữ các nút đã mở rộng để tránh mở rộng lại chúng.

### BFS (Breadth-First Search)
Duyệt theo chiều rộng. Sử dụng Queue FIFO. Mở rộng tất cả các nút con ở tầng hiện tại trước khi đi xuống tầng tiếp theo.

### DFS (Depth-First Search)
Duyệt theo chiều sâu. Sử dụng Stack LIFO. Đi sâu xuống một nhánh cho đến khi gặp nút lá rồi quay lui.

### Uniform Cost Search (UCS)
Tìm kiếm chi phí tối ưu. Sử dụng Priority Queue dựa trên hàm chi phí đường đi g(n) từ nút gốc đến nút hiện tại.

### Greedy Best First Search
Tìm kiếm tham lam. Sử dụng Heuristic h(n) ước lượng chi phí từ nút hiện tại đến đích để quyết định hướng đi.

### A* Search
Tìm kiếm tối ưu sử dụng cả chi phí thực tế g(n) và chi phí ước lượng h(n). Hàm đánh giá f(n) = g(n) + h(n).

### Constraint Satisfaction Problem (CSP)
Bài toán thỏa mãn ràng buộc với biến, miền giá trị và các ràng buộc. Các thuật toán chính bao gồm Backtracking, Forward Checking, Arc Consistency (AC-3).

---

## HANDWRITTEN EXERCISE SOLUTIONS: AND-OR TREE SEARCH

Dưới đây là lời giải chi tiết cho 3 dạng bài tập tự luận AND-OR Tree đặc trưng từ slide bài giảng:

### Exercise 1: AND-OR Tree Search (Slide Chapter 7 Page 9-12)
**1. Đề bài chuẩn hóa:**
- Trạng thái bắt đầu: S
- Danh sách các luật hành động (Actions):
  - R1: S -> A, B (AND connector)
  - R2: S -> C (OR connector)
  - R3: A -> D, E (AND connector)
  - R4: F -> G, E (AND connector)
  - R5: F -> H (OR connector)
  - R6: C -> F (OR connector)
- Goal Test: Kiểm tra xem các tập hợp đích sau có khả thi hay không:
  - Trường hợp 1: Goal = {B, D, E, G}
  - Trường hợp 2: Goal = {D, E}
  - Trường hợp 3: Goal = {B, D, E}

**2. State Space Graph:**
- S có 2 nhánh:
  - Nhánh AND (R1) đi tới nhóm nút {A, B}.
  - Nhánh OR (R2) đi tới nút C.
- A có nhánh AND (R3) đi tới nhóm nút {D, E}.
- C đi tới F qua luật R6 (OR).
- F có 2 nhánh:
  - Nhánh AND (R4) đi tới nhóm nút {G, E}.
  - Nhánh OR (R5) đi tới nút H.

**3. Lời giải từng bước:**
- **Trường hợp 1 (Goal = {B, D, E, G}):**
  - Thử áp dụng luật R1 đi tới {A, B}. 
    - Nhánh B: B thuộc Goal (Thành công).
    - Nhánh A: Áp dụng R3 đi tới {D, E}. D và E đều thuộc Goal (Thành công).
  - Vì vậy, bài toán KHẢ THI. Kế hoạch có điều kiện (Conditional Plan) là:
    `[R1, if state == A then R3 else []]`
- **Trường hợp 2 (Goal = {D, E}):**
  - Không khả thi vì từ S bắt buộc phải qua B (nếu đi R1) hoặc C (nếu đi R2) mà B không thuộc Goal.
- **Trường hợp 3 (Goal = {B, D, E}):**
  - Khả thi. Kế hoạch có điều kiện tương tự Trường hợp 1: `[R1, if state == A then R3 else []]`.

---

### Exercise 2: AND-OR Tree Search (Slide Chapter 7 Page 31)
**1. Đề bài chuẩn hóa:**
- Trạng thái bắt đầu: S
- Danh sách luật hành động:
  - R1: S -> A, B, C (AND connector)
  - R2: A -> D (OR)
  - R3: B -> E, F (AND)
  - R4: C -> D, G (AND)
  - R5: F -> H (OR)
- Goal States: {D, G, H}

**2. Lời giải từng bước:**
- Áp dụng R1 đi tới {A, B, C} (tất cả 3 nhánh con phải khả thi).
  - Nhánh A: Áp dụng R2 đi tới D. D là Goal (Thành công).
  - Nhánh B: Áp dụng R3 đi tới {E, F}. E không là Goal và không có hành động đi tiếp từ E. Do đó nhánh B thất bại.
- Kết luận: Bài toán KHÔNG KHẢ THI vì nhánh B không thể dẫn tới Goal.

---

### Exercise 3: AND-OR Tree Search (Slide Chapter 8 Page 2-3)
**1. Đề bài chuẩn hóa:**
- Trạng thái bắt đầu: S
- Danh sách luật hành động:
  - R1: S -> A (OR)
  - R2: S -> B (OR)
  - R3: A -> C, D (AND)
  - R4: B -> D, E, F (AND)
  - R5: C -> G (OR)
  - R6: D -> H (OR)
  - R7: E -> H (OR)
  - R8: E -> K (OR)
- Goal States: {H, F}

**2. Lời giải từng bước:**
- Thử nhánh S -> B qua R2. Điều này dẫn tới nhóm con {D, E, F} (tất cả phải thành công).
  - Nhánh D: Áp dụng R6 đi tới H. H thuộc Goal (Thành công).
  - Nhánh E: Áp dụng R7 đi tới H. H thuộc Goal (Thành công).
  - Nhánh F: F thuộc Goal (Thành công).
- Kết luận: Bài toán KHẢ THI. Kế hoạch có điều kiện là:
  `[R2, R4, if state == E then R7 elif state == D then R6 else []]`

---

### Exercise 4: Simple AND-OR Graph (Slide Chapter 7 Page 11-12)
**1. Đề bài chuẩn hóa:**
- Trạng thái bắt đầu: a
- Danh sách luật hành động:
  - R1: a -> b, c (AND)
  - R2: a -> d (OR)
- Goal States: {b, c}

**2. Lời giải từng bước:**
- Thử áp dụng luật R1 đi tới {b, c}.
  - Nhánh b: b thuộc Goal (Thành công).
  - Nhánh c: c thuộc Goal (Thành công).
- Kết luận: Bài toán KHẢ THI. Kế hoạch có điều kiện là `[R1]`.

---

### Exercise 5: Multi-layer AND-OR Graph (Bài tập tự luyện tổng hợp)
**1. Đề bài chuẩn hóa:**
- Trạng thái bắt đầu: S
- Danh sách luật hành động:
  - R1: S -> A, B (AND)
  - R2: A -> C (OR)
  - R3: B -> D (OR)
  - R4: C -> G (OR)
  - R5: D -> G (OR)
- Goal States: {G}

**2. Lời giải từng bước:**
- Áp dụng R1 đi tới {A, B}. Cả hai nhánh A và B đều phải khả thi dẫn tới G.
  - Nhánh A: Áp dụng R2 đi tới C. Tại C áp dụng R4 đi tới G. G thuộc Goal (Thành công).
  - Nhánh B: Áp dụng R3 đi tới D. Tại D áp dụng R5 đi tới G. G thuộc Goal (Thành công).
- Kết luận: Bài toán KHẢ THI. Kế hoạch là `[R1, R2, R3, R4, R5]`.

