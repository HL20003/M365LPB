# Hướng dẫn speaker - Copilot Overview Workshop

Bản general v2, cập nhật 25/11/2026. Tài liệu nội bộ cho người trình bày và trợ giảng, không gửi cho học viên.

## 1. Buổi workshop này là gì

Đây là buổi **giới thiệu 120 phút**, không phải khóa đào tạo đủ tính năng. Mục tiêu là để khách hàng thấy giá trị của Microsoft 365 Copilot trong công việc của họ, tự tay tạo được một agent, và muốn đi tiếp (thử nghiệm, mở rộng licence, xây agent, workshop kỹ thuật).

- Site lab có 7 lab. **Không cố làm hết**: trong buổi chỉ làm phần "Thực hành trong buổi học"; phần "Tự thực hành thêm" để học viên tự làm sau.
- Lab 1-4 cùng **một câu chuyện** (chuẩn bị báo cáo quý 3 và Kế hoạch 2027) để speaker kể liền mạch Chat → Word → Excel → PowerPoint. Nhưng mỗi lab bắt đầu từ file demo có sẵn, nên học viên làm lab nào trước cũng được.
- Mỗi lab Office có ít nhất một bước **tạo file mới từ file nguồn**: báo cáo Word → tờ trình Word, file Excel thô → sheet báo cáo, bộ slide → slide tóm tắt điều hành (skill), báo cáo Word → email. Đây là cách minh họa điểm 3 "luồng công việc liên tục".
- Bài có nhãn "Tính năng mới" dùng tính năng Microsoft mới phát hành hoặc đang triển khai dần: phải chạy thử trên tenant trước (mục 3.3 và 3.4).

### 5 điểm khách hàng phải nhớ

1. **Copilot hiểu ngữ cảnh công việc**: làm việc với email, cuộc họp, con người, tài liệu mà người dùng có quyền truy cập, ngay từ ngày đầu nhờ Work IQ. Không cần "dạy" AI nhiều năm.
2. **Dấu "/" là thao tác lặp lại** trong mọi demo: gọi người, file, email, cuộc họp làm nguồn.
3. **Microsoft 365 là một luồng công việc liên tục**: không chép nội dung sang công cụ AI bên ngoài rồi chép kết quả trở lại.
4. **Teams là trọng tâm**: cuộc họp, chat, cộng tác và là nơi đưa agent đến nhiều người dùng.
5. **Người dùng tự tạo được tài sản AI**: agent, skill chuẩn hóa một quy trình nhiều bước thay vì viết lại prompt.

### Nên tránh

- Đi lần lượt toàn bộ tính năng Word, Excel, PowerPoint, Outlook; giảng kỹ thuật viết prompt cơ bản quá lâu.
- Tạo PowerPoint từ trang trắng. Lab 4 chỉ **chỉnh deck có sẵn**.
- Demo việc AI nào cũng làm được (viết một đoạn văn, vẽ biểu đồ đơn giản). Vì vậy "viết tóm tắt điều hành" chỉ còn trong Prompt đề xuất của Lab 2.
- Cam kết về mô hình, giá, quyền sử dụng hay ngày phát hành khi chưa có thông tin chính thức.
- Dừng agent ở chỗ "đã tạo xong". Luôn kết thúc bằng chia sẻ và đưa agent vào Teams (Lab 7 Bài 4), rồi demo SharePoint agent trong nhóm chat.
- Giới thiệu Analyst.

## 2. Agenda 120 phút và việc của speaker

