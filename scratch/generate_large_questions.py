# -*- coding: utf-8 -*-
import json
import os

questions_pool = []

# Helper to add questions
def add_q(id_num, topic_id, q_type, question, options, correct_ans, explanation):
    questions_pool.append({
        "id": id_num,
        "topicId": topic_id,
        "type": q_type,
        "question": question,
        "options": options,
        "correctAnswer": correct_ans,
        "explanation": explanation
    })

# ==========================================
# 1. servlet_lifecycle (Vòng đời Servlet)
# ==========================================
add_q(1, "servlet_lifecycle", "concept", 
      "Giai đoạn nào trong vòng đời Servlet chịu trách nhiệm giải phóng tài nguyên hệ thống trước khi hủy instance?",
      ["A. Giai đoạn init()", "B. Giai đoạn service()", "C. Giai đoạn destroy()", "D. Giai đoạn doFilter()"],
      "C", "Phương thức destroy() được gọi duy nhất một lần bởi container khi tắt ứng dụng hoặc gỡ bỏ servlet để dọn dẹp tài nguyên.")

add_q(2, "servlet_lifecycle", "comparison", 
      "Điểm khác biệt chính giữa phương thức init() và init(ServletConfig config) trong HttpServlet là gì?",
      ["A. init() không thể nạp tham số cấu hình, còn init(config) thì có.", "B. init() chỉ chạy trên Tomcat cũ, còn init(config) chạy trên Tomcat mới.", "C. init(config) bắt buộc phải gọi super.init(config) nếu không sẽ bị lỗi null cấu hình sau đó.", "D. Không có sự khác biệt nào về chức năng."],
      "C", "Khi override init(ServletConfig config), nếu quên gọi super.init(config) thì đối tượng ServletConfig sẽ không được gán vào GenericServlet, dẫn đến các lệnh gọi getServletConfig() hay getServletContext() sau đó ném NullPointerException.")

add_q(3, "servlet_lifecycle", "situation", 
      "Một lập trình viên muốn thiết lập một kết nối Database dùng chung cho toàn bộ thời gian sống của Servlet. Lập trình viên đó nên viết code kết nối này ở phương thức nào để tối ưu hiệu năng?",
      ["A. service()", "B. init()", "C. destroy()", "D. doGet()"],
      "B", "init() được gọi đúng một lần duy nhất khi servlet khởi tạo, việc thiết lập database connection ở đây giúp tránh việc kết nối lặp đi lặp lại ở mỗi request trong service().")

add_q(4, "servlet_lifecycle", "blank", 
      "Mặc định trong môi trường Servlet, đối với mỗi lớp Servlet được định nghĩa, Web Container sẽ khởi tạo đúng ______ đối tượng duy nhất để xử lý tất cả các request gửi đến.",
      ["A. một (1)", "B. hai (2)", "C. mười (10)", "D. n (bằng số luồng xử lý)"],
      "A", "Web Container áp dụng mẫu Singleton, chỉ tạo duy nhất 1 đối tượng cho mỗi class Servlet để tiết kiệm bộ nhớ và tài nguyên.")

add_q(5, "servlet_lifecycle", "process", 
      "Quy trình xử lý một HTTP Request gửi tới Servlet diễn ra theo trình tự nào sau đây?",
      ["A. Client -> service() -> init() -> Response", "B. Client -> init() -> service() -> doGet()/doPost() -> Response", "C. Client -> doGet() -> service() -> destroy() -> Response", "D. Client -> service() -> doGet()/doPost() -> destroy() -> Response"],
      "B", "Container nạp servlet và gọi init() trước, sau đó với mỗi request sẽ gọi service() để điều hướng qua doGet()/doPost(), cuối cùng render phản hồi về client.")

add_q(6, "servlet_lifecycle", "bug", 
      "Hiện tượng gì xảy ra nếu bạn khai báo một biến instance (biến thành viên của class) trong Servlet và thay đổi giá trị của nó trong phương thức doGet()?",
      ["A. Trình duyệt của người dùng sẽ bị treo.", "B. Lỗi biên dịch xảy ra ngay lập tức.", "C. Xảy ra tranh chấp dữ liệu (Race Condition) vì Servlet là đơn luồng.", "D. Xảy ra tranh chấp dữ liệu vì nhiều luồng (thread) request cùng truy cập và chỉnh sửa biến dùng chung này (Thread-safety issue)."],
      "D", "Vì servlet chỉ có 1 đối tượng duy nhất xử lý đồng thời nhiều luồng request, việc ghi đè biến thành viên lớp sẽ gây lỗi đồng bộ dữ liệu giữa các người dùng.")

add_q(7, "servlet_lifecycle", "code", 
      "Cho đoạn mã Servlet sau:\n\npublic class TestServlet extends HttpServlet {\n    int count = 0;\n    protected void doGet(HttpServletRequest req, HttpServletResponse res) {\n        count++;\n    }\n}\n\nNếu có 3 request đồng thời gửi tới Servlet này, giá trị của biến count cuối cùng có thể là gì?",
      ["A. Chắc chắn bằng 3", "B. Chắc chắn bằng 1", "C. Có thể nhỏ hơn 3 do xung đột ghi dữ liệu giữa các thread", "D. Trình duyệt báo lỗi 500"],
      "C", "Do biến count là biến instance không được đồng bộ hóa (non-thread-safe), các thao tác tăng giá trị đồng thời có thể đè lên nhau khiến kết quả nhỏ hơn 3.")

# ==========================================
# 2. session_cookie (Session vs Cookie)
# ==========================================
add_q(8, "session_cookie", "concept", 
      "Cookie nào sẽ tự động bị xóa sau khi người dùng đóng trình duyệt web?",
      ["A. Persistent Cookie", "B. Secure Cookie", "C. Session Cookie (Cookie phiên)", "D. HttpOnly Cookie"],
      "C", "Session Cookie không có thời hạn hết hạn cụ thể (Max-Age hoặc Expires), nó chỉ được lưu tạm thời trong RAM của trình duyệt và biến mất khi đóng tab/trình duyệt.")

add_q(9, "session_cookie", "comparison", 
      "Khi so sánh Session và Cookie, phát biểu nào sau đây là SAI?",
      ["A. Session lưu dữ liệu ở Server-side, còn Cookie lưu dữ liệu ở Client-side.", "B. Dữ liệu trong Cookie dễ bị giả mạo hơn dữ liệu trong Session.", "C. Session có thể lưu trữ dung lượng lớn hơn nhiều so với Cookie (thường giới hạn 4KB).", "D. Session có tốc độ truy xuất nhanh hơn Cookie vì dữ liệu truyền tải qua mạng ít hơn."],
      "D", "Dữ liệu session nằm trên server nên server không cần truyền cả cục dữ liệu lớn qua mạng cho client, chỉ cần truyền ID. Tuy nhiên, phát biểu nói Session có tốc độ truy xuất nhanh hơn là sai vì server phải tốn chi phí đọc Session từ RAM hoặc Database, việc này không nhất thiết nhanh hơn việc client tự gửi cookie đính kèm.")

add_q(10, "session_cookie", "situation", 
      "Hệ thống của bạn cần lưu trữ giỏ hàng của người dùng chưa đăng nhập. Để thông tin giỏ hàng không bị mất kể cả khi người dùng tắt máy khởi động lại sau 2 ngày, giải pháp nào thích hợp nhất?",
      ["A. Lưu thông tin vào HttpSession trên server.", "B. Lưu thông tin vào Cookie có Max-Age = 2 ngày.", "C. Lưu vào ServletContext.", "D. Sử dụng RequestDispatcher."],
      "B", "HttpSession thường hết hạn sau 30 phút rảnh rỗi. Để lưu trữ bền vững qua nhiều ngày không cần đăng nhập, sử dụng Cookie lưu ở trình duyệt với thời gian sống xác định (Max-Age) là tối ưu.")

add_q(11, "session_cookie", "blank", 
      "Để bảo vệ Cookie khỏi các cuộc tấn công Cross-Site Scripting (XSS) nhằm ngăn chặn mã độc Javascript đọc được giá trị Cookie, ta nên cấu hình thuộc tính ______ cho Cookie đó.",
      ["A. Secure", "B. SameSite", "C. Domain", "D. HttpOnly"],
      "D", "Cấu hình HttpOnly ngăn chặn mã JavaScript phía client truy cập vào cookie (ví dụ qua lệnh document.cookie), giảm thiểu nguy cơ bị đánh cắp session token qua tấn công XSS.")

add_q(12, "session_cookie", "process", 
      "Quy trình kiểm tra phiên làm việc của người dùng thông qua Session ID diễn ra như thế nào?",
      ["A. Trình duyệt gửi request -> Server tạo Session ID -> Server lưu DB -> Trả về Client", "B. Request chứa Cookie JSESSIONID -> Server tìm Session khớp ID trong bộ nhớ -> Xác nhận trạng thái đăng nhập", "C. Request chứa Cookie -> Server giải mã toàn bộ thông tin tài khoản lưu trong cookie -> Phản hồi", "D. Server gửi Session ID -> Trình duyệt mã hóa -> Lưu trữ vào RAM"],
      "B", "Khi nhận được request, Container đọc cookie JSESSIONID từ client, tra cứu trong danh sách Session đang quản lý trên Server, nếu thấy khớp thì tái sử dụng đối tượng HttpSession đó.")

add_q(13, "session_cookie", "bug", 
      "Tại sao khi tắt chế độ lưu Cookie trên trình duyệt, chức năng đăng nhập sử dụng HttpSession thông thường lại bị lỗi (người dùng bị logout liên tục)?",
      ["A. Vì server không thể lưu trữ đối tượng Session được nữa.", "B. Vì trình duyệt không thể gửi mã JSESSIONID về server, khiến server tưởng mỗi request là một phiên làm việc mới.", "C. Vì giao thức HTTP tự động bị ngắt kết nối liên tục.", "D. Vì Servlet bị crash."],
      "B", "HttpSession phụ thuộc vào việc trình duyệt lưu trữ cookie chứa JSESSIONID để định danh. Nếu cookie bị tắt, trình duyệt không gửi được ID này, Server sẽ coi mỗi request là của khách mới và tạo Session mới tinh.")

add_q(14, "session_cookie", "code", 
      "Đoạn mã Servlet nào dưới đây tạo ra một Cookie an toàn chỉ truyền qua HTTPS và không cho phép truy cập qua JavaScript?",
      ["A. Cookie c = new Cookie(\"user\", \"val\"); c.setSecure(true);", "B. Cookie c = new Cookie(\"user\", \"val\"); c.setHttpOnly(true); c.setSecure(true);", "C. Cookie c = new Cookie(\"user\", \"val\"); c.setComment(\"secure\");", "D. Cookie c = new Cookie(\"user\", \"val\"); c.setMaxAge(0);"],
      "B", "setHttpOnly(true) giúp ngăn chặn JavaScript truy cập (chống XSS), c.setSecure(true) đảm bảo cookie chỉ được gửi qua kết nối HTTPS bảo mật.")

