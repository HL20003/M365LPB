# Hướng dẫn speaker - Copilot Overview Workshop

Bản general v2, cập nhật 21/11/2026. Tài liệu nội bộ cho người trình bày và trợ giảng, không gửi cho học viên.

## 1. Buổi workshop này là gì

Đây là buổi **giới thiệu 120 phút**, không phải khóa đào tạo đủ tính năng. Mục tiêu là để khách hàng thấy giá trị của Microsoft 365 Copilot trong công việc của họ, tự tay tạo được một agent, và muốn đi tiếp (thử nghiệm, mở rộng licence, xây agent, workshop kỹ thuật).

- Site lab có 9 lab. **Không cố làm hết**: trong buổi chỉ làm phần "Thực hành trong buổi học"; phần "Tự thực hành thêm" để học viên tự làm sau.
- Lab 1-4 cùng **một câu chuyện** (chuẩn bị báo cáo quý 3 và Kế hoạch 2027) để speaker kể liền mạch Chat → Word → Excel → PowerPoint. Nhưng mỗi lab bắt đầu từ file demo có sẵn, nên học viên làm lab nào trước cũng được.
- Mỗi lab Office có ít nhất một bước **tạo file mới từ file nguồn**: báo cáo Word → tờ trình Word, file Excel thô → sheet báo cáo, tài liệu Word → slide, báo cáo Word → email. Đây là cách minh họa điểm 3 "luồng công việc liên tục".
- Bài có nhãn "Tính năng mới" dùng tính năng Microsoft mới phát hành hoặc đang triển khai dần: phải chạy thử trên tenant trước (mục 3.3 và 3.4).

### 5 điểm khách hàng phải nhớ

1. **Copilot hiểu ngữ cảnh công việc**: làm việc với email, cuộc họp, con người, tài liệu mà người dùng có quyền truy cập, ngay từ ngày đầu nhờ Work IQ. Không cần "dạy" AI nhiều năm.
2. **Dấu "/" là thao tác lặp lại** trong mọi demo: gọi người, file, email, cuộc họp làm nguồn.
3. **Microsoft 365 là một luồng công việc liên tục**: không chép nội dung sang công cụ AI bên ngoài rồi chép kết quả trở lại.
4. **Teams là trọng tâm**: cuộc họp, chat, cộng tác và là nơi đưa agent đến nhiều người dùng.
5. **Người dùng tự tạo được tài sản AI**: agent, skill chuẩn hóa một quy trình nhiều bước thay vì viết lại prompt.

### Nên tránh

- Đi lần lượt toàn bộ tính năng Word, Excel, PowerPoint, Outlook; giảng kỹ thuật viết prompt cơ bản quá lâu.
- Tạo PowerPoint từ trang trắng. Demo trực tiếp là **chỉnh deck có sẵn**; tạo deck mới chỉ làm **trên mẫu thương hiệu từ tài liệu Word** và chiếu bằng video (Lab 4 Bài 4).
- Demo việc AI nào cũng làm được (viết một đoạn văn, vẽ biểu đồ đơn giản). Vì vậy "viết tóm tắt điều hành" chỉ còn trong Prompt đề xuất của Lab 2.
- Cam kết về mô hình, giá, quyền sử dụng hay ngày phát hành khi chưa có thông tin chính thức.
- Dừng agent ở chỗ "đã tạo xong". Luôn kết thúc bằng chia sẻ và đưa agent vào Teams (Lab 9).
- Giới thiệu Analyst.

## 2. Agenda 120 phút và việc của speaker

