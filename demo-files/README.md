# File demo - Copilot Overview Workshop (bản general)

File *Hợp đồng Dịch vụ Tổ chức Sự kiện (dự thảo).docx* vẫn được gen_docs.py tạo ra nhưng không còn dùng trên site bản v2.

Tài liệu nháp (draft) dùng cho đào tạo, công ty giả định không nêu tên, dùng được cho mọi phòng ban. Đây là bản gốc; site phục vụ bản sao trong
`public/files/` (tên không dấu, khi tải về vẫn giữ tên đầy đủ).
Sau khi tạo lại file, chạy `python _gen/sync_site_files.py` để chép sang site và đóng gói lại file zip, rồi deploy.

| id trong app.js | File | Dùng ở |
|---|---|---|
| `report` | Báo cáo quản lý Q3 2026 (bản nháp).docx (cố ý có lỗi) | Lab 2 Word, Lab 5 Outlook |
| `handbook` | Sổ tay Chính sách Nội bộ.docx | Lab 2 Word, Lab 8 Agent Builder, speaker demo SharePoint agent |
| `policy-sample` | SAMPLE Chính sách Bảo mật Thông tin.docx (cố ý lỗi định dạng) | Lab 2 Word (tự thực hành) |
| `business` | Báo cáo Kết quả Kinh doanh Q3 2026.xlsx | Lab 1 Copilot Chat, Lab 3 Excel, Lab 7 Researcher |
| `feedback` | Phản hồi khách hàng T9-T10 2026 (xuất từ hệ thống).xlsx (cố ý chưa làm sạch) | Lab 3 Excel Bài 2 (skill) |
| `memo-template` | Mẫu tờ trình (giả định).docx (mẫu trống có chỗ điền trong ngoặc vuông) | Lab 2 Word Bài 1 |
| `plan` | Kế hoạch Hoạt động 2027 (dự thảo).docx | Lab 1, Lab 2, Lab 4, Lab 7 |
| `transcript` | Transcript họp giao ban quý 3 (mẫu).docx | Lab 6 Teams |
| `townhall` | Town hall Q3 2026 (bản nháp).pptx (nhiều chữ, theme mặc định) | Lab 4 PowerPoint |
| `brand` | Mẫu thương hiệu (giả định).pptx | Lab 4 PowerPoint |
| `skill-excel` | Skill Excel - bao-cao-phan-hoi-khach-hang.zip (từ `skills/bao-cao-phan-hoi-khach-hang/SKILL.md`, có bọc thư mục) | Lab 3 Bài 2 (dự phòng) |
| `skill-ppt` | Skill PowerPoint - slide-tom-tat-dieu-hanh.zip (từ `skills/slide-tom-tat-dieu-hanh/SKILL.md`, có bọc thư mục) | Lab 4 Bài 2 (dự phòng) |
| `skill-chat` | Skill Copilot Chat - bao-cao-tuan.zip (từ `skills/bao-cao-tuan/SKILL.md`, SKILL.md ở gốc zip) | Lab 8 (tự thực hành) |

## Tạo lại file

Cần Python với `python-docx`, `openpyxl`, `python-pptx`, cùng Excel và PowerPoint trên Windows.

```bash
cd _gen
python gen_business.py       # sau đó: powershell -File recalc.ps1 -Path "..\Báo cáo Kết quả Kinh doanh Q3 2026.xlsx"
python gen_feedback.py       # file phản hồi khách hàng thô, in đáp án phần skill của Lab 3
python gen_docs.py           # hợp đồng, chính sách lỗi định dạng, kế hoạch 2027, Sổ tay
python gen_scenario.py       # báo cáo quản lý Q3 (bản nháp) và transcript họp giao ban
python gen_template.py       # mẫu tờ trình (Lab 2 Bài 1)
powershell -File make_base_pptx.ps1   # chỉ cần khi chưa có base-16x9.pptx (nền 16:9 tạo bằng PowerPoint)
python gen_slides.py         # 2 file PowerPoint
python sync_site_files.py    # chép sang public/files, đóng gói 2 skill mẫu + zip tổng
```

`export_thumbs.ps1 -Path <file.pptx> -OutDir <thư mục>` xuất ảnh từng slide để kiểm tra nhanh.
`recalc.ps1` mở file bằng Excel để tính và lưu sẵn giá trị công thức (bắt buộc với file Báo cáo Kết quả Kinh doanh).
Trên Windows, đặt `PYTHONIOENCODING=utf-8` nếu terminal báo lỗi in tiếng Việt.

