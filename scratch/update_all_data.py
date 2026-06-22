# -*- coding: utf-8 -*-
import json
import os

# Base paths
root_dir = "C:/Users/DELL/Downloads/ontap_html"
data_java_dir = os.path.join(root_dir, "data/java")
data_py_dir = os.path.join(root_dir, "data/python")
pdf_java_dir = os.path.join(root_dir, "pdf/java-on-tap")
pdf_py_dir = os.path.join(root_dir, "pdf/python-on-tap")

os.makedirs(pdf_java_dir, exist_ok=True)
os.makedirs(pdf_py_dir, exist_ok=True)

# --------------------------------------------------------------------------
# PART 1: JAVA DETAILED KNOWLEDGE DATA
# --------------------------------------------------------------------------
java_knowledge = [
  {
    "topicId": "servlet_lifecycle",
    "title": "Vòng đời Servlet (Servlet Lifecycle)",
    "content": """Vòng đời của một Servlet được quản lý hoàn toàn bởi Servlet Container (Web Container như Tomcat, Jetty). Quy trình này bắt đầu từ lúc nạp Servlet vào bộ nhớ cho đến khi Servlet bị hủy bỏ.

1. CÁC GIAI ĐOẠN VÒNG ĐỜI VÀ PHƯƠNG THỨC CHÍNH:
• Khởi tạo & Cấu hình - init(ServletConfig config) và init():
  - Khi có request đầu tiên gửi đến (hoặc khi server startup nếu cấu hình <load-on-startup>), Container nạp class Servlet, tạo một instance và gọi init(ServletConfig).
  - Phương thức này chỉ được gọi duy nhất 1 lần trong toàn bộ vòng đời của Servlet instance.
  - Sử dụng init() để khởi tạo các tài nguyên dùng chung lâu dài (ví dụ: thiết lập database connection, nạp file cấu hình). Điều này tránh việc kết nối lặp đi lặp lại ở mỗi request, giúp tối ưu hóa hiệu năng hệ thống.
• Xử lý Request - service(ServletRequest req, ServletResponse res):
  - Với mỗi request gửi tới Servlet, Container tạo một luồng (thread) mới và gọi phương thức service().
  - service() chịu trách nhiệm tiếp nhận request, ép kiểu sang HTTP ServletRequest/Response, phân tích phương thức HTTP (GET, POST, PUT, DELETE,...) và điều hướng đến các phương thức tương ứng như doGet(), doPost(), doPut(), doDelete(),...
• Hủy bỏ Servlet - destroy():
  - Trước khi tắt ứng dụng hoặc gỡ bỏ Servlet khỏi Container, destroy() được gọi duy nhất 1 lần.
  - Nhiệm vụ: Giải phóng các tài nguyên hệ thống (đóng database connection, đóng socket, ghi log cuối cùng).

2. PHẦN NÂNG CAO & CHI TIẾT CHUYÊN SÂU:
• init() vs init(ServletConfig config):
  - GenericServlet triển khai interface Servlet và cung cấp hai phiên bản init: `init(ServletConfig config)` (phương thức gốc của interface) và `init()` (phương thức helper không tham số).
  - Khi override `init(ServletConfig config)`, lập trình viên BẮT BUỘC phải gọi `super.init(config)` ở dòng đầu tiên. Nếu quên gọi, tham chiếu ServletConfig sẽ không được gán vào GenericServlet, dẫn đến các lệnh gọi `getServletConfig()` hay `getServletContext()` sau đó ném ra lỗi `NullPointerException`.
  - Khuyến nghị: Chỉ nên override phương thức không tham số `init()` để tránh lỗi quên gọi super.
• Cơ chế Singleton & Đa luồng (Thread-safety):
  - Container mặc định chỉ khởi tạo duy nhất một đối tượng (Single Instance) của mỗi lớp Servlet đã khai báo cho toàn bộ ứng dụng (Singleton pattern).
  - Khi có nhiều request đồng thời, Container tạo nhiều Thread chạy song song trên cùng một instance này.
  - Do đó, Servlet KHÔNG AN TOÀN VỚI LUỒNG (NON-THREAD-SAFE). Nếu bạn khai báo một biến instance (biến thành viên của class) và thay đổi giá trị của nó trong doGet() hay doPost(), các thread sẽ xảy ra tranh chấp dữ liệu (Race Condition), dẫn đến kết quả ghi đè lung tung giữa các client khác nhau.
  - Biện pháp: Tuyệt đối không dùng biến instance để lưu trữ trạng thái request. Hãy dùng biến cục bộ bên trong các phương thức (doGet, doPost) vì biến cục bộ được lưu trên Stack riêng của mỗi Thread, đảm bảo an toàn luồng.""",
    "example": """import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.IOException;

public class SecureLifecycleServlet extends HttpServlet {
    // BIẾN INSTANCE NÀY KHÔNG AN TOÀN LUỒNG! 
    // Tránh dùng biến thành viên class để lưu trạng thái request
    private int unsafeRequestCount = 0; 

    @Override
    public void init() throws ServletException {
        // Khởi tạo tài nguyên dùng chung 1 lần duy nhất
        System.out.println("Servlet đã được khởi tạo và sẵn sàng.");
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) 
            throws ServletException, IOException {
        // Biến cục bộ an toàn luồng (mỗi Thread có Stack riêng)
        int localCount = 0; 
        
        synchronized(this) {
            unsafeRequestCount++; // Bảo vệ biến instance bằng block synchronized nếu bắt buộc sử dụng
        }
        
        resp.getWriter().println("Request count: " + unsafeRequestCount);
    }

    @Override
    public void destroy() {
        // Giải phóng tài nguyên
        System.out.println("Servlet bị hủy. Đang đóng tất cả kết nối.");
    }
}"""
  },
  {
    "topicId": "session_cookie",
    "title": "Phân biệt Session vs Cookie",
    "content": """HTTP là một giao thức không trạng thái (stateless), nghĩa là mỗi request gửi đi độc lập và server không tự động nhớ client là ai. Để duy trì trạng thái phiên làm việc của người dùng, ta sử dụng Cookie và Session.

1. BẢNG SO SÁNH COOKIE VÀ SESSION:
• Cookie:
  - Vị trí lưu trữ: Client-side (Trình duyệt của người dùng, dưới dạng tệp văn bản nhỏ).
  - Dung lượng: Rất hạn chế (tối đa 4KB mỗi cookie, tối đa 20-50 cookie mỗi domain).
  - Tính bảo mật: Thấp. Dữ liệu lưu dưới máy client dễ bị xem trộm, sửa đổi hoặc bị đánh cắp thông qua mã độc XSS.
  - Thời gian sống: Có thể cấu hình tồn tại lâu dài kể cả khi tắt máy (Persistent Cookie nhờ setMaxAge) hoặc biến mất ngay khi đóng trình duyệt (Session Cookie).
• Session:
  - Vị trí lưu trữ: Server-side (Trong bộ nhớ RAM hoặc cơ sở dữ liệu của máy chủ web).
  - Dung lượng: Không giới hạn lý thuyết (phụ thuộc vào cấu hình bộ nhớ của server).
  - Tính bảo mật: Cao. Chỉ có mã định danh duy nhất (Session ID) được gửi qua lại giữa Client và Server. Dữ liệu thực tế được giấu trên máy chủ.
  - Thời gian sống: Mặc định hết hạn sau khoảng 30 phút không hoạt động (Session timeout), hoặc hủy thủ công qua session.invalidate().

2. PHẦN NÂNG CAO & CHI TIẾT CHUYÊN SÂU:
• Cơ chế JSESSIONID:
  - Khi Client gửi request đầu tiên, Server gọi `request.getSession()`, Container tự động tạo một đối tượng HttpSession mới trên Server và tạo ra một mã ID ngẫu nhiên không thể đoán trước là JSESSIONID.
  - Server trả về client mã này trong HTTP response header dưới dạng một Cookie đặc biệt tên là `JSESSIONID`.
  - Trong các request tiếp theo, trình duyệt tự động đính kèm Cookie `JSESSIONID` này lên Server. Server đọc ID này, tra cứu đối tượng Session tương ứng trong bộ nhớ và nhận diện được phiên làm việc của client.
  - Nếu trình duyệt tắt chế độ lưu Cookie, JSESSIONID sẽ không được lưu lại. Kết quả là ở mỗi request tiếp theo, trình duyệt không gửi được ID này, Server coi đây là khách mới và liên tục tạo ra Session mới tinh, khiến người dùng bị logout liên tục. Để khắc phục khi tắt Cookie, ta phải dùng cơ chế URL Rewriting (nhúng ID vào URL qua `response.encodeURL()`).
• Các thuộc tính bảo mật của Cookie:
  - HttpOnly Flag: Rất quan trọng. Khi setHttpOnly(true), Cookie này sẽ KHÔNG thể truy cập hoặc đọc được từ các đoạn mã JavaScript chạy ở client (như document.cookie). Điều này ngăn chặn các cuộc tấn công Cross-Site Scripting (XSS) đánh cắp session token.
  - Secure Flag: Khi setSecure(true), Cookie chỉ được truyền tải qua các kết nối được mã hóa bảo mật HTTPS, không gửi qua HTTP thường, tránh bị nghe lén (Sniffing).""",
    "example": """// Tương tác Session & Cookie trong Servlet
protected void doGet(HttpServletRequest request, HttpServletResponse response) 
        throws ServletException, IOException {
    // 1. HttpSession (Server-side)
    HttpSession session = request.getSession(); // Tạo mới hoặc lấy session hiện tại
    session.setAttribute("userRole", "ADMIN");
    
    // 2. Tạo Cookie bảo mật (Client-side)
    Cookie jwtCookie = new Cookie("authToken", "secret_token_123");
    jwtCookie.setMaxAge(24 * 60 * 60); // Sống trong 1 ngày (Persistent Cookie)
    jwtCookie.setHttpOnly(true);       // Chống XSS (JavaScript không đọc được)
    jwtCookie.setSecure(true);         // Chỉ gửi qua HTTPS
    jwtCookie.setPath("/");            // Phạm vi toàn bộ ứng dụng
    
    response.addCookie(jwtCookie);
}"""
  },
  {
    "topicId": "genericservlet_httpservlet",
    "title": "GenericServlet vs HttpServlet",
    "content": """Servlet API cung cấp hai lớp abstract nền tảng kế thừa lẫn nhau để giúp lập trình viên xây dựng Servlet: GenericServlet và HttpServlet.

1. BẢNG SO SÁNH CHI TIẾT:
• GenericServlet:
  - Định nghĩa: Là một abstract class trực tiếp triển khai interface Servlet và ServletConfig.
  - Tính phụ thuộc giao thức: Độc lập giao thức (Protocol-independent). Có thể sử dụng cho bất kỳ giao thức mạng nào (như HTTP, SMTP, FTP, NNTP).
  - Phương thức chính cần override: `service(ServletRequest req, ServletResponse res)`. Đây là phương thức trừu tượng duy nhất bắt buộc phải viết lại.
• HttpServlet:
  - Định nghĩa: Là một abstract class kế thừa từ GenericServlet. Nó được thiết kế chuyên biệt.
  - Tính phụ thuộc giao thức: Phụ thuộc giao thức (Protocol-dependent), tối ưu riêng cho giao thức HTTP/HTTPS.
  - Phương thức chính: Đã ghi đè sẵn service() gốc của GenericServlet để tự động ép kiểu đối tượng Request/Response sang HttpServletRequest/HttpServletResponse, sau đó điều phối xử lý đến doGet(), doPost(), doPut(), doDelete(),... tùy theo HTTP Method của request.

2. PHẦN NÂNG CAO & CHI TIẾT CHUYÊN SÂU:
• Chuỗi gọi phương thức khi nhận Request:
  - Khi client gửi request (ví dụ POST) đến HttpServlet, Container gọi phương thức:
    `service(ServletRequest, ServletResponse)`
  - Phương thức này kiểm tra và ép kiểu sang HTTP, sau đó gọi phương thức overload nội bộ:
    `service(HttpServletRequest, HttpServletResponse)`
  - Phương thức này đọc HTTP Method (GET, POST, PUT, DELETE,...) và điều hướng gọi phương thức cụ thể tương ứng (ví dụ: `doPost(HttpServletRequest, HttpServletResponse)`).
• Ghi đè phương thức service():
  - Thông thường, ta không ghi đè service() mà chỉ ghi đè doGet(), doPost(),...
  - Nếu lập trình viên ghi đè service() trong HttpServlet và QUÊN gọi `super.service(request, response)`, logic phân tích method và điều hướng mặc định sẽ bị phá vỡ hoàn toàn. Kết quả là các phương thức doGet() hay doPost() tự viết sẽ không bao giờ được gọi.
  - Nếu ghi đè service() rỗng và không gọi super, ứng dụng sẽ không làm gì và trả về phản hồi trắng với status code 200 mặc định.""",
    "example": """// Kế thừa GenericServlet (FTP Servlet)
public class FtpReceiverServlet extends GenericServlet {
    @Override
    public void service(ServletRequest req, ServletResponse res) 
            throws ServletException, IOException {
        // Logic xử lý bản tin độc lập với HTTP
        res.getWriter().println("FTP Message Processed.");
    }
}

// Kế thừa HttpServlet (HTTP Web Servlet)
public class ProductServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) 
            throws ServletException, IOException {
        // Xử lý request GET
        resp.getWriter().println("Danh sách sản phẩm");
    }
}"""
  },
  {
    "topicId": "requestdispatcher",
    "title": "RequestDispatcher: forward() vs sendRedirect()",
    "content": """Khi cần chuyển hướng luồng xử lý từ một tài nguyên (Servlet/JSP) sang một tài nguyên khác, Servlet API hỗ trợ hai cơ chế hoàn toàn khác biệt: RequestDispatcher.forward() và HttpServletResponse.sendRedirect().

1. BẢNG SO SÁNH CHUYỂN HƯỚNG:
• RequestDispatcher.forward():
  - Cơ chế hoạt động: Chuyển tiếp hoàn toàn ở phía Server-side. Servlet hiện tại chuyển giao việc render response cho tài nguyên đích. Trình duyệt client không hề biết có sự chuyển hướng này.
  - Số lượng HTTP Request: Chỉ có 1 request duy nhất được gửi từ client. Đối tượng request và response được tái sử dụng và chuyển tiếp nguyên vẹn.
  - Thay đổi URL hiển thị: Không thay đổi. Trình duyệt vẫn hiển thị URL ban đầu.
  - Phạm vi đích: Chỉ chuyển tiếp được tới các tài nguyên nằm trong cùng ứng dụng Web.
• HttpServletResponse.sendRedirect():
  - Cơ chế hoạt động: Chuyển hướng ở phía Client-side. Server trả về HTTP response với mã trạng thái 302 (Redirect) và Location chứa URL mới. Trình duyệt nhận được phản hồi sẽ tự động gửi một request mới tới URL đó.
  - Số lượng HTTP Request: Có 2 request độc lập được gửi từ client. Request thứ hai luôn là HTTP GET. Đối tượng request cũ bị hủy, các attribute lưu trong request cũ sẽ bị mất (trả về null).
  - Thay đổi URL hiển thị: Có thay đổi. Thanh địa chỉ của trình duyệt đổi sang URL mới.
  - Phạm vi đích: Có thể chuyển tới bất cứ URL nào, kể cả website bên ngoài (ví dụ: google.com).

2. PHẦN NÂNG CAO & CHI TIẾT CHUYÊN SÂU:
• Lỗi IllegalStateException:
  - Ngoại lệ này xảy ra nếu bạn cố tình gọi forward() hoặc sendRedirect() sau khi response đã được ghi dữ liệu (commit) về client (ví dụ: đã ghi dữ liệu qua writer.write(), writer.flush(), hoặc response.flushBuffer()). Server không thể thực hiện chuyển hướng vì các luồng phản hồi và header đã được gửi đi và cam kết với client.
• Mẫu thiết kế PRG (Post-Redirect-Get):
  - Khi xử lý xong một Form POST (ví dụ thanh toán đơn hàng, thêm mới dữ liệu), nếu ta dùng `forward()` để chuyển sang trang thành công, khi người dùng nhấn F5 (Reload), trình duyệt sẽ gửi lại request POST đó một lần nữa. Điều này dẫn đến lỗi trùng lặp dữ liệu (thanh toán 2 lần, thêm 2 bản ghi trùng nhau).
  - Giải pháp: Áp dụng PRG. Sau khi xử lý POST thành công, gọi `sendRedirect()` sang trang thành công (GET). Khi người dùng nhấn F5, họ chỉ reload lại request GET trang thành công, không gây lặp lại dữ liệu POST.""",
    "example": """// Minh họa forward vs sendRedirect
protected void doPost(HttpServletRequest request, HttpServletResponse response) 
        throws ServletException, IOException {
    
    boolean loginSuccess = checkLogin(request);
    
    if (loginSuccess) {
        // Áp dụng Post-Redirect-Get để tránh lặp submit khi F5
        request.getSession().setAttribute("user", "An");
        response.sendRedirect("dashboard.jsp"); // URL thay đổi sang dashboard.jsp
    } else {
        // Forward để giữ nguyên dữ liệu lỗi và thông báo trong request
        request.setAttribute("errorMessage", "Sai mật khẩu!");
        RequestDispatcher rd = request.getRequestDispatcher("/login.jsp");
        rd.forward(request, response); // URL giữ nguyên, client không biết có forward
    }
}"""
  },
  {
    "topicId": "filter_api",
    "title": "Servlet Filter & web.xml",
    "content": """Filter (Bộ lọc) là đối tượng trung gian dùng để can thiệp, kiểm tra và xử lý các HTTP Request và Response trước khi chúng đi tới Servlet đích hoặc quay trở về Client.

1. VÒNG ĐỜI VÀ PHƯƠNG THỨC CỦA FILTER:
• init(FilterConfig filterConfig): Được gọi duy nhất 1 lần khi container khởi tạo Filter để nạp cấu hình.
• doFilter(ServletRequest request, ServletResponse response, FilterChain chain):
  - Phương thức xử lý chính cho mỗi request đi qua URL tương ứng.
  - BẮT BUỘC phải gọi câu lệnh `chain.doFilter(request, response)` để đẩy request đi tiếp tới Filter kế tiếp hoặc Servlet đích. Nếu không gọi, request sẽ bị chặn đứng tại filter đó vĩnh viễn (gây ra hiện tượng treo trang hoặc phản hồi trắng).
• destroy(): Được gọi 1 lần khi container gỡ bỏ filter để dọn dẹp tài nguyên.

2. PHẦN NÂNG CAO & CHI TIẾT CHUYÊN SÂU:
• Thứ tự thực thi của các Filter (Filter Ordering):
  - Trong cấu hình truyền thống `web.xml`, thứ tự thực thi các Filter được quyết định hoàn toàn bởi thứ tự khai báo của các thẻ `<filter-mapping>` từ trên xuống dưới trong file. Thẻ nào khai báo trước sẽ chạy trước. Thứ tự của thẻ `<filter>` không ảnh hưởng đến thứ tự chạy.
  - Đối với cấu hình bằng Annotation `@WebFilter`, thứ tự chạy mặc định không được xác định rõ ràng (thường theo thứ tự bảng chữ cái class). Để cấu hình thứ tự chính xác, ta nên dùng cấu hình XML hoặc trong Spring Boot sử dụng `@Order` hoặc class `FilterRegistrationBean`.
• Character Encoding Filter:
  - Một ứng dụng thực tế có hàng chục Servlet, nếu mỗi Servlet đều phải gọi `request.setCharacterEncoding("UTF-8")` ở đầu doGet/doPost thì rất lặp code.
  - Giải pháp tối ưu: Viết một Filter duy nhất chặn toàn bộ URL (`/*`) và đặt mã hóa ký tự UTF-8 cho cả request và response.
• Cấu hình Servlet/Filter:
  - Trước Java EE 6: Mọi Servlet/Filter phải khai báo thủ công trong file cấu hình `/WEB-INF/web.xml`.
  - Từ Java EE 6 trở đi: Hỗ trợ các Annotation như `@WebServlet` và `@WebFilter` giúp khai báo nhanh ngay trên code mà không cần file XML.""",
    "example": """// Custom Encoding Filter đặt tiếng Việt UTF-8 toàn bộ web
import jakarta.servlet.*;
import jakarta.servlet.annotation.WebFilter;
import java.io.IOException;

@WebFilter(urlPatterns = "/*") // Áp dụng cho mọi URL trong website
public class Utf8EncodingFilter implements Filter {
    
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {}

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // Đặt mã hóa UTF-8 trước khi request tới Servlet
        request.setCharacterEncoding("UTF-8");
        response.setCharacterEncoding("UTF-8");
        response.setContentType("text/html; charset=UTF-8");

        // Gọi chain.doFilter để request tiếp tục di chuyển sang Servlet đích
        chain.doFilter(request, response);
        
        // Code ở đây sẽ chạy sau khi Servlet xử lý xong và phản hồi đi ra ngoài
    }

    @Override
    public void destroy() {}
}"""
  },
  {
    "topicId": "jdbc_api",
    "title": "JDBC API",
    "content": """JDBC (Java Database Connectivity) là một API tiêu chuẩn của Java cho phép kết nối, thực thi các câu lệnh SQL và tương tác với các hệ quản trị cơ sở dữ liệu quan hệ (RDBMS).

1. QUY TRÌNH JDBC TIÊU CHUẨN:
• JDBC bao gồm 5 bước cơ bản:
  1. Nạp JDBC Driver tương ứng (Ví dụ: MySQL, PostgreSQL, SQL Server).
  2. Tạo đối tượng Connection bằng cách gọi `DriverManager.getConnection(url, username, password)`.
  3. Tạo đối tượng Statement hoặc PreparedStatement.
  4. Thực thi câu lệnh SQL (executeQuery đối với SELECT, executeUpdate đối với các lệnh DML).
  5. Đóng các tài nguyên Connection, Statement, ResultSet sau khi sử dụng để giải phóng bộ nhớ.

2. PHẦN NÂNG CAO & CHI TIẾT CHUYÊN SÂU:
• Statement vs PreparedStatement (Chống SQL Injection):
  - Statement: Thường dùng để thực thi các câu lệnh SQL tĩnh. Lập trình viên phải cộng chuỗi trực tiếp để chèn tham số. Điều này cực kỳ nguy hiểm vì tạo ra lỗ hổng SQL Injection (kẻ tấn công truyền các chuỗi như `' OR '1'='1` để bypass đăng nhập hoặc drop bảng).
  - PreparedStatement: Biên dịch trước câu lệnh SQL (pre-compile) có chứa các tham số động đại diện bằng dấu hỏi chấm `?`. Khi chạy, chỉ có tham số được gửi xuống DB. Cơ chế này tách biệt hoàn toàn mã SQL với dữ liệu đầu vào, giúp ngăn chặn triệt để SQL Injection và tăng hiệu năng thực thi khi chạy lại nhiều lần.
• CallableStatement:
  - Kế thừa PreparedStatement, chuyên dụng dùng để gọi các Stored Procedure và Functions đã được định nghĩa sẵn trong CSDL.
• executeQuery() vs executeUpdate():
  - `executeQuery()`: Dùng cho các câu lệnh truy vấn dữ liệu (SELECT). Trả về một đối tượng `ResultSet` chứa kết quả trả về. Ta duyệt qua ResultSet bằng vòng lặp `rs.next()`.
  - `executeUpdate()`: Dùng cho các câu lệnh thay đổi dữ liệu (INSERT, UPDATE, DELETE) hoặc định nghĩa cấu trúc (DDL). Trả về một số nguyên `int` đại diện cho số dòng bị ảnh hưởng trong database.
• Quản lý đóng tài nguyên và Connection Pool:
  - Cơ sở dữ liệu giới hạn số lượng kết nối đồng thời. Nếu bạn liên tục mở kết nối qua `DriverManager.getConnection()` trong vòng lặp mà quên không gọi close(), hệ thống sẽ nhanh chóng cạn kiệt kết nối của Database Pool (Out of Connections), gây treo toàn bộ ứng dụng.
  - Thứ tự đóng tài nguyên chuẩn để tránh rò rỉ bộ nhớ (Memory Leak): Đóng ResultSet trước -> Đóng Statement -> Đóng Connection (Đóng ngược lại với thứ tự mở). Nên sử dụng try-with-resources để tự động đóng tài nguyên kể cả khi xảy ra Exception.""",
    "example": """// Truy vấn JDBC an toàn sử dụng try-with-resources và PreparedStatement
String sql = "SELECT username, email FROM users WHERE role = ? AND active = ?";
try (Connection conn = DriverManager.getConnection(dbUrl, dbUser, dbPassword);
     PreparedStatement pstmt = conn.prepareStatement(sql)) {
     
    // Gán tham số an toàn (Chỉ mục bắt đầu từ 1)
    pstmt.setString(1, "ADMIN");
    pstmt.setBoolean(2, true);
    
    try (ResultSet rs = pstmt.executeQuery()) {
        while (rs.next()) {
            String name = rs.getString("username");
            String email = rs.getString("email");
            System.out.println("User: " + name + " - " + email);
        }
    } // Tự động đóng ResultSet
} catch (SQLException e) {
    e.printStackTrace();
} // Tự động đóng PreparedStatement và Connection"""
  },
  {
    "topicId": "springboot_autoconfig",
    "title": "Spring Boot Auto-configuration",
    "content": """Spring Boot giải quyết bài toán cấu hình cồng kềnh (boilerplate code) của Spring Framework truyền thống bằng cơ chế cấu hình tự động (Auto-configuration) theo triết lý 'Convention over Configuration'.

1. PHÂN TÍCH ANNOTATION @SpringBootApplication:
• Annotation này là sự kết hợp của 3 annotation cốt lõi:
  - `@SpringBootConfiguration`: Đánh dấu class cấu hình chính của ứng dụng (phiên bản đặc biệt của @Configuration).
  - `@EnableAutoConfiguration`: Kích hoạt cơ chế tự động quét classpath. Khi quét qua classpath, nếu thấy sự xuất hiện của một thư viện starter nào đó, nó sẽ tự động cấu hình các Bean mặc định tương ứng (Ví dụ: thấy thư viện `h2` trong classpath, nó tự động tạo Bean `DataSource` kết nối với H2 database).
  - `@ComponentScan`: Tự động tìm kiếm và đăng ký các Spring Beans (như `@Component`, `@Service`, `@Repository`, `@Controller`) vào trong Spring ApplicationContext.

2. PHẦN NÂNG CAO & CHI TIẾT CHUYÊN SÂU:
• Quy tắc Component Scanning:
  - Mặc định, `@ComponentScan` bắt đầu quét từ package chứa class có annotation `@SpringBootApplication` và toàn bộ các package con bên dưới nó.
  - Nếu lập trình viên đặt class chứa `@SpringBootApplication` ở package `com.example.app.main`, nhưng lại viết các class Controller ở package `com.example.controller` (không phải package con), Spring Boot sẽ không thể tìm thấy và đăng ký Controller đó. Kết quả là client gọi API sẽ nhận mã lỗi `404 Not Found`. Để xử lý, phải cấu hình quét rõ ràng `@ComponentScan("com.example")` hoặc dời class main ra package cha chung.
• Vô hiệu hóa Auto-configuration cụ thể:
  - Trong trường hợp ứng dụng khai báo thư viện starter kết nối DB nhưng chưa cấu hình thông số và không muốn ứng dụng bị crash khi start, ta có thể tắt cấu hình tự động kết nối DB bằng cách sử dụng thuộc tính `exclude` trong `@SpringBootApplication`: `@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})`. Hoặc khai báo trong file application.properties: `spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration`.
• spring-boot-starter-parent:
  - Là một file POM đặc biệt cung cấp tính năng quản lý phiên bản tập trung (Dependency Management). Nhờ kế thừa parent này, ta không cần khai báo thẻ `<version>` cho các thư viện starter của Spring, giúp tránh xung đột phiên bản và đảm bảo tính đồng bộ hệ thống.""",
    "example": """// Class chạy chính của dự án Spring Boot, loại bỏ DataSource Auto-config
package com.example.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;

@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})
public class DemoApplication {
    public static void main(String[] args) {
        // Khởi chạy ứng dụng: 
        // 1. Tạo Context -> 2. Quét Component -> 3. Chạy Auto-config -> 4. Start Tomcat nhúng
        SpringApplication.run(DemoApplication.class, args);
    }
}"""
  },
  {
    "topicId": "spring_mvc_flow",
    "title": "Luồng Request trong Spring MVC",
    "content": """Spring MVC hoạt động dựa trên mẫu thiết kế Front Controller, trong đó toàn bộ các yêu cầu HTTP Request gửi tới ứng dụng đều được tiếp nhận và xử lý qua một Servlet trung tâm điều phối gọi là DispatcherServlet.

1. LUỒNG XỬ LÝ HTTP REQUEST CHI TIẾT (8 BƯỚC):
Luồng xử lý HTTP Request trong Spring MVC diễn ra tuần tự như sau:
  1. Client gửi một HTTP request. **DispatcherServlet** (Front Controller) tiếp nhận request đầu tiên.
  2. **DispatcherServlet** tham chiếu sang **HandlerMapping** để tìm kiếm Controller (Handler) nào phù hợp xử lý request dựa trên URL.
  3. **HandlerMapping** trả về cho DispatcherServlet một đối tượng xử lý và danh sách các Interceptors đi kèm (gọi là **HandlerExecutionChain**).
  4. **DispatcherServlet** gửi Handler sang **HandlerAdapter** để thực thi phương thức xử lý của **Controller** tương ứng.
  5. **Controller** thực thi business logic và trả về một đối tượng **ModelAndView** (chứa tên View và dữ liệu Model) cho DispatcherServlet.
  6. **DispatcherServlet** chuyển giao View Name cho **ViewResolver** để dịch ra file template giao diện vật lý thực tế (ví dụ JSP, Thymeleaf).
  7. **View** thực hiện render dữ liệu Model vào giao diện HTML.
  8. **DispatcherServlet** gửi giao diện HTML hoàn chỉnh về cho client dưới dạng HTTP Response.

2. PHẦN NÂNG CAO & CHI TIẾT CHUYÊN SÂU:
• @Controller vs @RestController:
  - `@Controller`: Dùng cho ứng dụng Web truyền thống hiển thị giao diện HTML. Phương thức trong Controller trả về một String đại diện cho View Name. ViewResolver sẽ tìm kiếm file tương ứng (ví dụ: trả về "home" -> tìm file /templates/home.html).
  - `@RestController`: Dùng để xây dựng các Web API (RESTful API). `@RestController` thực chất là sự kết hợp của `@Controller` và `@ResponseBody`. Mọi phương thức bên trong RestController sẽ tự động ghi dữ liệu thô (JSON/XML) trực tiếp vào Response Body mà không qua ViewResolver.
  - Sự cố hiển thị View Name: Nếu bạn muốn trả về trang HTML "home.html" bằng cách return String "home", nhưng lại đánh dấu class bằng `@RestController` hoặc `@ResponseBody`, trình duyệt sẽ hiển thị trực tiếp chữ "home" dạng văn bản thô thay vì hiển thị giao diện trang chủ.""",
    "example": """// Minh họa @Controller vs @RestController trong Spring MVC

// 1. Controller trả về trang HTML (Giao diện)
@Controller
public class WebController {
    @GetMapping("/welcome")
    public String welcomePage(Model model) {
        model.addAttribute("message", "Chào mừng tới Spring MVC!");
        return "welcome"; // Gửi tới ViewResolver để tìm welcome.html
    }
}

// 2. RestController trả về dữ liệu thô JSON làm API
@RestController
@RequestMapping("/api/users")
public class UserApiController {
    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        return new User(id, "Bình An"); // Trả về JSON thô thẳng cho Client
    }
}"""
  },
  {
    "topicId": "spring_mvc_annotations",
    "title": "Spring MVC Annotations: @PathVariable vs @RequestParam",
    "content": """Trong Spring MVC, để trích xuất và liên kết dữ liệu từ HTTP Request gửi lên vào các tham số của phương thức xử lý trong Controller, ta thường sử dụng hai annotation phổ biến: @PathVariable và @RequestParam.

1. BẢNG SO SÁNH @PathVariable VÀ @RequestParam:
• @PathVariable:
  - Mục đích: Trích xuất giá trị trực tiếp từ các phân đoạn đường dẫn URL (URI Path Segment).
  - Định dạng URL ví dụ: `/api/users/15` -> Số 15 là Path Variable.
  - Sử dụng trong Rest API: Rất phù hợp để định danh một tài nguyên cụ thể (chứa ID sản phẩm, ID người dùng).
• @RequestParam:
  - Mục đích: Trích xuất dữ liệu từ các tham số truy vấn (Query Parameter) sau dấu hỏi chấm `?` trên URL, hoặc từ dữ liệu Form gửi lên (x-www-form-urlencoded).
  - Định dạng URL ví dụ: `/api/users?page=2&limit=10` -> Số 2 và 10 là Request Param.
  - Sử dụng trong Rest API: Rất phù hợp cho việc lọc dữ liệu, tìm kiếm, phân trang, hoặc nhận dữ liệu submit form đăng ký.

2. PHẦN NÂNG CAO & CHI TIẾT CHUYÊN SÂU:
• Thuộc tính 'required' và 'defaultValue' trong @RequestParam:
  - Mặc định, `@RequestParam` thiết lập thuộc tính `required = true`. Nếu client gửi request mà không đính kèm tham số này, Spring MVC sẽ từ chối xử lý và trả về mã lỗi `400 Bad Request` cho client.
  - Để cấu hình tham số này là tùy chọn và tránh lỗi 400, lập trình viên cần đặt `required = false` và nên gán thêm `defaultValue` (ví dụ: `defaultValue = "1"`).
• Trùng khớp tên biến:
  - Nếu tên biến phương thức trùng khớp hoàn toàn với tên biến khai báo trong mẫu đường dẫn URL (ví dụ: `/books/{id}` và tham số đầu vào là `Long id`), Spring Boot có thể tự động ánh xạ giá trị mà không cần ghi rõ tên trong dấu ngoặc kép như `@PathVariable("id")`. Tuy nhiên, viết rõ ràng vẫn là best practice để tránh lỗi khi nén code (obfuscation).""",
    "example": """// Sử dụng PathVariable và RequestParam trong Spring Controller
@RestController
@RequestMapping("/store")
public class StoreController {

    // URL: http://localhost:8080/store/products/125
    @GetMapping("/products/{prodId}")
    public Product getProduct(@PathVariable("prodId") Long id) {
        return productService.findById(id);
    }

    // URL: http://localhost:8080/store/products?category=laptop&page=1
    // Nếu thiếu category -> category = null. Nếu thiếu page -> page = 1
    @GetMapping("/products")
    public List<Product> searchProducts(
            @RequestParam(value = "category", required = false) String category,
            @RequestParam(value = "page", required = false, defaultValue = "1") int page) {
        return productService.search(category, page);
    }
}"""
  },
  {
    "topicId": "spring_filters",
    "title": "Các loại Filter trong Spring",
    "content": """Spring cung cấp các cơ chế bộ lọc (Filter) để chặn request trước khi vào Controller. Lập trình viên cần phân biệt 3 loại filter phổ biến trong hệ sinh thái Spring: Filter (interface gốc của Servlet), GenericFilterBean và OncePerRequestFilter.

1. PHÂN BIỆT 3 LOẠI FILTER:
• Servlet Filter (jakarta.servlet.Filter):
  - Định nghĩa: Là interface tiêu chuẩn của Servlet Specification.
  - Đặc điểm: Chạy độc lập ngoài Spring Context. Do đó, việc tiêm (inject) các Spring Bean như Service hay Repository vào trong Filter này gặp khó khăn và dễ bị null nếu không được cấu hình qua DelegatingFilterProxy.
• GenericFilterBean (Spring Framework):
  - Định nghĩa: Là một abstract class triển khai interface Filter của Servlet, do Spring cung cấp.
  - Đặc điểm: Giúp giảm boilerplate code. Nó tự động liên kết các tham số cấu hình khởi tạo (init-parameters) vào các thuộc tính Spring Bean. Tuy nhiên, nó vẫn có thể bị gọi lại nhiều lần cho một request nếu request đó được chuyển tiếp (forward) nội bộ.
• OncePerRequestFilter (Spring Framework):
  - Định nghĩa: Lớp abstract kế thừa từ GenericFilterBean.
  - Đặc điểm: Đảm bảo phương thức lọc `doFilterInternal` chỉ chạy ĐÚNG MỘT LẦN DUY NHẤT cho mỗi Request gửi tới ứng dụng, bất kể có các hoạt động forward hoặc include nội bộ diễn ra sau đó. Đây là class được khuyến kh nghị sử dụng nhiều nhất khi viết Filter tùy chỉnh trong Spring Security (ví dụ filter xác thực JWT).

2. PHẦN NÂNG CAO & CHI TIẾT CHUYÊN SÂU:
• Đăng ký Custom Filter trong Spring Boot:
  - Để đăng ký một Custom Filter hoạt động mà không cần file cấu hình `web.xml`, ta định nghĩa class filter đó kế thừa OncePerRequestFilter và đăng ký nó như một `@Component`. Spring Boot sẽ tự động đăng ký nó vào Filter Chain toàn cục.
  - Để kiểm soát thứ tự chạy (Order) hoặc giới hạn URL mapping cụ thể, ta nên cấu hình class đó qua Bean `FilterRegistrationBean` trong một class `@Configuration`.
• Thứ tự thực thi của Filters và Interceptors:
  - Khi có request đi vào ứng dụng: Request -> Các Servlet Filter tiêu chuẩn -> Spring Security Filter Chain (đặc biệt OncePerRequestFilter) -> HandlerInterceptor -> Controller.""",
    "example": """// Đăng ký Custom Filter bằng FilterRegistrationBean
@Configuration
public class FilterConfig {

    @Bean
    public FilterRegistrationBean<JwtAuthenticationFilter> loggingFilter() {
        FilterRegistrationBean<JwtAuthenticationFilter> registrationBean = new FilterRegistrationBean<>();
        
        registrationBean.setFilter(new JwtAuthenticationFilter());
        registrationBean.addUrlPatterns("/api/v1/secure/*"); // Chỉ lọc đường dẫn bảo mật
        registrationBean.setOrder(1); // Thiết lập thứ tự chạy đầu tiên trong chuỗi lọc
        
        return registrationBean;
    }
}

// Custom Filter JWT kế thừa OncePerRequestFilter
public class JwtAuthenticationFilter extends OncePerRequestFilter {
    @Override
    protected void doFilterInternal(HttpServletRequest request, 
                                    HttpServletResponse response, 
                                    FilterChain filterChain)
            throws ServletException, IOException {
        String token = request.getHeader("Authorization");
        if (token == null || !token.startsWith("Bearer ")) {
            // Chặn lại và trả lỗi 401
            response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
            return;
        }
        // Cho phép request tiếp tục đi tiếp
        filterChain.doFilter(request, response);
    }
}"""
  },
  {
    "topicId": "spring_di_ioc",
    "title": "Dependency Injection (DI) & Inversion of Control (IoC)",
    "content": """Inversion of Control (IoC) và Dependency Injection (DI) là hai nguyên lý cốt lõi cấu thành nên Spring Framework, giúp giảm sự phụ thuộc chặt chẽ giữa các thành phần phần mềm (loose coupling).

1. PHÂN BIỆT IOC VÀ DI:
• Inversion of Control (IoC - Đảo ngược điều khiển):
  - Định nghĩa: Là một nguyên lý thiết kế phần mềm, trong đó quyền kiểm soát luồng hoạt động và việc quản lý vòng đời đối tượng (khởi tạo, cấu hình, hủy bỏ) được chuyển giao từ mã nguồn tự viết của lập trình viên sang cho Framework (cụ thể là Spring IoC Container).
• Dependency Injection (DI - Tiêm phụ thuộc):
  - Định nghĩa: Là một mẫu thiết kế cụ thể để triển khai nguyên lý IoC. Thay vì một đối tượng tự dùng từ khóa `new` để tạo ra các đối tượng phụ thuộc (dependencies) của nó, các phụ thuộc này sẽ được Spring Container tự động khởi tạo và 'tiêm' (inject) vào từ bên ngoài khi cần thiết.

2. CÁC PHƯƠNG THỨC DI CHÍNH VÀ ĐÁNH GIÁ:
• Field Injection (Tiêm trực tiếp vào biến thành viên qua @Autowired):
  - Ưu điểm: Ngắn gọn, dễ đọc nhất.
  - Nhược điểm: Khó viết Unit Test (vì không thể truyền mock objects vào field private nếu không dùng reflection). Gây phụ thuộc chặt chẽ vào Container, và có nguy cơ tạo ra Dependency vòng tròn (Circular Dependency).
• Setter Injection (Tiêm qua phương thức setXXX):
  - Thích hợp cho các phụ thuộc tùy chọn (optional dependency) có thể thay đổi hoặc gán sau.
• Constructor Injection (Tiêm qua hàm tạo):
  - BẮT BUỘC KHUYẾN NGHỊ SỬ DỤNG.
  - Ưu điểm: Đảm bảo các dependency không bao giờ bị null (bắt buộc phải truyền khi tạo đối tượng). Cho phép định nghĩa các trường phụ thuộc là `final` (bất biến, thread-safe). Dễ dàng viết Unit Test bằng cách new đối tượng và truyền tham số mock thủ công.

3. KHÁI NIỆM SPRING BEAN:
• Spring Bean là một đối tượng được khởi tạo, quản lý vòng đời và cấu hình bởi Spring IoC Container.
• Các cách để định nghĩa một Bean:
  - Khai báo các stereotype annotations trên class như `@Component`, `@Service`, `@Repository`, `@Controller` để Spring tự động quét.
  - Sử dụng `@Bean` trên các phương thức trả về đối tượng bên trong class cấu hình `@Configuration`.""",
    "example": """// Minh họa Constructor Injection (Khuyến nghị)
@Service
public class UserService {
    
    // Biến final bất biến, an toàn luồng, không thể null
    private final UserRepository userRepository; 
    
    // Spring Boot sẽ tự động tiêm UserRepository vào đây qua Constructor (Không cần viết @Autowired)
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    public User findUser(Long id) {
        return userRepository.findById(id);
    }
}"""
  },
  {
    "topicId": "spring_stereotype_annotations",
    "title": "Stereotype Annotations: @Component, @Service, @Repository, @Controller",
    "content": """Spring cung cấp các Stereotype Annotations chuyên biệt để phân loại vai trò của các Spring Bean trong cấu trúc ứng dụng 3 lớp (3-tier architecture). Điều này giúp Spring Container quét (Component Scanning) và quản lý vòng đời các đối tượng tự động.

1. PHÂN LOẠI CÁC ANNOTATION:
• @Component:
  - Là annotation cha dùng chung. Bất kỳ lớp nào được đánh dấu bằng `@Component` đều được quét và tạo Bean trong IoC Container.
• @Repository:
  - Chuyên biệt cho tầng truy cập dữ liệu (Data Access Object - DAO / Tầng Repository).
  - Tính năng nâng cao: Spring Security/JPA sẽ tự động bắt tất cả các ngoại lệ phát sinh từ database (như SQLException) và chuyển dịch chúng thành các Exception có tính nhất quán chung của Spring là `DataAccessException` (đây là các unchecked exception, dễ quản lý).
• @Service:
  - Chuyên biệt cho tầng xử lý nghiệp vụ (Business Logic Layer).
  - Không có tính năng bổ sung đặc biệt nào so với `@Component`, chủ yếu giữ vai trò ngữ nghĩa (giúp phân biệt tầng nghiệp vụ rõ ràng).
• @Controller:
  - Chuyên biệt cho tầng trình diễn (Presentation Layer / Web Controller) để tiếp nhận yêu cầu và điều hướng trả về view giao diện (JSP, HTML).
  - `@RestController` là sự kết hợp của `@Controller` và `@ResponseBody`, chuyên dùng cho Web API trả dữ liệu thô JSON.

2. PHẦN NÂNG CAO & CHI TIẾT CHUYÊN SÂU:
• Cơ chế Component Scanning của Spring:
  - Khi ứng dụng chạy, `@ComponentScan` sẽ quét qua toàn bộ classpath, tìm các class có gắn một trong các Stereotype Annotations trên và tự động khởi tạo chúng thành các Spring Bean duy nhất (Singleton mặc định) đưa vào Container.
  - Bản chất `@Service`, `@Repository`, `@Controller` đều kế thừa từ `@Component` (đều có `@Component` ở bên trong). Việc phân tách này giúp ứng dụng dễ bảo trì và cho phép Spring áp dụng các Aspect (AOP) chuyên biệt cho từng tầng (ví dụ Exception Translation ở Repository, @Transactional ở Service, Request Mapping ở Controller).""",
    "example": """// 1. Tầng Repository kết nối DB
@Repository
public class ProductRepository {
    public Product getById(Long id) {
        // Query database, các SQLException ở đây sẽ được Spring dịch sang DataAccessException
        return new Product(id, "IPhone 15");
    }
}

// 2. Tầng Service xử lý nghiệp vụ
@Service
public class ProductService {
    private final ProductRepository productRepository;

    public ProductService(ProductRepository productRepository) {
        this.productRepository = productRepository;
    }
    
    public Product getProduct(Long id) {
        return productRepository.getById(id);
    }
}

// 3. Tầng Controller tiếp nhận request Web API
@RestController
@RequestMapping("/products")
public class ProductController {
    private final ProductService productService;

    public ProductController(ProductService productService) {
        this.productService = productService;
    }

    @GetMapping("/{id}")
    public Product getProductById(@PathVariable Long id) {
        return productService.getProduct(id);
    }
}"""
  },
  {
    "topicId": "jpa_fetch_type",
    "title": "JPA Fetch Type: EAGER vs LAZY",
    "content": """Trong JPA và Hibernate, khi thiết lập mối quan hệ giữa các Entity (Bảng dữ liệu), Fetch Type định nghĩa cách thức và thời điểm tải các đối tượng liên quan (associated entities) từ cơ sở dữ liệu lên bộ nhớ.

1. SO SÁNH HAI PHƯƠNG THỨC TẢI DỮ LIỆU:
• EAGER Loading (Tải ngay lập tức):
  - Định nghĩa: Khi bạn truy vấn đối tượng cha, JPA sẽ tự động tạo câu lệnh JOIN hoặc SELECT phụ để tải tất cả các đối tượng con liên quan lên bộ nhớ ngay lập tức, bất kể bạn có cần sử dụng chúng hay không.
  - Mặc định cho: Các mối quan hệ đơn lẻ (to-one) gồm `@OneToOne` và `@ManyToOne`.
  - Khuyết điểm: Dẫn đến việc tải quá nhiều dữ liệu thừa, làm chậm truy vấn và có thể gây tràn bộ nhớ nếu số lượng thực thể lớn.
• LAZY Loading (Tải trì hoãn / nạp chậm):
  - Định nghĩa: Khi bạn truy vấn đối tượng cha, JPA chỉ tải thông tin của đối tượng cha. Các đối tượng con liên quan sẽ KHÔNG được tải lên bộ nhớ. Chỉ khi nào bạn thực tế gọi phương thức getter của tập hợp con lần đầu tiên, JPA mới kích hoạt câu truy vấn bổ sung để nạp dữ liệu (load on demand).
  - Mặc định cho: Các mối quan hệ tập hợp (to-many) gồm `@OneToMany` và `@ManyToMany`.
  - Ưu điểm: Rất tối ưu hiệu năng. Đây là phương thức được khuyến nghị mặc định để tránh lỗi N+1 Query và tối ưu tài nguyên.

2. PHẦN NÂNG CAO & CHI TIẾT CHUYÊN SÂU:
• Lỗi LazyInitializationException:
  - Ngoại lệ này xảy ra khi bạn truy cập vào một tập hợp con được cấu hình LAZY ở bên ngoài phạm vi của một Transaction hoặc Session đã đóng (sau khi EntityManager đã đóng kết nối).
  - Nguyên nhân: Do lúc này đối tượng đã trở thành trạng thái Detached, Hibernate không thể mở kết nối mới tới DB để thực hiện câu truy vấn nạp chậm cho tập hợp con đó.
  - Khắc phục: Giữ Transaction mở bằng `@Transactional` ở tầng Service để nạp dữ liệu trước khi đóng Session, hoặc sử dụng JPQL `JOIN FETCH` để lấy dữ liệu con chủ động.""",
    "example": """// Cấu hình Fetch Type trong Entity
@Entity
public class Company {
    @Id @GeneratedValue
    private Long id;
    private String name;

    // Khuyên dùng LAZY cho mối quan hệ 1-Nhiều
    // Nếu để EAGER, mỗi khi lấy Company, Hibernate sẽ SELECT luôn hàng ngàn Employee của công ty đó
    @OneToMany(mappedBy = "company", fetch = FetchType.LAZY)
    private List<Employee> employees;
    
    public List<Employee> getEmployees() {
        return employees;
    }
}"""
  },
  {
    "topicId": "jpa_entity_lifecycle",
    "title": "Vòng đời Entity trong JPA (Entity Lifecycle)",
    "content": """Một thực thể (Entity) trong JPA được quản lý vòng đời bởi Persistence Context (EntityManager). Thực thể này sẽ đi qua 4 trạng thái quản lý chính.

1. BỐN TRẠNG THÁI CỦA ENTITY:
• Transient (Tạm thời):
  - Định nghĩa: Đối tượng Java thuần túy vừa được tạo mới bằng từ khóa `new`.
  - Đặc điểm: Chưa được liên kết với Persistence Context, chưa có giá trị định danh khóa chính (ID) trong DB. Nếu chương trình kết thúc, đối tượng này sẽ biến mất.
• Managed (Được quản lý):
  - Định nghĩa: Đối tượng đang nằm trong Persistence Context và đại diện cho một dòng dữ liệu trong DB.
  - Đặc điểm: Có khóa chính (ID). Mọi thay đổi trên thuộc tính của đối tượng Managed sẽ được JPA tự động theo dõi. Khi transaction COMMIT, JPA tự động thực hiện câu lệnh UPDATE xuống DB mà không cần gọi hàm save/update thủ công (Cơ chế này gọi là **Dirty Checking**).
• Detached (Bị tách rời):
  - Định nghĩa: Đối tượng đã từng ở trạng thái Managed nhưng hiện tại Persistence Context đã bị đóng hoặc đối tượng bị đẩy ra ngoài (gọi qua em.detach() hoặc em.clear()).
  - Đặc điểm: Vẫn có ID, nhưng thay đổi trên đối tượng này không còn được JPA tự động lưu xuống DB nữa. Có thể đưa trở lại trạng thái Managed qua hàm `em.merge()`.
• Removed (Đã xóa):
  - Định nghĩa: Đối tượng được đánh dấu để xóa khỏi CSDL (bằng cách gọi em.remove()). Nó thực tế bị xóa khỏi DB khi transaction kết thúc (COMMIT).

2. PHẦN NÂNG CAO & CHI TIẾT CHUYÊN SÂU:
• Các hàm chuyển đổi trạng thái:
  - `persist()`: Chuyển đối tượng từ Transient sang Managed (Chuẩn bị INSERT).
  - `merge()`: Chuyển đối tượng từ Detached trở lại Managed (Chuẩn bị UPDATE dòng tương ứng).
  - `remove()`: Chuyển đối tượng từ Managed sang Removed (Chuẩn bị DELETE dòng tương ứng).
  - `detach()` / `clear()` / `close()`: Tách một hoặc toàn bộ đối tượng Managed thành Detached.""",
    "example": """// Minh họa luồng chuyển đổi trạng thái Entity
EntityManager em = emf.createEntityManager();
em.getTransaction().begin();

User user = new User("An"); // 1. Trạng thái TRANSIENT
em.persist(user);          // 2. Trạng thái MANAGED (Đã được quản lý)

user.setEmail("an@gmail.com"); // Thay đổi thuộc tính của Managed object

em.getTransaction().commit(); // Transaction commit -> kích hoạt INSERT và UPDATE tự động (Dirty Checking)
em.close(); // Persistence context đóng -> user chuyển sang trạng thái 3. DETACHED

user.setName("An Bình"); // Sẽ KHÔNG có UPDATE nào xuống DB vì đối tượng đã bị DETACHED

// Muốn cập nhật tiếp:
EntityManager em2 = emf.createEntityManager();
em2.getTransaction().begin();
User managedUser = em2.merge(user); // 4. Trở lại trạng thái MANAGED
em2.getTransaction().commit(); // Cập nhật thành công tên "An Bình" xuống DB"""
  },
  {
    "topicId": "jpa_transaction",
    "title": "JPA Transaction & @Transactional",
    "content": """Trong cơ sở dữ liệu, một Transaction (Giao dịch) là một tập hợp các câu lệnh SQL phải được thực hiện thành công trọn vẹn cùng nhau (đảm bảo tính toàn vẹn dữ liệu ACID - All or Nothing). Spring Framework cung cấp annotation `@Transactional` để quản lý giao dịch tự động.

1. CƠ CHẾ HOẠT ĐỘNG CỦA @Transactional:
• Quản lý Transaction khai báo:
  - Khi một phương thức được đánh dấu `@Transactional`, Spring sử dụng cơ chế AOP (Aspect-Oriented Programming) tạo ra một proxy bao quanh đối tượng để tự động mở kết nối và bắt đầu transaction (`begin`) trước khi chạy phương thức.
  - Nếu phương thức thực thi thành công không phát sinh lỗi, Spring tự động gọi `commit` để lưu dữ liệu.
  - Nếu xảy ra ngoại lệ (exception) trong quá trình thực thi, Spring tự động gọi `rollback` để hoàn trả dữ liệu về trạng thái ban đầu.

2. PHẦN NÂNG CAO & CHI TIẾT CHUYÊN SÂU:
• Quy tắc Rollback mặc định của Spring (Checked vs Unchecked Exceptions):
  - Mặc định, `@Transactional` chỉ tự động ROLLBACK khi xuất hiện ngoại lệ không kiểm soát (**Unchecked Exception** - là các class kế thừa từ `RuntimeException` như `NullPointerException`, `ArithmeticException`, `DataAccessException`, hoặc lỗi hệ thống `Error`).
  - Đối với các ngoại lệ có kiểm soát (**Checked Exception** - là các class kế thừa từ `Exception` nhưng không thuộc RuntimeException, ví dụ `IOException`, `SQLException`, `ClassNotFoundException`), Spring mặc định vẫn thực hiện **COMMIT** bình thường, không tự động rollback.
  - Khắc phục: Để ép Spring rollback khi gặp bất kỳ lỗi nào (kể cả checked exception), ta phải khai báo rõ thuộc tính rollbackFor trong annotation: `@Transactional(rollbackFor = Exception.class)`.
• Gọi phương thức nội bộ (Self-invocation):
  - Nếu bạn gọi một phương thức có `@Transactional` từ một phương thức khác nằm trong CÙNG một class, cơ chế Transaction sẽ KHÔNG hoạt động (không mở transaction).
  - Nguyên nhân: Vì cuộc gọi nội bộ bỏ qua lớp proxy do Spring tạo ra.""",
    "example": """@Service
public class OrderService {
    
    private final ProductRepository productRepository;
    private final OrderRepository orderRepository;

    public OrderService(ProductRepository prodRepo, OrderRepository orderRepo) {
        this.productRepository = prodRepo;
        this.orderRepository = orderRepo;
    }

    // Bắt buộc cấu hình rollbackFor để rollback cả khi gặp Checked Exception (như CustomOrderException)
    @Transactional(rollbackFor = CustomOrderException.class)
    public void createOrder(Long prodId, int qty) throws CustomOrderException {
        Product prod = productRepository.findById(prodId);
        if (prod.getStock() < qty) {
            throw new CustomOrderException("Không đủ hàng trong kho!"); // Sẽ rollback thành công
        }
        
        prod.setStock(prod.getStock() - qty); // Tự động update khi commit
        Order order = new Order(prodId, qty);
        orderRepository.save(order);
    }
}"""
  },
  {
    "topicId": "jpa_nplus1_problem",
    "title": "Vấn đề N+1 Query trong Hibernate & Cách xử lý",
    "content": """Vấn đề N+1 Query là một trong những nguyên nhân phổ biến nhất làm suy giảm hiệu năng nghiêm trọng trong các ứng dụng sử dụng ORM như Hibernate và JPA.

1. NGUYÊN NHÂN VÀ CƠ CHẾ GÂY LỖI:
• Định nghĩa vấn đề:
  - Xảy ra khi bạn muốn lấy danh sách N đối tượng cha (ví dụ lấy danh sách 10 Công ty - Company), nhưng để hiển thị thông tin các đối tượng con liên quan (Danh sách nhân viên - Employee), Hibernate tự động thực hiện thêm N câu lệnh SELECT phụ để tải con của từng cha (1 SELECT cha + N SELECT con = N+1 query).
• Cơ chế gây lỗi:
  - Khi sử dụng LAZY Loading, câu SELECT đầu tiên lấy N Company. Khi bạn chạy vòng lặp duyệt qua N Company này và gọi `company.getEmployees().size()`, ở mỗi vòng lặp Hibernate lại gửi 1 câu SELECT lấy nhân viên của công ty đó. Tổng cộng chạy 1 + N câu SQL, tốn rất nhiều kết nối mạng và làm nghẽn DB.

2. CÁC PHƯƠNG PHÁP KHẮC PHỤC CHUẨN:
• Sử dụng JOIN FETCH trong JPQL (Khuyên dùng):
  - Viết câu lệnh JPQL sử dụng từ khóa `JOIN FETCH` để ép Hibernate thực hiện duy nhất 1 câu SELECT dùng phép toán INNER JOIN hoặc LEFT JOIN để lấy đồng thời cả cha và con về cùng lúc.
  - Ví dụ: `SELECT c FROM Company c JOIN FETCH c.employees`.
• Sử dụng EntityGraph (@EntityGraph):
  - Khai báo trên phương thức của Spring Data Repository để chỉ định mối quan hệ nào cần được nạp EAGER chủ động trong truy vấn đó.
• Sử dụng Batch Size (@BatchSize):
  - Cấu hình số lượng bản ghi con được tải theo từng lô (ví dụ `@BatchSize(size = 20)`). Thay vì chạy N câu SELECT, Hibernate gộp chung lại dùng mệnh đề `IN` (ví dụ `WHERE company_id IN (1,2,3...20)`) để chỉ chạy `N/20 + 1` câu lệnh SELECT, giảm tải đáng kể cho database.""",
    "example": """// 1. Repository khắc phục lỗi N+1 bằng JPQL JOIN FETCH
public interface CompanyRepository extends JpaRepository<Company, Long> {
    
    // Chỉ chạy duy nhất 1 câu SELECT JOIN
    @Query("SELECT c FROM Company c JOIN FETCH c.employees")
    List<Company> findAllWithEmployees();
    
    // 2. Khắc phục lỗi N+1 bằng Annotation @EntityGraph
    @EntityGraph(attributePaths = {"employees"})
    List<Company> findByNameContaining(String name);
}

// 3. Sử dụng BatchSize trong Entity để tối ưu
@Entity
public class Company {
    @Id @GeneratedValue
    private Long id;
    
    @OneToMany(mappedBy = "company")
    @BatchSize(size = 50) // Hibernate sẽ gộp nạp con theo lô 50 bản ghi cha
    private List<Employee> employees;
}"""
  },
  {
    "topicId": "jpa_orm_languages",
    "title": "Phân biệt JPA, ORM, JPQL và HQL",
    "content": """Trong hệ sinh thái phát triển Java Web, lập trình viên cần phân biệt rõ ràng 4 khái niệm dễ gây nhầm lẫn: ORM, JPA, Hibernate, JPQL và HQL.

1. PHÂN BIỆT 4 KHÁI NIỆM CỐT LÕI:
• ORM (Object-Relational Mapping - Ánh xạ thực thể quan hệ):
  - Định nghĩa: Là một kỹ thuật/khái niệm lập trình giúp ánh xạ các đối tượng (Object) trong ngôn ngữ hướng đối tượng sang các bảng (Relation) trong cơ sở dữ liệu quan hệ, giúp lập trình viên thao tác với DB hoàn toàn bằng code đối tượng thay vì viết câu lệnh SQL thô.
• JPA (Java Persistence API):
  - Định nghĩa: Là một đặc tả tiêu chuẩn (Specification) của Java EE/Jakarta EE. Bản thân JPA chỉ là bộ các quy chuẩn, nguyên lý và interface định nghĩa (như EntityManager, Entity), không tự thực thi code.
• Hibernate:
  - Định nghĩa: Là một Framework ORM cụ thể triển khai (implementation) các tiêu chuẩn đã định nghĩa trong JPA. Hibernate là implementation phổ biến nhất hiện nay.
• JPQL (Java Persistence Query Language) và HQL (Hibernate Query Language):
  - JPQL: Ngôn ngữ truy vấn hướng đối tượng được định nghĩa bởi tiêu chuẩn JPA. Nó thực hiện truy vấn trực tiếp trên các Entity (Class) và thuộc tính của Entity chứ không làm việc trên bảng (Table) hay cột (Column) vật lý của DB.
  - HQL: Ngôn ngữ truy vấn riêng của Hibernate, xuất hiện trước JPQL. JPQL chính là một tập con được tiêu chuẩn hóa của HQL. HQL linh hoạt và hỗ trợ nhiều tính năng mở rộng chuyên biệt của Hibernate hơn.

2. ĐIỂM CHÚ Ý KHI ÔN THI:
• SQL làm việc trực tiếp trên Table và Column (ví dụ: `SELECT * FROM tbl_users WHERE user_age > 18`).
• JPQL/HQL làm việc trên Entity Class và Class Fields (ví dụ: `SELECT u FROM User u WHERE u.age > 18` - chữ User viết hoa là tên Class, u.age là thuộc tính Java).""",
    "example": """// Minh họa truy vấn JPQL
EntityManager em = entityManagerFactory.createEntityManager();

// Truy vấn trên Entity Class "User" (Không phải bảng "users" trong database)
String jpql = "SELECT u FROM User u WHERE u.email LIKE :domain";
TypedQuery<User> query = em.createQuery(jpql, User.class);
query.setParameter("domain", "%@gmail.com");

List<User> users = query.getResultList();"""
  }
]

