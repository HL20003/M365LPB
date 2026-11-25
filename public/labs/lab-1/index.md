# Lab 1 - Copilot Chat

## Sau lab này

> [!OUTCOME]
> **Làm được**
>
> - Hỏi Copilot về công việc của chính mình và nhận câu trả lời dựa trên email, cuộc họp, tài liệu của mình
> - Dùng dấu **"/"** để chỉ đúng **người, file, email, cuộc họp** cần dùng trong câu hỏi
> - Đặt file Excel và file Word cạnh nhau để Copilot chỉ ra vấn đề trong số liệu mà kế hoạch còn thiếu
>
> **Biết được**
>
> - Copilot hiểu **ngữ cảnh công việc** (Work IQ) ngay từ ngày đầu, không cần tải dữ liệu lên hay khai báo lại vai trò
> - Copilot chỉ dùng những gì **anh/chị đã có quyền xem**, không làm dữ liệu trở nên công khai
> - Mọi việc diễn ra ngay trong Microsoft 365, không cần chép nội dung sang công cụ AI bên ngoài rồi chép kết quả trở lại

## Tình huống

> **Anh/chị** - *chuyên viên Phòng Kế hoạch*
>
> Quý 3 vừa kết thúc. Anh/chị được mời cho ý kiến về dự thảo Kế hoạch Hoạt động 2027 và cần biết kế hoạch đã giải quyết được những vấn đề đang thể hiện trong số liệu quý 3 hay chưa. Trước đó, anh/chị muốn xem Copilot hiểu công việc của mình đến đâu.