## Ghi chú cho người hướng dẫn (không đưa lên site)

### Agenda 120 phút

| Thời gian | Phần | Trên site |
|---|---|---|
| 00-10 | Khởi động và định hướng. Hỏi nhanh: "Anh/chị mất nhiều thời gian nhất ở email, cuộc họp, báo cáo hay tìm tài liệu?" | Module 1 |
| 10-20 | Copilot, Work IQ và bảo mật dữ liệu: "Bạn biết gì về tôi và công việc của tôi?", dấu "/" gọi người, file, email, cuộc họp | Lab 1 Bài 1-2 |
| 20-50 | Từ dữ liệu công việc đến kết quả hoàn chỉnh: Chat (Lab 1 Bài 3) → Word (Lab 2) → Excel (Lab 3) → PowerPoint (Lab 4). Một câu chuyện (báo cáo quý 3, Kế hoạch 2027), nhưng mỗi lab bắt đầu từ file demo có sẵn. Mỗi lab có ít nhất một bước tạo file mới từ file nguồn (Word → tờ trình, Excel thô → báo cáo, deck → slide tóm tắt bằng skill, Word → email). Bài dài (tờ trình, skill Excel, skill PowerPoint) chiếu video. Outlook chỉ nói nhanh nếu còn thời gian. Chi tiết: speaker/Huong dan speaker.md mục 2.1 | Lab 1 Bài 3, Lab 2-5 |
| 50-70 | Teams: từ cuộc họp đến hành động (transcript mẫu, 3 câu hỏi), @Copilot trong nhóm chat | Lab 6 |
| 70-80 | Researcher: **chỉ show kết quả chạy sẵn**, nhấn mạnh việc đưa dữ liệu công ty vào phân tích | Lab 7 |
| 80-105 | Hands-on: Policy Assistant bằng Agent Builder | Lab 8 |
| 105-112 | Đưa agent vào Teams (Lab 8 Bài 4), speaker demo SharePoint agent trong nhóm chat, ba cấp độ SharePoint agent / Agent Builder / Copilot Studio | Lab 8; speaker/Hướng dẫn trình bày SharePoint agent.docx |
| 112-120 | Tổng kết, 3 câu hỏi, chốt 1-2 tình huống ưu tiên, giới thiệu workshop kỹ thuật tiếp theo | Tổng kết |

### 5 điểm speaker cần làm khách hàng nhớ

1. Copilot hiểu ngữ cảnh công việc (email, cuộc họp, con người, tài liệu có quyền truy cập), làm việc được từ ngày đầu nhờ Work IQ
2. Dấu "/" là thao tác cần lặp lại trong mọi demo
3. Microsoft 365 là một luồng công việc liên tục, không chép qua lại với công cụ AI bên ngoài
4. Teams là trọng tâm: cuộc họp, chat, cộng tác và phân phối agent đến nhiều người dùng
5. Người dùng tự tạo được tài sản AI (agent, skill) để chuẩn hóa quy trình nhiều bước

### Nên tránh

- Đi lần lượt toàn bộ tính năng Word, Excel, PowerPoint, Outlook; giải thích kỹ thuật prompt cơ bản quá lâu
- Tạo PowerPoint từ trang trắng; chỉ chỉnh deck có sẵn theo template
- Demo việc AI nào cũng làm được (viết một đoạn văn, vẽ biểu đồ đơn giản)
- Cam kết về mô hình, giá, quyền sử dụng hay roadmap khi chưa có thông tin chính thức
- Trình bày agent như nội dung độc lập: luôn kết thúc bằng chia sẻ và đưa agent vào Teams
- Cố hoàn thành cả 8 lab trong buổi; phần "Tự thực hành thêm" để học viên tự làm sau
- **Skills** (Excel, Copilot Chat): chuẩn bị sẵn để demo, hẹn buổi 2 hướng dẫn build chi tiết; bài build nằm ở "Tự thực hành thêm"
- Không giới thiệu Analyst

### Chuẩn bị trước buổi học

- Kiểm tra trên tenant các tính năng đang triển khai dần; chưa có thì trình diễn trên máy chiếu: Copilot bật Track Changes và comment (Word),
  Interactive canvas, Skill Builder, Record a skill (Excel), custom skill (PowerPoint),
  @Copilot trong group chat (public preview, cần bật Show preview features trong chính sách cập nhật Teams), Skills in Copilot Chat
  (cần licence Microsoft 365 Copilot; nút Agents có thể đã đổi thành Plugins).
