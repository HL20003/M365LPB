# Lab 4 - Copilot trong PowerPoint

## Sau lab này

> [!OUTCOME]
> **Làm được**
>
> - Làm mới một bộ slide **có sẵn**: áp mẫu thương hiệu, nhờ Copilot rút gọn chữ và viết lại tiêu đề, giữ nguyên số liệu
> - Thêm slide từ báo cáo Word bằng "/" và biến slide nhiều chữ thành hình minh họa với **Visualize this slide**
> - Tạo **interactive slide** (dòng thời gian bấm được khi trình chiếu)
> - Tạo **speaker notes** cho cả bài và diễn tập trước câu hỏi khó
>
> **Biết được**
>
> - Không cần làm lại từ đầu: Copilot sửa trên file đang có và theo mẫu thương hiệu của công ty
> - **Skill** trong PowerPoint là các việc Copilot làm sẵn được, chọn tại **+** > **Choose skills**
> - Interactive slide chỉ bấm được khi trình chiếu trong PowerPoint; in hoặc xuất PDF sẽ thành ảnh tĩnh

## Tình huống

> **Anh/chị** - *người được nhờ hoàn thiện bài trình bày cho buổi họp toàn công ty*
>
> Phòng Truyền thông nội bộ gửi bản nháp bộ slide cho buổi họp toàn công ty (town hall) quý 3: đúng nội dung, nhưng toàn chữ, tiêu đề chỉ là tên chủ đề, chưa theo mẫu thương hiệu, và chưa có slide về những vấn đề cần hành động trong báo cáo quản lý quý 3. Thay vì làm lại từ đầu, anh/chị cập nhật ngay trên bộ slide có sẵn.

**Tài liệu demo:**

