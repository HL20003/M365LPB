"""Tạo 2 file Word cho kịch bản xuyên suốt "báo cáo quý 3" (Lab 2, Lab 4, Lab 6).

1) Báo cáo quản lý Q3 2026 (bản nháp).docx - bản nháp do đồng nghiệp soạn, cố ý có lỗi để Copilot sửa ở chế độ Track Changes:
   - 5 chỗ ghi sai so với Kế hoạch Hoạt động 2027 (mục tiêu nghỉ việc, NPS, giờ đào tạo, thời điểm mở văn phòng Huế, ngân sách)
   - 3 đề xuất trái Sổ tay Chính sách Nội bộ (Mục 5.1 thẩm quyền và báo giá, 5.2 tạm ứng, 7.3 dữ liệu cá nhân)
   Số liệu quý 3 trong báo cáo đúng với Báo cáo Kết quả Kinh doanh Q3 2026.xlsx.
2) Transcript họp giao ban quý 3 (mẫu).docx - transcript cuộc họp 25/11/2026 có quyết định, việc cần làm và 2 điểm chưa chốt.
"""
from pathlib import Path

from docx_common import bullets, footer_note, new_doc, para, table, title

OUT = Path(__file__).resolve().parent.parent
FICTION = "Tài liệu nháp (draft) dùng cho mục đích đào tạo. Tên nhân vật, khách hàng, đối tác và số liệu là giả định."


def report():
    doc = new_doc()
    footer_note(doc, FICTION)
    title(doc, "BÁO CÁO QUẢN LÝ QUÝ 3/2026",
          "Gửi Ban Giám đốc  |  Đơn vị soạn thảo: Phòng Kế hoạch và Chiến lược  |  Bản nháp v0.3 ngày 18/11/2026  |  Mật")

    doc.add_heading("1. Kết quả quý 3", 1)
    table(doc, ["Chỉ tiêu", "Quý 2/2026", "Kế hoạch quý 3", "Thực hiện quý 3"], [
        ["Doanh thu (tỷ đồng)", "418", "436", "432"],
        ["Lợi nhuận trước thuế (tỷ đồng)", "101", "106", "84"],
        ["Chi phí thuê thầu phụ (tỷ đồng)", "38", "36", "50"],
        ["Tỷ lệ nghỉ việc năm hóa", "14,9%", "11,5%", "20,0%"],
        ["Điểm hài lòng khách hàng (NPS)", "41", "45", "36"],
    ], [6.5, 3, 3.3, 3.3])
    para(doc, "Doanh thu đạt 99,1% kế hoạch, tăng 3,3% so với quý 2. Tuy nhiên lợi nhuận trước thuế giảm 16,8% so với quý 2, "
         "chủ yếu do chi phí thuê thầu phụ vượt kế hoạch 39% để bù nhân sự nghỉ việc ở mảng Triển khai giải pháp.")

    doc.add_heading("2. Đối chiếu với dự thảo Kế hoạch Hoạt động 2027", 1)
    para(doc, "Dự thảo Kế hoạch Hoạt động 2027 đã có giải pháp cho các vấn đề nhân sự và khách hàng, với các mục tiêu chính như sau:")
    bullets(doc, [
        "Tỷ lệ nghỉ việc năm hóa giảm xuống dưới 15% vào cuối năm 2027.",
        "Điểm hài lòng khách hàng (NPS) đạt +42.",
        "Giờ đào tạo bình quân đạt 24 giờ/người/năm, giờ làm thêm dưới 8 giờ/người/tháng.",
        "Mở văn phòng Huế trong quý 2/2027.",
        "Tổng ngân sách thực hiện kế hoạch dự kiến 60 tỷ đồng.",
    ], style="Normal")

    doc.add_heading("3. Đề xuất xử lý trong quý 4", 1)
    bullets(doc, [
        ("Bảo đảm nhân lực cho dự án: ", "ký hợp đồng khung thuê thầu phụ trị giá 3,2 tỷ đồng với một nhà thầu đã hợp tác lâu năm để chủ động nhân lực "
         "cho các dự án đang chậm. Giám đốc Tài chính phê duyệt; không cần lấy thêm báo giá vì đã có giá từ các hợp đồng trước."),
        ("Giữ chân nhà thầu: ", "tạm ứng 45% giá trị hợp đồng khung ngay khi ký để nhà thầu giữ nhân sự cho công ty."),
        ("Khảo sát gắn kết nhân viên: ", "thuê đơn vị khảo sát bên ngoài; gửi cho đơn vị này danh sách toàn bộ nhân viên kèm số điện thoại cá nhân "
         "và ngày sinh để liên hệ trực tiếp."),
    ], style="Normal")

    doc.add_heading("4. Việc cần làm tiếp theo", 1)
    para(doc, "[CẦN BỔ SUNG sau cuộc họp giao ban ngày 25/11/2026]", italic=True)
    doc.save(OUT / "Báo cáo quản lý Q3 2026 (bản nháp).docx")