| Thời gian | Phần | Lab | Speaker làm | Học viên làm |
|---|---|---|---|---|
| 00-10 | Khởi động và định hướng | Module 1 | Hỏi nhanh: "Anh/chị mất nhiều thời gian nhất ở email, cuộc họp, báo cáo hay tìm tài liệu?". Nêu 5 điểm cần nhớ, nhấn mạnh Copilot tôn trọng quyền truy cập | Mở site, tải file demo lên OneDrive |
| 10-20 | Copilot, Work IQ, bảo mật dữ liệu | Lab 1 Bài 1-2 | Demo "Bạn biết gì về tôi và công việc của tôi?" và dấu "/" gọi người, cuộc họp | Làm Bài 1 trên tài khoản của mình |
| 20-50 | Từ dữ liệu công việc đến kết quả hoàn chỉnh | Lab 1 Bài 3, Lab 2, 3, 4 (Lab 5 nếu còn giờ) | Kể một câu chuyện qua 4 ứng dụng, xem mục 2.1. Demo trực tiếp bài ngắn, chiếu video bài dài. Skills chỉ demo, hẹn buổi 2 hướng dẫn build | Làm theo bài demo trực tiếp; bài có video để tự làm sau |
| 50-70 | Teams: từ cuộc họp đến hành động | Lab 6 | Demo 3 câu hỏi trên transcript mẫu; chia nhóm 3-4 người cho bài @Copilot | Bài 1 (transcript), Bài 2 (nhóm chat) |
| 70-80 | Researcher | Lab 7 | **Chỉ show báo cáo chạy sẵn**, nhấn mạnh việc đưa dữ liệu công ty vào phân tích | Xem, có thể gửi đề bài rồi chuyển lab |
| 80-105 | Hands-on: Policy Assistant | Lab 8 | Dẫn từng phần A-E, đi vòng hỗ trợ | Tự tạo, test và chia sẻ agent |
| 105-112 | Đưa agent vào Teams, 3 cấp độ | Lab 9 | Demo agent trong Teams và SharePoint agent trong nhóm chat; giải thích 3 cấp độ | Bài 1: mở agent trong Teams |
| 112-120 | Tổng kết, chốt bước tiếp theo | Tổng kết | Hỏi 3 câu, chốt 1-2 tình huống ưu tiên, giới thiệu buổi tiếp theo | Trả lời, góp ý |

### 2.1 Phút 20-50: một câu chuyện qua 4 ứng dụng

Câu chuyện: *"Quý 3 vừa xong, doanh thu gần đạt nhưng lợi nhuận giảm. Anh/chị phải chuẩn bị báo cáo và tờ trình cho Ban Giám đốc, rồi cập nhật slide họp toàn công ty."* Mỗi bước đều chỉ ra: file nào đi vào, file nào được tạo ra, và dấu "/" ở đâu.

| Phút | Ứng dụng | Demo trực tiếp | Chiếu video | File vào → file ra | Câu chuyển sang bước sau |
|---|---|---|---|---|---|
| 20-25 | Copilot Chat | Lab 1 Bài 3 | | Excel + Kế hoạch Word → bảng vấn đề | "Copilot đã chỉ ra vấn đề. Giờ đưa vào bản báo cáo đồng nghiệp đã soạn sẵn." |
| 25-32 | Word | Lab 2 Bài 1: Track Changes, mở 2-3 comment, Accept/Reject | Lab 2 Bài 2: tờ trình trên mẫu (demo trực tiếp nếu chạy thử ổn và còn giờ) | Báo cáo nháp → báo cáo có vết sửa; báo cáo + Sổ tay → **tờ trình mới** | "Ban Giám đốc sẽ hỏi: lợi nhuận giảm từ khi nào, ở đâu?" |
| 32-40 | Excel | Lab 3 Bài 1 (xu hướng, bất thường); Bài 2 Interactive canvas nếu tenant có | Lab 3 Bài 3: tạo và chạy skill (hẹn buổi 2 build chi tiết) | Excel → dashboard; Excel thô → **sheet báo cáo mới** | "Có kết luận rồi, giờ cập nhật slide họp toàn công ty, không làm lại từ đầu." |
| 40-48 | PowerPoint | Lab 4 Bài 1 (áp mẫu, thêm slide từ báo cáo Word, Visualize); Bài 2 interactive slide 1 phút; Bài 3 speaker notes 1 phút | Lab 4 Bài 4: deck mới từ Word trên mẫu thương hiệu | Báo cáo Word → slide; Kế hoạch Word + mẫu → **deck mới** | "Cuối cùng gửi cho Ban Giám đốc, cũng từ chính báo cáo đó." |
| 48-50 | Outlook | Lab 5 bước 5: email từ báo cáo Word (nếu còn giờ) | | Báo cáo Word → **email** | Sang Teams: "Báo cáo đã xong, giờ đến cuộc họp giao ban." |

- Video do team tự quay. Khi có link (Stream, SharePoint hoặc YouTube), điền vào `demoVideos` trong `public/js/app.js`; nút **Xem video demo** chỉ hiện ở bài có link.
- Trong lúc chiếu video, nói rõ học viên **có đủ bước trên site** để tự làm sau buổi học.
- Nếu một bài demo trực tiếp lỗi, chuyển ngay sang video của bài đó, không sửa lỗi trước mặt khách hàng.