# --------------------------------------------------------------------------
# PART 2: PYTHON DETAILED KNOWLEDGE DATA
# --------------------------------------------------------------------------
py_knowledge = [
  {
    "topicId": "python_basics",
    "title": "Khái niệm cơ bản & Nhập xuất dữ liệu",
    "content": """Python là ngôn ngữ lập trình cấp cao, thông dịch (interpreted), hướng đối tượng (OOP) và có kiểu dữ liệu động (dynamically typed).

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
• `print()`: Hàm xuất dữ liệu ra console. Mặc định tự động thêm ký tự xuống dòng `\\n` ở cuối kết quả in ra. Để in không xuống dòng, ta phải tùy chỉnh tham số `end` (ví dụ: `print("H", end="")`). Tham số `sep` dùng để định nghĩa ký tự ngăn cách giữa các giá trị in ra.
• `input()`: Nhập dữ liệu từ bàn phím. Mặc định LUÔN TRẢ VỀ kiểu dữ liệu chuỗi (`str`). Muốn tính toán số học, ta bắt buộc phải ép kiểu thủ công (ví dụ: `int(input())`).
• Định nghĩa chuỗi hợp lệ: Phải được bao quanh bởi cặp nháy đơn `'...'` hoặc nháy kép `"..."`, hoặc ba nháy `'''...'''` / `\"\"\"...\"\"\"` cho chuỗi nhiều dòng. Viết chuỗi thiếu cặp nháy (ví dụ chỉ ghi `python` mà không có nháy) sẽ được Python hiểu là một biến và ném ra NameError nếu biến đó chưa khai báo.""",
    "example": """# Minh họa nhập xuất và toán tử cơ bản
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
# s2 = python  # Lỗi NameError vì thiếu nháy bao quanh"""
  },
  {
    "topicId": "data_types_conditionals",
    "title": "Cấu trúc rẽ nhánh & Kiểu dữ liệu tập hợp",
    "content": """Python cung cấp cấu trúc rẽ nhánh điều kiện linh hoạt cùng các kiểu dữ liệu tập hợp phong phú để lưu trữ nhóm dữ liệu.

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
• Khối `finally` luôn luôn được thực thi bất kể có lỗi xảy ra hay không, thường dùng để giải phóng tài nguyên hệ thống.""",
    "example": """# Minh họa phép gán tham chiếu list
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
    print("Khối này luôn chạy.") # Luôn chạy sau try/except"""
  },
  {
    "topicId": "loops",
    "title": "Cấu trúc lặp (Loops)",
    "content": """Python hỗ trợ hai cấu trúc vòng lặp chính để lặp đi lặp lại khối lệnh: `while` (lặp kiểm tra điều kiện) và `for` (lặp duyệt qua tập hợp).

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
• Nếu vòng lặp bị ngắt quãng bởi lệnh `break`, khối `else` sẽ BỊ BỎ QUA.""",
    "example": """# Vòng lặp for-else và break
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
    print(x, end=" ") # Output: 5 3 1"""
  },
  {
    "topicId": "functions",
    "title": "Hàm & Phạm vi biến (Functions)",
    "content": """Hàm là khối lệnh được định nghĩa một lần để thực hiện một tác vụ cụ thể, giúp tái sử dụng mã nguồn và tăng tính module cho chương trình.

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
• Cú pháp: `lambda arguments: expression` (Ví dụ: `lambda x: x**2` trả về bình phương của x). Tự động trả về giá trị của biểu thức mà không cần từ khóa `return`.""",
    "example": """# Sự cố mutable default argument
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
print("Bình phương 5:", square(5)) # Output: 25"""
  },
  {
    "topicId": "strings",
    "title": "Xử lý chuỗi ký tự (Strings)",
    "content": """Chuỗi ký tự trong Python là một dãy các ký tự bất biến (immutable), đại diện bằng kiểu dữ liệu `str`.

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
• `s.isdigit()`: Kiểm tra xem toàn bộ các ký tự trong chuỗi có phải là chữ số hay không. Trả về `True` hoặc `False`.""",
    "example": """# Minh họa slicing và methods
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
print("Kiểm tra số '123':", "123".isdigit())    # Output: True"""
  },
  {
    "topicId": "files",
    "title": "Xử lý tệp tin (File Handling)",
    "content": """Python cung cấp các hàm dựng sẵn mạnh mẽ để làm việc với các tệp tin (đọc và ghi file) trên đĩa cứng hệ thống.

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
• `f.readlines()`: Đọc toàn bộ tất cả các dòng của file và trả về dưới dạng một **Danh sách** (List) các chuỗi, mỗi chuỗi đại diện cho một dòng (bao gồm cả ký tự xuống dòng `\\n`).

3. QUẢN LÝ TÀI NGUYÊN BẰNG CẤU TRÚC 'WITH' (CONTEXT MANAGER):
• Trong lập trình tệp tin, sau khi mở file, ta bắt buộc phải gọi `f.close()` để đóng file giải phóng tài nguyên. Nếu quên đóng, file bị khóa và rò rỉ bộ nhớ.
• Cách viết an toàn nhất là sử dụng từ khóa `with`. Cấu trúc này hoạt động như một Context Manager, đảm bảo file sẽ tự động được đóng an toàn khi khối lệnh kết thúc, ngay cả khi có ngoại lệ xảy ra đột ngột trong thân block.""",
    "example": """# Ghi dữ liệu vào file
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Dòng thứ nhất\\n")
    f.write("Dòng thứ hai\\n")

# Đọc dữ liệu an toàn với with
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        print(f"Dòng {idx+1}: {line.strip()}") 
        # dùng strip() để loại bỏ ký tự \\n ở cuối dòng khi in

# File tự động đóng khi thoát khỏi block with"""
  },
  {
    "topicId": "modules_libraries",
    "title": "Sử dụng Modules & Thư viện",
    "content": """Module trong Python là một file chứa các định nghĩa hàm, lớp, biến và mã nguồn Python, giúp phân tách mã nguồn thành các phần nhỏ để dễ quản lý và tái sử dụng.

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
• Pip (Python Package Index) là công cụ quản lý package tiêu chuẩn của Python, dùng để cài đặt các thư viện từ cộng đồng như NumPy, Pandas, Matplotlib.""",
    "example": """import math
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
print("Trái cây ngẫu nhiên:", selected)"""
  },
  {
    "topicId": "numpy",
    "title": "Thư viện tính toán NumPy (NumPy)",
    "content": """NumPy (Numerical Python) là thư viện nền tảng cho tính toán khoa học, phân tích số liệu và tối ưu hóa các phép toán ma trận đại số tuyến tính trong Python.

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
• Nhân hai ma trận thực tế trong đại số tuyến tính: Bắt buộc sử dụng toán tử `@` hoặc hàm `np.dot(m1, m2)`. Sử dụng phép nhân `*` thông thường giữa 2 ma trận chỉ là nhân các phần tử cùng vị trí với nhau (element-wise), không phải nhân ma trận.""",
    "example": """import numpy as np

# Khởi tạo mảng 2 chiều (ma trận) từ List lồng nhau
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Mảng ndarray:\\n", matrix)
print("Số chiều (ndim):", matrix.ndim)    # Output: 2
print("Kích thước (shape):", matrix.shape) # Output: (2, 3)
print("Kiểu dữ liệu (dtype):", matrix.dtype) # Output: int32 hoặc int64

# Phép toán element-wise vs Nhân ma trận đại số
arr = np.array([1, 2, 3])
print("Nhân element-wise arr * 2:", arr * 2) # Output: [2, 4, 6]

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[2, 0], [1, 2]])
print("Nhân ma trận đại số m1 @ m2:\\n", m1 @ m2)
# Output: [[4, 4], [10, 8]]"""
  },
  {
    "topicId": "pandas",
    "title": "Thư viện phân tích dữ liệu Pandas",
    "content": """Pandas là thư viện mã nguồn mở mạnh mẽ chuyên dùng để thao tác, làm sạch, phân tích và xử lý các tập dữ liệu có cấu trúc dưới dạng bảng biểu.

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
  - Pandas tích hợp trực tiếp với Matplotlib thông qua `.plot()`. Các biểu đồ phổ biến: `line` (biểu đồ đường - xem sự thay đổi theo thời gian), `bar` (biểu đồ cột), `hist` (biểu đồ tần suất), `pie` (biểu đồ tròn).""",
    "example": """import pandas as pd

# Khởi tạo DataFrame từ List of Dicts
dicts = [{'a': 10, 'b': 20}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(dicts)
print("DataFrame gốc:\\n", df)
print("Kích thước (shape):", df.shape) # Output: (2, 3) - 2 hàng, 3 cột
print("Tổng số ô (size):", df.size)   # Output: 6

# Lọc bằng iloc (dòng đầu tiên, cột đầu tiên)
print("Phần tử ở dòng 0 cột 0:", df.iloc[0, 0]) # Output: 10.0

# Xóa cột bằng del và drop
del df['c'] # Xóa trực tiếp cột 'c'
print("Sau khi del cột c:\\n", df)

df_dropped = df.drop(['b'], axis=1) # Trả về DF mới không có cột 'b'
print("Sau khi drop cột b:\\n", df_dropped)

# Chuyển vị
print("Ma trận chuyển vị (df.T):\\n", df.T)"""
  },
  {
    "topicId": "regex",
    "title": "Biểu thức chính quy (Regular Expressions)",
    "content": """Regular Expressions (Regex) là công cụ cực kỳ mạnh mẽ dùng để tìm kiếm, trích xuất và thao tác các chuỗi ký tự dựa trên một khuôn mẫu (pattern) xác định trước.

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
  - `.` : Khớp với bất kỳ ký tự nào ngoại trừ ký tự xuống dòng `\\n`.
  - `^` : Khớp ở điểm bắt đầu của chuỗi.
  - `$` : Khớp ở điểm kết thúc của chuỗi.
  - `\\d` : Khớp với chữ số tương đương `[0-9]`.
  - `\\D` : Khớp với ký tự không phải chữ số (ngược lại của `\\d`).
  - `\\w` : Khớp với ký tự chữ và số cùng dấu gạch dưới `_` (tương đương `[a-zA-Z0-9_]`).
  - `\\W` : Khớp với ký tự không phải chữ và số (ngược lại của `\\w`).
  - `\\s` : Khớp với ký tự khoảng trắng (space, tab, newline).
  - `\\S` : Khớp với ký tự không phải khoảng trắng.
• Bộ định lượng lặp lại (Quantifiers):
  - `*` : Khớp 0 hoặc nhiều lần của ký tự đứng trước.
  - `+` : Khớp 1 hoặc nhiều lần của ký tự đứng trước.
  - `?` : Khớp 0 hoặc 1 lần (tùy chọn).
  - `{n}` : Khớp đúng `n` lần xuất hiện.
  - `{n,m}` : Khớp từ `n` đến `m` lần xuất hiện.""",
    "example": """import re

text = "Liên hệ qua: 0912-345-678 hoặc 0987-654-321"

# 1. re.findall để trích xuất toàn bộ số điện thoại
# Định dạng: 4 số - 3 số - 3 số
phone_pattern = r'\\d{4}-\\d{3}-\\d{3}'
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
    print("search thấy:", match_obj.group()) # Output: 0912-345-678"""
  }
]