# ==========================================
# 3. genericservlet_httpservlet (GenericServlet vs HttpServlet)
# ==========================================
add_q(15, "genericservlet_httpservlet", "concept", 
      "Class nào đóng vai trò triển khai độc lập giao thức (Protocol-independent) trong các Servlet API?",
      ["A. HttpServlet", "B. GenericServlet", "C. Filter", "D. WebServlet"],
      "B", "GenericServlet là một abstract class triển khai interface Servlet nhưng không ràng buộc với bất kỳ giao thức mạng cụ thể nào.")

add_q(16, "genericservlet_httpservlet", "comparison", 
      "Điểm khác biệt chính giữa phương thức service() trong GenericServlet và HttpServlet là gì?",
      ["A. HttpServlet.service() tự động chuyển đổi ServletRequest/Response sang HttpServletRequest/Response và điều hướng HTTP methods.", "B. GenericServlet.service() tự động chạy đa luồng còn HttpServlet.service() thì không.", "C. HttpServlet không có phương thức service().", "D. GenericServlet.service() không cho phép ném ra Exception."],
      "A", "HttpServlet ghi đè service() để ép kiểu đối tượng Request/Response sang định dạng HTTP và phân tích các phương thức GET/POST/PUT... để chuyển tiếp xử lý sang doGet/doPost.")

add_q(17, "genericservlet_httpservlet", "situation", 
      "Bạn cần xây dựng một ứng dụng Java Servlet xử lý các bản tin qua giao thức FTP (không dùng HTTP). Bạn nên kế thừa lớp nào?",
      ["A. HttpServlet", "B. GenericServlet", "C. ServletConfig", "D. FilterChain"],
      "B", "GenericServlet độc lập với giao thức, rất phù hợp để xây dựng các servlet xử lý giao thức phi HTTP như FTP, SMTP, v.v.")

add_q(18, "genericservlet_httpservlet", "blank", 
      "Lớp HttpServlet kế thừa trực tiếp từ lớp abstract có tên là ______.",
      ["A. ServletContext", "B. Object", "C. GenericServlet", "D. AbstractServlet"],
      "C", "Cấu trúc kế thừa: Object -> GenericServlet (độc lập giao thức) -> HttpServlet (chuyên biệt cho HTTP).")

add_q(19, "genericservlet_httpservlet", "process", 
      "Khi một HttpServlet nhận một request HTTP POST, chuỗi gọi phương thức nào diễn ra trong Servlet?",
      ["A. init() -> doPost()", "B. service(ServletRequest, ServletResponse) -> service(HttpServletRequest, HttpServletResponse) -> doPost()", "C. service() -> doGet() -> doPost()", "D. init() -> doGet() -> service()"],
      "B", "Container gọi service() gốc với tham số chung trước, sau đó ép kiểu gọi service() HTTP, tiếp theo kiểm tra method là POST và gọi doPost().")

add_q(20, "genericservlet_httpservlet", "bug", 
      "Hiện tượng gì xảy ra nếu bạn ghi đè (override) phương thức service() trong lớp kế thừa HttpServlet và quên gọi super.service(request, response)?",
      ["A. Server bị sập.", "B. Các phương thức doGet() hoặc doPost() bạn viết thêm sẽ không bao giờ được tự động gọi nữa.", "C. Trình duyệt hiển thị mã lỗi 404.", "D. Các filter không thể hoạt động."],
      "B", "Logic phân tích request method và gọi doGet()/doPost() nằm trong super.service(). Nếu ghi đè mà không gọi super, các phương thức doGet/doPost của bạn sẽ bị bỏ qua hoàn toàn.")

add_q(21, "genericservlet_httpservlet", "code", 
      "Xem đoạn code sau:\n\npublic class CustomServlet extends HttpServlet {\n    public void service(HttpServletRequest req, HttpServletResponse res) {\n        // Không có code\n    }\n}\n\nNếu gửi request GET đến Servlet này, kết quả nhận được trên trình duyệt là gì?",
      ["A. Trang trắng (Không có nội dung phản hồi)", "B. Mã lỗi 405 Method Not Allowed", "C. Mã lỗi 500 Server Error", "D. Lỗi biên dịch"],
      "A", "Vì phương thức service() bị ghi đè rỗng và không gọi super.service(), servlet sẽ không thực hiện gì và trả về phản hồi rỗng (status 200 mặc định).")

# ==========================================
# 4. requestdispatcher (RequestDispatcher - forward vs sendRedirect)
# ==========================================
add_q(22, "requestdispatcher", "concept", 
      "Cơ chế chuyển hướng nào thực hiện chuyển tiếp hoàn toàn ở phía Server-side và che giấu URL đích đối với người dùng?",
      ["A. sendRedirect()", "B. forward()", "C. HTTP 302 Redirect", "D. JavaScript window.location"],
      "B", "Phương thức forward() của RequestDispatcher chuyển giao xử lý hoàn toàn trong máy chủ, trình duyệt client giữ nguyên URL ban đầu.")

add_q(23, "requestdispatcher", "comparison", 
      "So sánh giữa forward() và sendRedirect(), nhận định nào sau đây là ĐÚNG?",
      ["A. forward() chậm hơn sendRedirect() do phải tạo kết nối mới.", "B. sendRedirect() giữ nguyên được các attribute đã set trong HttpServletRequest.", "C. forward() chỉ chuyển hướng trong cùng một ứng dụng Web, còn sendRedirect() có thể dẫn tới URL ngoài trang web.", "D. Cả hai đều thay đổi địa chỉ URL hiển thị trên trình duyệt."],
      "C", "forward() xử lý nội bộ trong container nên không thể forward tới website khác. Ngược lại, sendRedirect() gửi mã 302 về trình duyệt client bắt client gọi URL mới, nên có thể dẫn tới bất cứ website nào.")

add_q(24, "requestdispatcher", "situation", 
      "Sau khi xử lý thành công một form thanh toán (POST request), lập trình viên nên sử dụng cơ chế nào để chuyển hướng người dùng đến trang 'Hoàn tất đơn hàng' nhằm tránh lỗi submit lặp dữ liệu khi người dùng ấn F5 (Reload)?",
      ["A. RequestDispatcher.forward()", "B. HttpServletResponse.sendRedirect() (Post-Redirect-Get pattern)", "C. Gọi trực tiếp doGet() từ doPost()", "D. Không chuyển hướng, render trực tiếp HTML"],
      "B", "Sử dụng sendRedirect() chuyển hướng trình duyệt sang phương thức GET (mẫu PRG - Post-Redirect-Get). Khi người dùng nhấn F5, trình duyệt chỉ gửi lại request GET trang hoàn thành, tránh gửi lại dữ liệu thanh toán POST.")

add_q(25, "requestdispatcher", "blank", 
      "Để lấy đối tượng RequestDispatcher trong Servlet, ta sử dụng phương thức `request.______(\"/path\")`.",
      ["A. getRequestDispatcher", "B. sendRedirect", "C. getServletContext", "D. forward"],
      "A", "Cú pháp: RequestDispatcher rd = request.getRequestDispatcher(\"/path\");")

add_q(26, "requestdispatcher", "process", 
      "Quy trình hoạt động mạng khi gọi phương thức response.sendRedirect(\"/success\") là gì?",
      ["A. Server gọi trực tiếp trang success -> gửi kết quả về client", "B. Server gửi HTTP response 302 kèm header Location: /success -> Client nhận được và tự động gửi request GET mới tới /success -> Server phản hồi", "C. Client tự động tải lại cache -> không gửi dữ liệu", "D. Server ném ngoại lệ -> Client hiển thị lỗi"],
      "B", "sendRedirect là quy trình 2 request riêng biệt: Server phản hồi mã 302 trỏ đường dẫn mới, trình duyệt đọc được sẽ tự động gửi request thứ 2 lên server.")

add_q(27, "requestdispatcher", "bug", 
      "Nguyên nhân gì dẫn đến ngoại lệ `IllegalStateException` khi gọi phương thức forward() hoặc sendRedirect()?",
      ["A. Do gọi phương thức sau khi response đã được ghi dữ liệu (commit) về client.", "B. Do không cài đặt thư viện JDBC.", "C. Do URL chuyển hướng bị sai chính tả.", "D. Do session bị timeout."],
      "A", "Nếu response đã được ghi (ví dụ đã gọi writer.write() hoặc flushBuffer() gửi header về client), việc gọi forward/redirect sẽ ném ra IllegalStateException vì không thể chuyển hướng phản hồi đã cam kết.")

add_q(28, "requestdispatcher", "code", 
      "Cho đoạn mã Servlet sau:\n\nrequest.setAttribute(\"val\", \"123\");\nresponse.sendRedirect(\"next.jsp\");\n\nTrong file next.jsp, lệnh `request.getAttribute(\"val\")` sẽ trả về giá trị gì?",
      ["A. \"123\"", "B. null", "C. Lỗi biên dịch", "D. Trình duyệt báo lỗi 500"],
      "B", "Vì sendRedirect tạo ra một request hoàn toàn mới từ client, đối tượng request cũ chứa thuộc tính \"val\" đã bị hủy bỏ, do đó next.jsp nhận giá trị null.")

# ==========================================
# 5. filter_api (Servlet Filter & web.xml)
# ==========================================
add_q(29, "filter_api", "concept", 
      "Đâu không phải là một phương thức vòng đời của interface jakarta.servlet.Filter?",
      ["A. init()", "B. doFilter()", "C. destroy()", "D. service()"],
      "D", "Interface Filter chỉ gồm init(), doFilter(), và destroy(). Phương thức service() thuộc về Servlet.")

add_q(30, "filter_api", "comparison", 
      "Trong web.xml, thứ tự thực thi của các Filter được quyết định bởi yếu tố nào?",
      ["A. Thứ tự bảng chữ cái tên của Filter.", "B. Thứ tự khai báo của các thẻ <filter-mapping> trong file web.xml.", "C. Thứ tự khai báo của các thẻ <filter> trong file web.xml.", "D. Do Web Container tự sắp xếp ngẫu nhiên."],
      "B", "Web Container duyệt chuỗi filter dựa trên thứ tự xuất hiện của các thẻ `<filter-mapping>` từ trên xuống dưới trong file cấu hình web.xml.")

