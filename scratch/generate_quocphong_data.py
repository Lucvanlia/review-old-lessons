# -*- coding: utf-8 -*-
import json
import os
import random

# Base paths
root_dir = "C:/Users/DELL/Downloads/ontap_html"
data_dir = os.path.join(root_dir, "data/quocphong")
os.makedirs(data_dir, exist_ok=True)

# Define Topics and Knowledge
topics = [
    {
        "topicId": "hp1_bai2_chien_tranh_quan_doi",
        "title": "Quan điểm của Chủ nghĩa Mác-Lênin, TT Hồ Chí Minh về Chiến tranh và Quân đội",
        "keywords": ["Chiến tranh", "Giai cấp", "Bạo lực cách mạng", "Quân đội kiểu mới", "Đảng lãnh đạo", "Chính trị chi phối", "Nhân dân lao động"],
        "summary": "Nghiên cứu quan điểm của chủ nghĩa Mác-Lênin và Tư tưởng Hồ Chí Minh về nguồn gốc, bản chất của chiến tranh và quân đội, từ đó rút ra bài học cho việc xây dựng quân đội nhân dân Việt Nam.",
        "focus": "- Chiến tranh bắt nguồn từ chế độ tư hữu, có giai cấp và đối kháng giai cấp.\n- Bản chất chiến tranh: Kế tục chính trị bằng thủ đoạn bạo lực.\n- Nguyên tắc xây dựng quân đội kiểu mới của Lênin: Đảng Cộng sản lãnh đạo là quan trọng nhất.\n- Quân đội nhân dân Việt Nam mang bản chất giai cấp công nhân, có tính nhân dân và tính dân tộc sâu sắc.",
        "mistakes": "- Nhầm lẫn nguồn gốc của chiến tranh: Nhiều sinh viên cho rằng chiến tranh có từ khi xuất hiện loài người (SAI), thực tế chiến tranh chỉ xuất hiện khi có chế độ tư hữu và giai cấp (ĐÚNG).\n- Phân biệt giữa chức năng và nhiệm vụ của quân đội.",
        "quick_memory": "Chiến tranh = Tư hữu + Giai cấp. Bản chất quân đội = Bản chất của giai cấp lãnh đạo (Nhà nước nuôi dưỡng)."
    },
    {
        "topicId": "hp1_bai3_duong_loi_quoc_phong",
        "title": "Đường lối Quốc phòng và An ninh của Đảng Cộng sản Việt Nam",
        "keywords": ["Toàn dân", "Toàn diện", "Tự lực cánh sinh", "Đại đoàn kết", "Tiềm lực kinh tế", "Tiềm lực chính trị", "Thế trận"],
        "summary": "Nội dung đường lối quốc phòng, an ninh của Đảng ta nhằm bảo vệ vững chắc Tổ quốc xã hội chủ nghĩa trong tình hình mới.",
        "focus": "- Hai nhiệm vụ chiến lược: Xây dựng CNXH và Bảo vệ Tổ quốc XHCN (luôn gắn bó chặt chẽ).\n- Đặc trưng của nền quốc phòng: Nền quốc phòng vì dân, do dân, của dân.\n- Mục đích: Tạo ra môi trường hòa bình, ổn định để phát triển kinh tế xã hội.\n- Tiềm lực quốc phòng an ninh: Tiềm lực chính trị tinh thần là nhân tố cơ bản, tiềm lực kinh tế là nền tảng vật chất.",
        "mistakes": "- Nhầm lẫn giữa 'Tiềm lực chính trị' và 'Tiềm lực quân sự'. Tiềm lực chính trị tinh thần mới là yếu tố quyết định sức mạnh tổng hợp.\n- Quên mất đặc trưng 'toàn dân, toàn diện' của nền quốc phòng Việt Nam.",
        "quick_memory": "Quốc phòng toàn dân = Bảo vệ hòa bình. Kinh tế là nền tảng, Chính trị tinh thần là quyết định."
    },
    {
        "topicId": "hp1_bai4_chien_tranh_nhan_dan",
        "title": "Chiến tranh Nhân dân Bảo vệ Tổ quốc",
        "keywords": ["Lực lượng vũ trang 3 thứ quân", "Toàn dân đánh giặc", "Thế trận", "Làng xã chiến đấu", "Chính nghĩa", "Bảo vệ độc lập"],
        "summary": "Nghệ thuật chiến tranh nhân dân của Việt Nam, phát huy sức mạnh của toàn dân tộc đánh giặc ngoại xâm.",
        "focus": "- Tính chất: Là cuộc chiến tranh chính nghĩa, tự vệ, mạng tính toàn dân, toàn diện.\n- Đặc điểm: Chống lại kẻ thù có vũ khí trang bị hiện đại hơn; diễn ra trong điều kiện quốc tế có nhiều biến động.\n- Lực lượng: Toàn dân tham gia, trong đó lực lượng vũ trang 3 thứ quân làm nòng cốt (Bộ đội chủ lực, bộ đội địa phương, dân quân tự vệ).",
        "mistakes": "- Thường nhầm lực lượng nòng cốt của chiến tranh nhân dân chỉ là Bộ đội chủ lực. Thực tế là LLVT 3 thứ quân.\n- Không phân biệt được Tính chất (chính nghĩa, toàn dân) và Đặc điểm (kẻ thù mạnh hơn) của chiến tranh nhân dân bảo vệ Tổ quốc.",
        "quick_memory": "Chiến tranh nhân dân = Toàn dân đánh giặc + LLVT 3 thứ quân làm nòng cốt."
    },
    {
        "topicId": "hp2_bai1_dien_bien_hoa_binh",
        "title": "Phòng chống Chiến lược Diễn biến hòa bình, Bạo loạn lật đổ",
        "keywords": ["DBHB", "Bạo loạn lật đổ", "Phi chính trị hóa", "Đa nguyên đa đảng", "Tôn giáo", "Dân tộc", "Tự diễn biến", "Tự chuyển hóa"],
        "summary": "Nhận diện âm mưu, thủ đoạn của các thế lực thù địch trong chiến lược DBHB và biện pháp phòng chống của ta.",
        "focus": "- Khái niệm: DBHB là chiến lược cơ bản nhằm lật đổ chế độ chính trị của các nước tiến bộ, trước hết là các nước XHCN từ bên trong bằng biện pháp phi quân sự.\n- Bạo loạn lật đổ là hành động bạo lực có tổ chức để lật đổ chính quyền.\n- Thủ đoạn chống phá: Kinh tế (phá hoại nền KTTT định hướng XHCN), Chính trị (đòi đa nguyên, đa đảng), Tư tưởng văn hóa (xóa bỏ CN Mác-Lênin), Tôn giáo dân tộc.\n- Giải pháp: Nâng cao nhận thức, giữ vững ổn định chính trị, chống 'tự diễn biến', 'tự chuyển hóa'.",
        "mistakes": "- Sinh viên hay nhầm lẫn giữa thủ đoạn về chính trị (đòi đa đảng) và thủ đoạn về tư tưởng văn hóa (đòi tự do báo chí, truyền bá lối sống thực dụng).\n- Nhầm 'phi chính trị hóa quân đội' thuộc lĩnh vực chính trị, thực chất đó là thủ đoạn trên lĩnh vực quốc phòng - an ninh.",
        "quick_memory": "DBHB = Đánh từ bên trong (Không dùng súng). Chống DBHB = Giữ vững trận địa tư tưởng và ổn định chính trị."
    },
    {
        "topicId": "hp2_bai3_bao_ve_moi_truong",
        "title": "Phòng chống vi phạm pháp luật về bảo vệ môi trường",
        "keywords": ["Ô nhiễm", "Tội phạm môi trường", "Mặt khách quan", "Mặt chủ quan", "Khách thể", "Chủ thể", "Phòng ngừa"],
        "summary": "Nắm vững các quy định pháp luật và biện pháp đấu tranh phòng chống tội phạm và vi phạm pháp luật về bảo vệ môi trường.",
        "focus": "- Tội phạm môi trường là hành vi nguy hiểm cho xã hội, vi phạm pháp luật hình sự về môi trường.\n- Các yếu tố cấu thành tội phạm: Khách thể (Quan hệ xã hội bị xâm phạm - quy định bảo vệ MT), Mặt khách quan (Hành vi xả thải, phá hoại), Chủ thể (Cá nhân, pháp nhân có năng lực TNHS), Mặt chủ quan (Lỗi cố ý hoặc vô ý).\n- Biện pháp phòng chống: Nâng cao ý thức cộng đồng, hoàn thiện hệ thống pháp luật, tăng cường chế tài xử phạt, ứng dụng công nghệ giám sát.",
        "mistakes": "- Nhầm lẫn giữa 'Khách thể' và 'Đối tượng tác động'. Khách thể là quan hệ xã hội được pháp luật bảo vệ, còn đối tượng tác động là môi trường sinh thái (rừng, nước, không khí).\n- Rất dễ nhầm lẫn Chủ thể của tội phạm môi trường chỉ bao gồm cá nhân. Thực tế pháp nhân thương mại cũng có thể là chủ thể của tội phạm môi trường.",
        "quick_memory": "4 yếu tố cấu thành: Khách thể (Cái bị hại) - Mặt khách quan (Hành vi) - Chủ thể (Kẻ làm) - Mặt chủ quan (Lỗi cố ý/vô ý)."
    }
]