# Write to data files (JSON)
with open(os.path.join(data_java_dir, "knowledge.json"), "w", encoding="utf-8") as f:
    json.dump(java_knowledge, f, ensure_ascii=False, indent=2)
print("Updated data/java/knowledge.json")

with open(os.path.join(data_py_dir, "knowledge.json"), "w", encoding="utf-8") as f:
    json.dump(py_knowledge, f, ensure_ascii=False, indent=2)
print("Updated data/python/knowledge.json")


# --------------------------------------------------------------------------
# PART 3: JAVA QUESTIONS DATA CLEANUP
# --------------------------------------------------------------------------
java_questions_path = os.path.join(data_java_dir, "questions.json")
with open(java_questions_path, "r", encoding="utf-8") as f:
    java_questions = json.load(f)

# Keep only syllabus questions (ID < 200)
java_syllabus_qs = [q for q in java_questions if q.get("id", 0) < 200]
print(f"Loaded {len(java_syllabus_qs)} Java syllabus questions (filtered out Java Core IDs >= 200)")

# Write cleaned questions back to data/java/questions.json
with open(java_questions_path, "w", encoding="utf-8") as f:
    json.dump(java_syllabus_qs, f, ensure_ascii=False, indent=2)
print("Cleaned data/java/questions.json")