## 3. Chuẩn bị trước buổi học (checklist)

### 3.1 Tài khoản, licence, quyền

- Mỗi học viên có **tài khoản công ty** với licence **Microsoft 365 Copilot**. Licence này cần cho Copilot trong Word, Excel, PowerPoint, Outlook, Teams, Researcher, @Copilot trong nhóm chat, agent trong Teams và Skills.
- Học viên dùng **Word, Excel, PowerPoint bản cài trên máy** (Microsoft 365, kênh cập nhật mới) cho Lab 2 và Lab 4, cùng **Teams bản desktop**.
- **Tài khoản demo mới sẽ trống**: Lab 1 Bài 1-2, Lab 5 cần email, cuộc họp, chat có thật trong 2 tuần gần nhất. Nếu dùng tài khoản lab, gửi vài email và tạo vài cuộc họp giữa các tài khoản trước 1-2 ngày.
- Quản trị viên tenant kiểm tra:
  - Người dùng **được tạo và chia sẻ agent** trong Copilot Chat (Agent Builder), chia sẻ được cho người dùng cụ thể trong tổ chức.
  - **Copilot trong Teams group chat** đang ở public preview: bật **Show preview features** trong chính sách cập nhật Teams cho học viên.
  - SharePoint agent được bật cho tenant.
- Chuẩn bị **2-3 tài khoản dự phòng** có đủ licence.

### 3.2 File demo

- Học viên tải tất cả từ trang Module 1 (nút **Tải tất cả .zip**), tạo thư mục **Copilot Workshop** trên OneDrive và tải các file lên. Copilot chỉ đọc được file trên OneDrive hoặc SharePoint.
- Speaker giữ sẵn một bản trên OneDrive của mình để demo.

| File | Dùng ở |
|---|---|
| Báo cáo Kết quả Kinh doanh Q3 2026.xlsx | Lab 1, Lab 3, Lab 7 |
| Kế hoạch Hoạt động 2027 (dự thảo).docx | Lab 1, Lab 2, Lab 4, Lab 7 |
| Báo cáo quản lý Q3 2026 (bản nháp).docx | Lab 2, Lab 4, Lab 5 |
| Mẫu tờ trình (giả định).docx | Lab 2 Bài 2 |
| Sổ tay Chính sách Nội bộ.docx | Lab 2, Lab 8, Lab 9 |
| Town hall Q3 2026 (bản nháp).pptx, Mẫu thương hiệu (giả định).pptx | Lab 4 |
| Transcript họp giao ban quý 3 (mẫu).docx | Lab 6 |
| Phản hồi khách hàng T9-T10 2026.xlsx, Skill Excel .zip | Lab 3 Bài 3 |
| Skill Copilot Chat .zip | Lab 8 (tự thực hành) |

### 3.3 Chạy thử phần Office (1-2 ngày trước)

Chạy lại **toàn bộ bài chính** của Lab 1-6 bằng một tài khoản giống tài khoản học viên (cùng licence, cùng phiên bản Office), trên đúng bộ file demo. Không chỉ xem tính năng có hay không, mà kiểm tra **kết quả có khớp đáp án** và **mỗi bài mất bao lâu**, để căn lại agenda.

**Kiểm tra chung cho mọi ứng dụng:**

- Thấy nút **Copilot** trên tab Home của Word, Excel, PowerPoint bản cài trên máy; thấy biểu tượng Copilot trong Outlook (bản mới hoặc web) và trong Teams
- File demo mở **từ OneDrive** (không mở bản tải về máy), **AutoSave** đang bật
- Gõ "/" trong khung Copilot thấy gợi ý đúng file demo; file vừa tải lên có thể cần vài phút mới xuất hiện
- Copilot trả lời bằng tiếng Việt, đọc được tên file và số liệu tiếng Việt
- Ghi lại thời gian thực tế của từng bài

