---
name: bao-cao-phan-hoi-khach-hang
description: Làm sạch dữ liệu phản hồi khách hàng xuất từ hệ thống CRM và lập báo cáo tháng gồm bảng tổng hợp, biểu đồ và 3 nhận xét có số liệu. Dùng khi người dùng muốn làm báo cáo phản hồi khách hàng của một tháng từ sheet dữ liệu thô.
---

# Báo cáo phản hồi khách hàng tháng

Skill mẫu của workshop Copilot (dữ liệu giả định). Áp dụng cho sheet dữ liệu thô có các cột:
STT, Ngày nhận, Văn phòng, Mã KH, Mảng dịch vụ, Nhóm vấn đề, Mức độ, Nội dung tóm tắt, Trạng thái.

## Các bước

1. **Xác định dữ liệu.** Dùng sheet người dùng chỉ định hoặc sheet đang mở. Dòng tiêu đề là dòng có ô "STT"; bỏ qua các dòng ghi chú xuất hệ thống phía trên.
2. **Làm sạch** trong một sheet mới tên `<tên sheet> sạch`, không sửa sheet gốc:
   - Bỏ dòng trống và dòng trùng hoàn toàn (so sánh mọi cột trừ STT).
   - Chuẩn hóa **Văn phòng** về đúng 6 tên: Hà Nội, TP. Hồ Chí Minh, Đà Nẵng, Hải Phòng, Cần Thơ, Bình Dương (ví dụ HCM, TP.HCM, tp hcm → TP. Hồ Chí Minh; HN, Ha Noi → Hà Nội).
   - Chuẩn hóa **Nhóm vấn đề** về đúng 6 nhóm: Chậm tiến độ, Thay đổi nhân sự dự án, Phản hồi chậm, Chất lượng bàn giao, Hóa đơn - thanh toán, Khen ngợi.
   - Chuẩn hóa **Mức độ** về Cao, Trung bình, Thấp (High → Cao, Medium/TB → Trung bình, Low → Thấp).
   - Chuyển **Ngày nhận** về kiểu ngày, định dạng dd/mm/yyyy.
   - Định dạng kết quả thành Table và đánh lại STT.
3. **Ghi nhận việc đã làm:** số dòng ban đầu, số dòng trống và dòng trùng đã bỏ, số giá trị đã chuẩn hóa ở mỗi cột, số dòng còn lại.
4. **Tổng hợp** trong sheet mới tên `<tên sheet> báo cáo`:
   - Bảng đếm Nhóm vấn đề (dòng) theo Văn phòng (cột), có dòng và cột tổng, sắp xếp nhóm từ nhiều đến ít.
   - Bảng tỷ lệ phản hồi mức độ Cao theo từng nhóm vấn đề.
5. **Biểu đồ:** biểu đồ cột chồng số phản hồi theo nhóm vấn đề, chia màu theo văn phòng. Tiêu đề biểu đồ nêu phát hiện chính (nhóm nào nhiều nhất, chiếm bao nhiêu phần trăm, tập trung ở văn phòng nào), không chỉ ghi tên chỉ số.
6. **Nhận xét:** viết đúng 3 nhận xét ngắn, mỗi nhận xét có con số cụ thể. Nếu workbook có sheet báo cáo của tháng trước, so sánh với tháng trước.

## Quy tắc

- Không xóa hay sửa sheet dữ liệu gốc.
- Giá trị không xác định được nhóm hoặc văn phòng thì giữ nguyên và đánh dấu "Cần kiểm tra", không tự đoán.
- Không đưa nội dung phản hồi có thông tin cá nhân vào nhận xét.
