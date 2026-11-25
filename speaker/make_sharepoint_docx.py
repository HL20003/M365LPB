"""Tạo "Hướng dẫn trình bày SharePoint agent.docx" cho speaker (tài liệu nội bộ, không đưa lên site).

SharePoint agent không còn là bài tập của học viên: speaker giới thiệu và demo sau Lab 7.
Chạy: python make_sharepoint_docx.py  (cần python-docx; dùng chung kiểu chữ với file demo trong demo-files/_gen)
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "demo-files" / "_gen"))
from docx_common import bullets, footer_note, new_doc, para, table, title  # noqa: E402

OUT = HERE / "Hướng dẫn trình bày SharePoint agent.docx"


def numbered(doc, items):
    bullets(doc, items, style="List Number")


def build():
    doc = new_doc()
    footer_note(doc, "Tài liệu nội bộ cho speaker và trợ giảng - không gửi học viên")
    title(doc, "HƯỚNG DẪN TRÌNH BÀY SHAREPOINT AGENT",
          "Copilot Overview Workshop (bản general v2)  |  Phần giới thiệu sau Lab 7  |  Cập nhật 25/11/2026")

    doc.add_heading("1. Phần này nằm ở đâu trong buổi học", 1)
    table(doc, ["Mục", "Nội dung"], [
        ["Thời điểm", "Phút 105-112, ngay sau Lab 7 Bài tập 4 (học viên vừa dùng Policy Assistant trong Teams)"],
        ["Hình thức", "Speaker demo trên máy chiếu, học viên xem. Trên site lab không có bài tập SharePoint agent, chỉ có bảng \"Ba cấp độ agent\" cuối Lab 7"],
        ["Thời lượng", "5 phút demo + 2 phút giải thích ba cấp độ agent"],
        ["Cần có", "Site SharePoint của workshop, agent Trợ lý Sổ tay tạo sẵn, một nhóm chat Teams demo, ảnh chụp dự phòng"],
    ], [3.5, 13])
    para(doc, "Vì sao speaker demo thay vì học viên tự làm: tạo SharePoint agent cần quyền chỉnh sửa site, và agent tạo bằng Agent Builder "
              "(Lab 7) hiện chưa thêm được vào nhóm chat Teams. Demo SharePoint agent cho khách hàng thấy bước tiếp theo: agent vào thẳng "
              "nhóm chat, cả nhóm cùng hỏi.")

    doc.add_heading("2. Ba thông điệp cần truyền tải", 1)
    numbered(doc, [
        ("Agent phải đến được nơi mọi người làm việc. ", "SharePoint agent thêm được vào nhóm chat và kênh Teams: cả nhóm cùng @mention, "
         "cùng thấy câu trả lời, không ai phải mở thêm trang nào."),
        ("Agent trả lời theo quyền của người hỏi. ", "Không ai đọc được tài liệu mà họ không có quyền xem, kể cả khi hỏi trong nhóm chat."),
        ("Chọn đúng cấp độ agent. ", "SharePoint agent cho tri thức của một site; Agent Builder cho agent nghiệp vụ đơn giản; "
         "Copilot Studio khi cần tích hợp, hành động và phân phối quy mô lớn."),
    ])

    doc.add_heading("3. Chuẩn bị trước 1 ngày", 1)
    table(doc, ["#", "Việc cần làm", "Kiểm tra đạt khi"], [
        ["1", "Tạo hoặc chọn site SharePoint của workshop. Speaker có quyền chỉnh sửa, học viên có quyền đọc", "Một tài khoản học viên mở được site"],
        ["2", "Vào thư viện Documents, tải lên Sổ tay Chính sách Nội bộ.docx", "File mở được trên site"],
        ["3", "Chọn file > Create an agent (trên thanh lệnh hoặc trong menu ...), đặt tên Trợ lý Sổ tay, lưu", "Agent hiện trong danh sách khi bấm biểu tượng Agent góc trên bên phải site"],
        ["4", "Hỏi thử 2 câu demo ở mục 5 ngay trên SharePoint", "Trả lời đúng đáp án, có dẫn mục Sổ tay"],
        ["5", "Biểu tượng Agent > Trợ lý Sổ tay > ... > Copy link for Teams", "Có link để dán vào Teams"],
        ["6", "Tạo nhóm chat demo với 2-3 tài khoản nội bộ (không có khách bên ngoài), dán link, chọn Add to this chat, thử @mention", "Agent chào trong nhóm chat và trả lời câu hỏi"],
        ["7", "Chụp ảnh màn hình từng bước 3-6", "Có bộ ảnh dự phòng nếu demo trực tiếp lỗi"],
        ["8", "Gỡ agent khỏi nhóm chat sau khi thử (... của nhóm chat > Manage apps > ... cạnh agent > Remove) nếu muốn demo lại bước thêm agent", "Nhóm chat sẵn sàng cho buổi học"],
    ], [0.8, 9.7, 6])
    para(doc, "Policy Assistant ở Lab 7 cũng nên dùng Sổ tay trên chính site này: khi học viên chia sẻ agent cho nhau, người nhận có quyền đọc "
              "file nên vẫn nhận được câu trả lời.")

    doc.add_heading("4. Kịch bản demo", 1)
    table(doc, ["Bước", "Thao tác trên màn hình", "Lời dẫn gợi ý"], [
        ["1", "Mở site SharePoint workshop, chỉ vào thư viện có Sổ tay", "\"Phòng ban nào cũng đã có tài liệu trên SharePoint. Không cần chuẩn bị gì thêm để có agent.\""],
        ["2", "Chọn Sổ tay > Create an agent (chỉ mở hộp thoại để khách thấy, dùng agent đã tạo sẵn)", "\"Chọn file, bấm Create an agent, đặt tên là xong. Agent chỉ trả lời từ các file đã chọn.\""],
        ["3", "Biểu tượng Agent > Trợ lý Sổ tay, hỏi câu 1 ngay trên site", "\"Agent trả lời có dẫn mục, giống Policy Assistant vừa tạo.\""],
        ["4", "... > Copy link for Teams, mở nhóm chat demo, dán link, Add to this chat", "\"Giờ đưa agent vào đúng nơi mọi người đang trao đổi: nhóm chat Teams.\""],
        ["5", "Gõ @Trợ lý Sổ tay và câu 1", "\"Cả nhóm cùng thấy câu hỏi và câu trả lời, không ai phải hỏi lại Pháp chế.\""],
        ["6", "Chuyển sang tài khoản thứ hai trong nhóm, hỏi câu 2", "\"Mỗi người hỏi việc của mình, cùng một agent, cùng một nguồn.\""],
        ["7", "Chỉ vào phần dẫn nguồn trong câu trả lời", "\"Agent trả lời theo quyền của người hỏi. Ai không có quyền xem tài liệu thì không thấy nội dung đó.\""],
    ], [1.2, 7.3, 8])

    doc.add_heading("5. Câu hỏi demo và đáp án", 1)
    table(doc, ["Câu hỏi (gõ @Trợ lý Sổ tay trước câu hỏi)", "Đáp án đúng"], [
        ["Phòng tôi đề xuất ký hợp đồng khung thuê thầu phụ 3,2 tỷ đồng và tạm ứng 45% cho nhà thầu. Cần mấy báo giá, ai phê duyệt, và tạm ứng tối đa bao nhiêu?",
         "Trên 2 tỷ đồng: 3 báo giá, Tổng Giám đốc phê duyệt sau khi Phòng Pháp chế rà soát (Mục 5.1). Tạm ứng tối đa 30%; 45% là ngoại lệ, cần Giám đốc Tài chính "
         "phê duyệt và bảo lãnh tạm ứng của ngân hàng (Mục 5.2)"],
        ["Mình có được gửi số điện thoại cá nhân và ngày sinh của nhân viên cho đơn vị khảo sát bên ngoài không?",
         "Không nên. Chỉ chia sẻ dữ liệu tối thiểu (họ tên, email công việc); cần thêm thì phải có sự đồng ý của nhân viên (Mục 7.3)"],
    ], [8.5, 8])

    doc.add_heading("6. Điểm cần nói khi demo", 1)
    bullets(doc, [
        "Mỗi lần hỏi phải @mention agent. Một nhóm chat có thể có nhiều agent.",
        "Agent trả lời theo quyền của người hỏi. Nếu có thành viên không có quyền xem tài liệu, người hỏi thấy View response và tự quyết định có chia sẻ câu trả lời không.",
        "Agent không trả lời trong nhóm chat hoặc kênh có khách bên ngoài (guest).",
        "Khi tài liệu trên site được cập nhật, agent tự dùng bản mới, không phải tạo lại.",
        "Câu trả lời trong nhóm chat hiển thị cho mọi thành viên: không hỏi thông tin Mật hay dữ liệu cá nhân trong nhóm chat đông người.",
    ])

    doc.add_heading("7. Ba cấp độ agent (2 phút)", 1)
    table(doc, ["", "SharePoint agent", "Agent Builder", "Copilot Studio"], [
        ["Dùng khi", "Hỏi đáp tài liệu của một site, thư viện", "Agent nghiệp vụ đơn giản: lời dặn, tài liệu nguồn, câu hỏi gợi ý",
         "Tích hợp hệ thống nghiệp vụ, thực hiện hành động, quản trị và phân phối quy mô lớn"],
        ["Ai tạo", "Người có quyền chỉnh sửa site", "Người dùng, ngay trong Copilot Chat", "Nhóm IT hoặc người phát triển"],
        ["Đưa đến người dùng", "Thêm vào nhóm chat, kênh Teams", "Chia sẻ link, dùng trong Copilot Chat và Teams", "Teams, Copilot Chat, website và các kênh khác"],
        ["Trong buổi học", "Speaker demo (tài liệu này)", "Lab 7, học viên tự làm", "Chỉ giới thiệu"],
    ], [3, 4.4, 4.6, 4.5])
    para(doc, "Câu nối sang bước tiếp theo (chỉ nói miệng): \"Khi doanh nghiệp muốn đưa agent đến nhiều người dùng Teams hơn, hoặc cần agent kết nối "
              "hệ thống nghiệp vụ và thực hiện hành động, đó là lúc dùng Copilot Studio. Phần này chúng tôi sẽ đi sâu trong buổi làm việc kỹ thuật.\"")

    doc.add_heading("8. Câu hỏi khách hàng hay hỏi", 1)
    table(doc, ["Câu hỏi", "Cách trả lời"], [
        ["Agent có đọc được tài liệu tôi không có quyền xem không?", "Không. Agent trả lời theo quyền của người hỏi, giống khi người đó tự mở tài liệu."],
        ["Tài liệu thay đổi thì agent có phải tạo lại không?", "Không. Agent dùng tài liệu trên site nên tự lấy bản mới nhất."],
        ["Bao giờ agent tạo bằng Agent Builder vào được nhóm chat?", "Microsoft chưa công bố thời điểm chính thức. Hiện dùng SharePoint agent cho nhóm chat. Không hứa ngày."],
        ["Người chưa có licence Copilot có dùng được không? Chi phí thế nào?", "Phụ thuộc gói licence và chính sách của tổ chức. Ghi nhận câu hỏi và trao đổi trong buổi làm việc kỹ thuật. Không nêu giá hay mô hình tính phí."],
    ], [6.5, 10])

    doc.add_heading("9. Sự cố và cách xử lý", 1)
    table(doc, ["Hiện tượng", "Xử lý"], [
        ["Không thấy Create an agent", "Kiểm tra quyền chỉnh sửa site và tenant đã bật SharePoint agent. Dùng agent đã tạo sẵn."],
        ["Không có Copy link for Teams hoặc Add to this chat", "Chuyển sang ảnh chụp dự phòng, vẫn giải thích đủ 3 thông điệp."],
        ["Agent không trả lời trong nhóm chat", "Kiểm tra nhóm chat không có khách bên ngoài và đã @mention đúng tên agent. File vừa tải lên có thể cần vài phút mới dùng được."],
        ["Câu trả lời khác đáp án", "Bình thường: Copilot trả lời khác nhau mỗi lần. Kiểm tra ý chính và mục Sổ tay được dẫn."],
    ], [6, 10.5])

    doc.add_heading("10. Không nên", 1)
    bullets(doc, [
        "Không hứa ngày phát hành tính năng, không nêu giá hay mô hình tính phí.",
        "Không demo trong nhóm chat có khách bên ngoài.",
        "Không hỏi thông tin Mật hay dữ liệu cá nhân thật trong nhóm chat demo.",
        "Không dừng ở \"agent đã được tạo\": luôn kết thúc bằng việc agent xuất hiện trong Teams.",
    ])
    doc.save(OUT)


if __name__ == "__main__":
    build()
    print(OUT)