# Generate Questions (Total: 75 questions - 15 per topic)
questions = []
q_id_counter = 1

def add_question(topicId, question, options, correctAnswer, explanation, type):
    global q_id_counter
    questions.append({
        "id": q_id_counter,
        "topicId": topicId,
        "question": question,
        "options": options,
        "correctAnswer": correctAnswer,
        "explanation": explanation,
        "type": type
    })
    q_id_counter += 1

# Topic 1: Chiến tranh và Quân đội
q1_data = [
    ("Theo quan điểm của chủ nghĩa Mác - Lênin, chiến tranh là gì?", 
     ["A. Là một hiện tượng tự nhiên tồn tại vĩnh viễn.", "B. Là một hiện tượng chính trị - xã hội có tính lịch sử.", "C. Là sự xung đột tự phát giữa các nhóm người.", "D. Là quy luật phát triển tất yếu của loài người."],
     "B", "Chủ nghĩa Mác - Lênin khẳng định chiến tranh không phải là hiện tượng tự nhiên hay vĩnh viễn, mà là một hiện tượng chính trị - xã hội có tính lịch sử, xuất hiện và mất đi trong những điều kiện lịch sử nhất định.", "Lý thuyết"),
    
    ("Theo quan điểm của Mác - Lênin, nguồn gốc sâu xa nảy sinh chiến tranh là gì?",
     ["A. Nguồn gốc kinh tế (Sự xuất hiện chế độ tư hữu về tư liệu sản xuất).", "B. Nguồn gốc chính trị (Sự mâu thuẫn giữa các nhà nước).", "C. Nguồn gốc xã hội (Sự xuất hiện của giai cấp).", "D. Nguồn gốc tư tưởng (Sự khác biệt về tôn giáo)."],
     "A", "Nguồn gốc kinh tế (sự xuất hiện chế độ tư hữu) là nguồn gốc sâu xa nhất, từ đó dẫn đến sự phân chia giai cấp (nguồn gốc xã hội/trực tiếp) và sinh ra chiến tranh.", "Phân tích"),

    ("Hồ Chí Minh khẳng định mục đích cuộc chiến tranh của dân tộc ta chống thực dân Pháp xâm lược là gì?",
     ["A. Để bảo vệ các nước xã hội chủ nghĩa.", "B. Để giành lại thị trường kinh tế trong khu vực.", "C. Bảo vệ độc lập dân tộc, chủ quyền quốc gia và thống nhất đất nước.", "D. Nhằm mở rộng tầm ảnh hưởng của Việt Nam ở Đông Nam Á."],
     "C", "Chiến tranh của Việt Nam là cuộc chiến tranh chính nghĩa, tự vệ, nhằm mục đích đánh đuổi ngoại xâm, bảo vệ độc lập, chủ quyền và thống nhất đất nước.", "Tổng hợp"),

    ("Trong mối quan hệ giữa chính trị và chiến tranh, yếu tố nào giữ vai trò quyết định?",
     ["A. Chiến tranh quyết định chính trị.", "B. Chính trị chi phối và quyết định toàn bộ tiến trình và kết cục của chiến tranh.", "C. Hai yếu tố tác động độc lập không liên quan.", "D. Chiến tranh và chính trị ngang hàng, tùy từng thời điểm."],
     "B", "Lênin khẳng định: Chính trị là sự thể hiện tập trung của kinh tế, chính trị chi phối, quyết định mục tiêu và toàn bộ tiến trình của chiến tranh. Chiến tranh chỉ là sự kế tục của chính trị bằng thủ đoạn bạo lực.", "Lý thuyết"),

    ("Nguyên tắc cơ bản và quan trọng nhất trong việc xây dựng quân đội kiểu mới của Lênin là gì?",
     ["A. Xây dựng quân đội chính quy, hiện đại.", "B. Tăng cường kỷ luật sắt trong quân đội.", "C. Sự lãnh đạo tuyệt đối, trực tiếp về mọi mặt của Đảng Cộng sản đối với quân đội.", "D. Đoàn kết quân dân gắn bó."],
     "C", "Để quân đội giữ vững bản chất giai cấp công nhân, nguyên tắc cốt lõi và quan trọng nhất là phải đặt dưới sự lãnh đạo tuyệt đối, trực tiếp về mọi mặt của Đảng Cộng sản.", "Phân tích"),

    ("Bản chất giai cấp của quân đội phụ thuộc vào yếu tố nào?",
     ["A. Tỉ lệ xuất thân của các binh sĩ trong quân đội.", "B. Bản chất của giai cấp, của nhà nước đã tổ chức, nuôi dưỡng và sử dụng quân đội đó.", "C. Khả năng tác chiến của quân đội.", "D. Truyền thống văn hóa của quốc gia đó."],
     "B", "Bản chất giai cấp của quân đội không phụ thuộc vào thành phần xuất thân của binh lính, mà phụ thuộc hoàn toàn vào bản chất của giai cấp, nhà nước đã tổ chức, lãnh đạo và nuôi dưỡng nó.", "Lý thuyết"),

    ("Theo Chủ tịch Hồ Chí Minh, Quân đội nhân dân Việt Nam mang bản chất của giai cấp nào?",
     ["A. Giai cấp nông dân.", "B. Giai cấp công nhân.", "C. Tầng lớp trí thức.", "D. Toàn dân tộc."],
     "B", "Theo tư tưởng Hồ Chí Minh, Quân đội nhân dân Việt Nam mang bản chất của giai cấp công nhân, đồng thời có tính nhân dân và tính dân tộc sâu sắc.", "Lý thuyết"),

    ("Chức năng của Quân đội nhân dân Việt Nam theo tư tưởng Hồ Chí Minh bao gồm:",
     ["A. Chiến đấu, tuần tra, bảo vệ.", "B. Chiến đấu, công tác, lao động sản xuất.", "C. Bảo vệ biên giới, bảo vệ hòa bình, phát triển kinh tế.", "D. Sẵn sàng chiến đấu, hỗ trợ an ninh, cứu hộ cứu nạn."],
     "B", "Chủ tịch Hồ Chí Minh đã xác định 3 chức năng cốt lõi của quân đội ta: Đội quân chiến đấu, đội quân công tác, đội quân lao động sản xuất.", "Tổng hợp"),

    ("Câu nói 'Phải dùng bạo lực cách mạng chống lại bạo lực phản cách mạng, giành lấy chính quyền và bảo vệ chính quyền' là của ai?",
     ["A. V.I. Lênin", "B. Các Mác", "C. Hồ Chí Minh", "D. Võ Nguyên Giáp"],
     "C", "Đây là tư tưởng xuyên suốt của Chủ tịch Hồ Chí Minh về tính tất yếu của bạo lực cách mạng để chống lại sự áp bức bóc lột bằng bạo lực của kẻ thù.", "Lý thuyết"),

    ("Để bảo vệ Tổ quốc XHCN, Lênin đã chỉ ra nội dung nào là nhiệm vụ cấp thiết?",
     ["A. Đẩy mạnh phát triển kinh tế thị trường.", "B. Bảo vệ Tổ quốc XHCN là một tất yếu khách quan, là nhiệm vụ thường xuyên.", "C. Tham gia các liên minh quân sự khu vực.", "D. Xây dựng vũ khí hạt nhân để răn đe."],
     "B", "Lênin khẳng định sau khi giai cấp vô sản giành được chính quyền, nhiệm vụ bảo vệ Tổ quốc XHCN là một tất yếu khách quan, liên tục và thường xuyên do sự chống phá của chủ nghĩa đế quốc.", "Lý thuyết"),

    ("Tình huống: Một sinh viên cho rằng 'Trong thời bình, chúng ta không cần phải xây dựng quân đội mạnh mà chỉ cần tập trung làm kinh tế'. Nhận định này sai ở điểm nào theo quan điểm Mác - Lênin?",
     ["A. Không sai, kinh tế mạnh thì tự nhiên quốc phòng sẽ mạnh.", "B. Sai, vì bảo vệ Tổ quốc XHCN là một nhiệm vụ thường xuyên, liên tục, phải gắn kết chặt chẽ giữa kinh tế và quốc phòng.", "C. Sai, vì chỉ có quân đội mạnh mới đi xâm chiếm được nước khác.", "D. Sai, vì trong thời bình quân đội vẫn phải đi làm kinh tế là chính."],
     "B", "Bảo vệ Tổ quốc là quy luật tất yếu. Kinh tế và quốc phòng phải luôn gắn bó chặt chẽ, không được lơ là cảnh giác ngay cả trong thời bình.", "Tình huống"),

    ("Tại sao quân đội ta lại có 'tính nhân dân và tính dân tộc sâu sắc' bên cạnh bản chất giai cấp công nhân?",
     ["A. Vì quân đội ta do Đảng lãnh đạo.", "B. Vì quân đội ta ra đời từ phong trào cách mạng của quần chúng, chiến đấu vì lợi ích của nhân dân và dân tộc.", "C. Vì quân đội ta không có chế độ đãi ngộ cao.", "D. Vì phần lớn quân đội ta xuất thân từ thành thị."],
     "B", "Sự thống nhất giữa bản chất giai cấp công nhân và tính nhân dân, tính dân tộc là do mục tiêu chiến đấu của quân đội ta hoàn toàn nhất trí với lợi ích của toàn dân tộc.", "Phân tích"),

    ("Một trong những nguyên tắc xây dựng Hồng quân của Lênin là 'Giữ vững quan điểm giai cấp'. Điều này có ý nghĩa gì?",
     ["A. Đảm bảo Hồng quân là công cụ bạo lực sắc bén của giai cấp vô sản.", "B. Đảm bảo mọi sĩ quan đều phải là người nghèo.", "C. Đảm bảo Hồng quân không sử dụng vũ khí của tư bản.", "D. Đảm bảo Hồng quân độc lập với Đảng."],
     "A", "Quan điểm giai cấp giúp Hồng quân xác định rõ đối tượng tác chiến, lý tưởng chiến đấu, phục vụ lợi ích của giai cấp vô sản và nhân dân lao động.", "Tổng hợp"),

    ("Nếu so sánh Quân đội tư sản và Quân đội XHCN, sự khác biệt bản chất nhất nằm ở đâu?",
     ["A. Số lượng vũ khí và quân số.", "B. Bản chất giai cấp và mục tiêu chiến đấu (Bảo vệ ai, chống lại ai).", "C. Hình thức huấn luyện chiến thuật.", "D. Trang phục và chế độ khen thưởng."],
     "B", "Bản chất của quân đội phụ thuộc vào giai cấp tổ chức và nuôi dưỡng nó. Quân đội tư sản bảo vệ thiểu số giai cấp bóc lột, quân đội XHCN bảo vệ đại đa số nhân dân lao động.", "So sánh"),

    ("Theo Lênin, yếu tố nào quyết định sức mạnh chiến đấu của Hồng quân?",
     ["A. Trang bị vũ khí hiện đại nhất.", "B. Sự lãnh đạo của Đảng, sự giác ngộ chính trị, tính kỷ luật tự giác.", "C. Sức mạnh thể chất của binh lính.", "D. Sự viện trợ từ bên ngoài."],
     "B", "Lênin luôn nhấn mạnh yếu tố con người, đặc biệt là sự giác ngộ chính trị và kỷ luật tự giác dưới sự lãnh đạo của Đảng là yếu tố quyết định sức mạnh.", "Tổng hợp")
]