| Ứng dụng | Chạy thử | Đạt khi | Nếu không đạt |
|---|---|---|---|
| Copilot Chat (Lab 1) | Bài 1 "Bạn biết gì về tôi?"; Bài 2 gõ "/" chọn một người và một cuộc họp; Bài 3 đính kèm file Excel và Word | Bài 1-2 trả lời có trích dẫn tới email, cuộc họp thật; Bài 3 chỉ ra kế hoạch chưa đề cập lợi nhuận giảm 16,8% và 36% doanh thu từ một khách hàng | Tài khoản trống dữ liệu: gửi email, tạo cuộc họp giữa các tài khoản trước 1-2 ngày; Bài 3 thiếu ý: hỏi tiếp trong cùng cuộc trò chuyện |
| Word (Lab 2) | Bài 1 trên Báo cáo quản lý Q3 (bản nháp), gõ "/" chọn Kế hoạch 2027 và Sổ tay; Bài 2 trên bản sao Mẫu tờ trình, gõ "/" chọn báo cáo và Sổ tay | Bài 1: đủ 8 chỗ sửa có vết sửa và comment ghi nguồn, Accept/Reject được. Bài 2: giữ bố cục 5 mục của mẫu, Kính gửi Tổng Giám đốc, 03 báo giá, tạm ứng tối đa 30%, chỗ thiếu ghi [CẦN XÁC NHẬN] | Không có vết sửa: bật tay Review > Track Changes rồi chạy lại prompt. Bài 2 Copilot chỉ trả lời trong khung chat: nhập "Cập nhật trực tiếp vào tài liệu"; vẫn không được thì chiếu video. Sau khi chạy thử, **tải lại bản nháp và mẫu gốc** |
| Excel (Lab 3) | Bài 1 trên Báo cáo Kết quả Kinh doanh Q3 và câu hỏi tiếp; Bài 2 @interactive-canvas; Bài 3 @skill-builder trên file Phản hồi khách hàng, chạy skill cho T9 rồi T10 | Bài 1 nêu đúng lợi nhuận lệch 5, 9, 8 tỷ từ tháng 7 và TP. Hồ Chí Minh bất thường, có tên sheet. Bài 3: T9 còn 120 phản hồi, T10 còn 134, có sheet sạch và sheet báo cáo mới | Nút Copilot mờ: mở file từ OneDrive. @skill-builder không có: dùng file Skill Excel .zip (Manage plugins & skills > Custom skills). Xóa skill đã tạo khi chạy thử để buổi demo tạo lại từ đầu |
| PowerPoint (Lab 4) | Bài 1: áp mẫu bằng Design > Browse for Themes, làm gọn deck, gõ "/" chọn báo cáo Word để thêm slide, Visualize. Bài 4: bản sao Mẫu thương hiệu, gõ "/" chọn Kế hoạch 2027 | Bài 1: cả deck đổi màu, font, chân trang; tiêu đề thành thông điệp; số liệu giữ nguyên; slide mới đúng 3 vấn đề. Bài 4: 6 slide dùng bố cục của mẫu, có bảng 3 cấp bậc 8 / 12 / 25 triệu | Copilot không sửa được cả deck một lần: sửa từng slide. Bài 4 ra theme mặc định: Design > Browse for Themes chọn lại mẫu. Giữ lại **bản deck và mẫu gốc** cho buổi học |
| Outlook (Lab 5) | Phân 3 nhóm email; Summary by Copilot một chuỗi email dài; Draft with Copilot; Coaching by Copilot; email mới gõ "/" chọn báo cáo Word | Có ít nhất 10 email trong 3 ngày gần nhất và 1 chuỗi email nhiều người; thư nháp bám đúng chuỗi email; email từ báo cáo có 432 tỷ, 84 tỷ, 39%, 20% | Hộp thư trống: gửi trước vài email và một chuỗi trả lời qua lại giữa các tài khoản |
| Teams (Lab 6) | Gõ "/" chọn transcript mẫu trong Copilot Chat, hỏi 3 câu và lập biên bản; nếu dùng cuộc họp thật: họp thử có bật Recording và Transcript | Trả lời đúng phần bỏ lỡ, việc của Phòng Kế hoạch (08/12, 10/12), 2 điểm chưa thống nhất; tab Recap xuất hiện sau cuộc họp thử | Không có Recap: kiểm tra đã bật Transcript và tài khoản có tham dự; Recap có thể mất vài phút mới hiện. Dùng transcript mẫu thay cho cuộc họp thật |

### 3.4 Chạy thử các tính năng mới

Tính năng nào chưa có trên tenant thì chuyển bài đó sang **speaker demo trên máy chiếu**, không để học viên làm.