| Thời gian | Phần | Lab | Speaker làm | Học viên làm |
|---|---|---|---|---|
| 00-10 | Khởi động và định hướng | Module 1 | Hỏi nhanh: "Anh/chị mất nhiều thời gian nhất ở email, cuộc họp, báo cáo hay tìm tài liệu?". Nêu 5 điểm cần nhớ, nhấn mạnh Copilot tôn trọng quyền truy cập | Mở site, tải file demo lên OneDrive |
| 10-20 | Copilot, Work IQ, bảo mật dữ liệu | Lab 1 Bài 1-2 | Demo "Bạn biết gì về tôi và công việc của tôi?" và dấu "/" gọi người, cuộc họp | Làm Bài 1 trên tài khoản của mình |
| 20-50 | Từ dữ liệu công việc đến kết quả hoàn chỉnh | Lab 1 Bài 3, Lab 2, 3, 4 (Lab 5 nếu còn giờ) | Kể một câu chuyện qua 4 ứng dụng, xem mục 2.1. Demo trực tiếp bài ngắn, chiếu video bài dài. Skills chỉ demo, hẹn buổi 2 hướng dẫn build | Làm theo bài demo trực tiếp; bài có video để tự làm sau |
| 50-70 | Teams: từ cuộc họp đến hành động | Lab 6 | Demo 3 câu hỏi trên transcript mẫu; chia nhóm 3-4 người cho bài @Copilot | Bài 1 (transcript), Bài 2 (nhóm chat) |
| 70-105 | Hands-on: Policy Assistant | Lab 7 Bài 1-3 | Dẫn từng bài, đi vòng hỗ trợ; có thêm 10 phút (trước đây dành cho Researcher) để giúp người làm chậm và cho cả lớp test kỹ | Tự tạo, hoàn thiện và test agent |
| 105-112 | Đưa agent vào Teams, 3 cấp độ | Lab 7 Bài 4 + speaker demo | Hướng dẫn chia sẻ và mở agent trong Teams; **speaker demo SharePoint agent** trong nhóm chat; giải thích 3 cấp độ | Bài 4: chia sẻ agent, dùng trong Teams; xem demo |
| 112-120 | Tổng kết, chốt bước tiếp theo | Tổng kết | Hỏi 3 câu, chốt 1-2 tình huống ưu tiên, giới thiệu buổi tiếp theo | Trả lời, góp ý |

### 2.1 Phút 20-50: một câu chuyện qua 4 ứng dụng

Câu chuyện: *"Quý 3 vừa xong, doanh thu gần đạt nhưng lợi nhuận giảm. Anh/chị phải chuẩn bị báo cáo và tờ trình cho Ban Giám đốc, rồi cập nhật slide họp toàn công ty."* Mỗi bước đều chỉ ra: file nào đi vào, file nào được tạo ra, và dấu "/" ở đâu.

| Phút | Ứng dụng | Demo trực tiếp | Chiếu video | File vào → file ra | Câu chuyển sang bước sau |
|---|---|---|---|---|---|
| 20-25 | Copilot Chat | Lab 1 Bài 3 | | Excel + Kế hoạch Word → bảng vấn đề | "Copilot đã chỉ ra vấn đề. Giờ đưa vào bản báo cáo đồng nghiệp đã soạn sẵn." |
| 25-32 | Word | Lab 2 Bài 1: tờ trình trên mẫu (bài cộng tác, mở đầu phần Word); Bài 2: Track Changes, mở 2-3 comment, Accept/Reject | Bài nào lỗi khi chạy thử thì chiếu video bài đó | Báo cáo + Sổ tay → **tờ trình mới**; báo cáo nháp → báo cáo có vết sửa | "Ban Giám đốc sẽ hỏi: lợi nhuận giảm từ khi nào, ở đâu?" |
| 32-40 | Excel | Lab 3 Bài 1 (xu hướng, bất thường); Bài 3 Interactive canvas nếu tenant có | Lab 3 Bài 2: tạo và chạy skill (hẹn buổi 2 build chi tiết) | Excel thô → **sheet báo cáo mới**; Excel → dashboard | "Có kết luận rồi, giờ cập nhật slide họp toàn công ty, không làm lại từ đầu." |
| 40-48 | PowerPoint | Lab 4 Bài 1 (áp brand của công ty bằng Select brand) | Lab 4 Bài 2: thêm skill slide tóm tắt điều hành và chạy @slide-tom-tat-dieu-hanh (hẹn buổi 2 viết skill riêng) | Deck → **slide tóm tắt điều hành** theo quy chuẩn | "Cuối cùng gửi cho Ban Giám đốc, cũng từ chính báo cáo đó." |
| 48-50 | Outlook | Lab 5 bước 5: email từ báo cáo Word (nếu còn giờ) | | Báo cáo Word → **email** | Sang Teams: "Báo cáo đã xong, giờ đến cuộc họp giao ban." |