add_q(31, "filter_api", "situation", 
      "Hệ thống của bạn có 50 servlet khác nhau, tất cả đều yêu cầu phải thiết lập bộ mã hóa tiếng Việt UTF-8 cho Request và Response. Giải pháp tốt nhất để tránh lặp code là gì?",
      ["A. Viết một phương thức tĩnh tiện ích rồi gọi ở đầu doGet của từng servlet.", "B. Tạo một Custom Filter thực hiện set CharacterEncoding rồi cấu hình mapping cho tất cả URL (/*).", "C. Cấu hình trực tiếp trong file server.xml của Tomcat.", "D. Sử dụng RequestDispatcher."],
      "B", "Sử dụng Filter chặn mọi request (urlPatterns = \"/*\") để đặt mã hóa ký tự là giải pháp tối ưu, tập trung hóa logic xử lý chung.")

add_q(32, "filter_api", "blank", 
      "Trong phương thức doFilter của Filter, đối tượng giúp chuyển tiếp request sang Filter kế tiếp hoặc Servlet đích có tên lớp là ______.",
      ["A. RequestDispatcher", "B. FilterChain", "C. FilterConfig", "D. ServletContext"],
      "B", "Đối tượng FilterChain quản lý danh sách các filter và được dùng để kích hoạt bộ lọc tiếp theo bằng lệnh chain.doFilter(req, res).")

add_q(33, "filter_api", "process", 
      "Quy trình hoạt động của một Filter khi xử lý một Request diễn ra như thế nào?",
      ["A. Filter doFilter -> Gọi Servlet service -> Trả kết quả trực tiếp cho Client", "B. Filter doFilter (trước) -> chain.doFilter() -> Servlet service() -> Filter doFilter (sau) -> Gửi response về Client", "C. Servlet service -> Filter doFilter -> Response", "D. Filter init -> Filter destroy -> Servlet service"],
      "B", "Filter chặn request trước khi vào servlet (code trước chain.doFilter), sau đó chuyển tiếp cho servlet chạy, khi servlet chạy xong và trả response ra ngoài, filter tiếp tục xử lý response (code sau chain.doFilter) trước khi gửi về client.")

add_q(34, "filter_api", "bug", 
      "Điều gì xảy ra nếu trong phương thức doFilter() của Filter, bạn không gọi câu lệnh chain.doFilter(request, response)?",
      ["A. Server báo lỗi biên dịch.", "B. Request bị chặn lại vĩnh viễn và không bao giờ đến được Servlet mục tiêu.", "C. Web Container tự động nhảy đến Servlet tiếp theo sau 5 giây.", "D. Servlet vẫn chạy bình thường nhưng response bị rỗng."],
      "B", "Nếu thiếu chain.doFilter(), chuỗi lọc bị ngắt quãng, request không được chuyển đi tiếp và client sẽ nhận trang trắng hoặc treo kết nối.")

add_q(35, "filter_api", "code", 
      "Quan sát đoạn cấu hình web.xml sau:\n\n<filter-mapping>\n    <filter-name>LogFilter</filter-name>\n    <url-pattern>/admin/*</url-pattern>\n</filter-mapping>\n\nFilter này sẽ chạy khi người dùng truy cập URL nào?",
      ["A. /index.jsp", "B. /admin/dashboard", "C. /user/admin", "D. Tất cả mọi trang trong website"],
      "B", "Đường dẫn `/admin/*` khớp với tất cả các request có tiền tố `/admin/` (ví dụ: `/admin/dashboard`, `/admin/login`,...).")

# ==========================================
# 6. jdbc_api (JDBC API)
# ==========================================
add_q(36, "jdbc_api", "concept", 
      "Interface nào trong JDBC API được thiết kế để thực thi các câu lệnh SQL có tham số đầu vào động một cách an toàn?",
      ["A. Statement", "B. PreparedStatement", "C. CallableStatement", "D. Connection"],
      "B", "PreparedStatement biên dịch trước câu lệnh SQL và hỗ trợ truyền tham số qua các ký tự hỏi chấm (?), giúp ngăn chặn SQL Injection.")

add_q(37, "jdbc_api", "comparison", 
      "So sánh giữa executeQuery() và executeUpdate() trong JDBC, phát biểu nào sau đây là ĐÚNG?",
      ["A. Cả hai đều trả về ResultSet chứa danh sách dòng dữ liệu.", "B. executeQuery() dùng cho lệnh SELECT, executeUpdate() dùng cho INSERT/UPDATE/DELETE và trả về số dòng bị ảnh hưởng.", "C. executeUpdate() nhanh hơn executeQuery() vì không cần kết nối Database.", "D. executeQuery() trả về kiểu boolean."],
      "B", "executeQuery() chuyên để đọc dữ liệu (SELECT) và trả về ResultSet. executeUpdate() chuyên ghi dữ liệu (INSERT, UPDATE, DELETE, DDL) và trả về số lượng bản ghi đã được xử lý (int).")

add_q(38, "jdbc_api", "situation", 
      "Bạn cần gọi một Store Procedure đã được định nghĩa sẵn trong cơ sở dữ liệu MySQL. Bạn nên sử dụng interface nào?",
      ["A. Statement", "B. PreparedStatement", "C. CallableStatement", "D. ResultSet"],
      "C", "CallableStatement kế thừa PreparedStatement, chuyên dụng cho việc thực thi các thủ tục lưu trữ (Stored Procedure) trong CSDL.")

add_q(39, "jdbc_api", "blank", 
      "Để duyệt qua các bản ghi dữ liệu trả về từ câu lệnh SELECT trong ResultSet, ta sử dụng vòng lặp kết hợp phương thức `rs.______()`.",
      ["A. next", "B. hasNext", "C. getRecord", "D. close"],
      "A", "Phương thức rs.next() di chuyển con trỏ xuống dòng tiếp theo và trả về true nếu dòng đó tồn tại dữ liệu.")

add_q(40, "jdbc_api", "process", 
      "Quy trình giải phóng tài nguyên JDBC nào sau đây tuân thủ đúng thứ tự chuẩn tránh rò rỉ bộ nhớ (memory leak)?",
      ["A. Đóng Connection -> Statement -> ResultSet", "B. Đóng ResultSet -> Statement -> Connection", "C. Đóng Statement -> ResultSet -> Connection", "D. Chỉ cần đóng Connection, các thành phần khác tự động đóng"],
      "B", "Quy tắc đóng tài nguyên ngược lại với thứ tự mở: đóng ResultSet trước, sau đó đóng Statement, cuối cùng đóng Connection.")

add_q(41, "jdbc_api", "bug", 
      "Nếu chương trình JDBC liên tục mở kết nối `DriverManager.getConnection()` trong vòng lặp mà không gọi phương thức close(), hệ thống sẽ gặp sự cố gì?",
      ["A. CPU quá tải 100%.", "B. Hết bộ nhớ Heap của JVM.", "C. Cạn kiệt kết nối của Database Pool (Out of Connections), khiến ứng dụng không thể truy cập CSDL được nữa.", "D. File dữ liệu của Database bị hỏng."],
      "C", "Cơ sở dữ liệu giới hạn số lượng kết nối đồng thời. Việc mở kết nối mà không đóng sẽ làm cạn kiệt tài nguyên kết nối khả dụng, gây ra lỗi nghẽn hệ thống.")

add_q(42, "jdbc_api", "code", 
      "Đoạn mã sau có lỗ hổng bảo mật gì?\n\nString sql = \"SELECT * FROM users WHERE user = '\" + username + \"'\";\nStatement stmt = conn.createStatement();\nResultSet rs = stmt.executeQuery(sql);\n",
      ["A. Rò rỉ tài nguyên Connection.", "B. SQL Injection do cộng chuỗi trực tiếp giá trị đầu vào của người dùng vào câu lệnh SQL.", "C. NullPointerException.", "D. Không có lỗ hổng nào."],
      "B", "Cộng chuỗi trực tiếp tạo điều kiện cho kẻ tấn công chèn các mã độc SQL (ví dụ: ' OR '1'='1) để vượt qua bước đăng nhập hoặc phá hủy database.")

# ==========================================
# 7. springboot_autoconfig (Spring Boot Auto-configuration)
# ==========================================
add_q(43, "springboot_autoconfig", "concept", 
      "Đâu là annotation chịu trách nhiệm trực tiếp kích hoạt cơ chế quét classpath để tự động cấu hình các bean tương ứng trong Spring Boot?",
      ["A. @Configuration", "B. @EnableAutoConfiguration", "C. @ComponentScan", "D. @SpringBootConfiguration"],
      "B", "@EnableAutoConfiguration ra lệnh cho Spring Boot quét các thư viện starter trong classpath và tự động tạo các cấu hình bean mặc định phù hợp.")

add_q(44, "springboot_autoconfig", "comparison", 
      "Phát biểu nào sau đây là ĐÚNG khi nói về sự khác biệt giữa @SpringBootConfiguration và @Configuration?",
      ["A. @SpringBootConfiguration cho phép khai báo đa luồng còn @Configuration thì không.", "B. @SpringBootConfiguration là một cấu hình chuyên biệt thay thế cho @Configuration dành riêng cho ứng dụng Spring Boot, hỗ trợ tự động tìm kiếm cấu hình trong các test.", "C. Hai annotation này hoàn toàn khác biệt nhau về bản chất.", "D. @Configuration chỉ dùng trong XML."],
      "B", "@SpringBootConfiguration là một phiên bản đặc biệt của @Configuration, được thiết kế để Spring Boot tự động nhận diện cấu hình chính của ứng dụng (đặc biệt trong các test tích hợp).")

add_q(45, "springboot_autoconfig", "situation", 
      "Dự án Spring Boot của bạn có thư viện DataSourceAutoConfiguration tự động tạo kết nối DB, nhưng hiện tại bạn chỉ viết API tính toán chưa cần kết nối DB và không muốn ứng dụng bị crash khi khởi động do thiếu URL cấu hình cơ sở dữ liệu. Bạn xử lý như thế nào?",
      ["A. Xóa thư viện spring-boot-starter ra khỏi pom.xml.", "B. Loại trừ lớp cấu hình đó bằng cách khai báo: @SpringBootApplication(exclude = {DataSourceAutoConfiguration.class}).", "C. Cấu hình database ảo.", "D. Tắt Spring Boot đi."],
      "B", "Thuộc tính `exclude` trong `@SpringBootApplication` cho phép lập trình viên vô hiệu hóa các class auto-configuration cụ thể khi không có nhu cầu sử dụng.")

add_q(46, "springboot_autoconfig", "blank", 
      "File POM cha mặc định trong các dự án Maven Spring Boot quản lý phiên bản thư viện tập trung có tên thẻ artifactId là `______`.",
      ["A. spring-boot-starter-web", "B. spring-boot-starter-parent", "C. spring-boot-autoconfigure", "D. spring-boot-dependencies"],
      "B", "spring-boot-starter-parent cung cấp các cấu hình build mặc định và quản lý version của các dependencies (dependency management) để tránh xung đột phiên bản.")