- [Town hall Q3 2026 (bản nháp).pptx](#file-townhall): 8 slide, nhiều chữ, theme mặc định
- [Mẫu thương hiệu (giả định).pptx](#file-brand): mẫu thương hiệu của công ty giả định (màu, font, chân trang "Phân loại: Nội bộ")
- [Báo cáo quản lý Q3 2026 (bản nháp).docx](#file-report): nguồn cho slide mới
- [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan): tài liệu gốc để kiểm tra số liệu

## Thực hành trong buổi học

### Bài tập 1: Áp mẫu thương hiệu và làm gọn bộ slide có sẵn

**Áp mẫu thương hiệu:**

1. Tải [Mẫu thương hiệu (giả định).pptx](#file-brand) về máy
2. Mở [Town hall Q3 2026 (bản nháp).pptx](#file-townhall) **từ OneDrive** bằng **PowerPoint trên máy tính**
3. Chọn tab **Design**, mở rộng nhóm **Themes** (mũi tên ở góc dưới bên phải), chọn **Browse for Themes...** và chọn file mẫu thương hiệu vừa tải. Cả bộ slide đổi sang màu, font và chân trang của công ty

> [!TIP]
> Nếu công ty đã có **mẫu thương hiệu dùng chung** (Brand Kit hoặc template trong thư viện của tổ chức), dùng mẫu đó thay cho file giả định. Copilot học bố cục từ các slide mẫu và slide master của template, nên template càng chuẩn thì slide Copilot tạo càng đúng thương hiệu.

**Làm gọn nội dung bằng Copilot:**

4. Nhấn **Copilot** trên ribbon, tab **Home**, gõ "/" chọn [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan), rồi nhập:

> **PROMPT:**
>
> Sửa bộ slide này cho buổi họp toàn công ty, người nghe là mọi nhân viên. Viết lại tiêu đề mỗi slide thành một thông điệp (ví dụ "Doanh thu đạt kế hoạch nhưng lợi nhuận giảm"), rút mỗi slide còn tối đa 4 ý ngắn, mỗi ý không quá 2 dòng. Giữ nguyên mọi con số và kiểm tra số liệu khớp với file Kế hoạch Hoạt động 2027 đính kèm. Không thêm thông tin mới. Cho tôi biết slide nào có số liệu không khớp.

**Kết quả mong đợi:** Tiêu đề thành thông điệp, ví dụ *"Doanh thu đạt 99,1% kế hoạch nhưng lợi nhuận giảm 16,8%"*, *"Nghỉ việc 20%, cao gần gấp đôi kế hoạch"*. Mỗi slide còn 3-4 ý, số liệu (432 tỷ, 84 tỷ, 1.162 nhân viên, 58 người nghỉ việc, 8/12/25 triệu ngân sách đào tạo) giữ nguyên.

### Bài tập 2: Thêm slide từ báo cáo và biến thành hình minh họa [MỚI]

1. Chọn slide **Kết quả kinh doanh quý 3**
2. Trong khung Copilot, gõ "/" chọn [Báo cáo quản lý Q3 2026 (bản nháp).docx](#file-report), rồi nhập:

> **PROMPT:**
>
> Thêm một slide ngay sau slide này với tiêu đề là thông điệp chính về những vấn đề cần hành động, lấy từ mục 1 "Kết quả quý 3" của báo cáo đính kèm: lợi nhuận giảm, chi phí thuê thầu phụ vượt kế hoạch, tỷ lệ nghỉ việc cao. Mỗi vấn đề một dòng, có con số so với kế hoạch. Giữ đúng số liệu trong báo cáo.

3. Với slide vừa thêm, bấm **+** > **Choose skills** > **Visualize this slide** (hoặc gõ *"Visualize this slide"*)
4. Lặp lại **Visualize this slide** với slide **Chương trình Phát triển và Phúc lợi 2027** (slide nhiều chữ nhất)

**Kết quả mong đợi:** Slide mới có tiêu đề kiểu *"Ba vấn đề cần xử lý trước khi chốt Kế hoạch 2027"*, gồm lợi nhuận **84 tỷ, giảm 16,8%**; chi phí thuê thầu phụ **50 tỷ, vượt kế hoạch 39%**; tỷ lệ nghỉ việc **20%** (kế hoạch 11,5%). Sau **Visualize this slide**, mỗi vấn đề thành một khối có biểu tượng; slide phúc lợi thành bố cục 3 cột theo cấp bậc (ngân sách đào tạo 8 / 12 / 25 triệu đồng).

> [!TIP]
> Kiểm tra lại từng con số trên hình sau khi Copilot vẽ. Nếu chưa ưng, hỏi tiếp: *"Dùng bố cục 3 cột, làm nổi bật con số bằng màu nhấn của mẫu thương hiệu"*.

### Bài tập 3: Tạo interactive slide cho lộ trình triển khai [MỚI]

1. Chọn slide **Lộ trình triển khai**
2. Chọn tab **Insert** (hoặc **Home**) > **Interactive Slide**. Khung Copilot hiện các dạng: **Summary**, **Timeline**, **Dashboard**, **Comparison**, **Custom**. Chọn **Timeline**
3. Nhập prompt:

> **PROMPT:**
>
> Tạo dòng thời gian tương tác cho lộ trình triển khai Kế hoạch 2027 từ nội dung slide này: 11/2026, 12/2026, 01/2027, Quý 1/2027, Quý 3/2027 và đánh giá hằng quý. Khi bấm vào mỗi mốc, hiện hoạt động, đơn vị chủ trì và việc nhân viên cần làm ở mốc đó. Dùng màu của mẫu thương hiệu.

4. Bấm **Slide Show** và thử bấm vào từng mốc
5. Chỉnh bằng câu lệnh nếu cần, ví dụ: *"Làm nổi bật mốc 01/2027 vì ảnh hưởng tới mọi nhân viên"*

**Kết quả mong đợi:** Dòng thời gian 6 mốc, bấm vào mốc **01/2027** hiện *"Áp dụng Chương trình Phát triển và Phúc lợi 2027, trao đổi 1:1 với quản lý"*, mốc **Quý 1/2027** hiện *"Đào tạo Copilot theo vai trò cho toàn bộ nhân viên"*.

> [!NOTE]
> Interactive slide **chỉ chỉnh được bằng câu lệnh cho Copilot**. Người xem không cần licence Copilot vẫn bấm được khi trình chiếu trong PowerPoint (Windows, Mac, web). Khi in, xuất PDF hoặc mở trên điện thoại, slide hiện thành ảnh tĩnh.

### Bài tập 4: Speaker notes và diễn tập câu hỏi khó

1. Chọn tab **View** > **Notes** (mũi tên) > **Generate speaker notes for all slides**
2. Đọc lời trình bày Copilot đề xuất, bấm **Keep it** để lưu vào phần ghi chú của từng slide (hoặc **Discard**)
3. Diễn tập: trong khung Copilot, nhập:

> **PROMPT:**
>
> Hãy đóng vai một nhân viên làm việc 3 năm, đang mệt vì làm thêm giờ và vừa nhận lời mời từ một công ty khác. Dựa trên bộ slide này, đặt 5 câu hỏi khó nhất người đó có thể hỏi tôi trong buổi họp toàn công ty. Với mỗi câu, gợi ý cách trả lời ngắn gọn, trung thực, chỉ dựa trên những gì kế hoạch đã nêu, và chỉ ra slide nào cần bổ sung.

**Kết quả mong đợi:** Mỗi slide có speaker notes, tổng thời lượng phù hợp một bài 10 phút. 5 câu hỏi sát thực tế, ví dụ *"Bao giờ giờ làm thêm thật sự giảm?"*, *"Lộ trình nghề nghiệp có gắn với tăng lương không?"*, *"Dùng Copilot có phải để cắt giảm người không?"*, kèm gợi ý trả lời.

> [!TIP]
> Chỉ cần notes cho một slide: chọn **Generate speaker notes for current slide**. Speaker notes hoạt động tốt nhất với bài dưới 50 slide.

## Tự thực hành thêm

### Tạo bộ slide mới từ tài liệu Word

1. Tạo bản trình bày mới, nhấn **Copilot**, gõ "/" để đính kèm [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan)
2. Nhập prompt:

> **PROMPT:**
>
> Dựa trên file đính kèm, tạo bộ slide 6 trang để trình bày kế hoạch 2027 tại buổi họp toàn công ty. Viết bằng ngôn ngữ của nhân viên: thay đổi gì, mỗi người được gì và cần làm gì. Có một slide về bốn sáng kiến trọng tâm, một slide so sánh quyền lợi của 3 cấp bậc dạng bảng, một slide lộ trình triển khai, slide cuối là 3 việc mỗi người làm trong tháng 1. Bỏ phần ngân sách chi tiết và chỉ tiêu theo từng văn phòng.

### Bộ slide riêng cho đội của anh/chị

> **PROMPT:**
>
> Tạo bộ slide 5 trang để trình bày kế hoạch 2027 cho đội sau: Đội Triển khai giải pháp tại văn phòng TP. Hồ Chí Minh, 85 người, nhiều thành viên vào làm dưới 1 năm, giờ làm thêm bình quân gần 19 giờ/người/tháng và tỷ lệ nghỉ việc cao nhất công ty. Dựa trên file /Kế hoạch Hoạt động 2027 (dự thảo), cho thấy: những vấn đề đội đang gặp, sáng kiến nào giúp giải quyết từng vấn đề, quyền lợi mới theo cấp bậc, và việc đội sẽ làm trong quý 1/2027. Giọng gần gũi, không hứa hẹn những gì kế hoạch chưa nêu. Chỗ nào cần kiểm tra lại ghi [CẦN XÁC NHẬN].

> [!NOTE]
> Thay mô tả đội trong prompt bằng đội của chính anh/chị. Không đưa tên, đánh giá hay thông tin lương của từng người vào prompt.

## Lưu ý tuân thủ

> [!NOTE]
> Slide dùng ngoài phạm vi người được xem tài liệu gốc không được chứa số liệu Mật. Không hứa hẹn quyền lợi chưa được phê duyệt. Kiểm tra mọi con số trên slide, kể cả trên hình do **Visualize this slide** và interactive slide tạo ra, khớp với tài liệu chính thức trước khi trình bày.

## Prompt đề xuất - PowerPoint

### Rút gọn cho buổi họp ngắn

> **PROMPT:**
>
> Rút bộ slide này còn 3 slide quan trọng nhất cho buổi họp 15 phút, giữ lại bảng so sánh và bước tiếp theo.

### Dashboard tương tác

> **PROMPT:**
>
> Tạo interactive slide dạng Dashboard từ slide kết quả kinh doanh: doanh thu, lợi nhuận trước thuế, tỷ lệ nghỉ việc và NPS, mỗi chỉ số so với kế hoạch; bấm vào chỉ số hiện nguyên nhân chính.

### Báo cáo định kỳ

> **PROMPT:**
>
> Tạo bài trình bày 6 slide báo cáo kết quả tháng của [phòng ban] từ file /[báo cáo], có một slide về điểm chưa đạt và nguyên nhân, một slide về đề xuất cần cấp trên hỗ trợ.

> [!NOTE]
> File cần được lưu trên OneDrive hoặc SharePoint thì Copilot mới tham chiếu được.
