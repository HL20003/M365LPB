# Lab 3 - Copilot trong Excel

## Sau lab này

> [!OUTCOME]
> **Làm được**
>
> - Hỏi Copilot về một workbook nhiều sheet để tìm **xu hướng** và **điểm bất thường**, có số liệu và tên sheet
> - Biến báo cáo nhiều sheet thành **dashboard tương tác** bằng Interactive canvas
> - Tạo **skill** để Copilot tự làm sạch file dữ liệu thô và lập sheet báo cáo mới mỗi tháng
>
> **Biết được**
>
> - Copilot không chỉ vẽ một biểu đồ: nó đọc nhiều sheet cùng lúc và giải thích **vì sao** số liệu thay đổi
> - Dạy một lần, dùng lại mỗi tháng: skill lưu trên OneDrive và được gọi bằng **@tên-skill**, không phải viết lại prompt dài

## Tình huống

> **Anh/chị** - *người cần hiểu nhanh số liệu quý 3*
>
> Doanh thu quý 3 gần đạt kế hoạch nhưng lợi nhuận lại giảm. Trước cuộc họp, anh/chị cần biết vấn đề **bắt đầu từ khi nào** và **tập trung ở đâu**, rồi có một dashboard để Ban Giám đốc tự xem theo từng văn phòng.

