# Lab 4 - Copilot trong PowerPoint

## Sau lab này

> [!OUTCOME]
> **Làm được**
>
> - Thêm một **skill** vào Copilot trong PowerPoint để tóm tắt bất kỳ bộ slide nào thành một slide chuyên nghiệp
> - Áp **brand** của công ty cho một bộ slide **có sẵn** ngay trong Copilot: chọn brand, nhập một câu yêu cầu, cả bộ slide đổi theo màu, font và bố cục thương hiệu
>
> **Biết được**
>
> - **Skill** là cách làm viết một lần, gọi lại bằng **@tên-skill**: không phải viết lại prompt dài, lần nào kết quả cũng theo cùng một chuẩn
> - Ngoài skill tự thêm, PowerPoint có sẵn các skill như **Visualize this slide**, **Review this presentation**, **Prepare for questions** tại **+** > **Choose plugins**
> - **Brand Kit** do công ty quản lý (màu, font, template, slide mẫu): chọn bằng **+** > **Select brand**, Copilot định dạng slide theo đúng thương hiệu thay vì tự đoán

> [!TIP]
> **Chuẩn bị trước khi bắt đầu**
>
> - Tải lên **OneDrive**: [Town hall Q3 2026 (bản nháp).pptx](#file-townhall), bộ slide dùng cho cả hai bài tập
> - Tải **về máy**: [Skill PowerPoint - slide-tom-tat.zip](#file-skill-ppt), skill mẫu cho Bài tập 1, và [Mẫu thương hiệu (giả định).pptx](#file-brand) nếu cần tự tạo Brand Kit ở Bài tập 2
>
> Xem [cách tải file về máy](#module-1/cach-tai-file-word-excel-ve-may) nếu cần.

## Tình huống

> **Anh/chị** - *người được nhờ hoàn thiện bài trình bày cho buổi họp toàn công ty*
>
> Phòng Truyền thông nội bộ gửi bản nháp bộ slide cho buổi họp toàn công ty (town hall) quý 3: nội dung đã đủ nhưng chưa có **slide tóm tắt** để người nghe nắm ý chính ngay từ đầu, và chưa theo thương hiệu công ty. Anh/chị dạy Copilot cách làm slide tóm tắt một lần bằng skill, rồi nhờ Copilot áp brand của công ty cho cả bộ slide thay vì chỉnh tay từng slide.

## Thực hành trong buổi học

### Bài tập 1: Tạo skill làm slide tóm tắt [MỚI]

[video:ppt-skill]

Bộ slide nào cũng cần một slide tóm tắt nội dung và số liệu chính, trình bày đủ chuyên nghiệp để đưa lên lãnh đạo. Thay vì mỗi lần viết lại một prompt dài, anh/chị dạy Copilot cách làm **một lần** dưới dạng **skill**, rồi gọi lại cho bất kỳ bộ slide nào.

**Thêm skill:**

1. Mở [Town hall Q3 2026 (bản nháp).pptx](#file-townhall) **từ OneDrive** bằng **PowerPoint trên máy tính**
2. Trong khung Copilot, bấm **+** > **Choose plugins**. Ở màn **Discover plugins**, bấm **Add** > **Create manually**
3. Form **Create manually** có 3 ô. Bấm **Sao chép** ở từng khung dưới đây và dán vào ô cùng tên, rồi lưu. Skill được lưu vào thư mục **Skills** trên OneDrive của anh/chị và hiện trong mục **Custom skills**

```skill-name
slide-tom-tat
```

```skill-description
Tóm tắt nội dung và số liệu chính của bộ slide đang mở thành một slide, trình bày chuyên nghiệp. Dùng khi người dùng nhờ làm slide tóm tắt, slide tổng hợp hoặc tóm tắt bộ slide.
```

```skill-instructions
Tóm tắt toàn bộ nội dung và số liệu chính của bộ slide đang mở thành MỘT slide. Slide phải đạt chuẩn trình bày chuyên nghiệp, đủ để trình lên cấp lãnh đạo.

Các bước:
1. Đọc toàn bộ bộ slide đang mở. Chỉ dùng thông tin trong bộ slide.
2. Thêm MỘT slide ngay sau slide bìa (không có slide bìa thì đặt ở đầu), dùng bố cục, màu và font của bộ slide.
3. Tiêu đề: một câu nêu thông điệp chính của cả bộ slide, tối đa 15 từ, có con số quan trọng nhất nếu có.
4. Nội dung: 3 đến 5 ý chính, xếp theo mức độ quan trọng, mỗi ý tối đa 2 dòng. Ưu tiên ý có con số, kèm so sánh (với kế hoạch, kỳ trước) nếu bộ slide có.
5. Làm nổi bật 2 đến 3 con số quan trọng nhất (chữ đậm hoặc ô số liệu riêng).
6. Giữ nguyên mọi con số như trong bộ slide. Con số nào không chắc chắn thì ghi [CẦN XÁC NHẬN].
7. Sau khi tạo slide, trả lời trong khung chat bằng bảng: Con số | Lấy từ slide nào.

Tiêu chuẩn trình bày:
- Câu ngắn, rõ, không lặp ý, không dùng từ ngữ chung chung.
- Bố cục thoáng, căn lề thẳng hàng, không quá nhiều chữ trên slide.

Không làm:
- Không thêm số liệu, nhận định hay cam kết không có trong bộ slide.
- Không sửa các slide khác.
```

> [!TIP]
> **Chưa thêm được skill?** Trong khung Copilot, bấm **+** > **Choose plugins** > **Add** > **Upload** và chọn file [Skill PowerPoint - slide-tom-tat.zip](#file-skill-ppt) đã tải về máy, rồi chạy tiếp bước 4.

**Chạy skill:**

4. Trong khung Copilot, gõ **@slide-tom-tat** (hoặc chọn trong **+** > **Choose plugins**) và nhập:

> **PROMPT:**
>
> @slide-tom-tat Tạo slide tóm tắt cho bộ slide này.

**Kết quả mong đợi:** Một slide mới ngay sau slide bìa, cùng bố cục và màu của bộ slide:

- **Tiêu đề** kiểu *"Doanh thu đạt 99,1% kế hoạch nhưng lợi nhuận giảm 16,8%"*
- 3 đến 5 ý chính, ví dụ: doanh thu **432 tỷ đồng** (99,1% kế hoạch); lợi nhuận trước thuế **84 tỷ** (79% kế hoạch) do chi phí thầu phụ vượt kế hoạch 39%; tỷ lệ nghỉ việc **20%** (kế hoạch 11,5%); bốn sáng kiến trong Kế hoạch 2027
- Các con số quan trọng nhất (432 tỷ, 84 tỷ, 20%) được làm nổi bật
- Trong khung chat có bảng Con số | Lấy từ slide nào để anh/chị kiểm tra

5. Thử lại với một bộ slide của chính anh/chị: mở file, gõ **@slide-tom-tat**. Không phải viết lại yêu cầu nào

> [!NOTE]
> Trong **+** > **Choose plugins** còn có các skill dựng sẵn như **Review this presentation** (góp ý từng slide), **Visualize this slide** và **Prepare for questions** (dự đoán câu hỏi của người nghe). Skill anh/chị tự thêm chỉ mình anh/chị thấy; muốn cả đơn vị dùng chung, nhờ quản trị viên triển khai skill cho tổ chức.

### Bài tập 2: Áp brand của công ty cho bộ slide có sẵn

[video:ppt-update-deck]

1. Mở lại [Town hall Q3 2026 (bản nháp).pptx](#file-townhall) đã có slide tóm tắt từ Bài tập 1
2. Nhấn **Copilot** trên ribbon, tab **Home**. Trong khung Copilot, bấm **+** > **Select brand** và chọn Brand Kit **Công ty giả định** (hoặc Brand Kit chính thức của công ty anh/chị). Chưa có Brand Kit nào thì xem TIP bên dưới

> [!TIP]
> **Chưa có Brand Kit?** Tạo nhanh tại [office.com/create/brandkit](https://office.com/create/brandkit):
>
> - Bấm **Create Brand Kit**, đặt tên **Công ty giả định**
> - **Templates**: tải lên file [Mẫu thương hiệu (giả định).pptx](#file-brand)
> - **Colors**: #0A2A4E, #00A3A1, #F28C28
> - **Fonts**: Segoe UI
> - Bấm **Publish**, rồi quay lại bước 2 để chọn brand
>
> Không thấy nút **Create Brand Kit** thì báo người hướng dẫn.

3. Chọn brand xong, bộ slide chưa tự đổi. Nhập yêu cầu:

> **PROMPT:**
>
> Định dạng lại toàn bộ bộ slide này theo brand đã chọn: dùng bố cục từ các slide mẫu của brand, đúng màu, font, slide bìa và chân trang của brand. Giữ nguyên nội dung chữ và số liệu.

**Kết quả mong đợi:** Slide bìa nền xanh đậm, chữ trắng; các slide nội dung có vạch nhấn xanh ngọc cạnh tiêu đề, dải chân trang xanh đậm ghi **◆ CÔNG TY GIẢ ĐỊNH** và **Phân loại: Nội bộ**; tiêu đề và nội dung dùng font Segoe UI. Slide tóm tắt vừa tạo cũng đổi theo brand. Nội dung chữ và số liệu giữ nguyên.

## Tự thực hành thêm

### Bộ slide riêng cho đội của anh/chị

> **PROMPT:**
>
> Tạo bộ slide 5 trang để trình bày kế hoạch 2027 cho đội sau: Đội Triển khai giải pháp tại văn phòng TP. Hồ Chí Minh, 85 người, nhiều thành viên vào làm dưới 1 năm, giờ làm thêm bình quân gần 19 giờ/người/tháng và tỷ lệ nghỉ việc cao nhất công ty. Dựa trên file /Kế hoạch Hoạt động 2027 (dự thảo), cho thấy: những vấn đề đội đang gặp, sáng kiến nào giúp giải quyết từng vấn đề, quyền lợi mới theo cấp bậc, và việc đội sẽ làm trong quý 1/2027. Giọng gần gũi, không hứa hẹn những gì kế hoạch chưa nêu. Chỗ nào cần kiểm tra lại ghi [CẦN XÁC NHẬN].

> [!NOTE]
> Thay mô tả đội trong prompt bằng đội của chính anh/chị. Không đưa tên, đánh giá hay thông tin lương của từng người vào prompt.

## Lưu ý tuân thủ

> [!NOTE]
> Slide dùng ngoài phạm vi người được xem tài liệu gốc không được chứa số liệu Mật. Không hứa hẹn quyền lợi chưa được phê duyệt. Kiểm tra mọi con số trên slide, kể cả trên slide Copilot tạo thêm, khớp với tài liệu chính thức trước khi trình bày.

## Prompt đề xuất - PowerPoint

### Rút gọn cho buổi họp ngắn

> **PROMPT:**
>
> Rút bộ slide này còn 3 slide quan trọng nhất cho buổi họp 15 phút, giữ lại bảng so sánh và bước tiếp theo.

### Báo cáo định kỳ

> **PROMPT:**
>
> Tạo bài trình bày 6 slide báo cáo kết quả tháng của [phòng ban] từ file /[báo cáo], có một slide về điểm chưa đạt và nguyên nhân, một slide về đề xuất cần cấp trên hỗ trợ.

> [!NOTE]
> File cần được lưu trên OneDrive hoặc SharePoint thì Copilot mới tham chiếu được.