# --------------------------------------------------------------------------
# PART 4: JAVA PRESET EXAMS GENERATION (NEW MOCK EXAMS BASED ON SYLLABUS)
# --------------------------------------------------------------------------
# Let's categorize the 119 questions by topic ID
servlet_topics = ["servlet_lifecycle", "session_cookie", "genericservlet_httpservlet", 
                  "requestdispatcher", "filter_api", "jdbc_api"]
spring_topics = ["springboot_autoconfig", "spring_mvc_flow", "spring_mvc_annotations", 
                 "spring_filters", "spring_di_ioc", "spring_stereotype_annotations"]
jpa_topics = ["jpa_fetch_type", "jpa_entity_lifecycle", "jpa_transaction", 
              "jpa_nplus1_problem", "jpa_orm_languages"]

servlet_qs = [q for q in java_syllabus_qs if q.get("topicId") in servlet_topics]
spring_qs = [q for q in java_syllabus_qs if q.get("topicId") in spring_topics]
jpa_qs = [q for q in java_syllabus_qs if q.get("topicId") in jpa_topics]

# Assert counts
print(f"Servlet Questions: {len(servlet_qs)} (Expected: 42)")
print(f"Spring Questions: {len(spring_qs)} (Expected: 42)")
print(f"JPA Questions: {len(jpa_qs)} (Expected: 35)")