- Lab 6: nếu dùng cuộc họp thật, bật Recording và Transcript; nếu không, học viên dùng file transcript mẫu.
- Lab 7: chạy sẵn một báo cáo Researcher (mất 3-10 phút).
- Demo SharePoint agent (speaker): tạo trước **Trợ lý Sổ tay** từ Sổ tay trên site SharePoint của workshop, cấp quyền đọc cho học viên, gửi link site. Xem speaker/Hướng dẫn trình bày SharePoint agent.docx.
  Kiểm tra tenant cho phép tạo agent trong Copilot Chat; agent của Agent Builder xuất hiện trong Copilot ở Teams.
- Roadmap: agent tạo bằng Agent Builder chưa thêm được vào group chat Teams; khi phát hành, có thể đưa bước thêm agent vào nhóm chat vào Lab 8.
  @Copilot trong kênh (channel agent) chưa có tài liệu chính thức, kiểm tra trước khi giới thiệu.

## Đáp án tham khảo

- **Lab 1 Bài 3:** Kế hoạch 2027 đã có giải pháp cho nghỉ việc (20%, ngành 13,5%), giờ làm thêm và NPS giảm (41 → 36), nhưng chưa đề cập
  lợi nhuận trước thuế giảm 16,8% so với Q2 (thuê thầu phụ 50 tỷ, vượt kế hoạch 39%) và 36% doanh thu từ một khách hàng (ngành 20%).
- **Lab 2 Bài 2 (báo cáo quản lý, Track Changes):** sai so với Kế hoạch 2027: nghỉ việc dưới 15% → dưới 13%, NPS +42 → +45, đào tạo 24 → 32 giờ (mục 2),
  văn phòng Huế quý 2 → quý 3/2027 (mục 3, 6), ngân sách 60 → 64 tỷ (mục 8). Trái Sổ tay: hợp đồng thầu phụ 3,2 tỷ cần 3 báo giá,
  Tổng Giám đốc duyệt sau Pháp chế (5.1); tạm ứng 45% → tối đa 30%, vượt cần Giám đốc Tài chính và bảo lãnh (5.2); gửi SĐT cá nhân,
  ngày sinh cho đơn vị khảo sát (7.3). Số liệu quý 3 ở mục 1 đúng với file Excel.
- **Lab 2 Bài 2 (bảng thay đổi còn mở):** hợp đồng thầu phụ 3,2 tỷ cần Tổng Giám đốc sau Pháp chế; tạm ứng trên 30% cần Giám đốc Tài chính.
- **Lab 2 Bài 1 (tờ trình trên mẫu):** Kính gửi Tổng Giám đốc (> 2 tỷ, 5.1); sự cần thiết: thầu phụ 50 tỷ vượt KH 39%, LNTT 84 tỷ -16,8%, nghỉ việc 20%;
  giá trị 3,2 tỷ, tạm ứng tối đa 30% (960 triệu), nhà thầu và thời hạn [CẦN XÁC NHẬN]; căn cứ: 03 báo giá, Pháp chế rà soát (5.1), tạm ứng 45% → 30%
  hoặc ngoại lệ có Giám đốc Tài chính + bảo lãnh (5.2), điều khoản phát sinh và phạt 8% (5.3); phê duyệt: Pháp chế rà soát, Tổng Giám đốc duyệt.
- **Lab 2 (Prompt đề xuất, tóm tắt điều hành):** doanh thu 432 tỷ (99,1% KH), LNTT 84 tỷ (-16,8% so với Q2) do thầu phụ vượt 39%, nghỉ việc 20%, NPS 36.
- **Lab 3 Bài 1:** lợi nhuận T1-T6 lệch kế hoạch 0 đến -2 tỷ; T7 -5, T8 -9, T9 -8 tỷ, do chi phí vượt kế hoạch 4, 5, 9 tỷ (doanh thu gần kế hoạch).
  TP. Hồ Chí Minh: biên lợi nhuận 15% (thấp nhất), nghỉ việc 26,3%, làm thêm 18,6 giờ, NPS 29 (thấp nhất).