- Video do team tự quay. Khi có link (Stream, SharePoint hoặc YouTube), điền vào `demoVideos` trong `public/js/app.js`; nút **Xem video demo** chỉ hiện ở bài có link.
- Trong lúc chiếu video, nói rõ học viên **có đủ bước trên site** để tự làm sau buổi học.
- Nếu một bài demo trực tiếp lỗi, chuyển ngay sang video của bài đó, không sửa lỗi trước mặt khách hàng.

## 3. Chuẩn bị trước buổi học (checklist)

### 3.1 Tài khoản, licence, quyền

- Mỗi học viên có **tài khoản công ty** với licence **Microsoft 365 Copilot**. Licence này cần cho Copilot trong Word, Excel, PowerPoint, Outlook, Teams, @Copilot trong nhóm chat, agent trong Teams và Skills.
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
| Báo cáo Kết quả Kinh doanh Q3 2026.xlsx | Lab 1, Lab 3 |
| Kế hoạch Hoạt động 2027 (dự thảo).docx | Lab 1, Lab 2, Lab 4 |
| Báo cáo quản lý Q3 2026 (bản nháp).docx | Lab 2, Lab 5 |
| Mẫu tờ trình (giả định).docx | Lab 2 Bài 1 |
| Sổ tay Chính sách Nội bộ.docx | Lab 2, Lab 7, demo SharePoint agent |
| Town hall Q3 2026 (bản nháp).pptx | Lab 4 |
| Mẫu thương hiệu (giả định).pptx | Lab 4 Bài 1: template để tạo Brand Kit Công ty giả định |
| Skill PowerPoint .zip (slide-tom-tat-dieu-hanh) | Lab 4 Bài 2 (dự phòng) |
| Transcript họp giao ban quý 3 (mẫu).docx | Lab 6 |
| Phản hồi khách hàng T9-T10 2026.xlsx, Skill Excel .zip | Lab 3 Bài 2 |
| Skill Copilot Chat .zip | Lab 7 (tự thực hành) |

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
| Word (Lab 2) | Bài 1 trên bản sao Mẫu tờ trình, gõ "/" chọn báo cáo và Sổ tay; Bài 2 trên Báo cáo quản lý Q3 (bản nháp), gõ "/" chọn Kế hoạch 2027 và Sổ tay | Bài 1: giữ bố cục 5 mục của mẫu, Kính gửi Tổng Giám đốc, 03 báo giá, tạm ứng tối đa 30%, chỗ thiếu ghi [CẦN XÁC NHẬN]. Bài 2: đủ 8 chỗ sửa có vết sửa và comment ghi nguồn, Accept/Reject được | Không có vết sửa: bật tay Review > Track Changes rồi chạy lại prompt. Bài 1 Copilot chỉ trả lời trong khung chat: nhập "Cập nhật trực tiếp vào tài liệu"; vẫn không được thì chiếu video. Sau khi chạy thử, **tải lại bản nháp và mẫu gốc** |
| Excel (Lab 3) | Bài 1 trên Báo cáo Kết quả Kinh doanh Q3 và câu hỏi tiếp; Bài 2 @skill-builder trên file Phản hồi khách hàng, chạy skill cho T9 rồi T10; Bài 3 @interactive-canvas | Bài 1 nêu đúng lợi nhuận lệch 5, 9, 8 tỷ từ tháng 7 và TP. Hồ Chí Minh bất thường, có tên sheet. Bài 2: T9 còn 120 phản hồi, T10 còn 134, có sheet sạch và sheet báo cáo mới | Nút Copilot mờ: mở file từ OneDrive. @skill-builder không có: dùng file Skill Excel .zip (Manage plugins & skills > Custom skills). Xóa skill đã tạo khi chạy thử để buổi demo tạo lại từ đầu |
| PowerPoint (Lab 4) | Bài 1: trong khung Copilot bấm + > Select brand, chọn Brand Kit **Công ty giả định**, nhập prompt định dạng lại theo brand (chọn brand xong deck chưa đổi). Bài 2: + > Choose skills > Manage skills > Add skill, dán SKILL.md, rồi gõ @slide-tom-tat-dieu-hanh | Bài 1: cả deck đổi màu, font, chân trang theo brand; nội dung và số liệu giữ nguyên. Bài 2: skill hiện trong Choose skills; slide tóm tắt nằm sau bìa, đủ 3 khối Kết quả / Vấn đề / Hướng xử lý và dòng "Cần Ban Giám đốc quyết định", có bảng nguồn trong khung chat | Không thấy Brand Kit trong Select brand: Brand Kit chưa publish hoặc chưa chia sẻ quyền Viewer; học viên tự tạo theo phần Tạo Brand Kit trong Bài 1 (office.com/create/brandkit, tải file Mẫu thương hiệu lên Templates, Publish). Không có nút Create Brand Kit: trình diễn trên máy chiếu. Copilot không sửa được cả deck một lần: sửa từng slide. Không thấy Manage skills hoặc Add skill: dùng file Skill PowerPoint .zip qua ... > Manage skills > Custom skills > Create OneDrive folder; vẫn không được thì chiếu video. Xóa skill đã thêm khi chạy thử. Giữ lại **bản deck gốc** cho buổi học |
| Outlook (Lab 5) | Phân 3 nhóm email; Summary by Copilot một chuỗi email dài; Draft with Copilot; Coaching by Copilot; email mới gõ "/" chọn báo cáo Word | Có ít nhất 10 email trong 3 ngày gần nhất và 1 chuỗi email nhiều người; thư nháp bám đúng chuỗi email; email từ báo cáo có 432 tỷ, 84 tỷ, 39%, 20% | Hộp thư trống: gửi trước vài email và một chuỗi trả lời qua lại giữa các tài khoản |
| Teams (Lab 6) | Gõ "/" chọn transcript mẫu trong Copilot Chat, hỏi 3 câu và lập biên bản; nếu dùng cuộc họp thật: họp thử có bật Recording và Transcript | Trả lời đúng phần bỏ lỡ, việc của Phòng Kế hoạch (08/12, 10/12), 2 điểm chưa thống nhất; tab Recap xuất hiện sau cuộc họp thử | Không có Recap: kiểm tra đã bật Transcript và tài khoản có tham dự; Recap có thể mất vài phút mới hiện. Dùng transcript mẫu thay cho cuộc họp thật |