**Tệp demo:** [Báo cáo Kết quả Kinh doanh Q3 2026.xlsx](#file-business), gồm các sheet *Tổng quan Q3*, *PL_Budget_Actual*, *Doanh thu tháng*, *Danh sách dự án*, *Theo văn phòng*, *Benchmark*. Bài tập 3 dùng thêm [Phản hồi khách hàng T9-T10 2026 (xuất từ hệ thống).xlsx](#file-feedback).

## Thực hành trong buổi học

### Bài tập 1: Tìm xu hướng và điểm bất thường

1. Mở [Báo cáo Kết quả Kinh doanh Q3 2026.xlsx](#file-business) **từ OneDrive**
2. Nhấn **Copilot** trên ribbon, tab **Home**, nhập prompt:

> **PROMPT:**
>
> Phân tích các sheet Doanh thu tháng và Theo văn phòng. Lợi nhuận bắt đầu lệch khỏi kế hoạch từ tháng nào, lệch bao nhiêu mỗi tháng, và do doanh thu hay chi phí? Văn phòng nào có số liệu bất thường so với các văn phòng còn lại về biên lợi nhuận, tỷ lệ nghỉ việc, giờ làm thêm và NPS? Trả lời trong 5 gạch đầu dòng, mỗi ý có con số và tên sheet.

**Kết quả mong đợi:**

- Từ tháng 1 đến tháng 6, lợi nhuận **gần đúng kế hoạch** (lệch 0 đến 2 tỷ)
- Từ **tháng 7**, lợi nhuận thấp hơn kế hoạch **5, 9 và 8 tỷ đồng** (tháng 7, 8, 9), trong khi doanh thu vẫn gần kế hoạch. Nguyên nhân là **chi phí** thực hiện vượt kế hoạch 4, 5 và 9 tỷ đồng
- **TP. Hồ Chí Minh** bất thường: biên lợi nhuận **15%** (thấp nhất), tỷ lệ nghỉ việc **26,3%**, giờ làm thêm **18,6 giờ/tháng**, NPS **29** (thấp nhất)

3. Hỏi tiếp để đào sâu:

> **PROMPT:**
>
> Trong sheet Danh sách dự án, các dự án của văn phòng TP. Hồ Chí Minh có tỷ lệ chi phí lũy kế trên ngân sách cao hơn các văn phòng khác không? Liệt kê 5 dự án vượt chi phí nhiều nhất so với % hoàn thành.

> [!TIP]
> Copilot ghi tên sheet cho từng con số để anh/chị kiểm tra nhanh.

### Bài tập 2: Dashboard tương tác với Interactive canvas [MỚI]

[video:excel-canvas]

1. Vẫn trong file trên, nhấn **Copilot** và nhập:

> **PROMPT:**
>
> @interactive-canvas Tạo dashboard tương tác cho cuộc họp kết quả quý 3 từ các sheet Theo văn phòng, PL_Budget_Actual và Benchmark. Gồm: thẻ chỉ số doanh thu, lợi nhuận trước thuế và tỷ lệ nghỉ việc so với kế hoạch; biểu đồ tỷ lệ nghỉ việc theo văn phòng có đường trung vị ngành; biểu đồ doanh thu và biên lợi nhuận theo văn phòng; bộ lọc chọn văn phòng. Làm nổi bật các văn phòng có tỷ lệ nghỉ việc trên 15%.

2. Bấm thử bộ lọc văn phòng, rồi chỉnh dashboard bằng câu lệnh, ví dụ:

> **PROMPT:**
>
> Thêm một thẻ chỉ số NPS so với quý 2, và đổi biểu đồ doanh thu thành biểu đồ cột sắp xếp từ cao xuống thấp.

**Kết quả mong đợi:** Dashboard có thẻ **doanh thu 432 tỷ đồng** (đạt 99,1% kế hoạch), **lợi nhuận trước thuế 84 tỷ đồng** (79% kế hoạch), **tỷ lệ nghỉ việc 20%** (kế hoạch 11,5%). Biểu đồ nghỉ việc có đường trung vị ngành **13,5%**, **TP. Hồ Chí Minh 26,3%** được làm nổi bật; chỉ Đà Nẵng thấp hơn trung vị. Khi sửa số liệu trong sheet, dashboard cập nhật theo.

### Bài tập 3: Tạo skill biến file dữ liệu thô thành báo cáo hằng tháng [MỚI]

[video:excel-skill]

Mỗi tháng anh/chị nhận file phản hồi khách hàng xuất từ hệ thống CRM: dòng tiêu đề thừa, dòng trống, dòng trùng, tên văn phòng chỗ ghi "HCM" chỗ ghi "TP. Hồ Chí Minh". Thay vì làm sạch và lập báo cáo tay mỗi tháng, anh/chị dạy Copilot làm **một lần**.

1. Mở [Phản hồi khách hàng T9-T10 2026 (xuất từ hệ thống).xlsx](#file-feedback) **từ OneDrive**, chọn sheet **T9**
2. Nhấn **Copilot**, gõ **@skill-builder** và mô tả công việc:

> **PROMPT:**
>
> @skill-builder Tạo skill tên "bao-cao-phan-hoi-khach-hang" để làm báo cáo phản hồi khách hàng hằng tháng từ sheet dữ liệu thô xuất từ CRM. Các bước: (1) bỏ các dòng ghi chú phía trên dòng tiêu đề có cột STT; (2) trong một sheet mới tên "<tên sheet> sạch": bỏ dòng trống và dòng trùng, chuẩn hóa Văn phòng về 6 tên (Hà Nội, TP. Hồ Chí Minh, Đà Nẵng, Hải Phòng, Cần Thơ, Bình Dương), Nhóm vấn đề về 6 nhóm, Mức độ về Cao/Trung bình/Thấp, Ngày nhận về kiểu ngày dd/mm/yyyy, định dạng thành Table; (3) ghi lại đã bỏ bao nhiêu dòng và sửa bao nhiêu giá trị; (4) trong sheet "<tên sheet> báo cáo": bảng đếm Nhóm vấn đề theo Văn phòng có tổng, và tỷ lệ mức độ Cao theo nhóm; (5) biểu đồ cột chồng theo nhóm vấn đề, tiêu đề nêu phát hiện chính; (6) 3 nhận xét có số liệu, so sánh với tháng trước nếu có. Không sửa sheet gốc, giá trị không xác định được thì đánh dấu "Cần kiểm tra".

3. Copilot hiển thị nội dung skill (tên, mô tả, các bước). Đọc lại, trả lời nếu Copilot hỏi thêm, rồi chọn **lưu**. Skill được lưu vào thư mục **skills** trên OneDrive
4. Chạy skill cho tháng 9, rồi cho tháng 10:

> **PROMPT:**
>
> @bao-cao-phan-hoi-khach-hang Làm báo cáo cho sheet T9.

> **PROMPT:**
>
> @bao-cao-phan-hoi-khach-hang Làm báo cáo cho sheet T10 và so sánh với báo cáo tháng 9.

**Kết quả mong đợi:**

- **Tháng 9:** từ 131 dòng, bỏ 3 dòng trống và 8 dòng trùng, còn **120 phản hồi**; **Chậm tiến độ** nhiều nhất (**38, 32%**), TP. Hồ Chí Minh nhiều phản hồi nhất (**45/120**)
- **Tháng 10:** cùng cấu trúc, không phải mô tả lại các bước: **134 phản hồi**; **Thay đổi nhân sự dự án tăng từ 24 lên 33** (20% lên 25%)

> [!TIP]
> Không tạo được skill bằng @skill-builder? Tải [Skill Excel - bao-cao-phan-hoi-khach-hang.zip](#file-skill-excel) và giải nén. Trong khung Copilot, bấm **...** > **Manage plugins & skills** > **Custom skills** > **Create OneDrive folder** > **Open skills folder**, chép thư mục **bao-cao-phan-hoi-khach-hang** vào đó và bấm **Refresh**. Một cách khác: chọn **Add** > **Record a skill**, tự làm một lần các bước rồi bấm **Stop** và **Save skill**.

## Tự thực hành thêm

### Phân loại dự án theo tình trạng

> **PROMPT:**
>
> Trong sheet Danh sách dự án, thêm cột "Tình trạng": "Rủi ro" nếu dự án vừa chậm tiến độ (% hoàn thành thấp hơn % thời gian đã qua quá 10 điểm phần trăm) vừa vượt chi phí (chi phí lũy kế chia ngân sách lớn hơn % hoàn thành); "Đúng hướng" nếu không chậm tiến độ và không vượt chi phí; còn lại là "Cần chú ý". Sau đó lập bảng đếm số dự án theo từng tình trạng và từng văn phòng.

**Kết quả mong đợi:** 57 dự án Đúng hướng, 71 Cần chú ý và 22 Rủi ro; tỷ lệ Rủi ro cao nhất ở TP. Hồ Chí Minh (13/52 dự án).

### So sánh với chuẩn ngành

> **PROMPT:**
>
> Từ sheet Theo văn phòng, tạo biểu đồ cột tỷ lệ nghỉ việc năm hóa của từng văn phòng, thêm đường trung vị ngành lấy từ sheet Benchmark, tiêu đề nêu đúng phát hiện chính.

## Lưu ý tuân thủ

> [!NOTE]
> Báo cáo kết quả kinh doanh và dữ liệu phản hồi khách hàng là thông tin Mật. Chỉ dùng Copilot với file đã gắn nhãn phân loại và mã khách hàng đã ẩn danh. Không ghi mật khẩu, dữ liệu khách hàng hay số liệu Mật vào nội dung skill. Số liệu Copilot tính phải được đối chiếu với báo cáo chính thức trước khi gửi đi.

## Prompt đề xuất - Excel

### Insights

> **PROMPT:**
>
> So sánh hai văn phòng [tên văn phòng] và [tên văn phòng]: khác nhau ở đâu về doanh thu trên mỗi nhân viên, biên lợi nhuận, giờ làm thêm và tỷ lệ nghỉ việc? Điều gì giải thích chênh lệch?

### Skill cho việc lặp lại

> **PROMPT:**
>
> @skill-builder Tạo skill "doi-chieu-chi-phi-thang" để mỗi tháng so sánh chi phí thực hiện với kế hoạch theo khoản mục, đánh dấu khoản vượt trên 10%, vẽ biểu đồ thác nước và viết 3 nhận xét cho Ban Giám đốc.

> [!NOTE]
> Dữ liệu nên được định dạng dạng **Table** (Ctrl + T) để Copilot đọc chính xác hơn. Với file của chính anh/chị, thay tên sheet và tên cột trong prompt cho khớp.
