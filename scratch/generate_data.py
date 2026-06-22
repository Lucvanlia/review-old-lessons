import os
import shutil
import json

# Ensure directories exist
os.makedirs("c:/Users/DELL/Downloads/ontap_html/pdf", exist_ok=True)
os.makedirs("c:/Users/DELL/Downloads/ontap_html/data/java", exist_ok=True)

# Move ontap.pdf if it exists in root
pdf_src = "c:/Users/DELL/Downloads/ontap_html/ontap.pdf"
pdf_dest = "c:/Users/DELL/Downloads/ontap_html/pdf/ontap.pdf"
if os.path.exists(pdf_src) and not os.path.exists(pdf_dest):
    shutil.move(pdf_src, pdf_dest)
    print("Moved ontap.pdf to pdf/ folder.")

# Generate subjects.json
subjects = [
    {
        "id": "java",
        "name": "Lập Trình Web (Java/Spring/JPA)",
        "description": "Ôn tập Java Core, Servlet, Spring Boot, Spring MVC, JPA và Hibernate theo đề cương ôn thi.",
        "icon": "☕",
        "pdfs": ["ontap.pdf"]
    }
]

with open("c:/Users/DELL/Downloads/ontap_html/data/subjects.json", "w", encoding="utf-8") as f:
    json.dump(subjects, f, ensure_ascii=False, indent=2)
print("Generated subjects.json")