# Topic 2: Đường lối Quốc phòng An ninh
q2_data = [
    ("Đảng ta xác định, trong xây dựng sức mạnh tổng hợp của nền quốc phòng, an ninh, tiềm lực nào giữ vai trò NỀN TẢNG vật chất?",
     ["A. Tiềm lực chính trị - tinh thần.", "B. Tiềm lực khoa học - công nghệ.", "C. Tiềm lực kinh tế.", "D. Tiềm lực quân sự, an ninh."],
     "C", "Tiềm lực kinh tế tạo ra cơ sở vật chất, vũ khí, trang bị, duy trì sức mạnh chiến đấu, do đó nó là nền tảng vật chất của nền quốc phòng toàn dân.", "Lý thuyết"),

    ("Tiềm lực nào giữ vai trò CƠ BẢN, QUYẾT ĐỊNH sức mạnh tổng hợp của nền quốc phòng toàn dân, an ninh nhân dân?",
     ["A. Tiềm lực quân sự.", "B. Tiềm lực kinh tế.", "C. Tiềm lực chính trị - tinh thần.", "D. Tiềm lực đối ngoại."],
     "C", "Tiềm lực chính trị - tinh thần (lòng dân, niềm tin vào Đảng, chế độ) là nhân tố cốt lõi, cơ bản nhất quyết định khả năng huy động các tiềm lực khác để chiến đấu.", "Lý thuyết"),

    ("Đặc trưng nổi bật của nền quốc phòng toàn dân, an ninh nhân dân của Việt Nam là gì?",
     ["A. Nền quốc phòng mang tính phi chính trị.", "B. Nền quốc phòng mang tính tấn công răn đe.", "C. Nền quốc phòng vì dân, của dân, do nhân dân tiến hành.", "D. Nền quốc phòng chủ yếu dựa vào vũ khí hiện đại."],
     "C", "Nền quốc phòng của Việt Nam là nền quốc phòng mang tính chất tự vệ, chính nghĩa, được xây dựng dựa trên sức mạnh của toàn dân (vì dân, của dân, do dân).", "Tổng hợp"),

    ("Hai nhiệm vụ chiến lược của cách mạng Việt Nam hiện nay là gì?",
     ["A. Xây dựng công nghiệp hóa và hiện đại hóa đất nước.", "B. Xây dựng nền kinh tế thị trường và hội nhập quốc tế.", "C. Xây dựng chủ nghĩa xã hội và bảo vệ Tổ quốc xã hội chủ nghĩa.", "D. Đẩy mạnh sản xuất và bảo vệ chủ quyền biển đảo."],
     "C", "Đây là hai nhiệm vụ chiến lược có mối quan hệ biện chứng, gắn bó hữu cơ với nhau trong suốt thời kỳ quá độ lên CNXH ở Việt Nam.", "Lý thuyết"),

    ("Tình huống: Địa phương X đang quy hoạch một khu công nghiệp lớn ven biển, có yếu tố nước ngoài tham gia. Theo quan điểm kết hợp kinh tế với quốc phòng, chính quyền cần chú ý điều gì nhất?",
     ["A. Cấp phép nhanh nhất để thu hút đầu tư.", "B. Bỏ qua các quy định an ninh để giảm chi phí.", "C. Thẩm định chặt chẽ về vị trí chiến lược, đảm bảo không ảnh hưởng đến thế trận phòng thủ khu vực.", "D. Giao toàn bộ khu vực cho đối tác tự quản lý."],
     "C", "Mọi quy hoạch kinh tế, đặc biệt ở vùng ven biển, biên giới phải gắn chặt với yêu cầu bảo đảm quốc phòng, thế trận phòng thủ khu vực.", "Tình huống"),

    ("Nội dung cốt lõi của việc xây dựng 'thế trận quốc phòng toàn dân' là gì?",
     ["A. Xây dựng lực lượng quân đội thường trực có quân số đông.", "B. Tổ chức, bố trí lực lượng, tiềm lực quốc phòng trên toàn lãnh thổ theo ý định chiến lược.", "C. Xây dựng hệ thống pháo đài ngầm ở biên giới.", "D. Ký kết các hiệp ước phòng thủ chung với các cường quốc."],
     "B", "Thế trận quốc phòng toàn dân là việc tổ chức, bố trí các lực lượng và tiềm lực quốc phòng một cách khoa học trên toàn bộ lãnh thổ quốc gia để sẵn sàng đối phó với chiến tranh.", "Phân tích"),

    ("So sánh giữa Tiềm lực quân sự và Tiềm lực quốc phòng. Nhận định nào ĐÚNG?",
     ["A. Tiềm lực quân sự bao trùm toàn bộ tiềm lực quốc phòng.", "B. Tiềm lực quân sự là bộ phận nòng cốt của tiềm lực quốc phòng.", "C. Hai khái niệm này là một, không có sự khác biệt.", "D. Tiềm lực quân sự chỉ bao gồm vũ khí, không bao gồm con người."],
     "B", "Tiềm lực quốc phòng là sức mạnh tổng hợp của nhiều lĩnh vực (kinh tế, chính trị, khoa học...), trong đó tiềm lực quân sự, an ninh là nhân tố nòng cốt, biểu hiện trực tiếp sức mạnh quân sự.", "So sánh"),

    ("Đảng ta khẳng định: 'Luôn luôn coi trọng quốc phòng, an ninh, coi đó là ... gắn bó chặt chẽ'. Điền từ thích hợp.",
     ["A. Nhiệm vụ cấp bách", "B. Nhiệm vụ trọng tâm", "C. Nhiệm vụ chiến lược", "D. Nhiệm vụ quan trọng"],
     "C", "Đảng ta luôn xác định xây dựng đất nước và bảo vệ Tổ quốc là hai nhiệm vụ CHIẾN LƯỢC gắn bó chặt chẽ.", "Lý thuyết"),

    ("Việc xây dựng tiềm lực khoa học - công nghệ trong quốc phòng an ninh có ý nghĩa gì?",
     ["A. Để thay thế hoàn toàn con người bằng robot trên chiến trường.", "B. Tạo khả năng ứng dụng thành tựu KH-CN phục vụ cho việc hiện đại hóa vũ khí, trang bị kỹ thuật và nghệ thuật quân sự.", "C. Để xuất khẩu công nghệ sang nước khác.", "D. Chỉ để phục vụ cho các doanh nghiệp viễn thông."],
     "B", "Trong chiến tranh hiện đại, tiềm lực KH-CN đóng vai trò cực kỳ quan trọng giúp cải tiến, chế tạo và làm chủ các trang bị vũ khí công nghệ cao.", "Phân tích"),

    ("Lực lượng nòng cốt trong sự nghiệp bảo vệ an ninh quốc gia, bảo đảm trật tự an toàn xã hội là:",
     ["A. Quân đội nhân dân.", "B. Công an nhân dân.", "C. Dân quân tự vệ.", "D. Quần chúng nhân dân."],
     "B", "Luật An ninh quốc gia quy định rõ lực lượng Công an nhân dân làm nòng cốt trong sự nghiệp bảo vệ an ninh quốc gia và giữ gìn trật tự an toàn xã hội.", "Lý thuyết"),

    ("Nền quốc phòng toàn dân mang tính chất gì nổi bật nhất khác biệt với các nước tư bản?",
     ["A. Tính chất tự vệ, hòa bình và chính nghĩa.", "B. Tính chất bành trướng lãnh thổ.", "C. Tính chất tấn công tàn bạo.", "D. Tính chất chạy đua vũ trang."],
     "A", "Quốc phòng Việt Nam luôn lấy tự vệ, bảo vệ hòa bình làm mục tiêu tối thượng, không đe dọa vũ lực hay chạy đua vũ trang.", "So sánh"),

    ("Một trong những nội dung xây dựng khối đại đoàn kết toàn dân thuộc về việc xây dựng tiềm lực nào?",
     ["A. Tiềm lực kinh tế.", "B. Tiềm lực khoa học công nghệ.", "C. Tiềm lực quân sự.", "D. Tiềm lực chính trị - tinh thần."],
     "D", "Xây dựng khối đại đoàn kết toàn dân, nâng cao nhận thức chính trị, tạo niềm tin vào Đảng là yếu tố cốt lõi của tiềm lực chính trị - tinh thần.", "Phân tích"),

    ("Luật Quốc phòng của nước CHXHCN Việt Nam đang áp dụng hiện nay được Quốc hội thông qua vào năm nào?",
     ["A. 2015", "B. 2016", "C. 2018", "D. 2020"],
     "C", "Luật Quốc phòng hiện hành được Quốc hội khóa XIV thông qua năm 2018 và có hiệu lực từ 1/1/2019.", "Lý thuyết"),

    ("Tình huống: Trên mạng xã hội xuất hiện luận điệu kêu gọi 'Quân đội phi chính trị hóa', chỉ trung thành với Tổ quốc chứ không cần trung thành với Đảng. Theo đường lối của Đảng, điều này là:",
     ["A. Phù hợp với thông lệ quốc tế.", "B. Là một tư tưởng cấp tiến cần xem xét.", "C. Là âm mưu diễn biến hòa bình nhằm tước bỏ sự lãnh đạo của Đảng đối với quân đội, làm mất bản chất giai cấp công nhân của Quân đội ta.", "D. Sẽ giúp quân đội mạnh hơn."],
     "C", "Luận điệu 'phi chính trị hóa' quân đội là một thủ đoạn cực kỳ nguy hiểm nhằm tách quân đội khỏi sự lãnh đạo của Đảng, làm quân đội mất phương hướng chính trị.", "Tình huống"),

    ("Biện pháp nào sau đây là biện pháp trọng tâm để xây dựng nền quốc phòng toàn dân hiện nay?",
     ["A. Tập trung đầu tư 100% ngân sách cho quân đội.", "B. Thường xuyên thực hiện giáo dục quốc phòng, an ninh cho toàn dân.", "C. Bắt buộc mọi công dân phải nhập ngũ dù bất kỳ hoàn cảnh nào.", "D. Giải tán dân quân tự vệ để dồn lực cho quân chủ lực."],
     "B", "Giáo dục quốc phòng, an ninh cho toàn dân là biện pháp nền tảng, cơ bản để nâng cao ý thức trách nhiệm bảo vệ Tổ quốc của mỗi công dân.", "Tổng hợp")
]