| Tính năng | Lab | Kiểm tra |
|---|---|---|
| Nút Work IQ | 1 | Thấy nút Work IQ góc trên bên trái Copilot Chat |
| Copilot bật Track Changes, thêm comment | 2 | Prompt Bài 1 tạo được vết sửa và comment trong Word desktop |
| Interactive canvas | 3 | Gõ @interactive-canvas trong Copilot của Excel tạo được dashboard |
| Skills trong Excel | 3 | Gõ @skill-builder tạo và lưu được skill; thấy **Manage plugins & skills** > **Custom skills** |
| Visualize this slide, Interactive Slide, Generate speaker notes | 4 | Có skill trong **+ > Choose skills**, nút **Interactive Slide** ở tab Insert, mục **Generate speaker notes** ở View > Notes |
| @Copilot trong nhóm chat | 6 | Thêm được Copilot vào nhóm chat bằng **Add agents and bots** |
| Researcher | 7 | Thấy Researcher trong Agents; **chạy sẵn báo cáo** bằng đề bài trong lab, đính kèm cả file Excel và Kế hoạch 2027 (mất 3-10 phút), giữ tab kết quả |
| Agent Builder | 8 | Thấy **New Agent**, tạo và chia sẻ được agent |
| SharePoint agent, agent trong Teams | 9 | Xem mục 4.2 |

## 4. Phần agent (Lab 8 và Lab 9)

Đây là phần học viên nhớ nhất: họ **tự tạo** được một agent và thấy agent **đến được Teams**. Cần chuẩn bị kỹ nhất.

### 4.1 Lab 8 - Policy Assistant (hands-on, 25 phút)

**Chuẩn bị:**

- Speaker tự làm hết Lab 8 trên tenant trước 1 ngày, giữ lại agent của mình làm bản demo.
- Tạo sẵn một **Policy Assistant dự phòng** và chia sẻ cho toàn bộ học viên, để ai không tạo được agent vẫn làm tiếp được phần test và Lab 9.
- **Nên đặt Sổ tay trên site SharePoint của workshop** (học viên có quyền đọc) và cho học viên chọn file từ đó làm knowledge. Nếu mỗi người dùng file trên OneDrive cá nhân, khi chia sẻ agent cho người ngồi cạnh, người đó **không nhận được câu trả lời** vì không có quyền đọc file của người tạo.

**Nhịp dẫn:**

| Phần | Thời gian | Speaker nhấn mạnh |
|---|---|---|
| A. Mở Agent Builder | 2 phút | Copilot > Agents > New Agent; màn hình gồm ô mô tả, nút Configure, khung chat thử |
| B. Mô tả bằng 3 prompt | 6 phút | Gửi lần lượt, đợi trả lời xong mới gửi prompt tiếp; không cần lập trình |
| C. Configure | 6 phút | Kiểm tra Instructions; thêm Sổ tay làm knowledge; **bật Only use specified sources**; chỉnh starter prompts |
| D. Test | 6 phút | 4 câu có đáp án và 1 câu ngoài phạm vi (giá vàng); xem agent có dẫn mục không |
| E. Create và chia sẻ | 3 phút | Create > Change sharing settings > **Specific users in your organization** > Save |

**Đáp án Phần D:**

| Câu hỏi | Đáp án đúng |
|---|---|
| Phép năm, 6 năm thâm niên | 15 ngày; chuyển tối đa 5 ngày, dùng trước 31/03 (Mục 2.2) |
| Công tác Đà Nẵng, chuyên viên | Khách sạn tối đa 1,2 triệu/đêm, ăn 250.000 đồng/ngày, quyết toán trong 10 ngày làm việc (Mục 4) |
| Mua phần mềm 650 triệu | 3 báo giá, Giám đốc Tài chính duyệt (Mục 5.1) |
| Tạm ứng 40% | Ngoại lệ: Giám đốc Tài chính duyệt và bảo lãnh tạm ứng ngân hàng (Mục 5.2) |
| Giá vàng | Agent từ chối, ngoài phạm vi |

**Lỗi thường gặp và cách xử lý:**

| Hiện tượng | Nguyên nhân | Xử lý |
|---|---|---|
| Không thấy New Agent | Giao diện mới, hoặc tenant chưa cho tạo agent | Ctrl + F5; nếu vẫn không có, dùng agent dự phòng |
| Agent vẫn trả lời câu giá vàng | Chưa bật Only use specified sources | Bật toggle trong Configure, test lại |
| Phần chỉnh tay trong Instructions bị mất | Gõ thêm prompt mô tả sau khi đã sửa Configure, Agent Builder viết lại | Từ Phần C trở đi chỉ sửa trong Configure |
| Agent không trả lời từ Sổ tay | File vừa tải lên chưa được xử lý xong | Đợi vài phút rồi test lại |
| Người được chia sẻ không nhận câu trả lời | Không có quyền đọc file knowledge | Dùng Sổ tay trên site chung, hoặc chia sẻ file cho người đó |