### 3.4 Chạy thử các tính năng mới

Tính năng nào chưa có trên tenant thì chuyển bài đó sang **speaker demo trên máy chiếu**, không để học viên làm.

| Tính năng | Lab | Kiểm tra |
|---|---|---|
| Nút Work IQ | 1 | Thấy nút Work IQ góc trên bên trái Copilot Chat |
| Copilot bật Track Changes, thêm comment | 2 | Prompt Bài 2 tạo được vết sửa và comment trong Word desktop |
| Interactive canvas | 3 | Gõ @interactive-canvas trong Copilot của Excel tạo được dashboard |
| Skills trong Excel | 3 | Gõ @skill-builder tạo và lưu được skill; thấy **Manage plugins & skills** > **Custom skills** |
| Skills trong PowerPoint | 4 | Thấy **+** > **Choose skills**, có **Manage skills** > **Add skill**; skill tự thêm gọi được bằng @tên-skill |
| @Copilot trong nhóm chat | 6 | Thêm được Copilot vào nhóm chat bằng **Add agents and bots** |
| Agent Builder | 8 | Thấy **New Agent**, tạo và chia sẻ được agent |
| Agent trong Teams | 8 | Agent tạo bằng Agent Builder hiện trong Teams > Copilot |
| SharePoint agent | Demo | Xem mục 4.2 |