add_q(47, "springboot_autoconfig", "process", 
      "Khi chạy lệnh SpringApplication.run(), Spring Boot thực hiện quá trình khởi tạo theo thứ tự nào?",
      ["A. Quét Component -> Chạy Auto-configuration -> Tạo ApplicationContext -> Khởi động server nhúng Tomcat", "B. Khởi động Tomcat -> Quét Component -> Chạy Auto-configuration", "C. Tạo ApplicationContext -> Quét Component -> Chạy Auto-configuration -> Khởi động server Tomcat nhúng -> Sẵn sàng nhận request", "D. Tạo Bean -> Quét Component -> Chạy Auto-configuration"],
      "C", "Ứng dụng sẽ tạo context chứa môi trường trước, quét các bean tự viết, bổ sung các bean tự động cấu hình từ classpath, khởi động Tomcat nhúng và lắng nghe cổng mạng.")

add_q(48, "springboot_autoconfig", "bug", 
      "Nếu bạn đặt class chứa annotation @SpringBootApplication ở trong package `com.example.app.main`, nhưng lại viết các class Controller ở package `com.example.controller`, tại sao khi chạy ứng dụng, trình duyệt báo lỗi 404 cho tất cả các API?",
      ["A. Do controller viết sai code.", "B. Do Spring ComponentScan mặc định chỉ quét trong package của class main (`com.example.app.main`) và các package con của nó, nên không phát hiện ra Controller.", "C. Do cổng Tomcat bị chặn.", "D. Do thiếu file application.properties."],
      "B", "Mặc định @ComponentScan bắt đầu quét từ package chứa class cấu hình chính. Để quét các package nằm ngoài cây thư mục này, ta phải cấu hình quét rõ ràng: @ComponentScan(\"com.example\") hoặc dời class main ra ngoài.")

add_q(49, "springboot_autoconfig", "code", 
      "Xem đoạn mã sau:\n\n@SpringBootApplication\npublic class DemoApplication {\n    public static void main(String[] args) {\n        SpringApplication.run(DemoApplication.class, args);\n    }\n}\n\nAnnotation @SpringBootApplication là sự kết hợp của 3 annotation nào sau đây?",
      ["A. @Configuration, @EnableAutoConfiguration, @ComponentScan", "B. @SpringBootConfiguration, @EnableAutoConfiguration, @ComponentScan", "C. @Component, @Service, @Repository", "D. @Controller, @ResponseBody, @Configuration"],
      "B", "@SpringBootApplication tích hợp sẵn 3 annotation gồm: @SpringBootConfiguration, @EnableAutoConfiguration, và @ComponentScan.")

# ==========================================
# 8. spring_mvc_flow (Luồng Request trong Spring MVC)
# ==========================================
add_q(50, "spring_mvc_flow", "concept", 
      "Thành phần nào trong kiến trúc Spring MVC chịu trách nhiệm ánh xạ giữa đường dẫn yêu cầu (URL) và Controller xử lý?",
      ["A. DispatcherServlet", "B. HandlerMapping", "C. HandlerAdapter", "D. ViewResolver"],
      "B", "HandlerMapping phân tích URL request để tìm ra Handler (Controller) và trả về một HandlerExecutionChain cho DispatcherServlet.")

add_q(51, "spring_mvc_flow", "comparison", 
      "Sự khác biệt giữa Controller truyền thống và RestController trong Spring MVC là gì?",
      ["A. Controller chỉ dùng cho ứng dụng console.", "B. RestController tự động đính kèm annotation @ResponseBody lên mọi phương thức để trả về dữ liệu thô (JSON/XML) thay vì trả về View Name.", "C. Controller nhanh hơn RestController.", "D. RestController bắt buộc phải sử dụng JSP để render."],
      "B", "@RestController là một annotation kết hợp giữa @Controller và @ResponseBody, tự động chuyển đổi giá trị trả về của phương thức thành dữ liệu API (JSON/XML) trực tiếp trong Response Body.")

add_q(52, "spring_mvc_flow", "situation", 
      "Bạn đang xây dựng ứng dụng Web trả về giao diện HTML sử dụng công nghệ Thymeleaf làm View Engine. Controller của bạn nên trả về kiểu dữ liệu gì để ViewResolver tìm được file HTML?",
      ["A. Chuỗi String chứa tên của file giao diện (View Name).", "B. Đối tượng JSON thô.", "C. Đối tượng Connection.", "D. Trả về void."],
      "A", "Trong Controller truyền thống, việc trả về một String (ví dụ: \"index\") đại diện cho View Name sẽ được ViewResolver tiếp nhận để tìm file mẫu tương ứng (ví dụ: /templates/index.html).")

add_q(53, "spring_mvc_flow", "blank", 
      "Trong Spring MVC, đối tượng đóng vai trò là Front Controller tiếp nhận tất cả mọi HTTP request gửi đến hệ thống có tên là `______`.",
      ["A. ServletContext", "B. DispatcherServlet", "C. WebMvcConfigurer", "D. HandlerInterceptor"],
      "B", "DispatcherServlet là trái tim của Spring MVC, tiếp nhận mọi request đầu vào và điều phối quá trình xử lý qua các thành phần khác.")

add_q(54, "spring_mvc_flow", "process", 
      "Thứ tự đúng của luồng xử lý Request trong Spring MVC là gì?",
      ["A. Request -> Controller -> DispatcherServlet -> View", "B. Request -> DispatcherServlet -> HandlerMapping -> HandlerAdapter -> Controller -> ViewResolver -> View -> Response", "C. Request -> ViewResolver -> Controller -> DispatcherServlet -> Response", "D. Request -> HandlerAdapter -> ViewResolver -> DispatcherServlet"],
      "B", "Luồng đi: DispatcherServlet tiếp nhận -> hỏi HandlerMapping tìm Controller -> gọi HandlerAdapter để thực thi Controller -> Controller trả về ModelAndView -> ViewResolver biên dịch View -> Trình bày kết quả.")

add_q(55, "spring_mvc_flow", "bug", 
      "Tại sao khi truy cập API bạn nhận được chuỗi text tên view \"users\" hiển thị trực tiếp trên trình duyệt thay vì trang giao diện HTML của trang quản lý người dùng?",
      ["A. Do chưa cấu hình Database.", "B. Do bạn đánh dấu Controller bằng annotation @RestController hoặc @ResponseBody, khiến Spring bỏ qua ViewResolver và viết thẳng chuỗi String đó vào Response Body.", "C. Do file HTML bị lỗi cú pháp.", "D. Do lỗi kết nối mạng."],
      "B", "@ResponseBody chỉ định giá trị trả về của phương thức được ghi trực tiếp vào body của HTTP Response dưới dạng dữ liệu thô, vô hiệu hóa quy trình tìm View của ViewResolver.")

add_q(56, "spring_mvc_flow", "code", 
      "Cho đoạn mã Spring MVC Controller sau:\n\n@Controller\npublic class MainController {\n    @GetMapping(\"/home\")\n    public String homepage() {\n        return \"home\";\n    }\n}\n\nKhi người dùng truy cập /home, hệ thống sẽ thực hiện hành động nào?",
      ["A. Trả về dòng chữ \"home\" thô cho trình duyệt.", "B. Nhờ ViewResolver tìm file giao diện có tên tương ứng là \"home\" để kết xuất giao diện.", "C. Gây lỗi sập server.", "D. Chuyển hướng sang trang google.com."],
      "B", "Vì class sử dụng @Controller (không phải @RestController) và phương thức trả về kiểu String, Spring MVC sẽ gửi chuỗi \"home\" tới ViewResolver để tìm trang template.")

# ==========================================
# 9. spring_mvc_annotations (Annotations @PathVariable vs @RequestParam)
# ==========================================
add_q(57, "spring_mvc_annotations", "concept", 
      "Annotation nào dùng để trích xuất trực tiếp giá trị nằm trên phân đoạn của đường dẫn URL (URI Path)?",
      ["A. @RequestParam", "B. @PathVariable", "C. @RequestBody", "D. @RequestHeader"],
      "B", "@PathVariable cho phép ánh xạ các biến mẫu đường dẫn URI (ví dụ: /users/{id}) thành các tham số trong phương thức Java.")

add_q(58, "spring_mvc_annotations", "comparison", 
      "Sự khác biệt chính giữa @PathVariable và @RequestParam là gì?",
      ["A. @PathVariable lấy tham số từ body, @RequestParam lấy từ header.", "B. @PathVariable lấy dữ liệu từ URI path segment (ví dụ /users/5), còn @RequestParam lấy từ query parameter (ví dụ /users?id=5) hoặc form data.", "C. @RequestParam chỉ dùng được với POST request.", "D. Không có sự khác biệt."],
      "B", "@PathVariable ánh xạ biến trên đường dẫn URL. @RequestParam ánh xạ biến từ chuỗi truy vấn (query string sau dấu ?) hoặc dữ liệu gửi lên từ form.")

add_q(59, "spring_mvc_annotations", "situation", 
      "Bạn cần xây dựng API tìm kiếm sản phẩm hỗ trợ lọc theo tên và sắp xếp theo thuộc tính (ví dụ: `/products?name=iphone&sort=price`). Bạn nên khai báo các tham số này sử dụng annotation nào?",
      ["A. @PathVariable", "B. @RequestParam", "C. @RequestBody", "D. @ModelAttribute"],
      "B", "Các tham số lọc và sắp xếp động truyền theo query string cực kỳ phù hợp để xử lý bằng @RequestParam (ví dụ: @RequestParam(\"name\") String name).")

add_q(60, "spring_mvc_annotations", "blank", 
      "Để thiết lập một tham số @RequestParam là không bắt buộc và có giá trị mặc định bằng 1 nếu người dùng không truyền lên, ta dùng thuộc tính `______`.",
      ["A. required = false, defaultValue = \"1\"", "B. optional = true, val = \"1\"", "C. required = true, defaultVal = 1", "D. exclude = true"],
      "A", "Cú pháp: @RequestParam(value = \"page\", required = false, defaultValue = \"1\").")

add_q(61, "spring_mvc_annotations", "process", 
      "Khi người dùng gửi request tới `/users/12?type=admin`, Spring MVC phân tích và gán giá trị cho controller như thế nào?",
      ["A. Gán 12 cho RequestParam và type cho PathVariable", "B. Không gán được vì trùng lặp tham số", "C. Ánh xạ 12 thành PathVariable và 'admin' thành RequestParam", "D. Đọc từ Request Body"],
      "C", "Số 12 là một phần của đường dẫn được bắt bằng @PathVariable. Chuỗi truy vấn `type=admin` được bắt bằng @RequestParam.")