### 4.2 Lab 9 - Đưa agent vào Teams (7 phút)

Thông điệp: **agent chỉ có giá trị khi đến được nơi mọi người làm việc.** Không dừng ở việc "agent đã được tạo".

**Bài 1 - học viên tự làm (2 phút):** mở Teams > Copilot, chọn Policy Assistant (của mình hoặc bản dự phòng), hỏi một câu; gửi link agent vào nhóm chat.

**Bài 2 - SharePoint agent trong nhóm chat.** Agent tạo bằng Agent Builder hiện **chưa thêm được vào nhóm chat**, nên phần nhóm chat dùng **SharePoint agent**. Không hứa ngày Agent Builder hỗ trợ việc này.

Speaker tạo sẵn agent **Trợ lý Sổ tay** (1 ngày trước):

1. Tạo hoặc chọn site SharePoint của workshop; speaker có quyền chỉnh sửa, học viên có quyền đọc
2. Vào thư viện **Documents**, tải lên Sổ tay Chính sách Nội bộ.docx
3. Chọn file, chọn **Create an agent** (trên thanh lệnh hoặc trong menu ...), đặt tên **Trợ lý Sổ tay**, lưu
4. Thử agent ngay trên SharePoint bằng 2 câu hỏi bên dưới
5. Bấm biểu tượng **Agent** góc trên bên phải site > chọn Trợ lý Sổ tay > **...** > **Copy link for Teams**
6. Tạo sẵn một nhóm chat demo với 2-3 tài khoản, dán link, chọn **Add to this chat**, thử @mention
7. Gửi link site cho học viên trước buổi học

Câu hỏi demo và đáp án:

| Câu hỏi (@Trợ lý Sổ tay ...) | Đáp án |
|---|---|
| Đề xuất ký hợp đồng khung thuê thầu phụ 3,2 tỷ đồng và tạm ứng 45%: cần mấy báo giá, ai duyệt, tạm ứng tối đa bao nhiêu? | 3 báo giá, Tổng Giám đốc duyệt sau Pháp chế (Mục 5.1); tạm ứng tối đa 30%, 45% là ngoại lệ cần Giám đốc Tài chính và bảo lãnh ngân hàng (Mục 5.2) |
| Có được gửi số điện thoại cá nhân, ngày sinh nhân viên cho đơn vị khảo sát không? | Không nên; chỉ chia sẻ dữ liệu tối thiểu, cần nhân viên đồng ý (Mục 7.3) |

Điểm cần nói khi demo:

- Mỗi lần hỏi phải @mention agent; một nhóm chat có thể có nhiều agent.
- Agent trả lời theo **quyền của người hỏi**; nếu có thành viên không có quyền xem tài liệu, người hỏi thấy **View response** và tự quyết định có chia sẻ không.
- Agent không trả lời trong nhóm chat hoặc kênh có khách bên ngoài (guest).

**Ba cấp độ agent (2 phút):**

| Cấp độ | Dùng khi |
|---|---|
| SharePoint agent | Hỏi đáp tri thức của một site, thư viện tài liệu; đưa được vào nhóm chat và kênh Teams |
| Agent Builder | Agent nghiệp vụ đơn giản do người dùng tự tạo trong Microsoft 365 |
| Copilot Studio | Cần tích hợp hệ thống nghiệp vụ, thực hiện hành động, quản trị và phân phối ở quy mô lớn |

Câu nối sang bước tiếp theo (chỉ nói miệng): khi doanh nghiệp muốn đưa agent đến **nhiều người dùng Teams hơn nhóm đang có licence Copilot**, hoặc cần tích hợp hệ thống, đó là lúc cần Copilot Studio và một buổi làm việc kỹ thuật riêng. **Không nêu giá, mô hình tính phí hay ngày phát hành.**

**Nếu SharePoint agent không chạy được:** chuyển sang trình bày bằng ảnh chụp đã chuẩn bị sẵn, vẫn giải thích đủ 3 điểm trên.

## 5. Ghi chú theo từng lab còn lại

