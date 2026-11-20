# Lab 6 - Copilot trong Teams

## Sau lab này

> [!OUTCOME]
> **Làm được**
>
> - Biến một cuộc họp thành hành động: biết mình đã bỏ lỡ gì, việc nào cần mình xử lý, điểm nào chưa thống nhất
> - Lập biên bản có quyết định, người phụ trách và thời hạn
> - Gọi **@Copilot** ngay trong nhóm chat để cả nhóm cùng thấy bản tóm tắt và bảng chia việc
>
> **Biết được**
>
> - Teams là nơi Copilot thể hiện giá trị rõ nhất: cuộc họp, chat và cộng tác của cả nhóm
> - Copilot trong nhóm chat trả lời cho mọi thành viên, theo đúng quyền truy cập của người hỏi
> - Teams cũng là nơi đưa agent đến với đồng nghiệp

## Tình huống

> **Anh/chị** - *chuyên viên Phòng Kế hoạch*
>
> Sáng 25/11, Ban Giám đốc họp giao ban kết quả quý 3 để chốt hành động cho ba vấn đề: chi phí thuê thầu phụ, nghỉ việc ở văn phòng TP. Hồ Chí Minh, phụ thuộc khách hàng lớn. Anh/chị **vào họp muộn 5 phút**. Sau cuộc họp, các phòng tiếp tục trao đổi trong một nhóm chat Teams.