# Build 4 balanced exams
preset_exams = []

# Exam 1: Đề thi chuyên đề 1 - Java Core & Servlet (42 câu)
preset_exams.append({
    "id": "de_1",
    "name": "Đề thi thử số 1 (Servlet & JDBC)",
    "description": "Đề kiểm tra chuyên sâu phần Java Core, Servlet, Session, Cookie, Filter, RequestDispatcher và JDBC API (42 câu hỏi).",
    "questions": servlet_qs
})

# Exam 2: Đề thi chuyên đề 2 - Spring Framework (42 câu)
preset_exams.append({
    "id": "de_2",
    "name": "Đề thi thử số 2 (Spring Framework)",
    "description": "Đề kiểm tra chuyên sâu phần Spring Boot Auto-configuration, Spring MVC Flow, Stereotypes, Dependency Injection và Spring Filters (42 câu hỏi).",
    "questions": spring_qs
})

# Exam 3: Đề thi chuyên đề 3 - JPA & Hibernate (35 câu)
preset_exams.append({
    "id": "de_3",
    "name": "Đề thi thử số 3 (JPA & Hibernate)",
    "description": "Đề kiểm tra chuyên sâu phần JPA Fetch Type (EAGER/LAZY), Entity Lifecycle, Transactions (@Transactional) và khắc phục lỗi N+1 Query (35 câu hỏi).",
    "questions": jpa_qs
})