# Topic 3: Chiến tranh Nhân dân
q3_data = [
    ("Chiến tranh nhân dân bảo vệ Tổ quốc ở Việt Nam có đặc điểm gì nổi bật?",
     ["A. Kẻ thù là quân nổi dậy trong nước.", "B. Chúng ta lấy mạnh đánh yếu, lấy nhiều đánh ít.", "C. Là cuộc chiến tranh diễn ra trong điều kiện địch có ưu thế tuyệt đối về kinh tế và vũ khí trang bị kỹ thuật.", "D. Chỉ sử dụng lực lượng chính quy hiện đại để chiến đấu."],
     "C", "Đặc điểm xuyên suốt lịch sử và trong tương lai của chiến tranh bảo vệ Tổ quốc là ta thường phải đối mặt với kẻ thù có sức mạnh kinh tế và vũ khí vượt trội.", "Phân tích"),

    ("Lực lượng nòng cốt của chiến tranh nhân dân bảo vệ Tổ quốc gồm những thành phần nào?",
     ["A. Quân chủng Hải quân và Phòng không không quân.", "B. Bộ đội chủ lực và Bộ đội địa phương.", "C. Lực lượng vũ trang 3 thứ quân (Bộ đội chủ lực, bộ đội địa phương, dân quân tự vệ).", "D. Công an nhân dân và Dân quân tự vệ."],
     "C", "Nghệ thuật quân sự Việt Nam gắn liền với lực lượng vũ trang 3 thứ quân, đây là lực lượng nòng cốt để phát động chiến tranh nhân dân rộng khắp.", "Lý thuyết"),

    ("Quan điểm của Đảng ta về chuẩn bị cho chiến tranh nhân dân bảo vệ Tổ quốc là:",
     ["A. Chỉ chuẩn bị khi có nguy cơ chiến tranh nổ ra.", "B. Chuẩn bị mọi mặt trên cả nước, cũng như từng địa phương ngay từ thời bình.", "C. Chờ viện trợ vũ khí từ bên ngoài mới bắt đầu chuẩn bị.", "D. Tập trung toàn bộ nguồn lực vào quân sự, tạm dừng phát triển kinh tế."],
     "B", "Quan điểm chỉ đạo của Đảng là phải 'chuẩn bị từ sớm, từ xa', xây dựng thế trận và tiềm lực ngay trong thời bình để sẵn sàng chủ động đối phó.", "Tổng hợp"),

    ("Trong nghệ thuật đánh giặc của chiến tranh nhân dân, tư tưởng chỉ đạo tác chiến cốt lõi là gì?",
     ["A. Phòng ngự thụ động chờ thời cơ.", "B. Tích cực chủ động tiến công, kết hợp tiến công và phòng ngự.", "C. Rút lui chiến lược để bảo toàn lực lượng.", "D. Đánh tiêu hao là chính, không cần đánh tiêu diệt."],
     "B", "Tư tưởng chỉ đạo tác chiến của ta luôn là tích cực, chủ động, kiên quyết tiến công địch để giành lại thế chủ động trên chiến trường.", "Phân tích"),

    ("Tình huống: Nếu kẻ thù sử dụng vũ khí công nghệ cao tấn công từ xa vào các mục tiêu trọng yếu của ta, thế trận chiến tranh nhân dân của ta sẽ phát huy tác dụng như thế nào?",
     ["A. Sẽ bị phá vỡ hoàn toàn do không có vũ khí tương đương.", "B. Lực lượng tại chỗ của khu vực phòng thủ sẽ tổ chức sơ tán, ngụy trang, đánh trả và khắc phục hậu quả nhanh chóng.", "C. Chỉ dựa vào lực lượng phòng không quốc gia để bảo vệ.", "D. Xin hòa hoãn để bảo vệ mục tiêu."],
     "B", "Với thế trận chiến tranh nhân dân, mỗi địa phương, mỗi nhà máy đều là một pháo đài. Lực lượng dân quân, tự vệ tại chỗ kết hợp với bộ đội địa phương sẽ thực hiện đánh trả và bảo vệ mục tiêu.", "Tình huống"),

    ("Yếu tố nào đóng vai trò then chốt quyết định thắng lợi của cuộc chiến tranh nhân dân?",
     ["A. Khả năng ngoại giao và viện trợ quốc tế.", "B. Số lượng vũ khí hiện đại.", "C. Sự lãnh đạo tuyệt đối, trực tiếp về mọi mặt của Đảng.", "D. Địa hình hiểm trở của đất nước."],
     "C", "Đường lối, nghệ thuật chiến tranh và sức mạnh toàn dân chỉ được phát huy tối đa và đi đến thắng lợi khi có sự lãnh đạo sáng suốt, đúng đắn của Đảng Cộng sản.", "Tổng hợp"),

    ("Thế trận chiến tranh nhân dân được kết hợp chặt chẽ giữa hai yếu tố nào trên chiến trường?",
     ["A. Chiến tranh du kích và chiến tranh chính quy.", "B. Chiến tranh trên bộ và chiến tranh trên không.", "C. Tác chiến phòng ngự và rút lui chiến lược.", "D. Chiến tranh kinh tế và chiến tranh thông tin."],
     "A", "Đỉnh cao của chiến tranh nhân dân Việt Nam là sự kết hợp nhuần nhuyễn giữa thế trận chiến tranh du kích rộng khắp của địa phương và các đòn đánh quyết định của chiến tranh chính quy (bộ đội chủ lực).", "So sánh"),

    ("Trong tiến hành chiến tranh nhân dân, chúng ta phải kết hợp kháng chiến đi đôi với việc gì?",
     ["A. Kiến quốc (Xây dựng đất nước).", "B. Cầu viện quốc tế.", "C. Mở rộng lãnh thổ.", "D. Di tản dân cư ra nước ngoài."],
     "A", "Truyền thống của dân tộc và tư tưởng Hồ Chí Minh luôn nhấn mạnh 'Vừa kháng chiến, vừa kiến quốc', đảm bảo duy trì sức mạnh lâu dài cho chiến tranh.", "Lý thuyết"),

    ("Tính chất 'Toàn diện' của chiến tranh nhân dân thể hiện ở điểm nào?",
     ["A. Đánh giặc bằng mọi lực lượng.", "B. Đánh giặc trên mọi mặt trận: Quân sự, chính trị, kinh tế, văn hóa - tư tưởng, ngoại giao.", "C. Đánh giặc trên mọi loại địa hình: Rừng núi, đồng bằng, thành thị.", "D. Đánh giặc bằng mọi loại vũ khí có trong tay."],
     "B", "Toàn diện nghĩa là đấu tranh kết hợp trên nhiều mặt trận khác nhau để tạo sức mạnh tổng hợp, trong đó mặt trận quân sự giữ vai trò quyết định thắng lợi trực tiếp.", "Phân tích"),

    ("Theo quan điểm của Đảng, khi tiến hành chiến tranh nhân dân ta phải 'Lấy nhỏ đánh lớn, lấy ít địch nhiều', vậy để giành thắng lợi ta phải dựa vào yếu tố nào?",
     ["A. Dựa vào vũ khí hủy diệt hàng loạt.", "B. Lấy chất lượng cao thắng số lượng đông, phát huy sức mạnh tổng hợp của mưu trí, sáng tạo.", "C. Dựa hoàn toàn vào sự chi viện của lực lượng gìn giữ hòa bình quốc tế.", "D. Liên tục lùi bước để kéo dài chiến tranh vô thời hạn."],
     "B", "Nghệ thuật quân sự Việt Nam luôn đề cao chất lượng, thế trận hiểm hóc, mưu kế và tinh thần dũng cảm để bù đắp sự chênh lệch về quân số và vũ khí.", "Tổng hợp"),

    ("Một trong những mục đích của chiến tranh nhân dân bảo vệ Tổ quốc là:",
     ["A. Bảo vệ vững chắc độc lập, chủ quyền, thống nhất, toàn vẹn lãnh thổ.", "B. Tranh giành tài nguyên thiên nhiên của nước khác.", "C. Đảo chính lật đổ chính quyền đối phương.", "D. Thiết lập căn cứ quân sự ở nước ngoài."],
     "A", "Mục đích tối cao của chiến tranh nhân dân Việt Nam mang tính chất tự vệ, chính nghĩa, chỉ nhằm mục đích bảo vệ toàn vẹn lãnh thổ và chế độ XHCN.", "Lý thuyết"),

    ("So sánh giữa thế trận quốc phòng toàn dân và thế trận chiến tranh nhân dân, nhận định nào ĐÚNG?",
     ["A. Thế trận quốc phòng toàn dân được xây dựng trong thời chiến, thế trận chiến tranh nhân dân xây dựng trong thời bình.", "B. Thế trận quốc phòng toàn dân xây dựng thời bình, và chuyển hóa thành thế trận chiến tranh nhân dân khi có chiến tranh nổ ra.", "C. Hai thế trận này hoàn toàn tách biệt và không liên quan đến nhau.", "D. Không có khái niệm thế trận chiến tranh nhân dân."],
     "B", "Thế trận quốc phòng toàn dân được chuẩn bị từ thời bình. Khi đất nước có chiến tranh, nó sẽ tự động chuyển hóa, mở rộng và phát huy sức mạnh trở thành thế trận chiến tranh nhân dân.", "So sánh"),

    ("Trong tổ chức lực lượng chiến tranh nhân dân, vai trò của 'Dân quân tự vệ' là gì?",
     ["A. Lực lượng cơ động chiến lược trên toàn quốc.", "B. Lực lượng bảo vệ vùng trời và vùng biển xa.", "C. Lực lượng vũ trang quần chúng không thoát ly sản xuất, làm nòng cốt bảo vệ an ninh trật tự và đánh địch tại cơ sở (xã/phường/nhà máy).", "D. Lực lượng chuyên trách về tình báo ngoại quốc."],
     "C", "Dân quân tự vệ là một trong 3 thứ quân, gắn liền với cơ sở sản xuất, 'vừa cầm cày vừa cầm súng', là lực lượng tại chỗ tạo thành lưới lửa bảo vệ từng tấc đất.", "Lý thuyết"),

    ("Tình huống: Địch tiến công bằng hỏa lực mạnh vào một tỉnh biên giới. Ban chỉ huy quân sự tỉnh quyết định phát lệnh huy động toàn dân trong tỉnh tham gia đánh giặc bằng mọi vũ khí có sẵn (gậy gộc, súng săn, cuốc xẻng...). Hành động này thể hiện quan điểm nào?",
     ["A. Chiến tranh toàn diện.", "B. Kháng chiến trường kỳ.", "C. Chiến tranh toàn dân.", "D. Kết hợp sức mạnh dân tộc và thời đại."],
     "C", "Quan điểm chiến tranh 'Toàn dân' nghĩa là mỗi người dân là một chiến sĩ, mỗi làng xã là một pháo đài, dùng mọi vũ khí có trong tay để chống giặc.", "Tình huống"),

    ("Biện pháp để xây dựng thế trận chiến tranh nhân dân vững chắc là gì?",
     ["A. Xây dựng khu vực phòng thủ tỉnh/thành phố vững mạnh toàn diện.", "B. Xây dựng các căn cứ hạt nhân ngầm.", "C. Triệt phá rừng rậm để tạo tầm nhìn trống trải.", "D. Yêu cầu toàn bộ nam thanh niên tập trung ở biên giới."],
     "A", "Khu vực phòng thủ tỉnh/thành phố là hạt nhân cơ bản cấu thành thế trận chiến tranh nhân dân trên cả nước, giúp phòng thủ bảo vệ từng địa bàn.", "Tổng hợp")
]