| Lab | Bài chính | Chuẩn bị và lưu ý |
|---|---|---|
| 1 - Copilot Chat | "Bạn biết gì về tôi?", dấu "/", bức tranh quý 3 từ Excel và Word | Cần dữ liệu thật trong hộp thư, lịch. Đáp án Bài 3: kế hoạch chưa đề cập lợi nhuận giảm 16,8% (thầu phụ vượt 39%) và 36% doanh thu từ một khách hàng |
| 2 - Word | Bài 1 Track Changes và duyệt thay đổi; Bài 2 tờ trình trên mẫu có sẵn | Word desktop. Đáp án Bài 1: 5 chỗ sai so với kế hoạch (dưới 13%, +45, 32 giờ, quý 3/2027, 64 tỷ) và 3 đề xuất trái Sổ tay (Mục 5.1, 5.2, 7.3). Bài 2: điểm cần chỉ cho khách hàng là Copilot **tự sửa đề xuất sai** của bản nháp (Giám đốc Tài chính → Tổng Giám đốc, không báo giá → 03 báo giá, 45% → 30%) khi điền mẫu |
| 3 - Excel | Xu hướng và điểm bất thường; Interactive canvas; skill làm báo cáo hằng tháng | File mở từ OneDrive. Đáp án: từ tháng 7 lợi nhuận thấp hơn kế hoạch 5, 9, 8 tỷ do chi phí; TP. Hồ Chí Minh bất thường (biên 15%, nghỉ việc 26,3%, NPS 29). Skill: chiếu video, nhấn mạnh tháng 10 chạy lại chỉ bằng một câu |
| 4 - PowerPoint | Bài 1 cập nhật deck có sẵn từ báo cáo Word + Visualize; Bài 2 interactive slide; Bài 3 speaker notes; Bài 4 deck mới từ Word trên mẫu thương hiệu | PowerPoint desktop; học viên tải file mẫu thương hiệu về máy để dùng Browse for Themes. Bài 4 chiếu video |
| 5 - Outlook | Hộp thư thành danh sách việc, tóm tắt chuỗi email, soạn thư trả lời, email từ báo cáo Word | Chỉ làm nếu còn thời gian; ưu tiên bước 5 vì nối tiếp câu chuyện |
| 6 - Teams | 3 câu hỏi trên transcript mẫu; @Copilot trong nhóm chat | Chia nhóm 3-4 người trước khi vào bài. Người gọi @Copilot cần licence. Copilot chưa dùng được trong chat của cuộc họp |
| 7 - Researcher | Đề bài 3 câu hỏi, đính kèm số liệu quý 3 và Kế hoạch 2027 | Chỉ show báo cáo chạy sẵn. Nhấn mạnh: viết báo cáo AI nào cũng làm được, khác biệt là Researcher **đối chiếu với tài liệu nội bộ** (chỉ ra kế hoạch còn thiếu rủi ro khách hàng lớn và thầu phụ) |

Đáp án đầy đủ của mọi lab nằm trong demo-files/README.md của dự án.

## 6. Xử lý sự cố nhanh

| Hiện tượng | Xử lý |
|---|---|
| Không thấy nút Copilot trong ứng dụng | Kiểm tra licence, đăng xuất và đăng nhập lại, dùng tài khoản dự phòng |
| Copilot không thấy file khi gõ "/" | File phải nằm trên OneDrive hoặc SharePoint; file vừa tải lên có thể cần vài phút |
| Copilot trong Excel bị mờ | Mở file từ OneDrive, không mở bản tải về máy |
| Tính năng mới không có trên máy học viên | Chuyển bài đó sang speaker demo |
| Kết quả khác đáp án mẫu | Bình thường: Copilot trả lời khác nhau mỗi lần. Kiểm tra ý chính và con số |

## 7. Kết thúc buổi học

Hỏi 3 câu và ghi lại câu trả lời:

1. Tình huống nào trong buổi hôm nay có giá trị nhất với anh/chị?
2. Phòng ban nào nên thử trước?
3. Dữ liệu hoặc quy trình nào phù hợp để xây agent?

Chốt 1-2 tình huống ưu tiên. Giới thiệu buổi tiếp theo: hướng dẫn build skill chi tiết, và workshop kỹ thuật cho IT về agent, SharePoint agent, Copilot Studio, tích hợp và quản trị. Học viên giữ site lab để tự thực hành phần "Tự thực hành thêm".
