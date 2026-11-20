# Lab 2 - Copilot trong Word

## Sau lab này

> [!OUTCOME]
> **Làm được**
>
> - Nhờ Copilot sửa một báo cáo **có sẵn** ở chế độ **Track Changes**, đối chiếu với tài liệu nội bộ, mỗi chỗ sửa có comment ghi nguồn
> - Duyệt từng thay đổi của Copilot trong tab **Review**: chấp nhận, từ chối, trả lời comment
> - Nhờ Copilot viết tóm tắt điều hành từ chính báo cáo đã sửa
>
> **Biết được**
>
> - Copilot làm việc được trên file đang dùng, không chỉ tạo văn bản mới
> - Mọi chỗ Copilot sửa đều **hiện rõ** và có lý do; người phụ trách vẫn là người quyết định giữ hay bỏ
> - Gõ "/" để nối nhiều tài liệu nội bộ trong cùng một yêu cầu

## Tình huống

> **Anh/chị** - *chuyên viên Phòng Kế hoạch*
>
> Đồng nghiệp đã soạn bản nháp **Báo cáo quản lý quý 3** và nhờ anh/chị hoàn thiện trước khi gửi Ban Giám đốc. Bản nháp có vài chỗ ghi sai mục tiêu của Kế hoạch 2027, và mục đề xuất chưa được đối chiếu với Sổ tay Chính sách Nội bộ. Ban Giám đốc cũng cần một đoạn tóm tắt ngắn ở đầu báo cáo.

**Tài liệu demo:** [Báo cáo quản lý Q3 2026 (bản nháp).docx](#file-report), [Kế hoạch Hoạt động 2027 (dự thảo).docx](#file-plan) và [Sổ tay Chính sách Nội bộ.docx](#file-handbook).

## Thực hành trong buổi học

### Bài tập 1: Copilot sửa báo cáo bằng Track Changes [MỚI]

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

### Bài tập 2: Duyệt thay đổi và viết tóm tắt điều hành

**Duyệt thay đổi của Copilot:**

1. Chọn tab **Review**, bấm **Next** để đi lần lượt từng chỗ sửa, đọc comment, mở tài liệu gốc để kiểm tra
2. Bấm **Accept** nếu đồng ý, **Reject** nếu không
3. Hỏi Copilot những gì còn mở:

> **PROMPT:**
>
> Liệt kê các tracked changes và comment còn chưa xử lý trong tài liệu này thành bảng: Mục | Nội dung thay đổi | Căn cứ | Cần ai quyết định.

**Viết tóm tắt điều hành:**

4. Đặt con trỏ ở đầu báo cáo, nhấn **Copilot** và nhập:

> **PROMPT:**
>
> Viết mục "Tóm tắt điều hành" khoảng 5 dòng ở đầu báo cáo cho Ban Giám đốc: kết quả chính của quý 3, hai vấn đề cần quyết định sớm và đề xuất. Chỉ dùng thông tin trong báo cáo này, giữ nguyên số liệu.

5. Lưu file

**Kết quả mong đợi:** Bảng các thay đổi còn mở, trong đó hợp đồng thầu phụ 3,2 tỷ cần **Tổng Giám đốc** duyệt sau **Pháp chế** và tạm ứng trên 30% cần **Giám đốc Tài chính**. Tóm tắt điều hành nêu doanh thu **432 tỷ** (đạt 99,1% kế hoạch), lợi nhuận **84 tỷ** (giảm 16,8% so với quý 2) do chi phí thuê thầu phụ **vượt kế hoạch 39%**, tỷ lệ nghỉ việc **20%**, NPS **36**, kèm đề xuất xử lý.

> [!TIP]
> Copilot **đề xuất**, anh/chị **quyết định**: không bấm **Accept All** khi chưa đọc từng thay đổi. Comment có ghi nguồn giúp kiểm tra mỗi chỗ trong vài giây.

## Tự thực hành thêm

### Sửa hợp đồng theo chính sách bằng Track Changes

Mở [Hợp đồng Dịch vụ Tổ chức Sự kiện (dự thảo).docx](#file-contract) (hợp đồng 2,35 tỷ đồng với Công ty Sự kiện Lam Kiều, cuối tài liệu có *Ghi chú của người soạn thảo*), gõ "/" chọn Sổ tay, rồi nhập:

> **PROMPT:**
>
> Bật Track Changes. Phần Ghi chú của người soạn thảo ở cuối hợp đồng cần đưa vào Điều 8 (Thanh toán) và Điều 9 (Chi phí phát sinh, hủy và phạt vi phạm). Hãy soạn Điều 8 và Điều 9 ngay sau Điều 7, đồng thời sửa mọi điểm chưa đúng Sổ tay Chính sách Nội bộ, kể cả nội dung về dữ liệu khách mời. Với mỗi chỗ sửa, thêm một comment ghi mục Sổ tay làm căn cứ. Những điểm cần cấp có thẩm quyền quyết định thì không tự sửa, chỉ thêm comment nêu rõ cần ai quyết định.

**Kết quả mong đợi:** Tạm ứng 50% → tối đa 30% (Mục 5.2); thanh toán 5 ngày → 30 ngày sau nghiệm thu (5.2); chi phí phát sinh phải được chấp thuận bằng văn bản (5.3); phạt 5% → 8% (5.3); dữ liệu khách mời chỉ họ tên và email công việc (7.3). Phí hủy 100% (cần Pháp chế rà soát) và mới có 2 báo giá (cần 3, Tổng Giám đốc duyệt) chỉ được ghi comment.

### Soạn tờ trình từ hai tài liệu

Mở file Word mới, trong khung **Draft with Copilot** gõ "/" chọn hợp đồng và Sổ tay:

> **PROMPT:**
>
> Dựa trên hợp đồng với Lam Kiều và Sổ tay Chính sách Nội bộ, soạn tờ trình một trang gửi Tổng Giám đốc xin phê duyệt ký hợp đồng: bối cảnh, các điểm đã sửa cho đúng chính sách, các điểm cần phê duyệt ngoại lệ (dạng bảng), rủi ro và biện pháp kiểm soát, đề xuất. Chỗ nào cần số liệu tôi bổ sung thì ghi [CẦN XÁC NHẬN].

### Từ chính sách thành hướng dẫn cho đồng nghiệp

Mở [SAMPLE Chính sách Bảo mật Thông tin.docx](#file-policy-sample) (bản chuyển từ PDF, định dạng còn lỗi) và nhập:

> **PROMPT:**
>
> Từ chính sách này, soạn bản hướng dẫn một trang gửi toàn bộ nhân viên với tiêu đề "Dùng AI trong công việc: được làm và không được làm". Dạng bảng hai cột, tối đa 8 dòng, ngôn ngữ dễ hiểu, cuối trang nêu đầu mối liên hệ khi có sự cố.

## Lưu ý tuân thủ

> [!NOTE]
> Bản sửa và comment do Copilot tạo chỉ là bản nháp: mọi con số, mục tiêu và cấp phê duyệt phải được đối chiếu với văn bản gốc trước khi gửi. Báo cáo quản lý và hợp đồng là tài liệu Mật, chỉ lưu trên OneDrive/SharePoint của công ty. Trước khi gửi file ra ngoài, xử lý hết tracked changes và xóa comment nội bộ.

## Prompt đề xuất - Word

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
