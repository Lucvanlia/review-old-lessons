# TỔNG HỢP KIẾN THỨC ÔN TẬP JAVA WEB

# Vòng đời Servlet (Servlet Lifecycle)

## Tóm tắt
Vòng đời của một Servlet được quản lý hoàn toàn bởi Servlet Container (Web Container như Tomcat, Jetty). Quy trình này bắt đầu từ lúc nạp Servlet vào bộ nhớ cho đến khi Servlet bị hủy bỏ. 1. CÁC GIAI ĐOẠN VÒNG ĐỜI VÀ PHƯƠNG THỨC CHÍNH:

## Khái niệm
Vòng đời của một Servlet được quản lý hoàn toàn bởi Servlet Container (Web Container như Tomcat, Jetty). Quy trình này bắt đầu từ lúc nạp Servlet vào bộ nhớ cho đến khi Servlet bị hủy bỏ.

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
  - Biện pháp: Tuyệt đối không dùng biến instance để lưu trữ trạng thái request. Hãy dùng biến cục bộ bên trong các phương thức (doGet, doPost) vì biến cục bộ được lưu trên Stack riêng của mỗi Thread, đảm bảo an toàn luồng.

## Ví dụ
```java
import jakarta.servlet.*;
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
}
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Phân biệt Session vs Cookie

## Tóm tắt
HTTP là một giao thức không trạng thái (stateless), nghĩa là mỗi request gửi đi độc lập và server không tự động nhớ client là ai. Để duy trì trạng thái phiên làm việc của người dùng, ta sử dụng Cookie và Session. 1. BẢNG SO SÁNH COOKIE VÀ SESSION:

## Khái niệm
HTTP là một giao thức không trạng thái (stateless), nghĩa là mỗi request gửi đi độc lập và server không tự động nhớ client là ai. Để duy trì trạng thái phiên làm việc của người dùng, ta sử dụng Cookie và Session.

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
  - Secure Flag: Khi setSecure(true), Cookie chỉ được truyền tải qua các kết nối được mã hóa bảo mật HTTPS, không gửi qua HTTP thường, tránh bị nghe lén (Sniffing).

## Ví dụ
```java
// Tương tác Session & Cookie trong Servlet
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
}
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# GenericServlet vs HttpServlet

## Tóm tắt
Servlet API cung cấp hai lớp abstract nền tảng kế thừa lẫn nhau để giúp lập trình viên xây dựng Servlet: GenericServlet và HttpServlet. 1. BẢNG SO SÁNH CHI TIẾT:

## Khái niệm
Servlet API cung cấp hai lớp abstract nền tảng kế thừa lẫn nhau để giúp lập trình viên xây dựng Servlet: GenericServlet và HttpServlet.

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
  - Nếu ghi đè service() rỗng và không gọi super, ứng dụng sẽ không làm gì và trả về phản hồi trắng với status code 200 mặc định.

## Ví dụ
```java
// Kế thừa GenericServlet (FTP Servlet)
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
}
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# RequestDispatcher: forward() vs sendRedirect()

## Tóm tắt
Khi cần chuyển hướng luồng xử lý từ một tài nguyên (Servlet/JSP) sang một tài nguyên khác, Servlet API hỗ trợ hai cơ chế hoàn toàn khác biệt: RequestDispatcher.forward() và HttpServletResponse.sendRedirect(). 1. BẢNG SO SÁNH CHUYỂN HƯỚNG:

## Khái niệm
Khi cần chuyển hướng luồng xử lý từ một tài nguyên (Servlet/JSP) sang một tài nguyên khác, Servlet API hỗ trợ hai cơ chế hoàn toàn khác biệt: RequestDispatcher.forward() và HttpServletResponse.sendRedirect().

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
  - Giải pháp: Áp dụng PRG. Sau khi xử lý POST thành công, gọi `sendRedirect()` sang trang thành công (GET). Khi người dùng nhấn F5, họ chỉ reload lại request GET trang thành công, không gây lặp lại dữ liệu POST.

## Ví dụ
```java
// Minh họa forward vs sendRedirect
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
}
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Servlet Filter & web.xml

## Tóm tắt
Filter (Bộ lọc) là đối tượng trung gian dùng để can thiệp, kiểm tra và xử lý các HTTP Request và Response trước khi chúng đi tới Servlet đích hoặc quay trở về Client. 1. VÒNG ĐỜI VÀ PHƯƠNG THỨC CỦA FILTER:

## Khái niệm
Filter (Bộ lọc) là đối tượng trung gian dùng để can thiệp, kiểm tra và xử lý các HTTP Request và Response trước khi chúng đi tới Servlet đích hoặc quay trở về Client.

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
  - Từ Java EE 6 trở đi: Hỗ trợ các Annotation như `@WebServlet` và `@WebFilter` giúp khai báo nhanh ngay trên code mà không cần file XML.

## Ví dụ
```java
// Custom Encoding Filter đặt tiếng Việt UTF-8 toàn bộ web
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
}
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# JDBC API

## Tóm tắt
JDBC (Java Database Connectivity) là một API tiêu chuẩn của Java cho phép kết nối, thực thi các câu lệnh SQL và tương tác với các hệ quản trị cơ sở dữ liệu quan hệ (RDBMS). 1. QUY TRÌNH JDBC TIÊU CHUẨN:

## Khái niệm
JDBC (Java Database Connectivity) là một API tiêu chuẩn của Java cho phép kết nối, thực thi các câu lệnh SQL và tương tác với các hệ quản trị cơ sở dữ liệu quan hệ (RDBMS).

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
  - Thứ tự đóng tài nguyên chuẩn để tránh rò rỉ bộ nhớ (Memory Leak): Đóng ResultSet trước -> Đóng Statement -> Đóng Connection (Đóng ngược lại với thứ tự mở). Nên sử dụng try-with-resources để tự động đóng tài nguyên kể cả khi xảy ra Exception.

## Ví dụ
```java
// Truy vấn JDBC an toàn sử dụng try-with-resources và PreparedStatement
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
} // Tự động đóng PreparedStatement và Connection
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Spring Boot Auto-configuration

## Tóm tắt
Spring Boot giải quyết bài toán cấu hình cồng kềnh (boilerplate code) của Spring Framework truyền thống bằng cơ chế cấu hình tự động (Auto-configuration) theo triết lý 'Convention over Configuration'. 1. PHÂN TÍCH ANNOTATION @SpringBootApplication:

## Khái niệm
Spring Boot giải quyết bài toán cấu hình cồng kềnh (boilerplate code) của Spring Framework truyền thống bằng cơ chế cấu hình tự động (Auto-configuration) theo triết lý 'Convention over Configuration'.

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
  - Là một file POM đặc biệt cung cấp tính năng quản lý phiên bản tập trung (Dependency Management). Nhờ kế thừa parent này, ta không cần khai báo thẻ `<version>` cho các thư viện starter của Spring, giúp tránh xung đột phiên bản và đảm bảo tính đồng bộ hệ thống.

## Ví dụ
```java
// Class chạy chính của dự án Spring Boot, loại bỏ DataSource Auto-config
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
}
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Luồng Request trong Spring MVC

## Tóm tắt
Spring MVC hoạt động dựa trên mẫu thiết kế Front Controller, trong đó toàn bộ các yêu cầu HTTP Request gửi tới ứng dụng đều được tiếp nhận và xử lý qua một Servlet trung tâm điều phối gọi là DispatcherServlet. 1. LUỒNG XỬ LÝ HTTP REQUEST CHI TIẾT (8 BƯỚC):

## Khái niệm
Spring MVC hoạt động dựa trên mẫu thiết kế Front Controller, trong đó toàn bộ các yêu cầu HTTP Request gửi tới ứng dụng đều được tiếp nhận và xử lý qua một Servlet trung tâm điều phối gọi là DispatcherServlet.

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
  - Sự cố hiển thị View Name: Nếu bạn muốn trả về trang HTML "home.html" bằng cách return String "home", nhưng lại đánh dấu class bằng `@RestController` hoặc `@ResponseBody`, trình duyệt sẽ hiển thị trực tiếp chữ "home" dạng văn bản thô thay vì hiển thị giao diện trang chủ.

## Ví dụ
```java
// Minh họa @Controller vs @RestController trong Spring MVC

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
}
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Spring MVC Annotations: @PathVariable vs @RequestParam

## Tóm tắt
Trong Spring MVC, để trích xuất và liên kết dữ liệu từ HTTP Request gửi lên vào các tham số của phương thức xử lý trong Controller, ta thường sử dụng hai annotation phổ biến: @PathVariable và @RequestParam. 1. BẢNG SO SÁNH @PathVariable VÀ @RequestParam:

## Khái niệm
Trong Spring MVC, để trích xuất và liên kết dữ liệu từ HTTP Request gửi lên vào các tham số của phương thức xử lý trong Controller, ta thường sử dụng hai annotation phổ biến: @PathVariable và @RequestParam.

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
  - Nếu tên biến phương thức trùng khớp hoàn toàn với tên biến khai báo trong mẫu đường dẫn URL (ví dụ: `/books/{id}` và tham số đầu vào là `Long id`), Spring Boot có thể tự động ánh xạ giá trị mà không cần ghi rõ tên trong dấu ngoặc kép như `@PathVariable("id")`. Tuy nhiên, viết rõ ràng vẫn là best practice để tránh lỗi khi nén code (obfuscation).