# Exam 4: Đề thi tổng hợp toàn diện (40 câu)
# Let's select:
# - 15 questions from Servlet (2 from each topic 1-6, plus 3 extra)
# - 15 questions from Spring (2 from each topic 7-12, plus 3 extra)
# - 10 questions from JPA (2 from each topic 13-17)
selected_mixed_qs = []

# Servlet selections
for t in servlet_topics:
    t_qs = [q for q in servlet_qs if q.get("topicId") == t]
    selected_mixed_qs.extend(t_qs[:2]) # Take 2 from each -> 12 qs
# Take 3 extra servlet questions
extra_servlet = [q for q in servlet_qs if q not in selected_mixed_qs][:3]
selected_mixed_qs.extend(extra_servlet)

# Spring selections
for t in spring_topics:
    t_qs = [q for q in spring_qs if q.get("topicId") == t]
    selected_mixed_qs.extend(t_qs[:2]) # Take 2 from each -> 12 qs
# Take 3 extra spring questions
extra_spring = [q for q in spring_qs if q not in selected_mixed_qs][:3]
selected_mixed_qs.extend(extra_spring)

# JPA selections
for t in jpa_topics:
    t_qs = [q for q in jpa_qs if q.get("topicId") == t]
    selected_mixed_qs.extend(t_qs[:2]) # Take 2 from each -> 10 qs