add_q(62, "spring_mvc_annotations", "bug", 
      "Lỗi `400 Bad Request` xảy ra khi gọi API sử dụng @RequestParam trong Controller. Nguyên nhân phổ biến nhất là gì?",
      ["A. Do database bị đầy.", "B. Do tham số được cấu hình mặc định là bắt buộc (`required=true`), nhưng client gửi request không đính kèm tham số này trong URL hoặc form.", "C. Do không dùng HTTPS.", "D. Do sai kiểu trả về của Controller."],
      "B", "Mặc định, @RequestParam có `required=true`. Nếu client không gửi tham số đó lên, Spring Boot sẽ tự động từ chối và trả về lỗi 400 Bad Request.")

add_q(63, "spring_mvc_annotations", "code", 
      "Xem đoạn mã sau:\n\n@GetMapping(\"/api/v1/orders/{orderId}\")\npublic Order getOrder(@PathVariable Long orderId) { ... }\n\nNếu client gửi request tới `/api/v1/orders/999`, biến orderId sẽ nhận giá trị bao nhiêu?",
      ["A. null", "B. 999", "C. Lỗi 400", "D. Lỗi biên dịch vì thiếu tên biến rõ ràng"],
      "B", "Nếu tên biến phương thức trùng khớp với tên biến trong dấu ngoặc nhọn `{orderId}`, Spring Boot có thể tự động ánh xạ giá trị (ở đây là 999) mà không cần khai báo tường minh tên trong @PathVariable.")

# ==========================================
# 10. spring_filters (Các loại Filter trong Spring)
# ==========================================
add_q(64, "spring_filters", "concept", 
      "Class nào của Spring Framework được thiết kế chuyên biệt để đảm bảo một bộ lọc chỉ chạy duy nhất một lần cho mỗi Request?",
      ["A. GenericFilterBean", "B. OncePerRequestFilter", "C. FilterChainProxy", "D. DelegatingFilterProxy"],
      "B", "OncePerRequestFilter là một abstract class của Spring đảm bảo phương thức doFilterInternal chỉ được kích hoạt đúng 1 lần cho mỗi yêu cầu HTTP.")

add_q(65, "spring_filters", "comparison", 
      "Điểm khác biệt chính giữa GenericFilterBean và Filter chuẩn (jakarta.servlet.Filter) là gì?",
      ["A. GenericFilterBean không thể đọc được web.xml.", "B. GenericFilterBean là class của Spring, tích hợp sâu với Spring Context cho phép truy cập tham số cấu hình dễ dàng hơn và tránh boilerplate code.", "C. GenericFilterBean chạy nhanh hơn gấp 10 lần.", "D. Interface Filter không thể dùng trong Spring."],
      "B", "GenericFilterBean là lớp trung gian giúp tích hợp Servlet Filter tiêu chuẩn vào hệ sinh thái của Spring, tự động lấy cấu hình từ ServletConfig/ServletContext thành các thuộc tính bean.")

add_q(66, "spring_filters", "situation", 
      "Bạn cần xây dựng một Filter xác thực token JWT cho mọi request. Bộ lọc này không được phép chạy lại nếu request đó bị forward nội bộ sang một servlet khác. Bạn nên kế thừa class nào?",
      ["A. GenericFilterBean", "B. OncePerRequestFilter", "C. javax.servlet.Filter", "D. WebMvcConfigurer"],
      "B", "Kế thừa OncePerRequestFilter giúp ngăn chặn việc bộ lọc JWT chạy lại nhiều lần không cần thiết khi có hoạt động chuyển hướng nội bộ (forward/include).")

add_q(67, "spring_filters", "blank", 
      "Để đăng ký một Filter viết thủ công vào chuỗi lọc của Spring Boot mà không cần dùng web.xml, ta sử dụng lớp cấu hình có tên là `______`.",
      ["A. FilterRegistrationBean", "B. ServiceComponent", "C. DelegatingFilterProxy", "D. WebSecurityConfigurer"],
      "A", "FilterRegistrationBean giúp đăng ký một custom Filter làm Spring Bean và cấu hình thứ tự chạy (Order), URL mapping cụ thể.")

add_q(68, "spring_filters", "process", 
      "Khi có request đi vào ứng dụng Spring Boot sử dụng Spring Security, thứ tự lọc diễn ra thế nào?",
      ["A. Controller -> Filter -> Interceptor", "B. Servlet Filter tiêu chuẩn -> Spring Security Filter Chain (OncePerRequestFilter) -> HandlerInterceptor -> Controller", "C. Interceptor -> Filter -> Controller", "D. Quét Component -> Filter -> Response"],
      "B", "Request đi qua các Filter ngoài container trước, sau đó đi vào bộ lọc bảo mật của Spring Security, qua Interceptor của Spring MVC và cuối cùng mới tới Controller.")

add_q(69, "spring_filters", "bug", 
      "Tại sao một Filter kế thừa GenericFilterBean khi được khai báo làm `@Component` trong Spring Boot lại tự động áp dụng cho tất cả URL (/*) mặc dù bạn không hề cấu hình mapping cho nó?",
      ["A. Do Tomcat tự cấu hình.", "B. Vì Spring Boot tự động phát hiện mọi Bean kiểu Filter và đăng ký nó vào Servlet container mặc định với đường dẫn '/*'.", "C. Do lỗi thư viện Maven.", "D. Do Spring Security ép buộc."],
      "B", "Spring Boot tự động đăng ký mọi Bean kế thừa Filter vào ứng dụng. Để kiểm soát chính xác URL mapping hoặc tránh tự động đăng ký, ta nên sử dụng FilterRegistrationBean.")

add_q(70, "spring_filters", "code", 
      "Xem đoạn mã định nghĩa Custom Filter sau:\n\npublic class LogFilter extends OncePerRequestFilter {\n    protected void doFilterInternal(HttpServletRequest req, HttpServletResponse res, FilterChain chain) {\n        // Ghi log\n        chain.doFilter(req, res);\n    }\n}\n\nPhương thức cần override để viết logic lọc chính trong OncePerRequestFilter là gì?",
      ["A. doFilter(ServletRequest, ServletResponse, FilterChain)", "B. doFilterInternal(HttpServletRequest, HttpServletResponse, FilterChain)", "C. init(FilterConfig)", "D. destroy()"],
      "B", "OncePerRequestFilter định nghĩa phương thức abstract doFilterInternal() làm nơi viết logic lọc chính sau khi đã xử lý xong các kiểm tra lặp request.")

# ==========================================
# 11. spring_di_ioc (DI và IoC)
# ==========================================
add_q(71, "spring_di_ioc", "concept", 
      "IoC (Inversion of Control) là gì?",
      ["A. Là một thư viện giúp kết nối Database.", "B. Là một nguyên lý thiết kế đảo ngược quyền kiểm soát quản lý vòng đời đối tượng từ lập trình viên sang cho Framework.", "C. Là cơ chế biên dịch mã nguồn Java thành mã máy.", "D. Là một mẫu thiết kế để tạo Singleton Class."],
      "B", "IoC đảo ngược sự kiểm soát việc khởi tạo và quản lý liên kết đối tượng, giao nhiệm vụ này cho container quản lý.")

add_q(72, "spring_di_ioc", "comparison", 
      "So sánh giữa Constructor Injection và Field Injection (@Autowired trực tiếp lên biến), tại sao Constructor Injection lại được khuyến nghị sử dụng hơn?",
      ["A. Constructor Injection giúp ứng dụng khởi động nhanh hơn.", "B. Constructor Injection cho phép khai báo các dependency là 'final' (bất biến), đảm bảo đối tượng không bị null khi chạy, và dễ dàng viết Unit Test mà không cần mock framework.", "C. Field Injection bị cấm trong các phiên bản Java mới.", "D. Constructor Injection chiếm ít bộ nhớ hơn."],
      "B", "Constructor Injection bắt buộc phải truyền đủ các đối tượng phụ thuộc khi khởi tạo đối tượng, cho phép dùng thuộc tính 'final' bảo vệ dữ liệu và giúp code dễ test hơn do không phụ thuộc vào Spring Container.")

add_q(73, "spring_di_ioc", "situation", 
      "Lớp `PaymentService` của bạn cần sử dụng đối tượng `EmailService` để gửi thông báo. Thiết kế lớp `PaymentService` như thế nào để tuân thủ nguyên lý Dependency Injection chuẩn chỉnh nhất?",
      ["A. Khởi tạo trực tiếp: private EmailService service = new EmailService();", "B. Tiêm qua hàm tạo: khai báo EmailService là final và truyền vào Constructor của PaymentService.", "C. Tạo EmailService bằng Reflection.", "D. Viết EmailService làm lớp con của PaymentService."],
      "B", "Khai báo biến thành viên là `final` và tiêm qua Constructor là mẫu thiết kế Dependency Injection được khuyến nghị chính thức bởi Spring.")

add_q(74, "spring_di_ioc", "blank", 
      "Nơi lưu trữ, quản lý vòng đời và cấu hình các Bean trong Spring Framework được gọi là ______.",
      ["A. Database Connection Pool", "B. JVM Memory", "C. Spring IoC Container (ApplicationContext)", "D. Web Container Tomcat"],
      "C", "Spring IoC Container (được đại diện bởi interface ApplicationContext) chịu trách nhiệm khởi tạo, cấu hình và quản lý vòng đời của tất cả các Spring Beans.")

add_q(75, "spring_di_ioc", "process", 
      "Quy trình khởi tạo một Bean trong Spring IoC Container diễn ra như thế nào?",
      ["A. Đọc định nghĩa Bean -> Khởi tạo Instance -> Tiêm Dependency -> Gọi init-method -> Sẵn sàng sử dụng -> Gọi destroy-method khi đóng container", "B. Chạy code -> Tạo Connection -> Hủy Bean", "C. Gọi destroy -> Khởi tạo Bean -> Quét Component", "D. Khởi động Tomcat -> Tạo DB -> Tạo Bean"],
      "A", "Container quét định nghĩa cấu hình, tạo đối tượng (new), tiêm các phụ thuộc (DI), chạy hàm khởi tạo bổ sung (init), đưa vào sử dụng và hủy (destroy) khi dừng ứng dụng.")

add_q(76, "spring_di_ioc", "bug", 
      "Lỗi `CircularDependencyException` (Phụ thuộc vòng quanh) xảy ra khi nào trong ứng dụng Spring Boot?",
      ["A. Khi kết nối Database bị gián đoạn.", "B. Khi hai Bean phụ thuộc chéo lẫn nhau (ví dụ: Bean A cần Bean B trong Constructor, và Bean B cũng cần Bean A trong Constructor).", "C. Khi đặt tên trùng hai Bean.", "D. Khi thiếu annotation @Service."],
      "B", "Phụ thuộc vòng quanh làm container rơi vào vòng lặp vô hạn khi khởi tạo đối tượng (A đợi B khởi tạo xong, B lại đợi A khởi tạo xong), dẫn đến lỗi khởi động.")