# Generate knowledge.json for Java
knowledge = [
  {
    "topicId": "servlet_lifecycle",
    "title": "Vòng đời Servlet (Servlet Lifecycle)",
    "content": "Vòng đời của Servlet được quản lý bởi Web Container (ví dụ: Tomcat). Gồm 3 phương thức chính:\n1. init(): Khởi tạo Servlet. Được gọi duy nhất 1 lần khi Servlet được nạp vào bộ nhớ. Thường dùng để cấu hình ban đầu hoặc nạp tài nguyên.\n2. service(): Xử lý các request từ Client. Mỗi request sẽ chạy trên một Thread riêng. service() sẽ gọi các phương thức doGet(), doPost(), doPut(), doDelete(),... tương ứng với HTTP Method.\n3. destroy(): Hủy Servlet. Được gọi duy nhất 1 lần trước khi Container giải phóng Servlet khỏi bộ nhớ để thu hồi tài nguyên.\n\nLưu ý: Chỉ có DUY NHẤT một instance (đối tượng) của mỗi lớp Servlet được tạo ra cho toàn bộ ứng dụng (Singleton pattern mặc định trong Container).",
    "example": "import jakarta.servlet.*;\nimport jakarta.servlet.http.*;\nimport java.io.IOException;\n\npublic class HelloServlet extends HttpServlet {\n    @Override\n    public void init() throws ServletException {\n        // Khởi tạo tài nguyên\n    }\n\n    @Override\n    protected void doGet(HttpServletRequest req, HttpServletResponse resp) \n            throws ServletException, IOException {\n        resp.getWriter().println(\"Hello World!\");\n    }\n\n    @Override\n    public void destroy() {\n        // Giải phóng tài nguyên\n    }\n}"
  },
  {
    "topicId": "session_cookie",
    "title": "Phân biệt Session vs Cookie",
    "content": "Đây là hai cơ chế phổ biến dùng để duy trì trạng thái người dùng (Session Management) trong giao thức HTTP không trạng thái (stateless):\n\n1. Cookie:\n- Vị trí lưu trữ: Client-side (ở trình duyệt người dùng dưới dạng file text).\n- Dung lượng: Rất nhỏ (thường tối đa 4KB mỗi cookie).\n- Thời gian sống: Có thể cấu hình tồn tại lâu dài (Persistent Cookie) hoặc mất đi khi đóng trình duyệt (Session Cookie).\n- Bảo mật: Thấp, dễ bị giả mạo hoặc đánh cắp (XSS, CSRF). Nên đặt thuộc tính HttpOnly và Secure.\n\n2. Session:\n- Vị trí lưu trữ: Server-side (trong bộ nhớ hoặc database của server).\n- Dung lượng: Không giới hạn (tùy thuộc vào bộ nhớ server).\n- Thời gian sống: Thường mặc định hết hạn sau 30 phút không hoạt động (Session timeout).\n- Bảo mật: Cao hơn Cookie vì dữ liệu nằm trên Server. Client chỉ giữ một mã định danh Session ID (thường lưu trong cookie tên JSESSIONID).\n\n* HttpServletRequest đại diện cho thông tin gửi đến từ client, còn HttpServletResponse đại diện cho dữ liệu server phản hồi về client.",
    "example": "// Cấu hình Session trong Servlet\nHttpSession session = request.getSession();\nsession.setAttribute(\"username\", \"nguyenvana\");\n\n// Tạo Cookie\nCookie cookie = new Cookie(\"userTheme\", \"dark\");\ncookie.setMaxAge(24 * 60 * 60); // 1 ngày\nresponse.addCookie(cookie);"
  },
  {
    "topicId": "genericservlet_httpservlet",
    "title": "GenericServlet vs HttpServlet",
    "content": "Hai class nền tảng để tạo Servlet trong Java:\n\n1. GenericServlet:\n- Là một abstract class triển khai interface Servlet và ServletConfig.\n- Là giao thức chung (Protocol-independent), không gắn liền với bất kỳ giao thức cụ thể nào (có thể dùng cho SMTP, FTP, HTTP...).\n- Phải override phương thức abstract: service(ServletRequest, ServletResponse).\n\n2. HttpServlet:\n- Kế thừa từ GenericServlet và được tối ưu chuyên dụng cho giao thức HTTP (Protocol-dependent).\n- Đã ghi đè sẵn service() để phân tích request và gọi doGet(), doPost(), doPut(), doDelete()...\n- Khi xây dựng ứng dụng Web, ta hầu như luôn kế thừa từ HttpServlet và override các phương thức doXXX() thay vì service().",
    "example": "// Kế thừa GenericServlet (Ít dùng trong lập trình web thông thường)\npublic class MyGenericServlet extends GenericServlet {\n    public void service(ServletRequest req, ServletResponse res) throws ... {\n        // Phải xử lý thủ công\n    }\n}\n\n// Kế thừa HttpServlet (Chuẩn cho web ứng dụng)\npublic class MyHttpServlet extends HttpServlet {\n    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ... {\n        // Xử lý request HTTP GET\n    }\n}"
  },
  {
    "topicId": "requestdispatcher",
    "title": "RequestDispatcher: forward() vs sendRedirect()",
    "content": "Đây là hai cách chuyển hướng request trong Java Web:\n\n1. RequestDispatcher.forward():\n- Cơ chế: Chuyển tiếp request xử lý hoàn toàn phía Server-side. Trình duyệt client không hề biết có sự chuyển tiếp.\n- Số lượng request: Chỉ có 1 request duy nhất được gửi từ client. Đối tượng request và response được tái sử dụng.\n- Địa chỉ URL trên trình duyệt: Không thay đổi.\n- Tốc độ: Nhanh hơn vì không tốn kết nối mạng mới.\n\n2. HttpServletResponse.sendRedirect():\n- Cơ chế: Server gửi phản hồi mã 302 (Redirect) kèm URL mới về Client. Trình duyệt nhận được sẽ tự động gửi một request mới tới URL đó.\n- Số lượng request: Có 2 request riêng biệt từ client.\n- Địa chỉ URL trên trình duyệt: Thay đổi sang URL mới.\n- Phạm vi: Có thể chuyển hướng sang tài nguyên ngoài ứng dụng (ví dụ: google.com).",
    "example": "// Sử dụng forward (Client giữ nguyên URL)\nrequest.setAttribute(\"message\", \"Thành công\");\nRequestDispatcher rd = request.getRequestDispatcher(\"/result.jsp\");\nrd.forward(request, response);\n\n// Sử dụng sendRedirect (Trình duyệt đổi URL)\nresponse.sendRedirect(\"https://google.com\");"
  },
  {
    "topicId": "filter_api",
    "title": "Servlet Filter & web.xml",
    "content": "1. Filter là gì:\n- Filter là một đối tượng trung gian dùng để chặn (intercept) các request và response trước khi chúng đến Servlet hoặc phản hồi về Client.\n- Công dụng: Ghi log, nén dữ liệu, kiểm tra quyền đăng nhập (authentication/authorization), phân tích mã hóa ký tự (UTF-8).\n- Ba phương thức vòng đời: init(FilterConfig), doFilter(request, response, chain), destroy().\n- Trong doFilter(), ta phải gọi chain.doFilter(request, response) để chuyển tiếp request đến Filter kế tiếp hoặc Servlet đích.\n\n2. Cấu hình Filter/Servlet:\n- Trước Java EE 6: Phải khai báo thủ công trong file cấu hình `/WEB-INF/web.xml`.\n- Từ Java EE 6 trở đi: Có thể sử dụng Annotation như `@WebServlet` và `@WebFilter` giúp tinh giản mã nguồn.",
    "example": "// Khai báo Filter bằng Annotation\n@WebFilter(urlPatterns = \"/admin/*\")\npublic class AuthFilter implements Filter {\n    public void init(FilterConfig config) {} \n    \n    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain) \n            throws IOException, ServletException {\n        HttpServletRequest request = (HttpServletRequest) req;\n        if (request.getSession().getAttribute(\"user\") == null) {\n            ((HttpServletResponse) res).sendRedirect(\"/login\");\n        } else {\n            chain.doFilter(req, res); // Đi tiếp\n        }\n    }\n    \n    public void destroy() {}\n}"
  },
  {
    "topicId": "jdbc_api",
    "title": "JDBC API",
    "content": "JDBC (Java Database Connectivity) là API tiêu chuẩn giúp ứng dụng Java kết nối và tương tác với cơ sở dữ liệu quan hệ.\nQuy trình làm việc cơ bản với JDBC gồm 5 bước:\n1. Nạp JDBC Driver (từ JDBC 4.0 trở đi, việc này tự động qua Service Provider Interface).\n2. Thiết lập Connection bằng DriverManager.getConnection(url, username, password).\n3. Tạo Statement hoặc PreparedStatement. (Nên dùng PreparedStatement để tránh lỗi SQL Injection và tối ưu hiệu năng do cơ chế biên dịch trước).\n4. Thực thi câu lệnh (executeQuery cho SELECT, executeUpdate cho INSERT/UPDATE/DELETE) và nhận kết quả ResultSet.\n5. Đóng Connection, Statement và ResultSet để tránh rò rỉ tài nguyên (nên dùng try-with-resources).",
    "example": "String query = \"SELECT * FROM users WHERE id = ?\";\ntry (Connection conn = DriverManager.getConnection(dbUrl, user, pass);\n     PreparedStatement pstmt = conn.prepareStatement(query)) {\n    pstmt.setInt(1, 10);\n    try (ResultSet rs = pstmt.executeQuery()) {\n        if (rs.next()) {\n            System.out.println(\"Username: \" + rs.getString(\"username\"));\n        }\n    }\n} catch (SQLException e) {\n    e.printStackTrace();\n}"
  },
  {
    "topicId": "springboot_autoconfig",
    "title": "Spring Boot Auto-configuration",
    "content": "Spring Boot giải quyết bài toán cấu hình phức tạp (boilerplate) bằng cơ chế cấu hình tự động (Auto-configuration):\n\n1. `@SpringBootApplication`:\nLà annotation tích hợp 3 annotation quan trọng:\n- `@SpringBootConfiguration`: Đánh dấu class cấu hình.\n- `@EnableAutoConfiguration`: Kích hoạt cơ chế tự động quét classpath, tìm các thư viện starter và tự động tạo ra các Bean cấu hình mặc định (ví dụ: thấy thư viện h2 trong classpath thì tự tạo DataSource H2).\n- `@ComponentScan`: Quét tất cả các Spring Beans trong package hiện tại và các package con.\n\n2. Vô hiệu hóa Auto-configuration cụ thể:\nNếu không muốn dùng cấu hình tự động nào đó, ta khai báo thuộc tính `exclude` trong `@SpringBootApplication`.\n\n3. `spring-boot-starter-parent`:\nLà một file POM cha đặc biệt định nghĩa sẵn các phiên bản của các thư viện dependency, cấu hình build mặc định, giúp tránh xung đột phiên bản và đồng bộ hóa thư viện.",
    "example": "@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})\npublic class MyMainApplication {\n    public static void main(String[] args) {\n        SpringApplication.run(MyMainApplication.class, args);\n    }\n}"
  },
  {
    "topicId": "spring_mvc_flow",
    "title": "Luồng Request trong Spring MVC",
    "content": "Spring MVC sử dụng mô hình Front Controller thông qua DispatcherServlet. Luồng xử lý HTTP Request chi tiết như sau:\n1. Client gửi HTTP Request đến ứng dụng, **DispatcherServlet** sẽ tiếp nhận đầu tiên.\n2. **DispatcherServlet** hỏi **HandlerMapping** để tìm ra Controller nào sẽ xử lý request này dựa trên URL.\n3. **DispatcherServlet** chuyển giao việc thực thi cho **HandlerAdapter** để gọi phương thức tương ứng của **Controller**.\n4. **Controller** xử lý nghiệp vụ (gọi Service, Repository) và trả về một đối tượng **ModelAndView** (chứa tên View và dữ liệu Model) hoặc trả về trực tiếp dữ liệu (nếu dùng `@RestController` / `@ResponseBody`).\n5. Nếu trả về View Name, **DispatcherServlet** nhờ **ViewResolver** xác định file giao diện vật lý (ví dụ: JSP, Thymeleaf).\n6. View tiến hành render dữ liệu và gửi HTTP Response ngược lại cho client.",
    "example": "/* Sơ đồ tóm tắt:\nRequest -> DispatcherServlet\n               ↓\n         HandlerMapping (Tìm Controller)\n               ↓\n         HandlerAdapter -> Controller (Xử lý)\n               ↓\n         ModelAndView / ViewResolver (Hiển thị)\n               ↓\nResponse <- DispatcherServlet */"
  },
  {
    "topicId": "spring_mvc_annotations",
    "title": "Spring MVC Annotations: @PathVariable vs @RequestParam",
    "content": "Hai annotation này dùng để trích xuất dữ liệu từ HTTP Request:\n\n1. `@PathVariable`:\n- Dùng để lấy giá trị trực tiếp từ đường dẫn URL (URI Path Segment).\n- Thường dùng trong các API RESTful để định danh một tài nguyên.\n- Ví dụ URL: `/users/15` -> Số 15 là PathVariable.\n\n2. `@RequestParam`:\n- Dùng để lấy giá trị từ Query Parameter (sau dấu ?) hoặc từ Form Data của phương thức POST.\n- Thường dùng khi lọc dữ liệu, tìm kiếm, phân trang hoặc submit form.\n- Ví dụ URL: `/users?id=15` -> Số 15 là RequestParam.\n- Hỗ trợ các thuộc tính: `required` (bắt buộc hay không), `defaultValue` (giá trị mặc định).",
    "example": "@GetMapping(\"/books/{id}\") // Path Variable\npublic Book getBookById(@PathVariable(\"id\") Long bookId) {\n    return bookService.findById(bookId);\n}\n\n@GetMapping(\"/books\") // Query Parameter\npublic List<Book> searchBooks(\n    @RequestParam(value = \"genre\", required = false, defaultValue = \"All\") String genre) {\n    return bookService.findByGenre(genre);\n}"
  },
  {
    "topicId": "spring_filters",
    "title": "Các loại Filter trong Spring",
    "content": "Spring cung cấp các cơ chế filter để chặn request trước khi vào Controller. Ba loại phổ biến:\n\n1. Filter (jakarta.servlet.Filter):\n- Là interface tiêu chuẩn của Servlet Specification.\n- Chạy độc lập ngoài Spring Context, không thể tiêm các Spring Bean một cách dễ dàng nếu không cấu hình đặc biệt.\n\n2. GenericFilterBean:\n- Là một class abstract của Spring triển khai interface Filter.\n- Tích hợp thêm các tiện ích cấu hình của Spring, tự động lấy các init-parameters từ web.xml hoặc Spring Boot environment.\n- Khuyết điểm: Vẫn có thể chạy nhiều lần cho một request nếu request đó được forward hoặc include nội bộ.\n\n3. OncePerRequestFilter:\n- Là class abstract kế thừa từ GenericFilterBean.\n- Đảm bảo phương thức lọc `doFilterInternal` chỉ chạy đúng một lần duy nhất cho mỗi Request (bất kể có forward hay redirect nội bộ).\n- Đây là class được khuyến nghị sử dụng nhiều nhất khi viết Filter trong Spring Security hoặc Custom Filter.",
    "example": "public class JwtFilter extends OncePerRequestFilter {\n    @Override\n    protected void doFilterInternal(HttpServletRequest request, \n                                    HttpServletResponse response, \n                                    FilterChain filterChain)\n            throws ServletException, IOException {\n        String token = request.getHeader(\"Authorization\");\n        // Xử lý xác thực JWT ở đây\n        filterChain.doFilter(request, response); // Đi tiếp\n    }\n}"
  },
  {
    "topicId": "spring_di_ioc",
    "title": "Dependency Injection (DI) & Inversion of Control (IoC)",
    "content": "1. Inversion of Control (IoC):\n- Là một nguyên lý thiết kế phần mềm, trong đó quyền kiểm soát luồng hoạt động và quản lý vòng đời đối tượng được chuyển giao từ mã nguồn của lập trình viên sang cho Framework (ở đây là Spring Container).\n\n2. Dependency Injection (DI):\n- Là một dạng triển khai cụ thể của IoC. Thay vì tự khởi tạo các đối tượng phụ thuộc (dependency) bằng từ khóa `new`, Spring Container sẽ tự động 'tiêm' (inject) các phụ thuộc này vào lớp cần dùng.\n- Có 3 cách Injection chính:\n  + Constructor Injection (Khuyến nghị sử dụng vì đảm bảo dependency không null, dễ viết unit test, an toàn luồng).\n  + Setter Injection.\n  + Field Injection (Dùng `@Autowired` trực tiếp lên field, ngắn gọn nhưng khó test và tạo ra phụ thuộc chặt chẽ).\n\n3. Bean trong Spring:\n- Bean là một đối tượng được quản lý vòng đời (khởi tạo, cấu hình, hủy bỏ) bởi Spring IoC Container.\n- Cách định nghĩa Bean: Dùng annotation cấu hình như `@Bean` bên trong các class `@Configuration`, hoặc dùng các Stereotype Annotation để Spring tự quét component.",
    "example": "// Constructor Injection (Khuyến nghị)\n@Service\npublic class UserService {\n    private final UserRepository userRepository;\n\n    // Tự động tiêm qua Constructor\n    public UserService(UserRepository userRepository) {\n        this.userRepository = userRepository;\n    }\n}"
  },
  {
    "topicId": "spring_stereotype_annotations",
    "title": "Stereotype Annotations: @Component, @Service, @Repository, @Controller",
    "content": "Spring cung cấp các annotation chuyên môn hóa để phân loại các Bean và giúp cơ chế Component Scanning tự động phát hiện:\n\n1. `@Component`:\n- Đóng vai trò là annotation cha chung. Bất cứ class nào đánh dấu `@Component` đều được quét và tạo Bean trong IoC Container.\n\n2. `@Repository`:\n- Chuyên biệt cho tầng truy cập dữ liệu (Data Access Layer - DAO).\n- Tự động bắt và chuyển đổi các ngoại lệ của DB thành các ngoại lệ chung của Spring Data Access Exception.\n\n3. `@Service`:\n- Chuyên biệt cho tầng xử lý nghiệp vụ (Business Logic Layer).\n- Không có chức năng bổ sung đặc biệt ngoài việc phân cấp rõ ràng và giữ tính ngữ nghĩa.\n\n4. `@Controller`:\n- Chuyên biệt cho tầng trình diễn (Presentation Layer), nhận request và trả về View (HTML, JSP).\n- `@RestController` là sự kết hợp của `@Controller` và `@ResponseBody`, tự động chuyển đổi dữ liệu trả về thành JSON/XML để làm Web API.",
    "example": "@Repository\npublic class UserRepository { /* Truy vấn DB */ }\n\n@Service\npublic class UserService {\n    // Sử dụng UserRepository\n}\n\n@RestController\n@RequestMapping(\"/api/users\")\npublic class UserController {\n    // Nhận request REST API\n}"
  },
  {
    "topicId": "jpa_fetch_type",
    "title": "JPA Fetch Type: EAGER vs LAZY",
    "content": "Fetch Type định nghĩa cách Hibernate tải các đối tượng liên quan (associated entities) từ database:\n\n1. EAGER Loading:\n- Ý nghĩa: Tải dữ liệu liên quan NGAY LẬP TỨC cùng với đối tượng chính.\n- Mặc định cho: Các mối quan hệ đơn lẻ như `@OneToOne`, `@ManyToOne`.\n- Nhược điểm: Dẫn đến việc tải quá nhiều dữ liệu thừa, làm chậm truy vấn nếu không cần dùng đến quan hệ đó.\n\n2. LAZY Loading:\n- Ý nghĩa: TRÌ HOÃN việc tải dữ liệu liên quan. Dữ liệu chỉ được tải từ DB khi ta gọi hàm getter của trường quan hệ đó lần đầu tiên (truy vấn theo yêu cầu - load on demand).\n- Mặc định cho: Các mối quan hệ danh sách như `@OneToMany`, `@ManyToMany`.\n- Lợi ích: Tối ưu hiệu năng, giảm dung lượng bộ nhớ. Khuyên dùng cho tất cả các quan hệ và chỉ lấy khi thực sự cần thiết.\n- Lưu ý: Gọi getter ngoài phạm vi Transaction (sau khi Session đóng) sẽ ném ra ngoại lệ `LazyInitializationException`.",
    "example": "@Entity\npublic class Department {\n    @Id\n    private Long id;\n    \n    // Mặc định là LAZY. Khuyến nghị giữ nguyên.\n    @OneToMany(mappedBy = \"department\", fetch = FetchType.LAZY)\n    private List<Employee> employees;\n}"
  },
  {
    "topicId": "jpa_entity_lifecycle",
    "title": "Vòng đời Entity trong JPA (Entity Lifecycle)",
    "content": "Một thực thể (Entity) trong JPA trải qua 4 trạng thái quản lý chính:\n1. Transient (Tạm thời):\n- Đối tượng mới được tạo bằng từ khóa `new`, chưa liên kết với bất kỳ dòng nào trong CSDL và chưa được quản lý bởi Persistence Context (EntityManager).\n2. Managed (Được quản lý):\n- Đối tượng đang được liên kết với một dòng trong CSDL và được Persistence Context quản lý. Mọi thay đổi trên đối tượng này sẽ được tự động đồng bộ xuống DB (Dirty Checking) khi Transaction commit.\n- Trở thành Managed qua các hàm: persist(), merge(), find().\n3. Detached (Bị tách rời):\n- Đối tượng từng nằm trong trạng thái Managed nhưng hiện tại không còn liên kết với Persistence Context nữa (ví dụ sau khi gọi clear(), detach() hoặc Session kết thúc).\n- Thay đổi trên đối tượng Detached không tự động lưu xuống DB.\n4. Removed (Đã xóa):\n- Đối tượng được đánh dấu để xóa khỏi CSDL (bằng cách gọi remove()). Nó sẽ bị xóa thực tế khỏi DB khi commit transaction.",
    "example": "// Minh họa chuyển đổi trạng thái\nUser user = new User(\"Bình\"); // Transient\nem.persist(user); // Trở thành Managed\nem.detach(user); // Trở thành Detached\nuser.setName(\"Bình An\"); // Không lưu xuống DB\nUser managedUser = em.merge(user); // Trở lại Managed\nem.remove(managedUser); // Trở thành Removed (đợi xóa khi commit)"
  },
  {
    "topicId": "jpa_transaction",
    "title": "JPA Transaction & @Transactional",
    "content": "1. Khái niệm Transaction:\n- Một Transaction (Giao dịch) là tập hợp các hoạt động cơ sở dữ liệu phải được thực hiện thành công trọn vẹn cùng nhau (All or Nothing - ACID).\n\n2. `@Transactional` trong Spring:\n- Cho phép quản lý transaction theo kiểu khai báo (Declarative Transaction Management).\n- Khi một phương thức được đánh dấu `@Transactional`, Spring sẽ tạo một proxy bao quanh để tự động bắt đầu transaction trước khi chạy và commit sau khi phương thức kết thúc.\n- **Điều kiện Rollback:** Mặc định, transaction chỉ rollback khi có ngoại lệ không được kiểm tra (**Unchecked Exception** - kế thừa từ `RuntimeException` hoặc `Error`) xảy ra. Với các ngoại lệ có kiểm tra (**Checked Exception**), transaction vẫn COMMIT bình thường trừ khi ta khai báo rõ ràng bằng `@Transactional(rollbackFor = Exception.class)`.",
    "example": "@Service\npublic class BankService {\n    @Transactional(rollbackFor = InsufficientFundsException.class)\n    public void transferMoney(Long fromId, Long toId, double amount) \n            throws InsufficientFundsException {\n        accountRepo.withdraw(fromId, amount);\n        accountRepo.deposit(toId, amount);\n        // Nếu có Exception ném ra ở đây, DB tự động Rollback\n    }\n}"
  },
  {
    "topicId": "jpa_nplus1_problem",
    "title": "Vấn đề N+1 Query trong Hibernate & Cách xử lý",
    "content": "1. Vấn đề N+1 là gì:\n- Xảy ra khi ta muốn lấy danh sách N đối tượng cha, và ứng dụng tự động thực hiện thêm N câu lệnh SELECT phụ để lấy các đối tượng con liên quan của từng đối tượng cha đó (tổng cộng 1 câu SELECT cha + N câu SELECT con = N+1 query).\n- Làm suy giảm hiệu năng nghiêm trọng khi N lớn.\n\n2. Nguyên nhân:\n- Do cấu hình quan hệ LAZY loading và ta duyệt qua danh sách cha rồi gọi getter con, hoặc do EAGER loading cấu hình sai cách khiến Hibernate tự động chạy SELECT bổ sung.\n\n3. Các cách khắc phục:\n- **Join Fetch (JPQL/HQL):** Sử dụng mệnh đề `JOIN FETCH` trong câu truy vấn JPQL để lấy cả cha và con chỉ trong 1 câu SQL JOIN duy nhất.\n- **Entity Graph (@EntityGraph):** Định nghĩa sơ đồ tải dữ liệu đi kèm với phương thức repository để ép Hibernate join bảng.\n- **Batch Size (@BatchSize):** Cho phép nạp các quan hệ con theo từng lô (ví dụ mỗi câu SELECT lấy con của 10-20 cha cùng lúc) để giảm số lượng câu truy vấn từ N+1 xuống còn N/BatchSize + 1.",
    "example": "// Gây lỗi N+1:\nList<Department> deps = em.createQuery(\"FROM Department\", Department.class).getResultList();\nfor(Department d : deps) {\n    System.out.println(d.getEmployees().size()); // Gọi SELECT cho mỗi Department\n}\n\n// Khắc phục bằng JOIN FETCH:\nList<Department> depsCorrect = em.createQuery(\n    \"SELECT d FROM Department d JOIN FETCH d.employees\", Department.class).getResultList();\n// Chỉ chạy duy nhất 1 câu SELECT JOIN"
  },
  {
    "topicId": "jpa_orm_languages",
    "title": "Phân biệt JPA, ORM, JPQL và HQL",
    "content": "Bốn thuật ngữ cốt lõi trong lập trình tương tác cơ sở dữ liệu trong hệ sinh thái Java:\n\n1. ORM (Object-Relational Mapping):\n- Là một kỹ thuật/khái niệm lập trình giúp ánh xạ các đối tượng (Object) trong ngôn ngữ hướng đối tượng sang các bảng (Relation) trong cơ sở dữ liệu quan hệ.\n\n2. JPA (Java Persistence API):\n- Là một đặc tả (Specification) - bộ các quy chuẩn, giao diện của Java EE/Jakarta EE về ORM.\n- Bản thân JPA không tự thực thi mà chỉ định nghĩa các interface (như EntityManager, Entity). Các thư viện bên thứ 3 sẽ triển khai các interface này.\n\n3. Hibernate:\n- Là một framework ORM cụ thể triển khai (implementation) đặc tả JPA phổ biến nhất hiện nay.\n\n4. JPQL (Java Persistence Query Language) & HQL (Hibernate Query Language):\n- JPQL là ngôn ngữ truy vấn hướng đối tượng được định nghĩa bởi đặc tả JPA. Nó thực hiện truy vấn trên các Entity và thuộc tính của Entity chứ không trực tiếp trên bảng và cột của CSDL.\n- HQL là ngôn ngữ truy vấn riêng của Hibernate, xuất hiện trước JPQL. JPQL chính là một tập con tiêu chuẩn hóa của HQL. HQL linh hoạt và hỗ trợ nhiều tính năng mở rộng hơn của Hibernate.",
    "example": "// Ví dụ câu truy vấn JPQL (đối tượng hóa, truy vấn theo Entity User chứ không phải bảng users)\nTypedQuery<User> query = em.createQuery(\n    \"SELECT u FROM User u WHERE u.age > :minAge\", User.class);\nquery.setParameter(\"minAge\", 18);\nList<User> list = query.getResultList();"
  }
]