## Ví dụ
```java
// Sử dụng PathVariable và RequestParam trong Spring Controller
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
}
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Các loại Filter trong Spring

## Tóm tắt
Spring cung cấp các cơ chế bộ lọc (Filter) để chặn request trước khi vào Controller. Lập trình viên cần phân biệt 3 loại filter phổ biến trong hệ sinh thái Spring: Filter (interface gốc của Servlet), GenericFilterBean và OncePerRequestFilter. 1. PHÂN BIỆT 3 LOẠI FILTER:

## Khái niệm
Spring cung cấp các cơ chế bộ lọc (Filter) để chặn request trước khi vào Controller. Lập trình viên cần phân biệt 3 loại filter phổ biến trong hệ sinh thái Spring: Filter (interface gốc của Servlet), GenericFilterBean và OncePerRequestFilter.

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
  - Khi có request đi vào ứng dụng: Request -> Các Servlet Filter tiêu chuẩn -> Spring Security Filter Chain (đặc biệt OncePerRequestFilter) -> HandlerInterceptor -> Controller.

## Ví dụ
```java
// Đăng ký Custom Filter bằng FilterRegistrationBean
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
}
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Dependency Injection (DI) & Inversion of Control (IoC)

## Tóm tắt
Inversion of Control (IoC) và Dependency Injection (DI) là hai nguyên lý cốt lõi cấu thành nên Spring Framework, giúp giảm sự phụ thuộc chặt chẽ giữa các thành phần phần mềm (loose coupling). 1. PHÂN BIỆT IOC VÀ DI:

## Khái niệm
Inversion of Control (IoC) và Dependency Injection (DI) là hai nguyên lý cốt lõi cấu thành nên Spring Framework, giúp giảm sự phụ thuộc chặt chẽ giữa các thành phần phần mềm (loose coupling).

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
  - Sử dụng `@Bean` trên các phương thức trả về đối tượng bên trong class cấu hình `@Configuration`.

## Ví dụ
```java
// Minh họa Constructor Injection (Khuyến nghị)
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
}
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Stereotype Annotations: @Component, @Service, @Repository, @Controller

## Tóm tắt
Spring cung cấp các Stereotype Annotations chuyên biệt để phân loại vai trò của các Spring Bean trong cấu trúc ứng dụng 3 lớp (3-tier architecture). Điều này giúp Spring Container quét (Component Scanning) và quản lý vòng đời các đối tượng tự động. 1. PHÂN LOẠI CÁC ANNOTATION:

## Khái niệm
Spring cung cấp các Stereotype Annotations chuyên biệt để phân loại vai trò của các Spring Bean trong cấu trúc ứng dụng 3 lớp (3-tier architecture). Điều này giúp Spring Container quét (Component Scanning) và quản lý vòng đời các đối tượng tự động.

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
  - Bản chất `@Service`, `@Repository`, `@Controller` đều kế thừa từ `@Component` (đều có `@Component` ở bên trong). Việc phân tách này giúp ứng dụng dễ bảo trì và cho phép Spring áp dụng các Aspect (AOP) chuyên biệt cho từng tầng (ví dụ Exception Translation ở Repository, @Transactional ở Service, Request Mapping ở Controller).

## Ví dụ
```java
// 1. Tầng Repository kết nối DB
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
}
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# JPA Fetch Type: EAGER vs LAZY

## Tóm tắt
Trong JPA và Hibernate, khi thiết lập mối quan hệ giữa các Entity (Bảng dữ liệu), Fetch Type định nghĩa cách thức và thời điểm tải các đối tượng liên quan (associated entities) từ cơ sở dữ liệu lên bộ nhớ. 1. SO SÁNH HAI PHƯƠNG THỨC TẢI DỮ LIỆU:

## Khái niệm
Trong JPA và Hibernate, khi thiết lập mối quan hệ giữa các Entity (Bảng dữ liệu), Fetch Type định nghĩa cách thức và thời điểm tải các đối tượng liên quan (associated entities) từ cơ sở dữ liệu lên bộ nhớ.

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
  - Khắc phục: Giữ Transaction mở bằng `@Transactional` ở tầng Service để nạp dữ liệu trước khi đóng Session, hoặc sử dụng JPQL `JOIN FETCH` để lấy dữ liệu con chủ động.