- **Lab 3 Bài 3 (canvas):** doanh thu 432 tỷ (99,1% KH), LNTT 84 tỷ (79% KH), nghỉ việc 20% (KH 11,5%); trung vị ngành 13,5%, chỉ Đà Nẵng thấp hơn (12,3%).
- **Lab 3 Bài 2 (skill phản hồi khách hàng):** T9 131 dòng, bỏ 3 trống + 8 trùng → 120, Chậm tiến độ 38 (32%), TP. HCM 45/120;
  T10 143 dòng → 134, Thay đổi nhân sự dự án 24 → 33 (25%).
- **Lab 3 (tự thực hành):** phân loại dự án 57 / 71 / 22, Rủi ro cao nhất TP. HCM 13/52.
- **Lab 4 Bài 1:** số liệu giữ nguyên (432 tỷ, 84 tỷ, -16,8%, 1.162 nhân viên, 58 nghỉ việc, 20%, đào tạo 8 / 12 / 25 triệu).
  Bài 2 (skill slide-tom-tat-dieu-hanh trên deck Town hall): slide sau bìa, tiêu đề kiểu "Doanh thu đạt 99,1% kế hoạch nhưng lợi nhuận giảm 16,8%";
  Kết quả 432 tỷ (99,1% KH, +3,3%); Vấn đề LNTT 84 tỷ (79% KH), thầu phụ 50 tỷ vượt 39%, nghỉ việc 20% (KH 11,5%, ngành 13,5%);
  Hướng xử lý: 4 sáng kiến 2027 (lộ trình nghề nghiệp, mentor, ngân sách đào tạo); Cần BGĐ quyết định: phê duyệt Kế hoạch 2027 tháng 11/2026.
- **Lab 5 (email từ báo cáo Word):** doanh thu 432 tỷ (99,1% KH), LNTT 84 tỷ (-16,8%) do thầu phụ vượt 39%, nghỉ việc 20%; dưới 120 chữ.
- **Lab 6 Bài 1 (transcript):** bỏ lỡ (trước 9:05): số liệu quý 3, đề xuất cắt 20% thầu phụ quý 4 và kiểm soát hợp đồng mới > 500 triệu từ 01/12,
  TP. HCM phản đối cắt ngay. Việc của Phòng Kế hoạch: báo cáo chốt cho Truyền thông trước 08/12, bổ sung Kế hoạch 2027 trước 10/12.
  Chưa thống nhất: mức cắt thầu phụ (trình Tổng Giám đốc), mentor sớm từ tháng 12 (Nhân sự tính chi phí). Việc khác: Tài chính gửi số liệu 01/12,
  Nhân sự gửi kế hoạch giữ chân TP. HCM 05/12.
- **Lab 6 Bài 2 (@Copilot):** việc: số liệu 01/12 (Tài chính), kiểm soát hợp đồng thầu phụ từ 01/12, kế hoạch giữ chân 05/12 (Nhân sự),
  báo cáo chốt 08/12 [CHƯA CÓ người gửi]; chưa ai trả lời: ai trình Tổng Giám đốc mức cắt thầu phụ, ai trả lời câu hỏi giờ làm thêm tại town hall.
- **Lab 7:** nghỉ việc 20% (trung vị 13,5%), giờ đào tạo 19,2 giờ/người/năm (trung vị 32), khách hàng lớn nhất 36% (trung vị 20%),
  biên LNTT 19,4% (trung vị 22%), NPS 36 (trung vị 44). Đối chiếu Kế hoạch 2027: đã có giải pháp nghỉ việc, đào tạo;
  chưa có mục rủi ro khách hàng lớn và kiểm soát chi phí thầu phụ.
- **Lab 8 Bài 3-4:** 6 năm thâm niên → 15 ngày phép, chuyển tối đa 5 ngày, dùng trước 31/03; chuyên viên đi Đà Nẵng: khách sạn tối đa
  1,2 triệu/đêm, ăn 250.000 đồng/ngày, quyết toán trong 10 ngày làm việc; mua sắm 650 triệu → 3 báo giá, Giám đốc Tài chính duyệt;
  tạm ứng 40% (Bài 4, hỏi trong Teams) là ngoại lệ, cần Giám đốc Tài chính duyệt và bảo lãnh tạm ứng của ngân hàng; giá vàng → từ chối.
- **Demo SharePoint agent (Trợ lý Sổ tay):** hợp đồng thầu phụ 3,2 tỷ → 3 báo giá, Tổng Giám đốc sau Pháp chế (5.1); tạm ứng tối đa 30%,
  45% là ngoại lệ cần Giám đốc Tài chính và bảo lãnh (5.2); không gửi SĐT cá nhân, ngày sinh (7.3).