TRANSCRIPT = [
    ("00:00:12", "Vũ Thanh Lam (Trưởng phòng Kế hoạch, chủ trì)",
     "Chào mọi người. Hôm nay mình họp giao ban kết quả quý 3. Mục tiêu là chốt hành động cho ba vấn đề: chi phí thuê thầu phụ, "
     "nghỉ việc ở văn phòng TP. Hồ Chí Minh và việc phụ thuộc vào khách hàng lớn. Cuộc họp có bật transcript để làm biên bản."),
    ("00:00:58", "Trần Quốc Bảo (Giám đốc Tài chính)",
     "Doanh thu quý 3 là 432 tỷ, đạt 99,1% kế hoạch, nhưng lợi nhuận trước thuế chỉ 84 tỷ, giảm 16,8% so với quý 2. "
     "Nguyên nhân chính là chi phí thuê thầu phụ 50 tỷ, vượt kế hoạch 39%. Tôi đề xuất hai việc: cắt 20% chi phí thầu phụ ngay trong quý 4, "
     "và từ ngày 01/12 mọi hợp đồng thầu phụ mới trên 500 triệu phải qua Giám đốc Tài chính."),
    ("00:02:40", "Đặng Hữu Phước (Giám đốc văn phòng TP. Hồ Chí Minh)",
     "Tôi đồng ý kiểm soát hợp đồng mới từ 01/12. Nhưng cắt 20% ngay quý 4 thì ba dự án đang chậm của khách hàng KH-001 sẽ trễ thêm. "
     "Tôi đề nghị giữ thầu phụ cho ba dự án này đến hết quý 1/2027."),
    ("00:03:55", "Trần Quốc Bảo (Giám đốc Tài chính)",
     "KH-001 đang chiếm 36% doanh thu, càng phụ thuộc thì rủi ro càng lớn. Tôi vẫn giữ quan điểm phải cắt ngay trong quý 4."),
    ("00:05:10", "Vũ Thanh Lam (Trưởng phòng Kế hoạch, chủ trì)",
     "Điểm này hai bên chưa thống nhất được. Mình ghi nhận cả hai phương án để trình Tổng Giám đốc quyết định. Chuyển sang nhân sự."),
    ("00:05:40", "Ngô Minh Thư (Trưởng phòng Nhân sự)",
     "Quý 3 văn phòng TP. Hồ Chí Minh có 27 người nghỉ việc, tỷ lệ năm hóa 26,3%, giờ làm thêm bình quân 18,6 giờ mỗi tháng. "
     "Phòng Nhân sự sẽ lập kế hoạch giữ chân nhân viên cho văn phòng TP. Hồ Chí Minh, gửi bản nháp trước ngày 05/12. "
     "Để làm được, tôi cần Phòng Tài chính gửi số liệu nghỉ việc và chi phí làm thêm giờ theo từng đội trước ngày 01/12."),
    ("00:06:50", "Trần Quốc Bảo (Giám đốc Tài chính)", "Được, Tài chính gửi trước 01/12."),
    ("00:07:15", "Đặng Hữu Phước (Giám đốc văn phòng TP. Hồ Chí Minh)",
     "Tôi đề nghị cho người mới ở văn phòng mình có mentor ngay từ tháng 12, không chờ đến tháng 1 như kế hoạch."),
    ("00:08:02", "Ngô Minh Thư (Trưởng phòng Nhân sự)",
     "Kế hoạch 2027 áp dụng mentor từ 01/01. Làm sớm từ tháng 12 thì cần thêm ngân sách. Nhân sự sẽ tính chi phí rồi báo lại, hôm nay chưa chốt được."),
    ("00:09:20", "Vũ Thanh Lam (Trưởng phòng Kế hoạch, chủ trì)",
     "Về khách hàng lớn: dự thảo Kế hoạch 2027 hiện chưa có mục nào về rủi ro này. Phòng Kế hoạch sẽ bổ sung mục rủi ro khách hàng lớn "
     "và kiểm soát chi phí thầu phụ vào Kế hoạch 2027, trước ngày 10/12. Ngoài ra, Phòng Kế hoạch gửi báo cáo quản lý quý 3 bản chốt "
     "cho Phòng Truyền thông trước ngày 08/12 để cập nhật slide họp toàn công ty."),
    ("00:10:35", "Vũ Thanh Lam (Trưởng phòng Kế hoạch, chủ trì)", "Cảm ơn mọi người. Biên bản sẽ gửi sau cuộc họp."),
]


def transcript():
    doc = new_doc()
    footer_note(doc, FICTION)
    title(doc, "TRANSCRIPT CUỘC HỌP: GIAO BAN KẾT QUẢ QUÝ 3/2026",
          "Microsoft Teams  |  25/11/2026, 09:00 - 09:11  |  Người tham dự: Trưởng phòng Kế hoạch (chủ trì), Giám đốc Tài chính, "
          "Giám đốc văn phòng TP. Hồ Chí Minh, Trưởng phòng Nhân sự, chuyên viên Phòng Kế hoạch")
    for ts, who, text in TRANSCRIPT:
        para(doc, text, bold_prefix=f"[{ts}] {who}: ")
    doc.save(OUT / "Transcript họp giao ban quý 3 (mẫu).docx")


if __name__ == "__main__":
    report()
    transcript()
    print("2 file Word ->", OUT)
