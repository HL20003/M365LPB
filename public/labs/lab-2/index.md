# Lab 2 - Copilot trong Word

## Sau lab này

> [!OUTCOME]
> **Làm được**
>
> - Từ báo cáo và Sổ tay, nhờ Copilot điền một **tờ trình mới trên mẫu có sẵn** của công ty
> - Nhờ Copilot sửa một báo cáo **có sẵn** ở chế độ **Track Changes**, đối chiếu với tài liệu nội bộ, mỗi chỗ sửa có comment ghi nguồn
> - Duyệt từng thay đổi của Copilot trong tab **Review**: chấp nhận, từ chối, trả lời comment
>
> **Biết được**
>
> - Gõ "/" để nối nhiều tài liệu nội bộ: một tài liệu Word có thể là nguồn để tạo ra tài liệu Word khác
> - Copilot làm việc trên file đang dùng và trên mẫu của công ty, không cần viết từ trang trắng
> - Mọi chỗ Copilot sửa đều **hiện rõ** và có lý do; người phụ trách vẫn là người quyết định giữ hay bỏ

## Tình huống

> **Anh/chị** - *chuyên viên Phòng Kế hoạch*
>
> Bản nháp **Báo cáo quản lý quý 3** do đồng nghiệp soạn có đề xuất ký hợp đồng khung thuê thầu phụ 3,2 tỷ đồng. Đề xuất này cần một **tờ trình** riêng theo mẫu của công ty để trình phê duyệt. Đồng nghiệp cũng nhờ anh/chị hoàn thiện chính bản nháp đó trước khi gửi Ban Giám đốc: vài chỗ ghi sai mục tiêu của Kế hoạch 2027, và mục đề xuất chưa được đối chiếu với Sổ tay Chính sách Nội bộ.