add_q(77, "spring_di_ioc", "code", 
      "Xem đoạn mã sau:\n\n@Configuration\npublic class AppConfig {\n    @Bean\n    public OrderService orderService() {\n        return new OrderServiceImpl();\n    }\n}\n\nBean tạo ra từ phương thức trên sẽ có tên mặc định là gì trong IoC Container?",
      ["A. orderServiceImpl", "B. orderService", "C. AppConfig", "D. bean1"],
      "B", "Mặc định, tên của Bean được tạo ra từ phương thức đánh dấu `@Bean` chính là tên của phương thức đó (ở đây là `orderService`).")

# ==========================================
# 12. spring_stereotype_annotations (Stereotype Annotations)
# ==========================================
add_q(78, "spring_stereotype_annotations", "concept", 
      "Annotation nào là annotation cơ sở (meta-annotation) cho tất cả các stereotype annotation khác của Spring?",
      ["A. @Service", "B. @Repository", "C. @Component", "D. @Controller"],
      "C", "@Component là annotation gốc. Các annotation Service, Repository, Controller đều được chú thích bởi @Component và mang các ngữ nghĩa bổ sung.")

add_q(79, "spring_stereotype_annotations", "comparison", 
      "Mục đích chính của việc chia nhỏ các annotation thành @Service, @Repository, @Controller thay vì chỉ dùng duy nhất @Component là gì?",
      ["A. Giúp mã nguồn chạy nhanh hơn.", "B. Phân cấp rõ ràng kiến trúc ứng dụng (Controller cho web, Service cho nghiệp vụ, Repository cho DB) và cho phép áp dụng các xử lý tự động chuyên biệt (như dịch lỗi DB trong Repository).", "C. Ràng buộc bảo mật dữ liệu.", "D. Yêu cầu bắt buộc của ngôn ngữ Java."],
      "B", "Tạo tính ngữ nghĩa cho mã nguồn giúp dễ quản lý và cho phép Spring kích hoạt các xử lý đặc thù (như dịch ngoại lệ CSDL cho @Repository, xử lý view cho @Controller).")

add_q(80, "spring_stereotype_annotations", "situation", 
      "Bạn cần xây dựng một class chịu trách nhiệm thực hiện các câu lệnh SQL tự viết bằng JDBCTemplate để tương tác với DB. Bạn nên đánh dấu class này bằng annotation nào?",
      ["A. @Component", "B. @Service", "C. @Repository", "D. @Controller"],
      "C", "@Repository được thiết kế dành riêng cho các lớp Data Access Object (DAO) thực hiện các thao tác truy vấn trực tiếp với DB.")

add_q(81, "spring_stereotype_annotations", "blank", 
      "Để đăng ký một class làm Controller cung cấp các API RESTful trả về dữ liệu thô JSON, ta sử dụng annotation kết hợp là `______`.",
      ["A. @Controller", "B. @RestController", "C. @Component", "D. @WebController"],
      "B", "@RestController = @Controller + @ResponseBody, chuyên dùng cho việc xây dựng các API RESTful.")

add_q(82, "spring_stereotype_annotations", "process", 
      "Quá trình quét và đăng ký các Stereotype Annotation diễn ra như thế nào khi khởi chạy ứng dụng?",
      ["A. Spring quét các class -> Tìm các class có annotation stereotype -> Khởi tạo Bean và đưa vào IoC Container", "B. Lập trình viên phải tự đăng ký từng class vào XML", "C. Quét database -> tạo entity -> gán Controller", "D. Chạy Tomcat -> Đăng ký filter -> Tạo Component"],
      "A", "Cơ chế Component Scanning quét classpath tìm các annotation được kế thừa từ @Component, tự động sinh mã khởi tạo instance cho chúng trong ứng dụng.")

add_q(83, "spring_stereotype_annotations", "bug", 
      "Tại sao khi bạn tạo một lớp mới chứa các xử lý nghiệp vụ nhưng quên thêm annotation `@Service`, khi khởi chạy ứng dụng, Spring báo lỗi `NoSuchBeanDefinitionException` tại nơi tiêm đối tượng đó?",
      ["A. Do thiếu kết nối DB.", "B. Do Spring ComponentScan không nhận diện class đó là một component để khởi tạo Bean vào Container, dẫn đến thiếu đối tượng để tiêm.", "C. Do Java không hỗ trợ class đó.", "D. Do lỗi cổng mạng."],
      "B", "Nếu không có stereotype annotation, Spring Container sẽ bỏ qua class đó và không tạo Bean. Khi class khác yêu cầu tiêm Bean này, Spring sẽ không tìm thấy và ném lỗi.")

add_q(84, "spring_stereotype_annotations", "code", 
      "Quan sát đoạn mã sau:\n\n@Repository\npublic class CustomUserDao { ... }\n\nLợi ích đặc biệt nhất của việc đánh dấu @Repository lên class CustomUserDao này là gì?",
      ["A. Tự động mở kết nối database.", "B. Spring tự động áp dụng proxy để chuyển đổi các Exception cấp thấp của Database (như SQLException) thành Exception cấp cao của Spring (DataAccessException).", "C. Cho phép class chạy đa luồng.", "D. Không có lợi ích nào ngoài việc đặt tên."],
      "B", "@Repository kích hoạt cơ chế PersistenceExceptionTranslationPostProcessor giúp chuẩn hóa các lỗi DB thành hệ thống lỗi chung của Spring.")

# ==========================================
# 13. jpa_fetch_type (Fetch Type: EAGER vs LAZY)
# ==========================================
add_q(85, "jpa_fetch_type", "concept", 
      "Fetch Type nào thực hiện việc trì hoãn tải dữ liệu quan hệ cho đến khi đối tượng liên kết thực sự được truy cập (gọi hàm getter)?",
      ["A. FetchType.EAGER", "B. FetchType.LAZY", "C. FetchType.DYNAMIC", "D. FetchType.DEFAULT"],
      "B", "FetchType.LAZY trì hoãn việc tải dữ liệu từ DB lên bộ nhớ cho tới khi phương thức getter của tập quan hệ đó được gọi.")

add_q(86, "jpa_fetch_type", "comparison", 
      "Sự khác biệt mặc định về FetchType giữa các mối quan hệ sở hữu đơn (@ManyToOne) và quan hệ bộ sưu tập (@OneToMany) là gì?",
      ["A. Cả hai đều mặc định là LAZY.", "B. @ManyToOne mặc định là EAGER, còn @OneToMany mặc định là LAZY.", "C. @ManyToOne mặc định là LAZY, còn @OneToMany mặc định là EAGER.", "D. Cả hai đều mặc định là EAGER."],
      "B", "Các quan hệ trỏ tới 1 thực thể đơn lẻ (@ManyToOne, @OneToOne) mặc định tải ngay (EAGER). Các quan hệ trỏ tới 1 danh sách (@OneToMany, @ManyToMany) mặc định tải trì hoãn (LAZY) để tránh nghẽn bộ nhớ.")

add_q(87, "jpa_fetch_type", "situation", 
      "Một thực thể `Order` chứa danh sách 10,000 thực thể `OrderDetail`. Để tránh việc mỗi lần lấy thông tin đơn hàng hệ thống phải load toàn bộ chi tiết hóa đơn khổng lồ lên RAM, bạn chọn FetchType như thế nào cho thuộc tính danh sách chi tiết?",
      ["A. FetchType.EAGER", "B. FetchType.LAZY", "C. Không dùng ORM, truy vấn SQL thủ công", "D. Đặt thuộc tính transient"],
      "B", "Sử dụng FetchType.LAZY là bắt buộc cho các danh sách lớn để tránh truy vấn thừa thãi khi chỉ cần thông tin tóm tắt của Order.")

add_q(88, "jpa_fetch_type", "blank", 
      "Khi truy cập một thuộc tính quan hệ cấu hình FetchType.LAZY ngoài phạm vi giao dịch (sau khi EntityManager/Session đã đóng), Hibernate sẽ ném ra ngoại lệ `______`.",
      ["A. NullPointerException", "B. LazyInitializationException", "C. SQLException", "D. TransactionRequiredException"],
      "B", "LazyInitializationException xảy ra vì Session quản lý kết nối CSDL của thực thể đã bị đóng, khiến Hibernate không thể thực hiện câu lệnh SQL bổ sung để nạp dữ liệu trì hoãn.")

add_q(89, "jpa_fetch_type", "process", 
      "Quy trình thực thi SQL của Hibernate khi truy vấn thực thể cha có chứa quan hệ con EAGER vs LAZY như thế nào?",
      ["A. EAGER: 1 câu SQL JOIN (hoặc SELECT liên tục); LAZY: chỉ chạy 1 câu SELECT cha, câu SELECT con chỉ chạy khi gọi getter", "B. LAZY chạy trước, EAGER chạy sau", "C. Cả hai đều chạy 2 câu lệnh SQL cùng lúc", "D. Không chạy câu lệnh SQL nào"],
      "A", "EAGER tải toàn bộ dữ liệu con ngay lập tức trong lần truy vấn đầu tiên. LAZY trì hoãn câu truy vấn lấy danh sách con cho tới khi code gọi hàm lấy dữ liệu con (ví dụ: parent.getChildren()).")

add_q(90, "jpa_fetch_type", "bug", 
      "Mã nguồn của bạn liên tục ném ra lỗi `LazyInitializationException` khi render giao diện ở tầng View (HTML). Cách khắc phục an toàn và tối ưu nhất là gì?",
      ["A. Chuyển tất cả quan hệ thành FetchType.EAGER.", "B. Đảm bảo dữ liệu quan hệ được nạp đầy đủ trong phạm vi Transaction bằng cách sử dụng JOIN FETCH trong truy vấn JPQL hoặc sử dụng EntityGraph.", "C. Tăng thời gian sống của session lên vô hạn.", "D. Bỏ qua không hiển thị dữ liệu đó nữa."],
      "B", "Sử dụng JOIN FETCH trong câu truy vấn JPQL cho phép nạp chủ động dữ liệu quan hệ LAZY ngay trong khi Session còn mở, tránh chuyển toàn bộ sang EAGER gây chậm hệ thống.")

add_q(91, "jpa_fetch_type", "code", 
      "Cho định nghĩa thuộc tính sau:\n\n@ManyToOne(fetch = FetchType.LAZY)\n@JoinColumn(name = \"dept_id\")\nprivate Department department;\n\nKhi chạy lệnh `Employee emp = em.find(Employee.class, 1L)`, Hibernate sẽ tạo ra đối tượng department kiểu gì để gán cho Employee?",
      ["A. Một đối tượng Department thật đầy đủ dữ liệu.", "B. Đối tượng Proxy (Department$HibernateProxy) rỗng chỉ chứa khóa chính id.", "C. Gán giá trị null.", "D. Lỗi ClassCastException"],
      "B", "Hibernate tạo ra một đối tượng Proxy kế thừa từ Department chứa id để gán vào Employee. Dữ liệu thật chỉ được tải từ DB khi gọi các getter phi-id (ví dụ: department.getName()).")

