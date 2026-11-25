# Lab 4 - Copilot trong PowerPoint

## Sau lab này

> [!OUTCOME]
> **Làm được**
>
> - Áp **brand** của công ty cho một bộ slide **có sẵn** ngay trong Copilot: chọn brand, nhập một câu yêu cầu, cả bộ slide đổi theo màu, font và bố cục thương hiệu
> - Thêm một **skill** vào Copilot trong PowerPoint và dùng lại cho mọi bộ slide trình Ban Giám đốc
>
> **Biết được**
>
> - **Brand Kit** do công ty quản lý (màu, font, template, slide mẫu): chọn bằng **+** > **Select brand**, Copilot định dạng slide theo đúng thương hiệu thay vì tự đoán
> - **Skill** là một quy chuẩn viết một lần, gọi lại bằng **@tên-skill**: cả đơn vị trình bày theo cùng một bố cục
> - Ngoài skill tự thêm, PowerPoint có sẵn các skill như **Visualize this slide**, **Review this presentation**, **Prepare for questions** tại **+** > **Choose skills**

> [!TIP]
> **Chuẩn bị trước khi bắt đầu**
>
> - Tải lên **OneDrive**: [Town hall Q3 2026 (bản nháp).pptx](#file-townhall), bộ slide dùng cho cả hai bài tập
> - Tải **về máy**: [Skill PowerPoint - slide-tom-tat-dieu-hanh.zip](#file-skill-ppt), skill mẫu cho Bài tập 2, và [Mẫu thương hiệu (giả định).pptx](#file-brand) nếu cần tự tạo Brand Kit ở Bài tập 1
>
> **Sau Bài tập 2, nếu vẫn chưa thêm được skill:** giải nén file zip trên. Trong khung Copilot của PowerPoint, bấm **...** > **Manage skills** > **Custom skills** > **Create OneDrive folder** > **Open skills folder**, chép thư mục **slide-tom-tat-dieu-hanh** vào đó và bấm **Refresh**. Tên thư mục phải trùng với dòng *name* trong SKILL.md.
>
> Xem [cách tải file về máy](#module-1/cach-tai-file-word-excel-ve-may) nếu cần.

## Tình huống

> **Anh/chị** - *người được nhờ hoàn thiện bài trình bày cho buổi họp toàn công ty*
>
> Phòng Truyền thông nội bộ gửi bản nháp bộ slide cho buổi họp toàn công ty (town hall) quý 3: nội dung đã đủ nhưng chưa theo thương hiệu công ty. Thay vì chỉnh tay từng slide, anh/chị nhờ Copilot áp brand của công ty cho cả bộ slide. Ngoài ra, Ban Giám đốc yêu cầu mọi bộ slide trình lên phải có một **slide tóm tắt điều hành** theo cùng bố cục.

## Thực hành trong buổi học

### Bài tập 1: Áp brand của công ty cho bộ slide có sẵn

[video:ppt-update-deck]

1. Mở [Town hall Q3 2026 (bản nháp).pptx](#file-townhall) **từ OneDrive** bằng **PowerPoint trên máy tính**
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

**Kết quả mong đợi:** Slide bìa nền xanh đậm, chữ trắng; các slide nội dung có vạch nhấn xanh ngọc cạnh tiêu đề, dải chân trang xanh đậm ghi **◆ CÔNG TY GIẢ ĐỊNH** và **Phân loại: Nội bộ**; tiêu đề và nội dung dùng font Segoe UI. Nội dung chữ và số liệu giữ nguyên.

### Bài tập 2: Dạy Copilot quy chuẩn slide tóm tắt điều hành bằng skill [MỚI]

[video:ppt-skill]

Mọi bộ slide trình Ban Giám đốc cần một slide tóm tắt điều hành theo cùng bố cục. Thay vì mỗi lần viết lại một prompt dài, anh/chị thêm quy chuẩn này vào Copilot **một lần** dưới dạng **skill**, rồi gọi lại cho bất kỳ bộ slide nào.

**Thêm skill:**

1. Mở [Town hall Q3 2026 (bản nháp).pptx](#file-townhall) **từ OneDrive** bằng **PowerPoint trên máy tính**
2. Trong khung Copilot, bấm **+** > **Choose skills**, cuộn xuống cuối danh sách, chọn **Manage skills** > **Add skill**
3. Bấm **Sao chép** ở khung dưới đây, dán vào ô nội dung skill và chọn **Add**. Skill được lưu vào thư mục **Skills** trên OneDrive của anh/chị

```skill
---
name: slide-tom-tat-dieu-hanh
description: Tạo một slide tóm tắt điều hành theo quy chuẩn trình Ban Giám đốc cho bộ slide đang mở. Dùng khi người dùng nhờ làm slide tóm tắt, executive summary hoặc chuẩn bị bộ slide trình Ban Giám đốc.
---

# Slide tóm tắt điều hành

Mọi bộ slide trình Ban Giám đốc có một slide tóm tắt điều hành theo cùng một bố cục, để người đọc nắm được toàn bộ nội dung trong 30 giây.

## Các bước

1. Đọc toàn bộ bộ slide đang mở. Không dùng thông tin ngoài bộ slide.
2. Thêm MỘT slide ngay sau slide bìa, dùng bố cục và màu của mẫu đang áp dụng, giữ chân trang phân loại.
3. Tiêu đề: một câu nêu thông điệp chính của cả bộ slide, tối đa 15 từ, có ít nhất một con số.
4. Nội dung chia đúng ba khối, mỗi khối tối đa 2 dòng, mỗi dòng có ít nhất một con số so sánh (với kế hoạch, kỳ trước hoặc chuẩn ngành):
   - **Kết quả**: những gì đã đạt được
   - **Vấn đề**: tối đa 2 vấn đề lớn nhất và nguyên nhân
   - **Hướng xử lý**: giải pháp đã có trong bộ slide
5. Dòng cuối: "Cần Ban Giám đốc quyết định:" kèm 1-2 việc cụ thể, có thời hạn nếu bộ slide có nêu.
6. Giữ nguyên mọi con số như trong bộ slide. Con số nào không chắc chắn thì ghi [CẦN XÁC NHẬN].
7. Sau khi tạo slide, trả lời trong khung chat bằng bảng: Con số | Lấy từ slide nào.

## Không làm

- Không thêm số liệu, cam kết hay quyền lợi không có trong bộ slide.
- Không sửa các slide khác.
```

**Chạy skill:**

4. Trong khung Copilot, gõ **@slide-tom-tat-dieu-hanh** (hoặc chọn trong **+** > **Choose skills**) và nhập:

> **PROMPT:**
>
> @slide-tom-tat-dieu-hanh Tạo slide tóm tắt điều hành cho bộ slide này.

**Kết quả mong đợi:** Một slide mới ngay sau slide bìa, cùng màu của mẫu đang dùng:

- **Tiêu đề** kiểu *"Doanh thu đạt 99,1% kế hoạch nhưng lợi nhuận giảm 16,8%"*
- **Kết quả:** doanh thu **432 tỷ đồng** (99,1% kế hoạch, tăng 3,3% so với quý 2)
- **Vấn đề:** lợi nhuận trước thuế **84 tỷ** (79% kế hoạch) do chi phí thầu phụ **50 tỷ, vượt kế hoạch 39%**; tỷ lệ nghỉ việc **20%** (kế hoạch 11,5%, ngành 13,5%)
- **Hướng xử lý:** bốn sáng kiến 2027, trong đó lộ trình nghề nghiệp, mentor và tăng ngân sách đào tạo
- **Cần Ban Giám đốc quyết định:** phê duyệt Kế hoạch 2027 trong **tháng 11/2026**
- Trong khung chat có bảng Con số | Lấy từ slide nào để anh/chị kiểm tra

5. Thử lại với một bộ slide của chính anh/chị: mở file, gõ **@slide-tom-tat-dieu-hanh**. Không phải viết lại yêu cầu nào

> [!TIP]
> Làm theo các bước trên mà vẫn chưa thêm được skill? Dùng skill mẫu theo phần **Chuẩn bị trước khi bắt đầu** ở đầu trang, rồi chạy tiếp bước 4.

> [!NOTE]
> Trong **+** > **Choose skills** còn có các skill dựng sẵn như **Review this presentation** (góp ý từng slide), **Visualize this slide** và **Prepare for questions** (dự đoán câu hỏi của người nghe). Skill anh/chị tự thêm chỉ mình anh/chị thấy; muốn cả đơn vị dùng chung, nhờ quản trị viên triển khai skill cho tổ chức.

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