print(f"Exam 4 (Mixed) Questions: {len(selected_mixed_qs)} (Expected: 40)")

preset_exams.append({
    "id": "de_4",
    "name": "Đề thi thử số 4 (Tổng hợp Đề cương Java Web)",
    "description": "Đề thi thử tổng hợp cấu trúc trộn ngẫu nhiên bám sát toàn bộ đề cương Java Web: Servlet, Spring Boot, Spring MVC, JPA & Hibernate (40 câu hỏi).",
    "questions": selected_mixed_qs
})

# Write to data/java/preset_exams.json
with open(os.path.join(data_java_dir, "preset_exams.json"), "w", encoding="utf-8") as f:
    json.dump(preset_exams, f, ensure_ascii=False, indent=2)
print("Updated data/java/preset_exams.json")


# --------------------------------------------------------------------------
# PART 5: GENERATE MARKDOWN COMPLIANT FILES (KNOWLEDGE & QUESTION BANKS)
# --------------------------------------------------------------------------
# 1. Java knowledge.md
java_knowledge_md_path = os.path.join(pdf_java_dir, "knowledge.md")
with open(java_knowledge_md_path, "w", encoding="utf-8") as f:
    f.write("# TỔNG HỢP KIẾN THỨC ÔN TẬP JAVA WEB\n\n")
    for t in java_knowledge:
        f.write(f"# {t['title']}\n\n")
        f.write("## Tóm tắt\n")
        first_lines = [line.strip() for line in t['content'].split('\n') if line.strip()][:2]
        f.write(" ".join(first_lines) + "\n\n")
        f.write("## Khái niệm\n")
        f.write(t['content'] + "\n\n")
        if "example" in t:
            f.write("## Ví dụ\n")
            f.write("```java\n" + t['example'] + "\n```\n\n")
        f.write("## Ghi nhớ\n")
        f.write("- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.\n")
        f.write("- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.\n\n")
        f.write("---\n\n")