**Tài liệu demo:** [Báo cáo Kết quả Kinh doanh Q3 2026.xlsx](#file-business) và [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan), đã lưu trên OneDrive.

## Thực hành trong buổi học

### Bài tập 1: "Bạn biết gì về tôi và công việc của tôi?"

1. Truy cập [https://m365.cloud.microsoft/](https://m365.cloud.microsoft/), đăng nhập bằng **tài khoản công ty**, chọn **Copilot**
2. Kiểm tra nút **Work IQ** ở góc trên bên trái đang **bật** (chữ Work IQ không bị gạch ngang)
3. Nhập prompt:

> **PROMPT:**
>
> Bạn biết gì về tôi và công việc của tôi? Tôi đang làm việc nhiều nhất với những ai, về những chủ đề hoặc dự án nào, và tuần này tôi có những việc gì quan trọng? Ghi nguồn cho từng ý.

**Kết quả mong đợi:** Câu trả lời mang tính **cá nhân**: vai trò, những người anh/chị trao đổi nhiều, các chủ đề và cuộc họp sắp tới, mỗi ý có trích dẫn tới email, cuộc họp hoặc file. Hai người hỏi cùng một câu sẽ nhận hai câu trả lời khác nhau, vì Copilot dựa trên dữ liệu mà **mỗi người có quyền xem**.

> [!TIP]
> Đây là điểm khác với các công cụ AI độc lập: anh/chị không phải giới thiệu mình là ai hay tải tài liệu lên. Bấm vào trích dẫn để thấy Copilot lấy thông tin từ đâu.

### Bài tập 2: Dùng "/" để gọi người, email, cuộc họp

1. Mở cuộc trò chuyện mới. Trong khung nhập, gõ **/** rồi gõ tên một đồng nghiệp anh/chị làm việc nhiều, chọn người đó trong danh sách gợi ý
2. Hoàn thành prompt:

> **PROMPT:**
>
> Tóm tắt những gì /[tên đồng nghiệp] và tôi đã trao đổi trong 2 tuần qua qua email, chat và cuộc họp: việc đã thống nhất, việc tôi đã hứa làm, và việc đang chờ người kia phản hồi.

3. Thử tiếp với một cuộc họp: gõ **/**, gõ tên một cuộc họp gần đây và chọn cuộc họp đó:

> **PROMPT:**
>
> Từ /[tên cuộc họp], liệt kê các quyết định và việc được giao cho tôi kèm thời hạn.

**Kết quả mong đợi:** Copilot chỉ dùng đúng người hoặc cuộc họp anh/chị chọn bằng "/", câu trả lời có trích dẫn tới email, tin nhắn, transcript tương ứng.

> [!TIP]
> Dấu **"/"** dùng được trong Copilot Chat, Word, Excel, PowerPoint: gõ "/" bất cứ khi nào cần chỉ rõ nguồn. Đây là thao tác anh/chị sẽ lặp lại trong mọi lab tiếp theo.

### Bài tập 3: Bức tranh quý 3 từ hai tài liệu

1. Mở cuộc trò chuyện mới, gõ **/** để đính kèm [Báo cáo Kết quả Kinh doanh Q3 2026.xlsx](#file-business), gõ **/** lần nữa để đính kèm [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan)
2. Nhập prompt:

> **PROMPT:**
>
> Tôi được mời cho ý kiến về dự thảo Kế hoạch Hoạt động 2027. Đặt kế hoạch 2027 cạnh kết quả quý 3 trong file Excel và lập bảng: Vấn đề trong số liệu (kèm con số và tên sheet) | Kế hoạch đã có giải pháp chưa | Giải pháp trong kế hoạch (ghi mục) | Nhận xét. Sau bảng, nêu 3 vấn đề Ban Giám đốc cần quyết định sớm nhất. Chỉ dùng thông tin trong 2 file.

**Kết quả mong đợi:**

- Kế hoạch **đã có** giải pháp cho tỷ lệ nghỉ việc cao (**20%**, trung vị ngành 13,5%), giờ làm thêm và NPS giảm (**41 xuống 36**)
- Kế hoạch **chưa đề cập**: lợi nhuận trước thuế **giảm 16,8%** so với quý 2 do chi phí thuê thầu phụ **vượt kế hoạch 39%**, và **36% doanh thu** đến từ một khách hàng (ngành khoảng 20%)

## Tự thực hành thêm

### Báo cáo tuần từ email và cuộc họp

> **PROMPT:**
>
> Dựa trên email, cuộc họp và tài liệu của tôi trong 7 ngày qua, soạn báo cáo tuần gửi quản lý trực tiếp gồm 4 phần: việc đã hoàn thành, việc đang làm và tiến độ, vấn đề cần hỗ trợ hoặc cần quyết định, và kế hoạch tuần tới. Mỗi ý ghi rõ nguồn thông tin. Tối đa một trang.

Tuần nào cũng viết báo cáo? Ở phần Tự thực hành thêm của [Lab 7](#lab-7), anh/chị biến prompt này thành **skill** để gọi lại bằng tên.

### Tắt Work IQ để cập nhật xu hướng công khai

1. Bấm nút **Work IQ** ở góc trên bên trái để **tắt** (chữ Work IQ bị gạch ngang). Copilot mở cuộc trò chuyện mới và chỉ dùng thông tin công khai trên web cùng file anh/chị đính kèm
2. Nhập prompt:

> **PROMPT:**
>
> Tóm tắt những xu hướng nổi bật trong 3 tháng qua về thị trường lao động và việc ứng dụng AI tại nơi làm việc ở Việt Nam. Với mỗi xu hướng, nêu tác động có thể có tới một công ty dịch vụ khoảng 1.000 nhân viên và một việc nên làm. Kèm nguồn cho từng ý.

3. Bấm lại nút **Work IQ** để **bật** trước khi sang lab tiếp theo

## Lưu ý tuân thủ

> [!NOTE]
> Báo cáo gửi Ban Giám đốc có thể chứa thông tin Mật: kiểm tra nhãn phân loại trước khi chia sẻ. Thông tin công khai trên web cần được kiểm tra nguồn trước khi chuyển cho người khác. Không nhập dữ liệu cá nhân vào prompt.

## Prompt đề xuất - Copilot Chat

### Làm việc hằng ngày

> **PROMPT:**
>
> 1. Những việc nào tôi đã hứa với quản lý hoặc đồng nghiệp trong 2 tuần qua mà chưa hoàn thành?
> 2. Tuần này tôi có những cuộc họp nào quan trọng, và cần chuẩn bị gì cho từng cuộc họp?

### Ra quyết định

> **PROMPT:**
>
> So sánh hai phương án trong file /[tên file]: ưu điểm, rủi ro, chi phí và tác động tới người dùng hoặc khách hàng của từng phương án. Đề xuất phương án nên chọn và lý do.