# Topic 4: DBHB - Bạo loạn lật đổ
q4_data = [
    ("Khái niệm 'Diễn biến hòa bình' là gì?",
     ["A. Là chiến lược quân sự sử dụng vũ khí hạt nhân để buộc đối phương đầu hàng.", "B. Là chiến lược cơ bản nhằm lật đổ chế độ chính trị xã hội của các nước tiến bộ, trước hết là các nước XHCN từ bên trong bằng biện pháp phi quân sự.", "C. Là sự phát triển kinh tế trong điều kiện hòa bình.", "D. Là quá trình đàm phán hòa bình giữa hai quốc gia có tranh chấp."],
     "B", "Diễn biến hòa bình là chiến lược nguy hiểm của chủ nghĩa đế quốc, sử dụng sức mạnh 'mềm' (văn hóa, tư tưởng, kinh tế, chính trị) để làm suy yếu và lật đổ đối phương mà không cần nổ súng.", "Lý thuyết"),

    ("Khái niệm 'Bạo loạn lật đổ' là gì?",
     ["A. Là cuộc biểu tình ôn hòa đòi tăng lương.", "B. Là hành động bạo lực có tổ chức do lực lượng phản động tiến hành nhằm lật đổ chính quyền cách mạng để thiết lập chính quyền phản động.", "C. Là sự xung đột cá nhân ngoài đường phố.", "D. Là cuộc tranh luận gay gắt trong quốc hội."],
     "B", "Bạo loạn lật đổ sử dụng bạo lực có tổ chức (có thể dùng vũ khí hoặc không) nhằm mục tiêu chính trị tối hậu là cướp chính quyền.", "Lý thuyết"),

    ("Thủ đoạn chống phá của chiến lược Diễn biến hòa bình trên lĩnh vực TƯ TƯỞNG - VĂN HÓA tập trung vào vấn đề gì?",
     ["A. Bao vây, cấm vận kinh tế.", "B. Đòi đa nguyên đa đảng.", "C. Phá vỡ nền tảng tư tưởng của Đảng (Chủ nghĩa Mác-Lênin, Tư tưởng Hồ Chí Minh), truyền bá lối sống thực dụng.", "D. Kích động biểu tình vũ trang."],
     "C", "Mặt trận tư tưởng văn hóa là mặt trận trọng yếu nhất. Kẻ thù nhằm xóa bỏ nền tảng tư tưởng, làm phai nhạt niềm tin của thanh niên, sinh viên vào chế độ.", "Phân tích"),

    ("Tình huống: Một tổ chức NGO nước ngoài tài trợ cho sinh viên Việt Nam nhưng yêu cầu sinh viên phải viết bài trên mạng xã hội nói xấu lịch sử dân tộc và bôi nhọ lãnh tụ. Đây là biểu hiện của thủ đoạn nào trong Diễn biến hòa bình?",
     ["A. Thủ đoạn chống phá về kinh tế.", "B. Thủ đoạn chống phá về ngoại giao.", "C. Thủ đoạn chống phá về tư tưởng - văn hóa.", "D. Thủ đoạn chống phá về quân sự."],
     "C", "Sử dụng vật chất để mua chuộc, dụ dỗ thanh niên phủ nhận lịch sử, bôi nhọ lãnh tụ là thủ đoạn thâm độc trên lĩnh vực tư tưởng văn hóa.", "Tình huống"),

    ("Thủ đoạn 'Phi chính trị hóa' quân đội và công an của các thế lực thù địch nhằm mục đích gì?",
     ["A. Để quân đội và công an tập trung làm kinh tế.", "B. Tách quân đội và công an khỏi sự lãnh đạo của Đảng Cộng sản, làm cho LLVT mất phương hướng chiến đấu.", "C. Để giảm bớt kinh phí quốc phòng.", "D. Để quân đội tự do tham gia các đảng phái khác."],
     "B", "Phi chính trị hóa LLVT là nhằm làm mất bản chất giai cấp công nhân của Quân đội và Công an, biến LLVT thành lực lượng trung lập, không bảo vệ chế độ.", "Phân tích"),

    ("Trong các giải pháp phòng chống DBHB, bạo loạn lật đổ, giải pháp nào được xem là quan trọng hàng đầu?",
     ["A. Tăng cường mua sắm vũ khí, trang bị chống bạo động.", "B. Nâng cao nhận thức về âm mưu, thủ đoạn của địch; xây dựng ý thức bảo vệ Tổ quốc cho toàn dân.", "C. Đóng cửa hoàn toàn mạng internet.", "D. Trục xuất tất cả người nước ngoài khỏi Việt Nam."],
     "B", "Đấu tranh chống DBHB là đấu tranh trên mặt trận tư tưởng, nhận thức. Do đó, giáo dục, nâng cao nhận thức, sức đề kháng chính trị cho nhân dân là quan trọng nhất.", "Tổng hợp"),

    ("Mối quan hệ giữa Diễn biến hòa bình (DBHB) và Bạo loạn lật đổ (BLLĐ) là gì?",
     ["A. Là hai chiến lược độc lập, không liên quan đến nhau.", "B. DBHB tạo tiền đề, điều kiện cho BLLĐ; BLLĐ là hệ quả, là nấc thang phát triển cao của DBHB.", "C. BLLĐ luôn xảy ra trước rồi mới đến DBHB.", "D. DBHB chỉ áp dụng ở nông thôn, BLLĐ chỉ áp dụng ở thành thị."],
     "B", "DBHB làm suy yếu chính trị, chia rẽ nội bộ, tạo ra mầm mống bất mãn. Khi thời cơ chín muồi, các thế lực thù địch sẽ kích động BLLĐ để cướp chính quyền.", "So sánh"),

    ("Thủ đoạn chống phá trên lĩnh vực CHÍNH TRỊ của chiến lược Diễn biến hòa bình tập trung vào mục tiêu gì?",
     ["A. Xóa bỏ nền tảng tư tưởng Mác Lênin.", "B. Kích động chia rẽ tôn giáo.", "C. Kích động đòi thực hiện chế độ 'đa nguyên chính trị, đa đảng đối lập'.", "D. Chuyển hóa nền kinh tế thị trường định hướng XHCN thành tư bản chủ nghĩa."],
     "C", "Mục tiêu trực diện trên lĩnh vực chính trị là đòi xóa bỏ Điều 4 Hiến pháp, từ bỏ vai trò lãnh đạo độc tôn của Đảng Cộng sản Việt Nam, tiến tới đa nguyên đa đảng.", "Lý thuyết"),

    ("Khái niệm 'Tự diễn biến', 'Tự chuyển hóa' trong nội bộ mang ý nghĩa gì?",
     ["A. Là quá trình cán bộ, đảng viên tự rèn luyện để tốt hơn.", "B. Là sự suy thoái về tư tưởng chính trị, đạo đức, lối sống, phai nhạt lý tưởng cách mạng của một bộ phận cán bộ, đảng viên.", "C. Là quá trình cổ phần hóa doanh nghiệp nhà nước.", "D. Là sự luân chuyển cán bộ giữa các địa phương."],
     "B", "Đây là quá trình thay đổi theo chiều hướng tiêu cực từ bên trong. Kẻ thù luôn lợi dụng sự 'tự diễn biến' này để thúc đẩy sự sụp đổ của chế độ từ bên trong.", "Phân tích"),

    ("Tình huống: Khi thấy một đám đông tụ tập gây rối, đập phá trụ sở Ủy ban nhân dân và hô hào lật đổ chính quyền. Là một công dân, bạn nhận định đây là hiện tượng gì và cần làm gì?",
     ["A. Đây là quyền tự do dân chủ, nên tham gia đứng xem cho biết.", "B. Đây là hành động bạo loạn lật đổ. Cần tránh xa, báo ngay cho cơ quan chức năng và không hùa theo đám đông.", "C. Đây là biểu tình hòa bình, có thể quay video livestream để câu view.", "D. Đây là hoạt động văn hóa của địa phương."],
     "B", "Hành động đập phá trụ sở và hô hào lật đổ là dấu hiệu rõ ràng của bạo loạn lật đổ. Công dân cần có thái độ lên án, tránh xa và hỗ trợ lực lượng chức năng.", "Tình huống"),

    ("Thủ đoạn lợi dụng vấn đề 'Dân tộc', 'Tôn giáo' của chiến lược DBHB nhằm mục đích gì?",
     ["A. Giúp các dân tộc thiểu số phát triển văn hóa.", "B. Chia rẽ khối đại đoàn kết toàn dân tộc, kích động đồng bào dân tộc thiểu số và tín đồ tôn giáo chống lại Đảng, Nhà nước.", "C. Mở rộng tự do tín ngưỡng cho nhân dân.", "D. Kêu gọi viện trợ quốc tế cho vùng sâu vùng xa."],
     "B", "Lợi dụng tôn giáo, dân tộc (như vấn đề Tây Nguyên, Tây Bắc, Tây Nam Bộ) để kích động ly khai, bạo loạn, phá hoại khối đại đoàn kết toàn dân tộc là một mũi nhọn của địch.", "Tổng hợp"),

    ("Đâu KHÔNG phải là đặc điểm của Bạo loạn lật đổ?",
     ["A. Sử dụng bạo lực có tổ chức.", "B. Nhằm mục đích lật đổ chính quyền cách mạng.", "C. Chỉ sử dụng lực lượng quân đội tinh nhuệ từ nước ngoài xâm nhập vào.", "D. Thường diễn ra nhanh, bất ngờ và có sự hậu thuẫn của thế lực thù địch bên ngoài."],
     "C", "Bạo loạn lật đổ chủ yếu dựa vào các phần tử phản động, bất mãn ở TỪNG BÊN TRONG đất nước bị kích động, chứ không phải là lực lượng quân đội từ bên ngoài đánh vào (đó là chiến tranh xâm lược).", "So sánh"),

    ("Giải pháp nào để phòng ngừa tình trạng 'tự diễn biến', 'tự chuyển hóa' hiệu quả nhất?",
     ["A. Cắt đứt mọi quan hệ với phương Tây.", "B. Xây dựng tổ chức Đảng trong sạch vững mạnh, đề cao tính tiền phong gương mẫu, chống tham nhũng, lãng phí.", "C. Bắt buộc mọi người dân đóng cửa mạng xã hội.", "D. Cấm cán bộ ra nước ngoài học tập."],
     "B", "Gốc rễ của 'tự diễn biến' là sự thoái hóa biến chất. Do đó, làm trong sạch bộ máy, chống tham nhũng và tăng cường giáo dục chính trị là giải pháp cốt lõi.", "Tổng hợp"),

    ("Thủ đoạn chống phá trên lĩnh vực KINH TẾ của chiến lược Diễn biến hòa bình là gì?",
     ["A. Đẩy mạnh đầu tư không hoàn lại cho Việt Nam.", "B. Bao vây, cấm vận, ép ta thay đổi thể chế kinh tế, hướng nền kinh tế ta đi theo quỹ đạo của chủ nghĩa tư bản.", "C. Tăng cường xuất khẩu hàng hóa giá rẻ sang Việt Nam.", "D. Mua lại toàn bộ nông sản của Việt Nam."],
     "B", "Sử dụng viện trợ, ODA và các đòn bẩy kinh tế làm điều kiện ép buộc Việt Nam phải nhượng bộ về chính trị, làm chệch hướng XHCN.", "Lý thuyết"),

    ("Là sinh viên, bạn cần làm gì để góp phần phòng chống chiến lược Diễn biến hòa bình?",
     ["A. Không quan tâm vì đây là việc của Công an và Quân đội.", "B. Tích cực chia sẻ mọi thông tin giật gân chưa kiểm chứng trên mạng để mọi người cảnh giác.", "C. Nâng cao cảnh giác chính trị, trang bị kiến thức, chọn lọc thông tin trên mạng xã hội, tích cực học tập và bảo vệ đường lối của Đảng.", "D. Tham gia các diễn đàn ẩn danh để tranh cãi với phản động."],
     "C", "Thanh niên, sinh viên là đối tượng chính kẻ thù nhắm tới. Việc trau dồi bản lĩnh chính trị và kỹ năng lọc thông tin là trách nhiệm và hành động thiết thực nhất.", "Tình huống")
]