**Tài liệu demo:** [Mẫu tờ trình (giả định).docx](#file-memo-template), [Báo cáo quản lý Q3 2026 (bản nháp).docx](#file-report), [Sổ tay Chính sách Nội bộ.docx](#file-handbook) và [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan).

## Thực hành trong buổi học

### Bài tập 1: Soạn tờ trình trên mẫu có sẵn từ báo cáo và Sổ tay

[video:word-memo-template]

Anh/chị không viết từ trang trắng mà để Copilot điền mẫu tờ trình có sẵn, lấy nội dung từ báo cáo và đối chiếu với Sổ tay.

1. Mở [Mẫu tờ trình (giả định).docx](#file-memo-template) **từ OneDrive** bằng **Word trên máy tính**
2. Chọn **File** > **Save a Copy**, đặt tên *Tờ trình hợp đồng thầu phụ Q4.docx* và mở bản sao (giữ nguyên mẫu gốc để dùng lại)
3. Nhấn **Copilot**, gõ "/" chọn [Báo cáo quản lý Q3 2026 (bản nháp).docx](#file-report), gõ "/" lần nữa chọn [Sổ tay Chính sách Nội bộ.docx](#file-handbook)
4. Nhập prompt:

> **PROMPT:**
>
> Điền mẫu tờ trình này để xin phê duyệt đề xuất ký hợp đồng khung thuê thầu phụ 3,2 tỷ đồng ở mục 3 của Báo cáo quản lý Q3 2026 đính kèm. Giữ nguyên cấu trúc 5 mục và các bảng của mẫu, thay toàn bộ nội dung trong ngoặc vuông. Mục 1 dùng số liệu quý 3 trong báo cáo. Mục 3 đối chiếu từng nội dung với Sổ tay Chính sách Nội bộ: đề xuất nào trong báo cáo chưa đúng quy định thì điều chỉnh cho đúng và ghi rõ đã điều chỉnh gì. Thông tin không có trong hai tài liệu thì ghi [CẦN XÁC NHẬN].

**Kết quả mong đợi:** Tờ trình mới đúng bố cục mẫu, đã điều chỉnh những đề xuất sai trong bản nháp báo cáo:

| Mục trong mẫu | Copilot điền |
|---------------|--------------|
| Kính gửi | **Tổng Giám đốc** (hợp đồng trên 2 tỷ đồng, Sổ tay Mục 5.1), không phải Giám đốc Tài chính như bản nháp |
| 1. Sự cần thiết | Chi phí thuê thầu phụ **50 tỷ**, vượt kế hoạch **39%**; lợi nhuận **84 tỷ**, giảm **16,8%**; tỷ lệ nghỉ việc **20%**, các dự án chậm cần nhân lực |
| 2. Nội dung đề xuất | Giá trị **3,2 tỷ đồng**; tạm ứng tối đa **30%** (960 triệu đồng); tên nhà thầu và thời hạn ghi **[CẦN XÁC NHẬN]** |
| 3. Căn cứ quy định | Cần **03 báo giá** (bản nháp ghi không lấy thêm báo giá); **Pháp chế** rà soát trước khi trình; tạm ứng 45% trong bản nháp hạ về tối đa 30%, vượt mức là ngoại lệ cần Giám đốc Tài chính duyệt và bảo lãnh ngân hàng (Mục 5.2); hợp đồng có điều khoản chi phí phát sinh và phạt vi phạm **8%** (Mục 5.3) |
| Ý kiến và phê duyệt | Người đề xuất, **Phòng Pháp chế** rà soát, **Tổng Giám đốc** phê duyệt (có thể thêm Giám đốc Tài chính cho ý kiến) |

> [!TIP]
> Nếu Copilot chỉ trả lời trong khung chat mà không điền vào tài liệu, nhập tiếp: *"Cập nhật trực tiếp nội dung này vào tài liệu, giữ nguyên các bảng của mẫu."* Với công việc thật, thay mẫu giả định bằng mẫu tờ trình, biên bản hay báo cáo chính thức của đơn vị.

### Bài tập 2: Copilot sửa báo cáo bằng Track Changes [MỚI]

[video:word-track-changes]

1. Mở [Báo cáo quản lý Q3 2026 (bản nháp).docx](#file-report) **từ OneDrive** bằng **Word trên máy tính**
2. Nhấn **Copilot** trên ribbon, tab **Home**
3. Trong khung Copilot, gõ "/" chọn [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan), gõ "/" lần nữa chọn [Sổ tay Chính sách Nội bộ.docx](#file-handbook)
4. Nhập prompt:

> **PROMPT:**
>
> Bật Track Changes. Đối chiếu báo cáo này với Kế hoạch Hoạt động 2027 và Sổ tay Chính sách Nội bộ đính kèm. Ở mục 2, sửa mọi mục tiêu, thời điểm và ngân sách ghi chưa đúng với Kế hoạch 2027. Ở mục 3, sửa các đề xuất chưa đúng Sổ tay cho đúng quy định. Mỗi chỗ sửa thêm một comment ngắn ghi mục tài liệu làm căn cứ. Không sửa số liệu quý 3 ở mục 1.

**Kết quả mong đợi:** Báo cáo có **vết sửa** (chữ gạch chân màu) và comment bên phải cho từng chỗ:

| Bản nháp ghi | Copilot sửa thành | Căn cứ |
|--------------|-------------------|--------|
| Nghỉ việc dưới 15% | Dưới **13%** | Kế hoạch, mục 2 |
| NPS +42 | **+45** | Kế hoạch, mục 2 |
| Đào tạo 24 giờ/người/năm | **32** giờ | Kế hoạch, mục 2 |
| Mở văn phòng Huế quý 2/2027 | **Quý 3/2027** | Kế hoạch, mục 3 và 6 |
| Ngân sách 60 tỷ đồng | **64 tỷ** đồng | Kế hoạch, mục 8 |
| Hợp đồng thầu phụ 3,2 tỷ, Giám đốc Tài chính duyệt, không lấy thêm báo giá | Trên 2 tỷ: **3 báo giá**, **Tổng Giám đốc** duyệt sau khi **Pháp chế** rà soát | Sổ tay, Mục 5.1 |
| Tạm ứng 45% | Tối đa **30%**; vượt mức cần Giám đốc Tài chính duyệt và bảo lãnh ngân hàng | Sổ tay, Mục 5.2 |
| Gửi số điện thoại cá nhân, ngày sinh nhân viên cho đơn vị khảo sát | Chỉ chia sẻ dữ liệu tối thiểu (họ tên, email công việc), cần nhân viên đồng ý | Sổ tay, Mục 7.3 |

> [!TIP]
> Nếu Copilot báo chưa bật được Track Changes, anh/chị tự bật: tab **Review** > **Track Changes**, rồi gửi lại prompt.

**Duyệt thay đổi của Copilot:**

5. Chọn tab **Review**, bấm **Next** để đi lần lượt từng chỗ sửa, đọc comment, mở tài liệu gốc để kiểm tra
6. Bấm **Accept** nếu đồng ý, **Reject** nếu không
7. Hỏi Copilot những gì còn mở:

> **PROMPT:**
>
> Liệt kê các tracked changes và comment còn chưa xử lý trong tài liệu này thành bảng: Mục | Nội dung thay đổi | Căn cứ | Cần ai quyết định.

**Kết quả mong đợi:** Bảng các thay đổi còn mở, trong đó hợp đồng thầu phụ 3,2 tỷ cần **Tổng Giám đốc** duyệt sau khi **Pháp chế** rà soát, và tạm ứng trên 30% cần **Giám đốc Tài chính** duyệt.

> [!TIP]
> Copilot **đề xuất**, anh/chị **quyết định**: không bấm **Accept All** khi chưa đọc từng thay đổi. Comment có ghi nguồn giúp kiểm tra mỗi chỗ trong vài giây.

## Tự thực hành thêm

### Từ chính sách thành hướng dẫn cho đồng nghiệp

Mở [SAMPLE Chính sách Bảo mật Thông tin.docx](#file-policy-sample) (bản chuyển từ PDF, định dạng còn lỗi) và nhập:

> **PROMPT:**
>
> Từ chính sách này, soạn bản hướng dẫn một trang gửi toàn bộ nhân viên với tiêu đề "Dùng AI trong công việc: được làm và không được làm". Dạng bảng hai cột, tối đa 8 dòng, ngôn ngữ dễ hiểu, cuối trang nêu đầu mối liên hệ khi có sự cố.

## Lưu ý tuân thủ

> [!NOTE]
> Bản sửa và comment do Copilot tạo chỉ là bản nháp: mọi con số, mục tiêu và cấp phê duyệt phải được đối chiếu với văn bản gốc trước khi gửi. Báo cáo quản lý và hợp đồng là tài liệu Mật, chỉ lưu trên OneDrive/SharePoint của công ty. Trước khi gửi file ra ngoài, xử lý hết tracked changes và xóa comment nội bộ.

## Prompt đề xuất - Word

### Tóm tắt điều hành

> **PROMPT:**
>
> Viết mục "Tóm tắt điều hành" khoảng 5 dòng ở đầu báo cáo cho Ban Giám đốc: kết quả chính, hai vấn đề cần quyết định sớm và đề xuất. Chỉ dùng thông tin trong tài liệu này, giữ nguyên số liệu.

### Sửa có vết

> **PROMPT:**
>
> Bật Track Changes và rút gọn phần Tóm tắt điều hành còn một nửa, giữ nguyên các con số. Thêm comment ở những chỗ cần Phòng Tài chính xác nhận số liệu.

### Tổng hợp góp ý

> **PROMPT:**
>
> Đọc tất cả comment và tracked changes chưa xử lý, tạo mục "Tóm tắt góp ý" ở đầu tài liệu: ai góp ý gì, góp ý nào mâu thuẫn nhau, việc gì cần chốt.

### So sánh phiên bản

> **PROMPT:**
>
> So sánh tài liệu này với phiên bản trước /[tên file]: liệt kê các thay đổi về điều khoản, số liệu và cam kết, đánh dấu thay đổi nào bất lợi cho công ty.