# ==========================================
# 14. jpa_entity_lifecycle (Vòng đời Entity trong JPA)
# ==========================================
add_q(92, "jpa_entity_lifecycle", "concept", 
      "Trạng thái nào của Entity đại diện cho đối tượng đã liên kết với một dòng trong DB và đang được quản lý bởi Persistence Context?",
      ["A. Transient", "B. Managed", "C. Detached", "D. Removed"],
      "B", "Trạng thái Managed chỉ định thực thể đang chịu sự quản lý trực tiếp của Persistence Context (EntityManager).")

add_q(93, "jpa_entity_lifecycle", "comparison", 
      "Sự khác biệt lớn nhất về hành vi giữa thực thể ở trạng thái Managed và Detached khi ta gọi các phương thức setter thay đổi giá trị thuộc tính của chúng là gì?",
      ["A. Managed sẽ ném lỗi, Detached thì không.", "B. Thay đổi trên Managed được tự động đồng bộ xuống DB khi commit (Dirty Checking), còn thay đổi trên Detached sẽ bị bỏ qua và không tự động lưu.", "C. Detached tự động xóa khỏi database.", "D. Không có sự khác biệt."],
      "B", "EntityManager theo dõi mọi thay đổi trên đối tượng Managed và đồng bộ tự động xuống DB. Đối với đối tượng Detached, EntityManager đã ngắt quản lý nên mọi thay đổi thuộc tính chỉ có hiệu lực trên bộ nhớ JVM.")

add_q(94, "jpa_entity_lifecycle", "situation", 
      "Bạn đọc một đối tượng `User` từ database ra, sau đó đóng phiên làm việc. Bạn thay đổi email của User này và muốn lưu cập nhật đó vào DB ở một phiên làm việc mới. Bạn nên sử dụng phương thức nào của EntityManager?",
      ["A. em.persist(user)", "B. em.merge(user)", "C. em.remove(user)", "D. em.refresh(user)"],
      "B", "Lệnh em.merge() được thiết kế để đưa một thực thể bị tách rời (Detached) trở lại trạng thái được quản lý (Managed) bằng cách sao chép các thay đổi vào một thực thể Managed mới tra cứu từ DB.")

add_q(95, "jpa_entity_lifecycle", "blank", 
      "Một thực thể mới được tạo bằng từ khóa `new` và chưa có giá trị định danh ID trong database được gọi là thực thể ở trạng thái ______.",
      ["A. Managed", "B. Transient", "C. Detached", "D. Removed"],
      "B", "Transient là trạng thái sơ khởi của thực thể: mới được tạo trên RAM, chưa có khóa chính và chưa liên kết với EntityManager.")

add_q(96, "jpa_entity_lifecycle", "process", 
      "Quy trình chuyển đổi trạng thái của Entity từ khi tạo mới đến khi xóa khỏi DB diễn ra như thế nào?",
      ["A. Transient -> Managed -> Removed -> Bị xóa khỏi DB (khi commit)", "B. Detached -> Transient -> Managed", "C. Managed -> Transient -> Detached", "D. Transient -> Detached -> Removed"],
      "A", "Quy trình chuẩn: Tạo mới (Transient) -> persistent/find (Managed) -> remove (Removed) -> xóa thực tế khỏi DB khi commit transaction.")

add_q(97, "jpa_entity_lifecycle", "bug", 
      "Lỗi `PersistentObjectException` xảy ra khi gọi phương thức em.persist(entity). Nguyên nhân do đâu?",
      ["A. Do thực thể không có annotation @Entity.", "B. Do thực thể ở trạng thái Transient nhưng đã được gán sẵn giá trị khóa chính ID thủ công (trong khi cấu hình ID là tự tăng IDENTITY).", "C. Do database bị khóa.", "D. Do session bị timeout."],
      "B", "persist() yêu cầu đối tượng phải là Transient hoàn toàn (chưa có ID). Nếu đối tượng đã có sẵn ID, Hibernate nghĩ rằng đối tượng này đã tồn tại và báo lỗi.")

add_q(98, "jpa_entity_lifecycle", "code", 
      "Xem đoạn mã xử lý sau:\n\nUser user = em.find(User.class, 1L);\nuser.setName(\"Nam\");\nem.clear();\nuser.setName(\"An\");\n// commit transaction\n\nTên của User trong database sau khi commit là gì?",
      ["A. Nam", "B. An", "C. Không thay đổi", "D. Gây lỗi Exception sập ứng dụng"],
      "A", "Sau khi set \"Nam\", lệnh em.clear() đưa mọi thực thể Managed (bao gồm user) về trạng thái Detached. Do đó lệnh set \"An\" tiếp theo không được đồng bộ xuống DB. Kết quả DB lưu tên \"Nam\".")

# ==========================================
# 15. jpa_transaction (JPA Transaction & @Transactional)
# ==========================================
add_q(99, "jpa_transaction", "concept", 
      "Annotation nào của Spring cung cấp cơ chế quản lý giao dịch khai báo (Declarative Transaction Management)?",
      ["A. @Transaction", "B. @Transactional", "C. @PersistenceContext", "D. @Rollback"],
      "B", "@Transactional được sử dụng để Spring tự động tạo các transaction nghiệp vụ bao quanh phương thức hoặc class.")

add_q(100, "jpa_transaction", "comparison", 
      "Sự khác biệt về hành vi Rollback mặc định của @Transactional giữa Unchecked Exception và Checked Exception là gì?",
      ["A. Cả hai đều tự động rollback.", "B. @Transactional tự động rollback với Unchecked Exception, nhưng mặc định không rollback với Checked Exception (vẫn commit bình thường).", "C. @Transactional chỉ rollback với Checked Exception.", "D. Cả hai đều không tự động rollback."],
      "B", "Mặc định, Spring chỉ tự động rollback khi có RuntimeException hoặc Error ném ra. Với các ngoại lệ kế thừa trực tiếp từ Exception (Checked Exception), Spring vẫn tiến hành commit trừ khi cấu hình rollbackFor rõ ràng.")

add_q(101, "jpa_transaction", "situation", 
      "Phương thức chuyển tiền của bạn cần rollback nếu xảy ra ngoại lệ `IOException` (là một Checked Exception). Bạn phải cấu hình annotation `@Transactional` như thế nào?",
      ["A. @Transactional", "B. @Transactional(rollbackFor = IOException.class)", "C. @Transactional(noRollbackFor = IOException.class)", "D. @Transactional(readOnly = true)"],
      "B", "Cấu hình rollbackFor định nghĩa rõ ràng các Checked Exception nào sẽ kích hoạt cơ chế rollback tự động.")

add_q(102, "jpa_transaction", "blank", 
      "Thuộc tính thiết lập mức độ cô lập dữ liệu của giao dịch trong @Transactional có tên tiếng Anh là `______`.",
      ["A. Propagation", "B. Isolation", "C. ReadOnly", "D. Timeout"],
      "B", "Isolation cấu hình mức độ cô lập để tránh các hiện tượng đọc dữ liệu rác (Dirty Read, Non-repeatable Read, Phantom Read).")

add_q(103, "jpa_transaction", "process", 
      "Quy trình xử lý giao dịch bằng cơ chế AOP Proxy của Spring đối với phương thức @Transactional diễn ra như thế nào?",
      ["A. Bắt đầu Transaction -> Chạy phương thức -> Commit (nếu thành công) hoặc Rollback (nếu ném Exception phù hợp) -> Đóng kết nối", "B. Chạy phương thức -> Bắt đầu Transaction -> Commit", "C. Commit -> Bắt đầu Transaction -> Chạy phương thức", "D. Bắt đầu -> Đóng kết nối -> Chạy phương thức"],
      "A", "Spring tạo một lớp proxy bọc ngoài: mở connection, khởi tạo transaction, chạy code của bạn. Nếu code ném RuntimeException -> rollback, ngược lại -> commit, cuối cùng đóng connection.")

add_q(104, "jpa_transaction", "bug", 
      "Tại sao khi gọi phương thức `@Transactional` nội bộ từ một phương thức khác trong cùng một class (Self-invocation), transaction lại không thể kích hoạt và không thực hiện rollback khi có lỗi?",
      ["A. Do CSDL không hỗ trợ transaction nội bộ.", "B. Vì cơ chế AOP của Spring hoạt động dựa trên Proxy. Khi gọi nội bộ (lệnh `this.method()`), request không đi qua lớp Proxy bọc ngoài của Spring nên các thiết lập giao dịch bị bỏ qua hoàn toàn.", "C. Do Java cấm gọi hàm nội bộ.", "D. Do thiếu file cấu hình."],
      "B", "Spring tiêm proxy để quản lý giao dịch. Gọi hàm nội bộ trực tiếp bỏ qua lớp proxy này, khiến các annotation cấu hình trên phương thức được gọi không có tác dụng.")

add_q(105, "jpa_transaction", "code", 
      "Xem đoạn mã sau:\n\n@Transactional(propagation = Propagation.REQUIRES_NEW)\npublic void updateStatus() { ... }\n\nÝ nghĩa của cấu hình `Propagation.REQUIRES_NEW` là gì?",
      ["A. Luôn luôn tái sử dụng transaction hiện có.", "B. Luôn luôn treo transaction hiện tại (nếu có) để tạo một transaction hoàn toàn mới độc lập.", "C. Không chạy trong transaction.", "D. Ném Exception nếu có transaction đang chạy."],
      "B", "REQUIRES_NEW tạo giao dịch độc lập mới. Giao dịch cha phía ngoài (nếu có) bị tạm dừng và không bị ảnh hưởng bởi kết quả commit/rollback của giao dịch mới này.")

# ==========================================
# 16. jpa_nplus1_problem (N+1 Query)
# ==========================================
add_q(106, "jpa_nplus1_problem", "concept", 
      "Hiện tượng N+1 Query trong Hibernate được định nghĩa là gì?",
      ["A. Lỗi xảy ra khi chèn thêm N+1 bản ghi mới vào bảng.", "B. Tình huống lấy danh sách N bản ghi cha, và ứng dụng chạy thêm N câu truy vấn SELECT phụ để lấy dữ liệu con liên quan của từng cha.", "C. Lỗi tràn bộ nhớ cache cấp 2.", "D. Truy vấn vượt quá giới hạn số lượng kết nối của database pool."],
      "B", "N+1 query mô tả sự suy giảm hiệu năng khi thay vì dùng 1 câu SQL JOIN, Hibernate chạy 1 câu SELECT cha và chạy thêm N câu SELECT con riêng biệt trong vòng lặp.")