# Topic 5: Môi trường
q5_data = [
    ("Khái niệm Môi trường được hiểu như thế nào theo Luật Bảo vệ môi trường?",
     ["A. Môi trường chỉ bao gồm cây xanh và động vật hoang dã.", "B. Môi trường bao gồm các yếu tố vật chất tự nhiên và nhân tạo quan hệ mật thiết với nhau, bao quanh con người, có ảnh hưởng đến sự sống, sản xuất và sự tồn tại của con người và thiên nhiên.", "C. Môi trường là các nguồn nước và khoáng sản dưới lòng đất.", "D. Môi trường là bầu khí quyển bao quanh Trái đất."],
     "B", "Khái niệm môi trường bao gồm cả yếu tố tự nhiên (không khí, nước, đất, sinh vật) và nhân tạo (kiến trúc, đô thị) có ảnh hưởng mật thiết đến con người.", "Lý thuyết"),

    ("Khách thể của tội phạm môi trường là gì?",
     ["A. Là sức khỏe của con người bị ảnh hưởng do ô nhiễm.", "B. Là các quy định của Nhà nước về bảo vệ môi trường, bảo vệ sự ổn định và phát triển của môi trường sinh thái.", "C. Là các nhà máy, xí nghiệp xả thải.", "D. Là động vật hoang dã."],
     "B", "Trong luật hình sự, 'Khách thể' là các QUAN HỆ XÃ HỘI được luật hình sự bảo vệ. Ở đây chính là trật tự quản lý nhà nước và các quy định về bảo vệ môi trường sinh thái.", "Lý thuyết"),

    ("Chủ thể của tội phạm môi trường có điểm gì đặc biệt so với nhiều loại tội phạm khác theo Bộ luật Hình sự 2015 (sửa đổi 2017)?",
     ["A. Chỉ bao gồm cá nhân từ 18 tuổi trở lên.", "B. Chỉ bao gồm pháp nhân thương mại.", "C. Bao gồm cả cá nhân có năng lực trách nhiệm hình sự và pháp nhân thương mại.", "D. Trẻ em dưới 14 tuổi cũng là chủ thể."],
     "C", "Một điểm mới và nổi bật của Bộ luật Hình sự là quy định trách nhiệm hình sự đối với PHÁP NHÂN THƯƠNG MẠI (các doanh nghiệp, công ty) xả thải gây ô nhiễm nghiêm trọng, bên cạnh trách nhiệm của cá nhân.", "So sánh"),

    ("Mặt khách quan của tội phạm môi trường thể hiện bằng hành vi nào?",
     ["A. Suy nghĩ và lên kế hoạch chặt phá rừng.", "B. Hành vi nguy hiểm cho xã hội như: xả chất thải chưa qua xử lý, hủy hoại rừng, buôn bán động vật quý hiếm vi phạm pháp luật.", "C. Sự vô ý làm đổ một chai nước suối ra đường.", "D. Việc trồng cây công nghiệp trái phép."],
     "B", "Mặt khách quan là những biểu hiện ra bên ngoài thế giới khách quan, cụ thể là các hành vi vi phạm trực tiếp gây nguy hại cho môi trường được quy định trong luật.", "Phân tích"),

    ("Tình huống: Công ty X lắp đặt một hệ thống xả thải ngầm để xả trực tiếp nước thải hóa chất độc hại chưa qua xử lý ra dòng sông, làm cá chết hàng loạt. Công ty X sẽ bị xử lý như thế nào?",
     ["A. Chỉ bị xử phạt hành chính và yêu cầu nộp thuế bảo vệ môi trường.", "B. Giám đốc công ty phải đi tù nhưng công ty không bị sao.", "C. Công ty X có thể bị truy cứu trách nhiệm hình sự đối với pháp nhân thương mại, chịu phạt tiền nặng, đình chỉ hoạt động hoặc cấm kinh doanh vĩnh viễn.", "D. Công ty X chỉ bị người dân biểu tình."],
     "C", "Hành vi xả thải độc hại có tổ chức (lắp ống ngầm) gây hậu quả nghiêm trọng đã cấu thành tội phạm môi trường đối với pháp nhân thương mại theo BLHS.", "Tình huống"),

    ("Tội vi phạm quy định về bảo vệ động vật hoang dã (ĐVHD) chủ yếu nhằm bảo vệ đối tượng nào?",
     ["A. Gia súc, gia cầm nuôi tại trang trại.", "B. Các loài động vật hoang dã có nguy cơ tuyệt chủng, quý hiếm được ưu tiên bảo vệ theo quy định.", "C. Vật nuôi trong nhà như chó, mèo.", "D. Các loài vi sinh vật."],
     "B", "Khách thể tác động của tội này là các loài ĐVHD nguy cấp, quý hiếm có tên trong Sách đỏ hoặc danh mục bảo vệ của Nhà nước và quốc tế.", "Lý thuyết"),

    ("Lỗi trong cấu thành tội phạm môi trường (Mặt chủ quan) có thể là:",
     ["A. Chỉ có lỗi cố ý trực tiếp.", "B. Chỉ có lỗi vô ý do cẩu thả.", "C. Thường là lỗi cố ý (cố tình xả thải vì lợi nhuận) hoặc đôi khi là lỗi vô ý (do quá tự tin hoặc cẩu thả trong vận hành máy móc).", "D. Tội phạm môi trường không cần xét yếu tố lỗi."],
     "C", "Mặt chủ quan của tội phạm môi trường bao gồm cả lỗi cố ý (ví dụ: biết xả độc nhưng vẫn làm để tiết kiệm chi phí) và vô ý (vận hành sai quy trình làm rò rỉ hóa chất).", "Phân tích"),

    ("Đâu là một trong những nguyên nhân khách quan dẫn đến vi phạm pháp luật bảo vệ môi trường ở Việt Nam?",
     ["A. Sự hám lợi, chạy theo lợi nhuận tối đa của các chủ doanh nghiệp.", "B. Sự thiếu hiểu biết của người dân.", "C. Hệ thống pháp luật về môi trường, các chế tài xử phạt đôi khi chưa đủ sức răn đe, lực lượng quản lý mỏng.", "D. Sự suy thoái đạo đức của cá nhân vi phạm."],
     "C", "Các phương án A, B, D là nguyên nhân CHỦ QUAN (từ phía người vi phạm). Phương án C là nguyên nhân KHÁCH QUAN (từ cơ chế, pháp luật, quản lý).", "So sánh"),

    ("Biện pháp mang tính phòng ngừa từ xa để chống vi phạm pháp luật bảo vệ môi trường là:",
     ["A. Bắt giam tất cả các giám đốc nhà máy.", "B. Tuyên truyền, giáo dục nâng cao ý thức bảo vệ môi trường cho cộng đồng và học sinh, sinh viên.", "C. Đóng cửa toàn bộ các khu công nghiệp hóa chất.", "D. Chỉ dựa vào lực lượng Cảnh sát phòng chống tội phạm môi trường đi rình bắt."],
     "B", "Giáo dục và tuyên truyền là biện pháp phòng ngừa từ xa cơ bản, bền vững và hiệu quả nhất để xây dựng văn hóa ứng xử thân thiện với môi trường.", "Tổng hợp"),

    ("Tình huống: Một nhóm người vào Vườn quốc gia để bẫy bắt Hổ (loài nguy cấp, quý hiếm). Khi bị kiểm lâm phát hiện, họ cho rằng họ chỉ bắt con vật hoang dã vô chủ nên không phạm tội. Lời bào chữa này đúng hay sai?",
     ["A. Đúng, vì động vật trong rừng là của trời cho, ai bắt cũng được.", "B. Sai, vì Hổ là loài động vật hoang dã nguy cấp, quý hiếm được pháp luật bảo vệ nghiêm ngặt. Hành vi săn bắt này phạm tội hình sự.", "C. Đúng, họ chỉ bị phạt hành chính nếu không có giấy phép săn bắn.", "D. Sai, vì họ chưa nộp thuế vào rừng."],
     "B", "Việc săn bắt các loài nguy cấp, quý hiếm được bảo vệ là vi phạm nghiêm trọng Bộ luật Hình sự (Tội vi phạm quy định về bảo vệ động vật nguy cấp, quý hiếm), đối diện với án tù nặng.", "Tình huống"),

    ("Cơ quan nào giữ vai trò chủ công, trực tiếp đấu tranh phòng chống tội phạm về môi trường?",
     ["A. Bộ Tài nguyên và Môi trường.", "B. Cảnh sát phòng, chống tội phạm về môi trường (C05) thuộc Công an nhân dân.", "C. Lực lượng Bộ đội Biên phòng.", "D. Cục Kiểm lâm."],
     "B", "Cảnh sát phòng, chống tội phạm về môi trường (C05) là lực lượng vũ trang chuyên trách nòng cốt trong việc điều tra, trinh sát và bắt giữ tội phạm môi trường.", "Lý thuyết"),

    ("Thế nào là hiện tượng 'Ô nhiễm môi trường'?",
     ["A. Là việc môi trường có nhiều cây xanh phát triển quá mức.", "B. Là sự biến đổi tính chất vật lý, hóa học, sinh học của môi trường không phù hợp với quy chuẩn kỹ thuật, gây ảnh hưởng xấu đến sức khỏe con người và sinh vật.", "C. Là sự thay đổi thời tiết theo mùa.", "D. Là hiện tượng trái đất nóng lên tự nhiên."],
     "B", "Ô nhiễm là sự đưa vào môi trường các chất thải, năng lượng vượt quá ngưỡng cho phép, làm biến đổi tiêu cực chất lượng môi trường.", "Lý thuyết"),

    ("Để kết tội một pháp nhân thương mại phạm tội môi trường, pháp nhân đó phải thỏa mãn điều kiện nào?",
     ["A. Hành vi phạm tội được thực hiện nhân danh pháp nhân và vì lợi ích của pháp nhân.", "B. Giám đốc pháp nhân vô tình đi chơi và xả rác.", "C. Pháp nhân đó phải là công ty nhà nước.", "D. Pháp nhân đó đang bị phá sản."],
     "A", "Pháp nhân thương mại chỉ phải chịu trách nhiệm hình sự khi hành vi được thực hiện nhân danh pháp nhân, vì lợi ích của pháp nhân và có sự chỉ đạo, điều hành của pháp nhân.", "Phân tích"),

    ("Sinh viên có thể tham gia bảo vệ môi trường bằng hành động thiết thực nào?",
     ["A. Mua sắm thật nhiều đồ nhựa dùng một lần để thúc đẩy kinh tế.", "B. Tham gia các chiến dịch dọn rác, tắt điện giờ trái đất, sử dụng phương tiện công cộng, phân loại rác thải tại nguồn.", "C. Báo cáo giả về các vụ ô nhiễm để thử tài cảnh sát.", "D. Trồng cây trên lòng đường giao thông."],
     "B", "Bắt đầu từ những hành động nhỏ, sinh viên có thể lan tỏa lối sống xanh và trực tiếp góp phần giảm thiểu tác động xấu lên môi trường.", "Tổng hợp"),

    ("Mối quan hệ giữa phát triển kinh tế và bảo vệ môi trường trong đường lối của Đảng ta là:",
     ["A. Phát triển kinh tế bằng mọi giá, sau đó mới dọn dẹp môi trường.", "B. Bảo vệ môi trường tuyệt đối, cấm mọi hoạt động công nghiệp khai thác.", "C. Phát triển kinh tế gắn liền với bảo vệ môi trường, phát triển bền vững, không đánh đổi môi trường lấy tăng trưởng kinh tế.", "D. Đẩy ô nhiễm sang các nước nghèo hơn."],
     "C", "Phát triển bền vững là nguyên tắc xuyên suốt. Không đánh đổi môi trường lấy tăng trưởng kinh tế là khẳng định mạnh mẽ của Chính phủ.", "So sánh")
]

