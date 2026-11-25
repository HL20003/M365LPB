# Lab 4 - Copilot trong PowerPoint

## Sau lab này

> [!OUTCOME]
> **Làm được**
>
> - Làm mới một bộ slide **có sẵn**: áp mẫu thương hiệu, nhờ Copilot rút gọn chữ và viết lại tiêu đề, giữ nguyên số liệu
> - Thêm một **skill** vào Copilot trong PowerPoint và dùng lại cho mọi bộ slide trình Ban Giám đốc
>
> **Biết được**
>
> - Không bắt đầu từ trang trắng: Copilot sửa trên bộ slide đang có và đối chiếu số liệu với tài liệu Word gọi bằng "/"
> - **Skill** là một quy chuẩn viết một lần, gọi lại bằng **@tên-skill**: cả đơn vị trình bày theo cùng một bố cục
> - Ngoài skill tự thêm, PowerPoint có sẵn các skill như **Visualize this slide**, **Review this presentation**, **Prepare for questions** tại **+** > **Choose skills**

> [!TIP]
> **Chuẩn bị trước khi bắt đầu**
>
> - Tải lên **OneDrive**: [Town hall Q3 2026 (bản nháp).pptx](#file-townhall), bộ slide cần làm mới, và [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan) để đối chiếu số liệu
> - Tải **về máy**: [Mẫu thương hiệu (giả định).pptx](#file-brand) để áp mẫu ở Bài tập 1, và [Skill PowerPoint - slide-tom-tat-dieu-hanh.zip](#file-skill-ppt), skill mẫu cho Bài tập 2
>
> **Sau Bài tập 2, nếu vẫn chưa thêm được skill:** giải nén file zip trên. Trong khung Copilot của PowerPoint, bấm **...** > **Manage skills** > **Custom skills** > **Create OneDrive folder** > **Open skills folder**, chép thư mục **slide-tom-tat-dieu-hanh** vào đó và bấm **Refresh**. Tên thư mục phải trùng với dòng *name* trong SKILL.md.
>
> Xem [cách tải file về máy](#module-1/cach-tai-file-word-excel-ve-may) nếu cần.

## Tình huống

> **Anh/chị** - *người được nhờ hoàn thiện bài trình bày cho buổi họp toàn công ty*
>
> Phòng Truyền thông nội bộ gửi bản nháp bộ slide cho buổi họp toàn công ty (town hall) quý 3: đúng nội dung, nhưng toàn chữ, tiêu đề chỉ là tên chủ đề và chưa theo mẫu thương hiệu. Thay vì làm lại từ đầu, anh/chị cập nhật ngay trên bộ slide có sẵn. Ngoài ra, Ban Giám đốc yêu cầu mọi bộ slide trình lên phải có một **slide tóm tắt điều hành** theo cùng bố cục.

## Thực hành trong buổi học

### Bài tập 1: Cập nhật bộ slide có sẵn theo mẫu thương hiệu

[video:ppt-update-deck]

**Áp mẫu thương hiệu:**

1. Mở [Town hall Q3 2026 (bản nháp).pptx](#file-townhall) **từ OneDrive** bằng **PowerPoint trên máy tính**
2. Chọn tab **Design**, mở rộng nhóm **Themes** (mũi tên ở góc dưới bên phải), chọn **Browse for Themes...** và chọn file [Mẫu thương hiệu (giả định).pptx](#file-brand) đã tải về máy. Cả bộ slide đổi sang màu, font và chân trang của công ty

> [!TIP]
> Nếu công ty đã có **mẫu thương hiệu dùng chung** (Brand Kit hoặc template trong thư viện của tổ chức), dùng mẫu đó thay cho file giả định. Copilot học bố cục từ các slide mẫu và slide master của template, nên template càng chuẩn thì slide Copilot tạo càng đúng thương hiệu.

**Làm gọn nội dung bằng Copilot:**

3. Nhấn **Copilot** trên ribbon, tab **Home**, gõ "/" chọn [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan), rồi nhập:

> **PROMPT:**
>
> Sửa bộ slide này cho buổi họp toàn công ty, người nghe là mọi nhân viên. Viết lại tiêu đề mỗi slide thành một thông điệp (ví dụ "Doanh thu đạt kế hoạch nhưng lợi nhuận giảm"), rút mỗi slide còn tối đa 4 ý ngắn, mỗi ý không quá 2 dòng. Giữ nguyên mọi con số và kiểm tra số liệu khớp với file Kế hoạch Hoạt động 2027 đính kèm. Không thêm thông tin mới. Cho tôi biết slide nào có số liệu không khớp.

**Kết quả mong đợi:** Tiêu đề thành thông điệp, ví dụ *"Doanh thu đạt 99,1% kế hoạch nhưng lợi nhuận giảm 16,8%"*, *"Nghỉ việc 20%, cao gần gấp đôi kế hoạch"*. Mỗi slide còn 3-4 ý, số liệu (432 tỷ, 84 tỷ, 1.162 nhân viên, 58 người nghỉ việc, 8/12/25 triệu ngân sách đào tạo) giữ nguyên.

### Bài tập 2: Dạy Copilot quy chuẩn slide tóm tắt điều hành bằng skill [MỚI]

[video:ppt-skill]

Mọi bộ slide trình Ban Giám đốc cần một slide tóm tắt điều hành theo cùng bố cục. Thay vì mỗi lần viết lại một prompt dài, anh/chị thêm quy chuẩn này vào Copilot **một lần** dưới dạng **skill**, rồi gọi lại cho bất kỳ bộ slide nào.

**Thêm skill:**

1. Mở [Town hall Q3 2026 (bản nháp).pptx](#file-townhall) **từ OneDrive** bằng **PowerPoint trên máy tính** (bộ slide sau Bài tập 1 hay bản nháp gốc đều được)
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