print(f"Generated {java_knowledge_md_path}")

# 2. Java question_bank.md
java_qb_md_path = os.path.join(pdf_java_dir, "question_bank.md")
with open(java_qb_md_path, "w", encoding="utf-8") as f:
    f.write("# NGÂN HÀNG CÂU HỎI ÔN TẬP JAVA WEB (BÁM SÁT ĐỀ CƯƠNG)\n\n")
    f.write(f"Tổng số câu hỏi: {len(java_syllabus_qs)}\n\n")
    
    # Group questions by topic for readable markdown
    grouped_qs = {}
    for q in java_syllabus_qs:
        tid = q.get("topicId")
        grouped_qs.setdefault(tid, []).append(q)
        
    for tid in (servlet_topics + spring_topics + jpa_topics):
        topic_title = next((t["title"] for t in java_knowledge if t["topicId"] == tid), tid)
        qs = grouped_qs.get(tid, [])
        f.write(f"## {topic_title} ({len(qs)} câu)\n\n")
        
        for idx, q in enumerate(qs):
            f.write(f"### Câu {idx+1} [Trắc nghiệm]\n")
            f.write(f"{q.get('question')}\n\n")
            for opt in q.get("options", []):
                f.write(f"- {opt}\n")
            f.write(f"\n* **Đáp án đúng:** {q.get('correctAnswer')}\n")
            f.write(f"* **Giải thích:** {q.get('explanation')}\n\n")
        f.write("---\n\n")
print(f"Generated {java_qb_md_path}")

# 3. Python knowledge.md (Update existing)
py_knowledge_md_path = os.path.join(pdf_py_dir, "knowledge.md")
with open(py_knowledge_md_path, "w", encoding="utf-8") as f:
    f.write("# TỔNG HỢP KIẾN THỨC ÔN TẬP PYTHON (BẢN CHI TIẾT)\n\n")
    for t in py_knowledge:
        f.write(f"# {t['title']}\n\n")
        f.write("## Tóm tắt\n")
        first_lines = [line.strip() for line in t['content'].split('\n') if line.strip()][:2]
        f.write(" ".join(first_lines) + "\n\n")
        f.write("## Khái niệm\n")
        f.write(t['content'] + "\n\n")
        if "example" in t:
            f.write("## Ví dụ\n")
            f.write("```python\n" + t['example'] + "\n```\n\n")
        f.write("## Ghi nhớ\n")
        f.write("- Hãy làm quen với cú pháp và các ví dụ thực tế trên.\n")
        f.write("- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.\n\n")
        f.write("---\n\n")
print(f"Updated {py_knowledge_md_path}")

print("All Java and Python data and markdown files generated/updated successfully!")