with open("c:/Users/DELL/Downloads/ontap_html/data/java/knowledge.json", "w", encoding="utf-8") as f:
    json.dump(knowledge, f, ensure_ascii=False, indent=2)
print("Generated knowledge.json for java")

# Generate questions.json for Java
questions = [
  {
    "id": 1,
    "topicId": "servlet_lifecycle",
    "question": "Phương thức nào trong vòng đời của một Servlet chỉ được Container gọi duy nhất một lần để khởi tạo đối tượng Servlet?",
    "options": [
      "A. service()",
      "B. init()",
      "C. destroy()",
      "D. doGet()"
    ],
    "correctAnswer": "B",
    "explanation": "Phương thức init() được Web Container gọi đúng một lần duy nhất khi Servlet được nạp vào bộ nhớ để thực hiện các cấu hình khởi tạo trước khi nó sẵn sàng xử lý các request."
  },
  {
    "id": 2,
    "topicId": "servlet_lifecycle",
    "question": "Trong kiến trúc Servlet của ứng dụng Java Web mặc định, có bao nhiêu đối tượng (instance) của một Servlet Class được Container khởi tạo cho toàn bộ ứng dụng?",
    "options": [
      "A. Mỗi request từ client sẽ tạo ra một đối tượng Servlet mới.",
      "B. Mỗi session của một user sẽ tạo ra một đối tượng Servlet mới.",
      "C. Chỉ có duy nhất một đối tượng duy nhất được tạo ra (Singleton pattern).",
      "D. Có tối đa 10 đối tượng được tạo ra theo cấu hình mặc định."
    ],
    "correctAnswer": "C",
    "explanation": "Mặc định, Servlet Container chỉ tạo ra một đối tượng (instance) duy nhất cho mỗi lớp Servlet đã khai báo. Các request gửi tới đồng thời sẽ được xử lý bằng các luồng (thread) khác nhau chạy trên cùng một đối tượng Servlet đó."
  },
  {
    "id": 3,
    "topicId": "servlet_lifecycle",
    "question": "Đâu là phương thức vòng đời của Servlet thực hiện chức năng xử lý các request và điều hướng đến các phương thức tương ứng như doGet(), doPost()?",
    "options": [
      "A. init(ServletConfig config)",
      "B. destroy()",
      "C. service(ServletRequest req, ServletResponse res)",
      "D. run()"
    ],
    "correctAnswer": "C",
    "explanation": "Phương thức service() là trung tâm xử lý request của Servlet. Mỗi khi có request gửi đến, Web Container sẽ gọi service(), từ đó servlet sẽ đọc HTTP method và gọi các hàm tương ứng như doGet(), doPost()."
  },
  {
    "id": 4,
    "topicId": "session_cookie",
    "question": "Cookie được lưu trữ ở đâu và kích thước tối đa của mỗi cookie thông thường là bao nhiêu?",
    "options": [
      "A. Lưu trữ ở Server-side, dung lượng không giới hạn.",
      "B. Lưu trữ ở Client-side (trình duyệt), dung lượng tối đa khoảng 4KB.",
      "C. Lưu trữ ở Database, dung lượng tùy thuộc cấu hình ổ đĩa.",
      "D. Lưu trữ ở RAM của Server, dung lượng tối đa 10MB."
    ],
    "correctAnswer": "B",
    "explanation": "Cookie là các tệp văn bản nhỏ được lưu trữ trực tiếp trên thiết bị của Client (trình duyệt). Dung lượng của mỗi cookie bị giới hạn bởi các trình duyệt, thông thường không vượt quá 4KB."
  },
  {
    "id": 5,
    "topicId": "session_cookie",
    "question": "Khi sử dụng Session để quản lý trạng thái người dùng trong Java Web, trình duyệt làm cách nào để liên kết các request tiếp theo với Session cụ thể trên Server?",
    "options": [
      "A. Trình duyệt gửi toàn bộ thông tin tài khoản người dùng kèm theo mỗi request.",
      "B. Trình duyệt gửi một Cookie chứa mã định danh duy nhất gọi là JSESSIONID.",
      "C. Server tự động nhận diện địa chỉ IP của client để map với Session.",
      "D. Trình duyệt sử dụng giao thức HTTPS để truyền tải thông tin Session ẩn."
    ],
    "correctAnswer": "B",
    "explanation": "Khi Session được tạo, Server sẽ gửi một mã định danh duy nhất (Session ID) về Client. Mã này thường được trình duyệt lưu trữ tự động trong một Cookie có tên mặc định là JSESSIONID và tự gửi kèm theo trong các request tiếp theo."
  },
  {
    "id": 6,
    "topicId": "genericservlet_httpservlet",
    "question": "Sự khác biệt cơ bản nhất giữa GenericServlet và HttpServlet là gì?",
    "options": [
      "A. GenericServlet hỗ trợ đa luồng còn HttpServlet thì không.",
      "B. GenericServlet là giao thức độc lập (Protocol-independent), còn HttpServlet chuyên biệt cho giao thức HTTP.",
      "C. GenericServlet là interface, HttpServlet là abstract class.",
      "D. GenericServlet chỉ chạy trên Tomcat cũ, HttpServlet chạy trên mọi web server."
    ],
    "correctAnswer": "B",
    "explanation": "GenericServlet triển khai interface Servlet một cách tổng quát và không phụ thuộc vào bất kỳ giao thức cụ thể nào. Trong khi đó, HttpServlet kế thừa GenericServlet và bổ sung các tính năng chuyên biệt chỉ dành riêng cho giao thức HTTP (ví dụ như các phương thức doGet, doPost)."
  },
  {
    "id": 7,
    "topicId": "requestdispatcher",
    "question": "Khi chuyển tiếp request sử dụng RequestDispatcher.forward(), địa chỉ URL hiển thị trên thanh địa chỉ của trình duyệt thay đổi như thế nào?",
    "options": [
      "A. URL thay đổi thành địa chỉ của trang đích.",
      "B. URL giữ nguyên không thay đổi.",
      "C. URL được nối thêm tham số ?redirect=true.",
      "D. URL bị xóa trắng."
    ],
    "correctAnswer": "B",
    "explanation": "Với forward(), quá trình chuyển tiếp request diễn ra hoàn toàn nội bộ trong Server. Client không gửi request mới mà chỉ nhận phản hồi từ trang đích, do đó địa chỉ URL trên thanh địa chỉ của trình duyệt được giữ nguyên không thay đổi."
  },
  {
    "id": 8,
    "topicId": "requestdispatcher",
    "question": "Phương thức HttpServletResponse.sendRedirect() hoạt động theo cơ chế nào?",
    "options": [
      "A. Chuyển hướng xử lý ở Server-side, client hoàn toàn không nhận biết được.",
      "B. Server gửi mã trạng thái HTTP 302 và URL mới về cho trình duyệt; trình duyệt sau đó tự động gửi một request mới tới URL đó.",
      "C. Server gọi trực tiếp phương thức doGet của Servlet đích thông qua phản chiếu (Reflection).",
      "D. Client tải lại toàn bộ ứng dụng web từ đầu."
    ],
    "correctAnswer": "B",
    "explanation": "sendRedirect() là cơ chế chuyển hướng ở Client-side. Server sẽ trả về client một HTTP response với status code 302 (Redirect) cùng tiêu đề Location chứa URL mới. Trình duyệt khi đọc được mã này sẽ tự động tạo một HTTP request hoàn toàn mới đến URL chỉ định."
  },
  {
    "id": 9,
    "topicId": "filter_api",
    "title": "Servlet Filter & web.xml",
    "question": "Trong phương thức doFilter() của một Filter, dòng lệnh nào bắt buộc phải được gọi để request có thể tiếp tục hành trình đến Servlet hoặc các Filter tiếp theo?",
    "options": [
      "A. response.sendRedirect()",
      "B. request.getRequestDispatcher().forward()",
      "C. chain.doFilter(request, response)",
      "D. filterConfig.getServletContext()"
    ],
    "correctAnswer": "C",
    "explanation": "Đối tượng FilterChain quản lý danh sách các filter và servlet đích. Việc gọi chain.doFilter(request, response) có tác dụng chuyển quyền điều khiển và request/response sang mắt xích tiếp theo trong chuỗi lọc. Nếu không gọi, request sẽ bị chặn đứng tại filter đó."
  },
  {
    "id": 10,
    "topicId": "jdbc_api",
    "question": "Tại sao việc sử dụng PreparedStatement lại được khuyến nghị hơn Statement thông thường trong lập trình JDBC?",
    "options": [
      "A. PreparedStatement dễ viết code hơn.",
      "B. PreparedStatement tự động đóng kết nối database khi chạy xong.",
      "C. PreparedStatement biên dịch trước câu lệnh SQL, giúp tăng hiệu năng khi chạy nhiều lần và ngăn chặn hiệu quả lỗi bảo mật SQL Injection.",
      "D. PreparedStatement không yêu cầu cài đặt JDBC Driver."
    ],
    "correctAnswer": "C",
    "explanation": "PreparedStatement gửi câu lệnh SQL có tham số (?) lên hệ quản trị CSDL để biên dịch và tối ưu hóa trước (pre-compile). Khi thực thi, ta chỉ gửi dữ liệu tham số đi. Điều này giúp tăng tốc độ thực thi khi câu lệnh chạy nhiều lần và tách biệt hoàn toàn dữ liệu với mã SQL, ngăn chặn triệt để SQL Injection."
  },
  {
    "id": 11,
    "topicId": "springboot_autoconfig",
    "question": "Annotation nào tích hợp cơ chế tự động quét component (@ComponentScan) và kích hoạt cấu hình tự động của Spring Boot (@EnableAutoConfiguration)?",
    "options": [
      "A. @Configuration",
      "B. @SpringBootApplication",
      "C. @EnableTransactionManagement",
      "D. @RestController"
    ],
    "correctAnswer": "B",
    "explanation": "@SpringBootApplication là một annotation tổ hợp (meta-annotation) bao gồm @SpringBootConfiguration, @EnableAutoConfiguration, và @ComponentScan giúp giảm thiểu cấu hình thủ công."
  },
  {
    "id": 12,
    "topicId": "springboot_autoconfig",
    "question": "Làm thế nào để vô hiệu hóa một cấu hình tự động (auto-configuration) cụ thể trong Spring Boot?",
    "options": [
      "A. Xóa file spring-boot-starter tương ứng trong file pom.xml.",
      "B. Sử dụng thuộc tính 'exclude' trong annotation @SpringBootApplication.",
      "C. Khai báo thuộc tính spring.autoconfigure.exclude trong file application.properties.",
      "D. Cả B và C đều đúng."
    ],
    "correctAnswer": "D",
    "explanation": "Có hai cách phổ biến để tắt một cấu hình tự động: sử dụng thuộc tính exclude trong annotation @SpringBootApplication (ví dụ: exclude = DataSourceAutoConfiguration.class) hoặc khai báo cấu hình loại trừ bằng text trong file properties/yml (spring.autoconfigure.exclude)."
  },
  {
    "id": 13,
    "topicId": "spring_mvc_flow",
    "question": "Trong luồng xử lý của Spring MVC, thành phần 'Front Controller' nào tiếp nhận toàn bộ các request đầu tiên và phân phối chúng đến các Controller tương ứng?",
    "options": [
      "A. Controller",
      "B. ViewResolver",
      "C. DispatcherServlet",
      "D. HandlerMapping"
    ],
    "correctAnswer": "C",
    "explanation": "DispatcherServlet hoạt động như một Front Controller trong Spring MVC. Nó là trung tâm tiếp nhận tất cả HTTP Request gửi đến ứng dụng và điều phối công việc cho các thành phần khác như HandlerMapping, Controller, ViewResolver."
  },
  {
    "id": 14,
    "topicId": "spring_mvc_flow",
    "question": "Vai trò của HandlerMapping trong Spring MVC là gì?",
    "options": [
      "A. Chuyển đổi dữ liệu đối tượng Java thành JSON.",
      "B. Ánh xạ (tìm kiếm) Controller và phương thức xử lý phù hợp dựa trên URL của request gửi tới.",
      "C. Tìm kiếm file giao diện JSP hoặc Thymeleaf trên đĩa cứng.",
      "D. Xử lý việc kiểm tra quyền đăng nhập của người dùng."
    ],
    "correctAnswer": "B",
    "explanation": "HandlerMapping có nhiệm vụ phân tích URL của request gửi đến và đối chiếu với các cấu hình định tuyến (như @GetMapping, @PostMapping) để xác định xem Controller và phương thức cụ thể nào chịu trách nhiệm xử lý request này."
  },
  {
    "id": 15,
    "topicId": "spring_mvc_annotations",
    "question": "Để lấy giá trị ID của một cuốn sách từ URL dạng '/books/102', ta nên sử dụng annotation nào trong phương thức xử lý của Spring Controller?",
    "options": [
      "A. @RequestParam",
      "B. @PathVariable",
      "C. @RequestBody",
      "D. @ModelAttribute"
    ],
    "correctAnswer": "B",
    "explanation": "@PathVariable được dùng để trích xuất các tham số biến nằm ngay trên phân đoạn đường dẫn URL (URI Path Segment). Trong trường hợp '/books/{id}', số 102 là một Path Variable."
  },
  {
    "id": 16,
    "topicId": "spring_mvc_annotations",
    "question": "Annotation @RequestParam dùng để trích xuất dữ liệu từ phần nào của HTTP Request?",
    "options": [
      "A. Từ Query Parameter (phần sau dấu ? trên URL) hoặc từ Form Data gửi lên.",
      "B. Từ phần Body của request dưới định dạng JSON.",
      "C. Từ các Header của HTTP request.",
      "D. Từ session của server."
    ],
    "correctAnswer": "A",
    "explanation": "@RequestParam được dùng để liên kết các tham số truy vấn (Query parameters ví dụ: ?page=1&limit=10) hoặc các trường dữ liệu được submit từ Form (x-www-form-urlencoded) vào các đối số của phương thức trong Controller."
  },
  {
    "id": 17,
    "topicId": "spring_filters",
    "question": "Trong ứng dụng Spring, class filter nào đảm bảo phương thức xử lý logic lọc chỉ được thực thi duy nhất một lần cho mỗi request gửi tới?",
    "options": [
      "A. GenericFilterBean",
      "B. OncePerRequestFilter",
      "C. SpringSecurityFilterChain",
      "D. LoggingFilter"
    ],
    "correctAnswer": "B",
    "explanation": "OncePerRequestFilter là một abstract class do Spring cung cấp, mở rộng từ GenericFilterBean. Điểm đặc biệt của nó là đảm bảo logic lọc trong doFilterInternal chỉ chạy đúng một lần duy nhất cho mỗi yêu cầu request, ngăn ngừa việc chạy lại do forward/redirect nội bộ."
  },
  {
    "id": 18,
    "topicId": "spring_di_ioc",
    "question": "Spring Container khuyên khích lập trình viên sử dụng phương thức Dependency Injection nào nhất để tiêm các phụ thuộc (dependencies) vào một Bean?",
    "options": [
      "A. Field Injection (sử dụng @Autowired trực tiếp trên biến thành viên).",
      "B. Constructor Injection (tiêm qua hàm tạo).",
      "C. Setter Injection (tiêm qua các phương thức setXXX).",
      "D. Interface Injection."
    ],
    "correctAnswer": "B",
    "explanation": "Constructor Injection là cách tiêm phụ thuộc được khuyến nghị nhiều nhất vì: đảm bảo các dependency không thể bị null (bắt buộc truyền khi tạo đối tượng), cho phép định nghĩa các trường phụ thuộc là 'final' (bất biến), dễ dàng viết Unit Test mà không cần mock framework phức tạp."
  },
  {
    "id": 19,
    "topicId": "spring_stereotype_annotations",
    "question": "Sự khác biệt cơ bản về mặt chức năng giữa annotation @Repository và các stereotype annotation khác như @Service hay @Component là gì?",
    "options": [
      "A. @Repository tự động thực hiện cấu hình kết nối DB.",
      "B. @Repository đánh dấu lớp thuộc tầng truy xuất dữ liệu (DAO) và tự động bắt các lỗi cơ sở dữ liệu để chuyển đổi chúng thành các Exception có tính nhất quán của Spring Data Access.",
      "C. @Repository giúp phương thức chạy song song đa luồng.",
      "D. Không có sự khác biệt nào ngoài mặt ngữ nghĩa gọi tên."
    ],
    "correctAnswer": "B",
    "explanation": "Ngoài việc đăng ký đối tượng làm Spring Bean, @Repository được thiết kế riêng cho tầng DAO. Spring sẽ áp dụng một bộ Aspect (AOP) để tự động dịch các ngoại lệ cụ thể của hệ quản trị CSDL (như SQLException) thành hệ thống ngoại lệ DataAccessException kế thừa từ RuntimeException của Spring."
  },
  {
    "id": 20,
    "topicId": "jpa_fetch_type",
    "question": "Tại sao chế độ tải dữ liệu LAZY Loading lại được khuyên dùng mặc định cho các quan hệ dạng bộ sưu tập như @OneToMany hay @ManyToMany?",
    "options": [
      "A. Vì LAZY Loading giúp ngăn chặn lỗi rò rỉ bộ nhớ (Memory Leak).",
      "B. Vì LAZY Loading giúp tránh việc truy vấn và tải các tập dữ liệu liên quan khổng lồ lên bộ nhớ khi chưa thực sự cần sử dụng, giúp tối ưu hiệu năng và thời gian truy vấn.",
      "C. Vì EAGER Loading bị cấm sử dụng trong đặc tả JPA mới nhất.",
      "D. Vì LAZY Loading tự động tạo chỉ mục (index) trong CSDL."
    ],
    "correctAnswer": "B",
    "explanation": "Trong mối quan hệ 1-Nhiều hoặc Nhiều-Nhiều, số lượng bản ghi con có thể rất lớn. Nếu sử dụng EAGER, mỗi lần lấy đối tượng cha, hệ thống sẽ tự động JOIN hoặc SELECT để lấy tất cả đối tượng con tương ứng. LAZY giúp trì hoãn việc này, chỉ khi nào ta gọi đến danh sách con thì Hibernate mới truy vấn."
  },
  {
    "id": 21,
    "topicId": "jpa_entity_lifecycle",
    "question": "Một đối tượng Entity vừa được khởi tạo bằng từ khóa 'new', chưa có ID và chưa được liên kết với Persistence Context nằm ở trạng thái nào trong vòng đời JPA?",
    "options": [
      "A. Managed",
      "B. Detached",
      "C. Transient",
      "D. Removed"
    ],
    "correctAnswer": "C",
    "explanation": "Trạng thái Transient (tạm thời) áp dụng cho các thực thể Java thuần túy vừa được khởi tạo bằng mã new. Nó chưa từng được lưu vào database, chưa có giá trị định danh khóa chính và chưa có sự kết nối nào với EntityManager."
  },
  {
    "id": 22,
    "topicId": "jpa_entity_lifecycle",
    "question": "Khi một Entity ở trạng thái 'Managed' trong Persistence Context, các thay đổi trên các thuộc tính của Entity đó được lưu xuống cơ sở dữ liệu vào thời điểm nào?",
    "options": [
      "A. Ngay lập tức khi ta gọi phương thức setter cho thuộc tính đó.",
      "B. Khi đối tượng bị bộ thu gom rác (Garbage Collector) dọn dẹp.",
      "C. Khi Transaction kết thúc và được COMMIT, Persistence Context tự động đối chiếu thay đổi (Dirty Checking) và đồng bộ xuống DB.",
      "D. Khi ta khởi động lại Server."
    ],
    "correctAnswer": "C",
    "explanation": "Với các Entity đang ở trạng thái Managed, EntityManager theo dõi các thay đổi trên đối tượng đó. Khi Transaction kết thúc và chuẩn bị COMMIT (hoặc khi gọi em.flush() thủ công), Hibernate sẽ chạy cơ chế Dirty Checking để tìm những thuộc tính bị thay đổi và tự tạo ra câu lệnh SQL UPDATE tương ứng để đồng bộ."
  },
  {
    "id": 23,
    "topicId": "jpa_transaction",
    "question": "Mặc định, một phương thức được đánh dấu @Transactional trong Spring Boot sẽ thực hiện ROLLBACK giao dịch khi xảy ra loại ngoại lệ nào?",
    "options": [
      "A. Bất kỳ loại ngoại lệ nào (bao gồm cả Checked và Unchecked Exception).",
      "B. Chỉ có các ngoại lệ được kiểm tra (Checked Exception - kế thừa từ Exception trực tiếp).",
      "C. Chỉ có các ngoại lệ không được kiểm tra (Unchecked Exception - kế thừa từ RuntimeException hoặc Error).",
      "D. Chỉ khi hệ thống bị mất kết nối cơ sở dữ liệu."
    ],
    "correctAnswer": "C",
    "explanation": "Theo mặc định trong Spring, cơ chế rollback tự động của @Transactional chỉ được kích hoạt bởi các ngoại lệ không được kiểm tra (RuntimeException và các lớp con của nó, hoặc các Error). Đối với Checked Exception, transaction vẫn commit trừ khi ta cấu hình bổ sung thuộc tính rollbackFor."
  },
  {
    "id": 24,
    "topicId": "jpa_nplus1_problem",
    "question": "Vấn đề N+1 Query trong Hibernate xảy ra trong tình huống nào sau đây?",
    "options": [
      "A. Khi thực hiện 1 câu lệnh SELECT lấy danh sách N bản ghi cha, và sau đó ứng dụng phải thực hiện thêm N câu lệnh SELECT phụ để lấy thông tin các bản ghi con liên quan của từng bản ghi cha.",
      "B. Khi hệ thống có hơn N kết nối đồng thời và gây nghẽn database.",
      "C. Khi ta thực hiện câu lệnh chèn thêm N+1 bản ghi mới vào một bảng trong một giao dịch duy nhất.",
      "D. Khi ta viết câu lệnh JOIN quá nhiều bảng vượt quá giới hạn N của DBMS."
    ],
    "correctAnswer": "A",
    "explanation": "Vấn đề N+1 xảy ra khi truy vấn danh sách N đối tượng cha (ví dụ lấy danh sách 10 Lớp học, mất 1 query). Sau đó, khi duyệt qua từng lớp học để lấy danh sách Học sinh, Hibernate lại thực thi thêm 10 câu lệnh SELECT học sinh của từng lớp tương ứng. Kết quả là mất tổng cộng 1 + 10 = 11 câu truy vấn, làm nghẽn DB."
  },
  {
    "id": 25,
    "topicId": "jpa_nplus1_problem",
    "question": "Để khắc phục triệt để vấn đề N+1 Query trong JPQL, giải pháp nào sau đây được khuyến nghị sử dụng giúp gộp tất cả dữ liệu cha và con vào trong một câu truy vấn SQL duy nhất?",
    "options": [
      "A. Sử dụng chế độ tải dữ liệu EAGER cho tất cả các quan hệ.",
      "B. Sử dụng mệnh đề 'JOIN FETCH' trong câu truy vấn JPQL.",
      "C. Sử dụng phương thức em.find() thay vì em.createQuery().",
      "D. Tăng kích thước Pool kết nối cơ sở dữ liệu."
    ],
    "correctAnswer": "B",
    "explanation": "Sử dụng từ khóa JOIN FETCH (ví dụ: 'SELECT d FROM Department d JOIN FETCH d.employees') yêu cầu Hibernate tạo ra một câu lệnh SQL sử dụng INNER JOIN hoặc LEFT JOIN để lấy tất cả dữ liệu Department và Employee liên quan cùng một lúc, giải quyết hoàn toàn vấn đề N+1."
  },
  {
    "id": 26,
    "topicId": "jpa_orm_languages",
    "question": "Phát biểu nào sau đây là ĐÚNG khi phân biệt giữa JPA và Hibernate?",
    "options": [
      "A. JPA là một thư viện ORM cụ thể, còn Hibernate là một đặc tả thiết kế của Java.",
      "B. Hibernate là một đặc tả tiêu chuẩn (Specification) còn JPA là framework triển khai cụ thể.",
      "C. JPA là một đặc tả tiêu chuẩn (Specification) quy chuẩn các interface, còn Hibernate là một framework triển khai cụ thể (Implementation) các interface đó.",
      "D. JPA và Hibernate là hai ngôn ngữ truy vấn hướng đối tượng khác nhau."
    ],
    "correctAnswer": "C",
    "explanation": "JPA (Java Persistence API) đóng vai trò là một đặc tả tiêu chuẩn, đưa ra các bộ quy tắc và các interface chung cho việc ánh xạ dữ liệu trong Java. Hibernate là một sản phẩm phần mềm hoàn chỉnh, đóng vai trò là nhà cung cấp dịch vụ (provider) triển khai cụ thể các interface định nghĩa sẵn của JPA."
  }
]

with open("c:/Users/DELL/Downloads/ontap_html/data/java/questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print("Generated questions.json for java")