# Append datasets
def load_all():
    for q in q1_data: add_question(topics[0]['topicId'], *q)
    for q in q2_data: add_question(topics[1]['topicId'], *q)
    for q in q3_data: add_question(topics[2]['topicId'], *q)
    for q in q4_data: add_question(topics[3]['topicId'], *q)
    for q in q5_data: add_question(topics[4]['topicId'], *q)

load_all()

# Write quocphong.json
json_path = os.path.join(data_dir, "quocphong.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump({"topics": topics, "questions": questions}, f, ensure_ascii=False, indent=2)

print(f"Generated {json_path}")

# Write knowledge.md
knowledge_md_path = os.path.join(data_dir, "knowledge.md")
with open(knowledge_md_path, "w", encoding="utf-8") as f:
    f.write("# TỔNG HỢP KIẾN THỨC MÔN HỌC QUỐC PHÒNG\n\n")
    for t in topics:
        f.write(f"## {t['title']}\n\n")
        f.write(f"**Tóm tắt:** {t['summary']}\n\n")
        f.write(f"**Keywords:** {', '.join(t['keywords'])}\n\n")
        f.write(f"**Nội dung trọng tâm:**\n{t['focus']}\n\n")
        f.write(f"**Những ý dễ nhầm:**\n{t['mistakes']}\n\n")
        f.write(f"**Ghi nhớ nhanh:** *{t['quick_memory']}*\n\n")
        f.write("---\n\n")

print(f"Generated {knowledge_md_path}")

# Write question_bank.md
qb_md_path = os.path.join(data_dir, "question_bank.md")
with open(qb_md_path, "w", encoding="utf-8") as f:
    f.write("# NGÂN HÀNG CÂU HỎI QUỐC PHÒNG (KÈM GIẢI THÍCH)\n\n")
    for q in questions:
        f.write(f"**Câu {q['id']}:** {q['question']}\n\n")
        for opt in q['options']:
            f.write(f"- {opt}\n")
        f.write(f"\n*Đáp án:* **{q['correctAnswer']}**\n")
        f.write(f"*Giải thích:* {q['explanation']}\n\n")
        f.write("---\n\n")

print(f"Generated {qb_md_path}")

# Update subjects.json
subjects_path = os.path.join(root_dir, "data/subjects.json")
try:
    with open(subjects_path, "r", encoding="utf-8") as f:
        subjects = json.load(f)
except Exception:
    subjects = []

# Check if quocphong exists
exists = any(s.get("id") == "quocphong" for s in subjects)
if not exists:
    subjects.append({
        "id": "quocphong",
        "name": "Môn học Quốc phòng - An ninh",
        "description": "Ôn tập Giáo dục Quốc phòng HP1 & HP2: Đường lối, Lịch sử nghệ thuật quân sự, Phòng chống Diễn biến hòa bình, Tội phạm môi trường.",
        "icon": "🛡️",
        "pdfs": [
            "quocphong/QUOCPHONG_HOCPHAN1.pdf",
            "quocphong/QUOCPHONG_HOCPHAN2.pdf"
        ]
    })
    with open(subjects_path, "w", encoding="utf-8") as f:
        json.dump(subjects, f, ensure_ascii=False, indent=2)
    print("Updated subjects.json")
else:
    print("Quoc phong subject already in subjects.json")