add_q(107, "jpa_nplus1_problem", "comparison", 
      "Khắc phục N+1 query bằng JOIN FETCH khác biệt gì so với JOIN thường trong JPQL?",
      ["A. JOIN FETCH chỉ chạy trên MySQL, JOIN thường chạy trên mọi DB.", "B. JOIN FETCH yêu cầu Hibernate nạp và ánh xạ dữ liệu bảng liên quan vào đối tượng Java ngay lập tức, còn JOIN thường chỉ lọc dữ liệu ở câu lệnh SQL nhưng không tự nạp dữ liệu con.", "C. JOIN thường nhanh hơn JOIN FETCH.", "D. Không có sự khác biệt."],
      "B", "JOIN FETCH chỉ định rõ cho Hibernate vừa thực hiện phép join ở DB vừa khởi tạo nạp đầy đủ dữ liệu cho thực thể con liên quan, tránh LazyInitializationException và N+1.")

add_q(108, "jpa_nplus1_problem", "situation", 
      "Ứng dụng của bạn bị chậm nghiêm trọng khi hiển thị danh sách 50 lớp học kèm theo danh sách học sinh của mỗi lớp. Log SQL hiển thị 51 câu lệnh SELECT. Giải pháp tối ưu nhất để xử lý vấn đề này là gì?",
      ["A. Chuyển quan hệ học sinh thành EAGER.", "B. Thay đổi câu truy vấn JPQL từ \"FROM Class\" thành \"SELECT c FROM Class c JOIN FETCH c.students\".", "C. Sử dụng Thread.sleep để giảm tải cho DB.", "D. Tăng cấu hình RAM cho server."],
      "B", "Sử dụng câu truy vấn JOIN FETCH gom tất cả dữ liệu lớp và học sinh vào duy nhất 1 câu SELECT JOIN duy nhất, giảm số lượng câu truy vấn từ 51 xuống 1.")

add_q(109, "jpa_nplus1_problem", "blank", 
      "Để giải quyết lỗi N+1 bằng cách cấu hình số lượng đối tượng con được nạp trước theo từng lô (batching), ta dùng annotation `@______` của Hibernate.",
      ["A. BatchSize", "B. FetchSize", "C. LazyCollection", "D. OrderColumn"],
      "A", "Annotation @BatchSize cấu hình nạp dữ liệu con theo lô (ví dụ kích thước 20), giúp giảm số lượng câu truy vấn phụ xuống còn N/BatchSize.")

add_q(110, "jpa_nplus1_problem", "process", 
      "Quy trình xuất hiện lỗi N+1 Query diễn ra như thế nào trong vòng lặp?",
      ["A. Ứng dụng SELECT cha -> Duyệt vòng lặp cha -> Gọi cha.getCon() -> Hibernate tự động chạy thêm 1 câu SELECT con cho mỗi dòng cha -> Tạo ra N câu lệnh SELECT con", "B. Ứng dụng chèn dữ liệu -> DB báo lỗi -> Rollback", "C. SELECT con -> SELECT cha -> Trả kết quả", "D. Chạy Tomcat -> Quét Component -> Lỗi CSDL"],
      "A", "Khi duyệt danh sách N thực thể cha và gọi thuộc tính con đang ở chế độ LAZY, với mỗi vòng lặp, Hibernate phải thực thi thêm 1 câu truy vấn để lấy dữ liệu con tương ứng.")

add_q(111, "jpa_nplus1_problem", "bug", 
      "Tại sao chuyển FetchType thành EAGER không giúp khắc phục triệt để lỗi N+1 Query khi sử dụng truy vấn JPQL/HQL thông thường?",
      ["A. Vì EAGER bị cấm sử dụng trong JPQL.", "B. Vì khi thực thi JPQL dạng \"FROM Parent\", Hibernate phân tích câu lệnh dạng text này trước và chạy SELECT lấy danh sách Parent. Sau đó, nó thấy quan hệ là EAGER nên tiếp tục chạy thêm N câu SELECT con để nạp dữ liệu lập tức.", "C. Do Driver JDBC không hỗ trợ.", "D. Do database không có khóa ngoại."],
      "B", "Truy vấn JPQL/HQL thuần túy bỏ qua cấu hình EAGER trong bước phân tích câu lệnh đầu tiên, dẫn đến việc vẫn chạy SELECT cha trước, sau đó mới chạy tiếp các SELECT con để thỏa mãn thuộc tính EAGER.")

add_q(112, "jpa_nplus1_problem", "code", 
      "Quan sát định nghĩa sau:\n\n@EntityGraph(attributePaths = {\"employees\"})\n@Query(\"SELECT d FROM Department d\")\nList<Department> findAllWithEmployees();\n\nSử dụng `@EntityGraph` ở đây có tác dụng gì?",
      ["A. Vẽ biểu đồ quan hệ thực thể.", "B. Chỉ đạo cho JPA/Hibernate thực hiện JOIN FETCH để lấy danh sách Department cùng Employee trong 1 query duy nhất, tương tự JOIN FETCH nhưng khai báo dạng declarative.", "C. Khóa bảng dữ liệu lại.", "D. Xóa dữ liệu thừa."],
      "B", "@EntityGraph cung cấp giải pháp khai báo các thuộc tính cần tải sớm (fetch plan) trực tiếp trên phương thức Repository để JPA tự động JOIN bảng chống lỗi N+1.")

# ==========================================
# 17. jpa_orm_languages (JPA, ORM, JPQL, HQL)
# ==========================================
add_q(113, "jpa_orm_languages", "concept", 
      "Đâu là đặc tả tiêu chuẩn (Specification) định nghĩa các quy tắc ánh xạ đối tượng sang CSDL quan hệ trong hệ sinh thái Java?",
      ["A. Hibernate", "B. JPA (Java Persistence API)", "C. JDBC", "D. Spring Data JPA"],
      "B", "JPA là tập hợp các giao diện và quy chuẩn đặc tả tiêu chuẩn chung. Hibernate là framework triển khai cụ thể (provider) của JPA.")

add_q(114, "jpa_orm_languages", "comparison", 
      "Điểm khác biệt chính giữa ngôn ngữ truy vấn JPQL/HQL và ngôn ngữ SQL truyền thống là gì?",
      ["A. SQL truy vấn nhanh hơn JPQL.", "B. SQL truy vấn trên bảng và cột của CSDL, còn JPQL/HQL truy vấn hướng đối tượng dựa trên các Entity và thuộc tính của Entity Java.", "C. JPQL chỉ chạy được trên Oracle Database.", "D. SQL không hỗ trợ mệnh đề WHERE."],
      "B", "JPQL/HQL hoạt động trên mô hình đối tượng (class và thuộc tính Java), giúp câu truy vấn độc lập với hệ quản trị CSDL vật lý phía dưới.")

add_q(115, "jpa_orm_languages", "situation", 
      "Bạn cần viết câu lệnh truy vấn tìm danh sách các thực thể `Book` có thuộc tính `price` lớn hơn 100. Viết câu truy vấn JPQL như thế nào là đúng chuẩn?",
      ["A. SELECT * FROM books WHERE price > 100", "B. SELECT b FROM Book b WHERE b.price > 100", "C. FROM Book WHERE book_price > 100", "D. Book.findAll(price > 100)"],
      "B", "Cú pháp JPQL chuẩn: truy vấn thực thể Book (chữ hoa đầu) bí danh b và thuộc tính b.price: `SELECT b FROM Book b WHERE b.price > 100`.")

add_q(116, "jpa_orm_languages", "blank", 
      "Thư viện của Spring Boot giúp bọc các EntityManager của JPA và tự động sinh mã SQL cho các interface Repository có tên là `Spring Data ______`.",
      ["A. JDBC", "B. Rest", "C. JPA", "D. Hibernate"],
      "C", "Spring Data JPA cung cấp các lớp trừu tượng hóa mạnh mẽ giúp tự sinh câu truy vấn CSDL từ tên phương thức định nghĩa trong interface Repository.")

add_q(117, "jpa_orm_languages", "process", 
      "Quy trình thực thi một câu truy vấn JPQL diễn ra như thế nào trong Hibernate?",
      ["A. Trình duyệt gửi SQL -> DB chạy trực tiếp", "B. JPQL -> Hibernate dịch sang SQL tương ứng của DB đang dùng -> Gửi SQL qua JDBC -> DB thực thi -> ResultSet -> Ánh xạ thành Entity Java -> Trả kết quả", "C. Dịch JPQL sang mã máy -> Chạy trực tiếp", "D. Không có quy trình dịch chuyển nào"],
      "B", "Hibernate đóng vai trò biên dịch câu truy vấn hướng đối tượng JPQL sang tiếng SQL chuẩn của CSDL hiện tại (thông qua cấu hình Dialect) trước khi gửi thực thi.")

add_q(118, "jpa_orm_languages", "bug", 
      "Lỗi `QuerySyntaxException: XXX is not mapped` khi thực hiện câu truy vấn JPQL/HQL là do nguyên nhân gì?",
      ["A. Do bảng XXX chưa được tạo trong CSDL.", "B. Do bạn sử dụng tên bảng vật lý trong DB thay vì sử dụng tên lớp Entity Java được cấu hình trong code.", "C. Do thiếu kết nối mạng.", "D. Do lỗi thư viện Java."],
      "B", "JPQL chỉ hiểu tên của các Entity Class được ánh xạ. Việc viết nhầm tên bảng vật lý (ví dụ: SELECT u FROM users u thay vì SELECT u FROM User u) sẽ ném lỗi Class chưa được mapped.")

add_q(119, "jpa_orm_languages", "code", 
      "Xem đoạn mã truy vấn sau:\n\nQuery query = em.createQuery(\"SELECT count(u) FROM User u\");\nLong total = (Long) query.getSingleResult();\n\nPhương thức `getSingleResult()` sẽ ném ra ngoại lệ gì nếu không tìm thấy bản ghi nào khớp trong Database?",
      ["A. Trả về null bình thường.", "B. Ném ngoại lệ NoResultException.", "C. Trả về giá trị 0.", "D. Ném NullPointerException."],
      "B", "Đối với các truy vấn trả về 1 kết quả duy nhất, `getSingleResult()` bắt buộc phải tìm thấy đúng 1 bản ghi. Nếu không có bản ghi nào khớp, nó sẽ ném ra `NoResultException`.")

# Output questions database
questions_path = "c:/Users/DELL/Downloads/ontap_html/data/java/questions.json"
with open(questions_path, "w", encoding="utf-8") as f:
    json.dump(questions_pool, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(questions_pool)} questions into {questions_path}!")