## 4. Phần agent (Lab 7 và demo SharePoint agent)

Đây là phần học viên nhớ nhất: họ **tự tạo** được một agent và thấy agent **đến được Teams**. Cần chuẩn bị kỹ nhất.

### 4.1 Lab 7 - Policy Assistant và đưa vào Teams (hands-on, khoảng 40 phút)

**Chuẩn bị:**

- Speaker tự làm hết Lab 7 trên tenant trước 1 ngày, giữ lại agent của mình làm bản demo.
- Tạo sẵn một **Policy Assistant dự phòng** và chia sẻ cho toàn bộ học viên, để ai không tạo được agent vẫn làm tiếp được phần test và Bài 4.
- **Nên đặt Sổ tay trên site SharePoint của workshop** (học viên có quyền đọc) và cho học viên chọn file từ đó làm knowledge. Nếu mỗi người dùng file trên OneDrive cá nhân, khi chia sẻ agent cho người ngồi cạnh, người đó **không nhận được câu trả lời** vì không có quyền đọc file của người tạo.

**Nhịp dẫn:**

| Bài | Thời gian | Speaker nhấn mạnh |
|---|---|---|
| 1. Mô tả agent bằng lời | 7 phút | Copilot > Agents > New Agent; gửi 2 prompt, đợi trả lời xong mới gửi prompt tiếp; không cần lập trình |
| 2. Configure | 6 phút | Kiểm tra Instructions; thêm Sổ tay làm knowledge; **bật Only use specified sources**; chỉnh starter prompts |
| 3. Test | 6 phút | 3 câu có đáp án và 1 câu ngoài phạm vi (giá vàng); xem agent có dẫn mục không |
| 4. Chia sẻ và dùng trong Teams | 6 phút | Create > Change sharing settings > **Specific users in your organization** > Save; mở Teams > Copilot > Policy Assistant; mở agent đồng nghiệp chia sẻ |

**Đáp án Bài 3 và Bài 4:**

| Câu hỏi | Đáp án đúng |
|---|---|
| Phép năm, 6 năm thâm niên | 15 ngày; chuyển tối đa 5 ngày, dùng trước 31/03 (Mục 2.2) |
| Công tác Đà Nẵng, chuyên viên | Khách sạn tối đa 1,2 triệu/đêm, ăn 250.000 đồng/ngày, quyết toán trong 10 ngày làm việc (Mục 4) |
| Mua phần mềm 650 triệu | 3 báo giá, Giám đốc Tài chính duyệt (Mục 5.1) |
| Tạm ứng 40% (Bài 4, hỏi trong Teams) | Ngoại lệ: Giám đốc Tài chính duyệt và bảo lãnh tạm ứng ngân hàng (Mục 5.2) |
| Giá vàng | Agent từ chối, ngoài phạm vi |

**Lỗi thường gặp và cách xử lý:**

| Hiện tượng | Nguyên nhân | Xử lý |
|---|---|---|
| Không thấy New Agent | Giao diện mới, hoặc tenant chưa cho tạo agent | Ctrl + F5; nếu vẫn không có, dùng agent dự phòng |
| Agent vẫn trả lời câu giá vàng | Chưa bật Only use specified sources | Bật toggle trong Configure, test lại |
| Phần chỉnh tay trong Instructions bị mất | Gõ thêm prompt mô tả sau khi đã sửa Configure, Agent Builder viết lại | Từ Bài 2 trở đi chỉ sửa trong Configure |
| Agent không trả lời từ Sổ tay | File vừa tải lên chưa được xử lý xong | Đợi vài phút rồi test lại |
| Người được chia sẻ không nhận câu trả lời | Không có quyền đọc file knowledge | Dùng Sổ tay trên site chung, hoặc chia sẻ file cho người đó |
| Không thấy Policy Assistant trong Teams | Agent vừa tạo, Teams chưa tải lại | Thoát và mở lại Teams; hoặc mở agent bằng link chia sẻ |