## Ví dụ
```java
// Cấu hình Fetch Type trong Entity
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
}
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Vòng đời Entity trong JPA (Entity Lifecycle)

## Tóm tắt
Một thực thể (Entity) trong JPA được quản lý vòng đời bởi Persistence Context (EntityManager). Thực thể này sẽ đi qua 4 trạng thái quản lý chính. 1. BỐN TRẠNG THÁI CỦA ENTITY:

## Khái niệm
Một thực thể (Entity) trong JPA được quản lý vòng đời bởi Persistence Context (EntityManager). Thực thể này sẽ đi qua 4 trạng thái quản lý chính.

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
  - `detach()` / `clear()` / `close()`: Tách một hoặc toàn bộ đối tượng Managed thành Detached.

## Ví dụ
```java
// Minh họa luồng chuyển đổi trạng thái Entity
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
em2.getTransaction().commit(); // Cập nhật thành công tên "An Bình" xuống DB
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# JPA Transaction & @Transactional

## Tóm tắt
Trong cơ sở dữ liệu, một Transaction (Giao dịch) là một tập hợp các câu lệnh SQL phải được thực hiện thành công trọn vẹn cùng nhau (đảm bảo tính toàn vẹn dữ liệu ACID - All or Nothing). Spring Framework cung cấp annotation `@Transactional` để quản lý giao dịch tự động. 1. CƠ CHẾ HOẠT ĐỘNG CỦA @Transactional:

## Khái niệm
Trong cơ sở dữ liệu, một Transaction (Giao dịch) là một tập hợp các câu lệnh SQL phải được thực hiện thành công trọn vẹn cùng nhau (đảm bảo tính toàn vẹn dữ liệu ACID - All or Nothing). Spring Framework cung cấp annotation `@Transactional` để quản lý giao dịch tự động.

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
  - Nguyên nhân: Vì cuộc gọi nội bộ bỏ qua lớp proxy do Spring tạo ra.

## Ví dụ
```java
@Service
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
}
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Vấn đề N+1 Query trong Hibernate & Cách xử lý

## Tóm tắt
Vấn đề N+1 Query là một trong những nguyên nhân phổ biến nhất làm suy giảm hiệu năng nghiêm trọng trong các ứng dụng sử dụng ORM như Hibernate và JPA. 1. NGUYÊN NHÂN VÀ CƠ CHẾ GÂY LỖI:

## Khái niệm
Vấn đề N+1 Query là một trong những nguyên nhân phổ biến nhất làm suy giảm hiệu năng nghiêm trọng trong các ứng dụng sử dụng ORM như Hibernate và JPA.

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
  - Cấu hình số lượng bản ghi con được tải theo từng lô (ví dụ `@BatchSize(size = 20)`). Thay vì chạy N câu SELECT, Hibernate gộp chung lại dùng mệnh đề `IN` (ví dụ `WHERE company_id IN (1,2,3...20)`) để chỉ chạy `N/20 + 1` câu lệnh SELECT, giảm tải đáng kể cho database.

## Ví dụ
```java
// 1. Repository khắc phục lỗi N+1 bằng JPQL JOIN FETCH
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
}
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

# Phân biệt JPA, ORM, JPQL và HQL

## Tóm tắt
Trong hệ sinh thái phát triển Java Web, lập trình viên cần phân biệt rõ ràng 4 khái niệm dễ gây nhầm lẫn: ORM, JPA, Hibernate, JPQL và HQL. 1. PHÂN BIỆT 4 KHÁI NIỆM CỐT LÕI:

## Khái niệm
Trong hệ sinh thái phát triển Java Web, lập trình viên cần phân biệt rõ ràng 4 khái niệm dễ gây nhầm lẫn: ORM, JPA, Hibernate, JPQL và HQL.

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
• JPQL/HQL làm việc trên Entity Class và Class Fields (ví dụ: `SELECT u FROM User u WHERE u.age > 18` - chữ User viết hoa là tên Class, u.age là thuộc tính Java).

## Ví dụ
```java
// Minh họa truy vấn JPQL
EntityManager em = entityManagerFactory.createEntityManager();

// Truy vấn trên Entity Class "User" (Không phải bảng "users" trong database)
String jpql = "SELECT u FROM User u WHERE u.email LIKE :domain";
TypedQuery<User> query = em.createQuery(jpql, User.class);
query.setParameter("domain", "%@gmail.com");

List<User> users = query.getResultList();
```

## Ghi nhớ
- Hãy làm quen với cấu trúc mã nguồn và các ví dụ thực tế trên.
- Lưu ý các điểm lý thuyết trọng tâm khi làm bài trắc nghiệm.

---

