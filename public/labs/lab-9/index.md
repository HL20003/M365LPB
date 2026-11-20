# Lab 9 - Đưa agent vào Teams

## Sau lab này

> [!OUTCOME]
> **Làm được**
>
> - Dùng agent của mình ngay trong Teams, không phải mở trang khác
> - Thêm một **SharePoint agent** vào nhóm chat để cả nhóm cùng @mention và cùng thấy câu trả lời
>
> **Biết được**
>
> - Agent chỉ thật sự có giá trị khi đến được nơi mọi người làm việc: **Teams**
> - Agent trả lời theo quyền truy cập của **người hỏi**
> - Ba cấp độ agent: **SharePoint agent**, **Agent Builder**, **Copilot Studio**, và khi nào dùng cấp độ nào

## Tình huống

> **Anh/chị** - *người muốn đồng nghiệp dùng được agent*
>
> Tạo xong một agent mới là một nửa công việc. Nhân viên không muốn mở thêm một trang web để hỏi về chính sách; họ hỏi nhau ngay trong nhóm chat Teams. Anh/chị đưa agent đến đúng nơi đó: dùng agent trong Teams, và thêm agent tra cứu Sổ tay vào nhóm chat để cả nhóm cùng hỏi.

**Tài liệu demo:** [Sổ tay Chính sách Nội bộ.docx](#file-handbook), nguồn của SharePoint agent **Trợ lý Sổ tay** trên site SharePoint của workshop.

## Thực hành trong buổi học

### Bài tập 1: Dùng agent của mình ngay trong Teams

1. Mở **Teams**, chọn **Copilot** ở thanh bên trái
2. Trong danh sách agent, chọn **Policy Assistant** đã tạo ở Lab 8, hoặc một agent bất kỳ đồng nghiệp đã chia sẻ cho anh/chị. Agent tạo bằng Agent Builder dùng được cả trong Copilot Chat trên web và Copilot trong Teams
3. Đặt một câu hỏi, ví dụ với Policy Assistant:

> **PROMPT:**
>
> Phòng tôi cần mua phần mềm trị giá 650 triệu đồng. Cần mấy báo giá và ai có thẩm quyền phê duyệt?

4. Gửi link agent vào một nhóm chat Teams để đồng nghiệp mở và dùng (lấy link: chọn agent ở thanh điều hướng bên trái Copilot Chat > **...** > **Share**)

**Kết quả mong đợi:** Policy Assistant trả lời ngay trong Teams như trong Copilot Chat: **3 báo giá**, **Giám đốc Tài chính** phê duyệt (Mục 5.1).

### Bài tập 2: Thêm SharePoint agent vào nhóm chat [MỚI]

Với agent tạo trên **SharePoint**, anh/chị thêm thẳng agent vào nhóm chat để **cả nhóm cùng @mention và cùng thấy câu trả lời**. Site SharePoint của workshop có sẵn agent **Trợ lý Sổ tay**, trả lời từ [Sổ tay Chính sách Nội bộ.docx](#file-handbook).

1. Mở site SharePoint của workshop, bấm biểu tượng **Agent** ở góc trên bên phải, chọn agent **Trợ lý Sổ tay**
2. Bấm **...** cạnh tên agent > **Copy link for Teams**
3. Mở một nhóm chat Teams (nếu chưa có, tạo nhóm chat mới với 2-3 người ngồi cạnh), dán link và gửi. Khi Teams hỏi, chọn **Add to this chat**
4. Sau khi agent chào, hỏi bằng cách @mention agent:

> **PROMPT:**
>
> @Trợ lý Sổ tay Phòng tôi đề xuất ký hợp đồng khung thuê thầu phụ 3,2 tỷ đồng và tạm ứng 45% cho nhà thầu. Cần mấy báo giá, ai phê duyệt, và tạm ứng tối đa bao nhiêu?

5. Mỗi thành viên hỏi thêm một câu liên quan tới việc của mình, ví dụ:

> **PROMPT:**
>
> @Trợ lý Sổ tay Mình có được gửi số điện thoại cá nhân và ngày sinh của nhân viên cho đơn vị khảo sát bên ngoài không?

**Kết quả mong đợi:**

- Hợp đồng trên 2 tỷ đồng cần **3 báo giá**, **Tổng Giám đốc** phê duyệt sau khi **Pháp chế** rà soát (Mục 5.1). Tạm ứng tối đa **30%**; vượt mức là ngoại lệ, cần **Giám đốc Tài chính** phê duyệt và **bảo lãnh ngân hàng** (Mục 5.2)
- Không nên gửi số điện thoại cá nhân, ngày sinh; chỉ chia sẻ dữ liệu tối thiểu, nếu cần thêm phải có sự đồng ý của nhân viên (Mục 7.3)

> [!NOTE]
> - Mỗi lần hỏi phải **@mention** agent; một nhóm chat có thể có nhiều agent.
> - Agent trả lời theo quyền của **người hỏi**. Nếu có thành viên không có quyền xem Sổ tay, người hỏi thấy **View response** và tự quyết định có chia sẻ không.
> - Agent không trả lời trong nhóm chat hoặc kênh có khách bên ngoài (guest).
> - Gỡ agent: **...** của nhóm chat > **Manage apps** > **...** cạnh agent > **Remove**.

> [!TIP]
> **Tạo SharePoint agent cho phòng mình:** vào thư viện tài liệu trên site SharePoint của phòng, chọn các file làm nguồn (quy trình, hướng dẫn), chọn **Create an agent** trên thanh lệnh (hoặc trong menu **...**), đặt tên và lưu. Agent chỉ trả lời từ các file đã chọn và tự cập nhật khi file thay đổi.

## Ba cấp độ agent

| | SharePoint agent | Agent Builder | Copilot Studio |
|---|------------------|---------------|----------------|
| **Dùng khi** | Hỏi đáp tri thức của một site, thư viện tài liệu | Agent nghiệp vụ đơn giản trong Microsoft 365: lời dặn, tài liệu nguồn, starter prompts | Cần tích hợp hệ thống nghiệp vụ, thực hiện hành động, quản trị và phân phối ở quy mô lớn |
| **Ai tạo** | Người dùng có quyền chỉnh sửa site | Người dùng, ngay trong Copilot Chat | Nhóm IT hoặc người phát triển |
| **Đưa đến người dùng** | Thêm vào nhóm chat, kênh Teams | Chia sẻ link, dùng trong Copilot Chat và Teams | Teams, Copilot Chat, website và các kênh khác |
| **Trong workshop** | Lab 9 Bài tập 2 | Lab 8, Lab 9 Bài tập 1 | Không thực hành |

## Lưu ý tuân thủ

> [!NOTE]
> Câu trả lời của agent trong nhóm chat **hiển thị cho mọi thành viên**: không hỏi về thông tin Mật hay dữ liệu cá nhân trong nhóm chat đông người. Agent tự tạo chỉ chia sẻ trong nội bộ công ty; tài liệu nguồn phải nằm ở thư mục hoặc site SharePoint có phân quyền đúng.