**Tài liệu demo:** [Transcript họp giao ban quý 3 (mẫu).docx](#file-transcript), dùng khi không có cuộc họp thật đã bật transcript.

## Thực hành trong buổi học

### Bài tập 1: Từ cuộc họp đến hành động

**Chọn một trong hai cách:**

- **Cuộc họp thật** đã bật transcript: trong cuộc họp bấm **Copilot** trên thanh công cụ; sau cuộc họp mở cuộc họp trong **Calendar**, chọn tab **Recap** rồi mở **Copilot**
- **Transcript mẫu:** vào Copilot Chat, gõ "/" chọn [Transcript họp giao ban quý 3 (mẫu).docx](#file-transcript)

Lần lượt hỏi 3 câu:

> **PROMPT:**
>
> Tôi là chuyên viên Phòng Kế hoạch, vào họp muộn lúc 9:05. Tôi đã bỏ lỡ nội dung gì?

> **PROMPT:**
>
> Những việc nào cần Phòng Kế hoạch của tôi xử lý, hạn khi nào?

> **PROMPT:**
>
> Điểm nào chưa được thống nhất? Mỗi bên đang giữ quan điểm gì, và vấn đề đó sẽ được quyết định thế nào?

Sau đó lập biên bản:

> **PROMPT:**
>
> Lập biên bản cuộc họp: các quyết định đã chốt, bảng việc cần làm gồm Việc | Người phụ trách | Thời hạn, và các vấn đề còn treo cần ai quyết định.

**Kết quả mong đợi:**

- **Đã bỏ lỡ:** doanh thu 432 tỷ, lợi nhuận 84 tỷ (giảm 16,8%), thầu phụ vượt 39%; Giám đốc Tài chính đề xuất cắt 20% chi phí thầu phụ trong quý 4 và kiểm soát hợp đồng mới; Giám đốc văn phòng TP. Hồ Chí Minh phản đối việc cắt ngay
- **Việc của Phòng Kế hoạch:** gửi báo cáo quản lý quý 3 bản chốt cho Phòng Truyền thông **trước 08/12**; bổ sung mục rủi ro khách hàng lớn và kiểm soát thầu phụ vào Kế hoạch 2027 **trước 10/12**
- **Chưa thống nhất:** mức cắt thầu phụ quý 4 (Tài chính muốn cắt 20% ngay, TP. Hồ Chí Minh muốn giữ cho 3 dự án chậm đến hết quý 1/2027), sẽ **trình Tổng Giám đốc**; mentor sớm từ tháng 12 cho TP. Hồ Chí Minh, Nhân sự tính chi phí rồi báo lại
- **Bảng việc:** Tài chính gửi số liệu nghỉ việc và làm thêm giờ theo đội **trước 01/12**; Nhân sự gửi kế hoạch giữ chân nhân viên TP. Hồ Chí Minh **trước 05/12**; từ **01/12**, hợp đồng thầu phụ mới trên 500 triệu phải qua Giám đốc Tài chính

### Bài tập 2: Gọi @Copilot trong nhóm chat [MỚI]

**Tạo nhóm chat:**

1. Ngồi theo nhóm 3-4 người. Một người tạo nhóm chat mới trong Teams, đặt tên **Hành động sau giao ban Q3 - Nhóm [số]** và thêm các thành viên
2. Mỗi người dán **một** tin nhắn mẫu dưới đây vào nhóm chat (nhóm 3 người thì bỏ tin D):

> **PROMPT:**
>
> (A - Nhân sự) Sau giao ban, Nhân sự đang làm kế hoạch giữ chân nhân viên văn phòng TP. Hồ Chí Minh, gửi bản nháp trước 05/12. Chuyện mentor sớm từ tháng 12 thì mình đang tính chi phí, chưa chốt.

> **PROMPT:**
>
> (B - Tài chính) Từ 01/12, hợp đồng thầu phụ mới trên 500 triệu phải qua Giám đốc Tài chính. Mình gửi số liệu nghỉ việc và chi phí làm thêm theo đội cho Nhân sự trước 01/12.

> **PROMPT:**
>
> (C - Văn phòng TP. HCM) Mức cắt thầu phụ trong quý 4 vẫn chưa chốt, 3 dự án của khách hàng lớn đang chậm. Ai trình Tổng Giám đốc và khi nào vậy?

> **PROMPT:**
>
> (D - Truyền thông) Mình cập nhật slide town hall theo báo cáo quý 3, cần bản chốt trước 08/12. Câu hỏi về giờ làm thêm trong buổi town hall thì ai trả lời?

**Thêm Copilot vào nhóm chat:**

3. Bấm **Add agents and bots** ở đầu khung chat và chọn **Copilot**. Hoặc gõ **@Copilot** trong khung soạn tin, chọn Copilot và gửi
4. Một người gõ:

> **PROMPT:**
>
> @Copilot Tóm tắt nhóm đã thống nhất những gì, câu hỏi nào chưa ai trả lời, và lập bảng việc cần làm: Việc | Người phụ trách | Hạn chót. Việc nào chưa có người phụ trách thì ghi [CHƯA CÓ].

5. Người khác trong nhóm hỏi tiếp:

> **PROMPT:**
>
> @Copilot Soạn một tin nhắn nhắc việc gửi cả nhóm, dưới 80 chữ, theo thứ tự hạn chót gần nhất, và đề xuất ai nên nhận các việc đang chưa có người phụ trách.

**Kết quả mong đợi:** Cả nhóm cùng thấy câu trả lời ngay trong nhóm chat. Bảng việc có: số liệu theo đội (Tài chính, **01/12**), kiểm soát hợp đồng thầu phụ mới (từ **01/12**), kế hoạch giữ chân TP. Hồ Chí Minh (Nhân sự, **05/12**), báo cáo quý 3 bản chốt cho Truyền thông (**08/12**, **[CHƯA CÓ]** người gửi). Hai câu hỏi chưa ai trả lời: **ai trình Tổng Giám đốc mức cắt thầu phụ**, và **ai trả lời câu hỏi giờ làm thêm** tại town hall.

> [!TIP]
> Nếu câu trả lời dùng thông tin mà không phải ai trong nhóm cũng xem được (ví dụ email riêng của anh/chị), Copilot hiện bản xem trước chỉ cho anh/chị và hỏi có đăng vào nhóm không.

## Tự thực hành thêm

### @Copilot trong kênh của nhóm

@Copilot cũng dùng được trong **kênh (channel)** của Team: Copilot dùng bối cảnh và quyền chung của kênh, nên cả đội cùng làm việc với một Copilot. Trong một bài đăng của kênh, gõ:

> **PROMPT:**
>
> @Copilot Tổng hợp các thông báo và quyết định trong kênh này tuần qua thành 5 gạch đầu dòng, đánh dấu việc nào có hạn trong tuần tới.

### Tóm tắt nhóm chat cho riêng mình

Mở một nhóm chat hoặc kênh, bấm biểu tượng **Copilot** ở góc trên khung chat (chỉ anh/chị thấy câu trả lời) và nhập:

> **PROMPT:**
>
> Tóm tắt các trao đổi trong 7 ngày qua: vấn đề nổi bật, câu hỏi chưa được trả lời, và những việc đang chờ tôi phản hồi.

## Lưu ý tuân thủ

> [!NOTE]
> Câu trả lời của @Copilot trong nhóm chat **hiển thị cho mọi thành viên**: không hỏi về thông tin Mật hay dữ liệu cá nhân trong nhóm chat đông người. Copilot trong cuộc họp cần bật transcript; với cuộc họp có khách hàng hoặc đối tác bên ngoài, người chủ trì phải thông báo và được các bên đồng ý trước khi bật Recording và Transcription. Biên bản do Copilot tạo phải được người chủ trì rà soát trước khi gửi.

## Prompt đề xuất - Teams

### Trong cuộc họp

> **PROMPT:**
>
> Có nội dung nào trong cuộc họp yêu cầu tôi thực hiện hoặc phản hồi không? Những con số nào đã được đưa ra (chỉ tiêu, chi phí, thời hạn), ai nói?

### Theo dõi qua nhiều cuộc họp

> **PROMPT:**
>
> So sánh cuộc họp này với cuộc họp tuần trước: những việc nào đã hoàn thành, những việc nào bị lùi thời hạn?

### Trong nhóm chat dự án

> **PROMPT:**
>
> @Copilot Những quyết định nào đã được chốt trong nhóm chat này từ đầu tháng? Liệt kê kèm người chốt và ngày.