### 4.2 Demo SharePoint agent (speaker, khoảng 7 phút)

SharePoint agent **không còn là bài tập** trên site: speaker demo trên máy chiếu ngay sau Lab 7 Bài 4. Chi tiết chuẩn bị, kịch bản, lời dẫn, đáp án và xử lý sự cố nằm trong file **speaker/Hướng dẫn trình bày SharePoint agent.docx**.

- Thông điệp: agent phải đến được nơi mọi người làm việc; SharePoint agent vào thẳng nhóm chat, cả nhóm cùng @mention và cùng thấy câu trả lời; agent trả lời theo quyền của người hỏi.
- Lý do demo SharePoint agent: agent tạo bằng Agent Builder hiện **chưa thêm được vào nhóm chat**. Không hứa ngày Agent Builder hỗ trợ việc này.
- Chuẩn bị trước 1 ngày: agent **Trợ lý Sổ tay** trên site SharePoint của workshop, nhóm chat demo 2-3 tài khoản nội bộ, ảnh chụp dự phòng.
- Kết thúc bằng bảng **Ba cấp độ agent** (cuối Lab 7 trên site) và câu nối sang Copilot Studio. **Không nêu giá, mô hình tính phí hay ngày phát hành.**

## 5. Ghi chú theo từng lab còn lại

| Lab | Bài chính | Chuẩn bị và lưu ý |
|---|---|---|
| 1 - Copilot Chat | "Bạn biết gì về tôi?", dấu "/", bức tranh quý 3 từ Excel và Word | Cần dữ liệu thật trong hộp thư, lịch. Đáp án Bài 3: kế hoạch chưa đề cập lợi nhuận giảm 16,8% (thầu phụ vượt 39%) và 36% doanh thu từ một khách hàng |
| 2 - Word | Bài 1 tờ trình trên mẫu có sẵn; Bài 2 Track Changes và duyệt thay đổi | Word desktop. Đáp án Bài 2: 5 chỗ sai so với kế hoạch (dưới 13%, +45, 32 giờ, quý 3/2027, 64 tỷ) và 3 đề xuất trái Sổ tay (Mục 5.1, 5.2, 7.3). Bài 1: điểm cần chỉ cho khách hàng là Copilot **tự sửa đề xuất sai** của bản nháp (Giám đốc Tài chính → Tổng Giám đốc, không báo giá → 03 báo giá, 45% → 30%) khi điền mẫu |
| 3 - Excel | Xu hướng và điểm bất thường; skill làm báo cáo hằng tháng; Interactive canvas | File mở từ OneDrive. Đáp án: từ tháng 7 lợi nhuận thấp hơn kế hoạch 5, 9, 8 tỷ do chi phí; TP. Hồ Chí Minh bất thường (biên 15%, nghỉ việc 26,3%, NPS 29). Skill: chiếu video, nhấn mạnh tháng 10 chạy lại chỉ bằng một câu |
| 4 - PowerPoint | Bài 1 cập nhật deck có sẵn theo mẫu thương hiệu; Bài 2 skill slide tóm tắt điều hành | PowerPoint desktop; brand chọn bằng + > Select brand (Brand Kit trainer đã tạo từ file Mẫu thương hiệu, học viên không cần tải file này). Bài 2: nhấn mạnh skill là **quy chuẩn của đơn vị**, viết một lần, ai cũng gọi được; skill tự thêm chỉ người thêm thấy, muốn dùng chung thì quản trị viên triển khai skill cho tổ chức. |
| 5 - Outlook | Hộp thư thành danh sách việc, tóm tắt chuỗi email, soạn thư trả lời, email từ báo cáo Word | Chỉ làm nếu còn thời gian; ưu tiên bước 5 vì nối tiếp câu chuyện |
| 6 - Teams | 3 câu hỏi trên transcript mẫu; @Copilot trong nhóm chat | Chia nhóm 3-4 người trước khi vào bài. Người gọi @Copilot cần licence. Copilot chưa dùng được trong chat của cuộc họp |

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
