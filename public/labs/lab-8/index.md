# Lab 8 - Agent Builder in Copilot Chat

**Ứng dụng:** Microsoft 365 Copilot Chat, Agent Builder

> [!NOTE]
> **Toàn bộ tài liệu, số liệu và tình huống trong workshop là bản nháp (draft) dùng cho mục đích đào tạo.** Tên nhân vật, khách hàng và đối tác là giả định.

---

## Mục tiêu

Sau khi hoàn thành lab này, anh/chị sẽ có thể:

- Tạo một trợ lý AI cho đội ngũ chỉ bằng ngôn ngữ tự nhiên, không cần code
- Cấu hình instructions, knowledge sources và starter prompts cho agent
- Kiểm tra câu trả lời của agent trước khi chia sẻ với đồng nghiệp

---

## Khái niệm cần biết

| Khái niệm | Giải thích |
|-----------|------------|
| **Agent** | Trợ lý AI được tuỳ chỉnh, trả lời câu hỏi dựa trên instructions và knowledge sources đã cấu hình |
| **Instructions** | Phần cấu hình quy định agent làm gì, trả lời theo giọng điệu nào và không được làm gì |
| **Knowledge source** | Tài liệu agent dùng để trả lời (file, thư mục SharePoint, website), giúp câu trả lời chính xác và có nguồn |
| **Starter prompts** | Các câu hỏi gợi ý hiển thị sẵn trên giao diện chat để người dùng bấm vào và bắt đầu |

Agent Builder có hai cách làm việc, lab này dùng lần lượt từng cách:

| Cách | Dùng để | Trong lab |
|------|---------|-----------|
| **Mô tả bằng prompt** (Describe) | Gõ mô tả agent bằng lời rồi nhấn **Send**, làm theo các câu hỏi của Agent Builder; Agent Builder tự điền cấu hình | Phần B |
| **Configure** | Xem và chỉnh trực tiếp từng trường: Name, Description, Instructions, Knowledge, Starter prompts | Phần C |

Khung chat thử nghiệm bên phải màn hình luôn hiển thị để anh/chị thử agent bất cứ lúc nào (Phần D).

---

## Tình huống

> Ở công ty nào cũng vậy, nhân viên liên tục hỏi Phòng Hành chính - Nhân sự, Kế toán và quản lý trực tiếp cùng những câu hỏi: được bao nhiêu ngày phép, công tác phí tối đa bao nhiêu, mua sắm cần mấy báo giá và ai duyệt. Anh/chị tạo **Policy Assistant** - một trợ lý nội bộ giúp mọi nhân viên tự tra cứu nhanh chính sách nghỉ phép, làm việc từ xa, công tác phí, mua sắm và thẩm quyền phê duyệt, đào tạo, bảo mật và phúc lợi. Agent chỉ trả lời dựa trên Sổ tay Chính sách Nội bộ để đảm bảo chính xác.

**Knowledge source:** [Sổ tay Chính sách Nội bộ.docx](#file-handbook) - tải file và lưu vào **OneDrive** của anh/chị trước khi bắt đầu (xem [cách tải file Word/Excel về máy](#module-1/cach-tai-file-word-excel-ve-may)).

**Kết quả cuối lab:** một agent tên **Policy Assistant**, trả lời từ Sổ tay, có dẫn mục, từ chối câu hỏi ngoài phạm vi và có link chia sẻ cho đồng nghiệp.

---

## Phần A: Mở Agent Builder

### Bước 1: Mở Agent Builder

1. Vào [https://m365.cloud.microsoft/](https://m365.cloud.microsoft/) bằng **tài khoản công ty** (không dùng tài khoản Microsoft cá nhân như Outlook.com, Hotmail) và mở **Copilot**
2. Ở thanh điều hướng bên trái, tìm mục **Agents**, chọn **New Agent**
3. Màn hình Agent Builder mở ra: ô mô tả agent ở giữa, nút **Configure** để chỉnh chi tiết, khung chat thử nghiệm ở bên phải

> [!TIP]
> Agent Builder còn cho phép **chọn một template có sẵn** trong danh sách rồi tuỳ chỉnh bằng **Configure**. Lab này tạo agent từ đầu bằng prompt để anh/chị nắm được từng phần cấu hình.

> [!NOTE]
> Microsoft đang triển khai giao diện **Home** mới cho Copilot, nên vị trí nút và tên gọi trên máy anh/chị có thể hơi khác hướng dẫn. Nếu không thấy **New Agent**, nhấn `Ctrl + F5` để tải lại trang.

---

## Phần B: Mô tả agent bằng prompt

Nhập lần lượt **cả 3 prompt** dưới đây vào ô mô tả, mỗi prompt nhấn **Send**. Sau mỗi prompt, đợi Agent Builder trả lời xong rồi mới gửi prompt tiếp theo. Agent Builder có thể hỏi thêm để làm rõ; 3 prompt dưới đây đã trả lời sẵn các câu hỏi thường gặp, nên anh/chị chỉ cần gửi prompt tiếp theo.

### Bước 2: Mô tả mục đích của agent

> **PROMPT:**
>
> Tôi muốn xây dựng một trợ lý nội bộ tên "Policy Assistant" cho toàn bộ nhân viên công ty. Agent giúp nhân viên tra cứu nhanh chính sách nội bộ: thời gian làm việc, nghỉ phép, làm việc từ xa, công tác phí, mua sắm và thẩm quyền phê duyệt, tạm ứng và thanh toán cho nhà cung cấp, đào tạo, bảo mật thông tin và phúc lợi.

### Bước 3: Quy định giọng điệu và cách trình bày

> **PROMPT:**
>
> Giọng điệu thân thiện, rõ ràng, đi thẳng vào vấn đề, dễ hiểu với cả nhân viên mới. Trả lời ngắn gọn, có ví dụ tính cụ thể khi người hỏi nêu thâm niên, chức danh hoặc giá trị mua sắm. Trình bày định mức và cấp phê duyệt dưới dạng bảng khi có thể. Cuối mỗi câu trả lời ghi rõ mục tương ứng trong Sổ tay, ví dụ "(Nguồn: Sổ tay, Mục 4)".

### Bước 4: Định nghĩa giới hạn của agent

> **PROMPT:**
>
> Agent chỉ trả lời dựa trên Sổ tay Chính sách Nội bộ. Nếu Sổ tay không có thông tin, nói rõ là chưa có thông tin và đề nghị người dùng liên hệ đúng đầu mối theo Mục 10 của Sổ tay. Không trả lời câu hỏi ngoài phạm vi chính sách và quy trình nội bộ. Không tự phê duyệt hay cam kết thay cho cấp có thẩm quyền, không tư vấn về trường hợp kỷ luật hay lương thưởng của cá nhân cụ thể. Khi câu hỏi cần phê duyệt ngoại lệ, chỉ ra đúng cấp phê duyệt. Nếu người dùng nhập số CCCD, số tài khoản, mật khẩu hoặc thông tin lương cá nhân, nhắc họ không chia sẻ dữ liệu này trong cuộc trò chuyện.

> [!NOTE]
> Sau 3 prompt, Agent Builder đã tự điền **tên**, **mô tả**, **instructions** và **starter prompts**. Nội dung tự sinh có thể hơi khác nhau giữa các học viên, điều này là bình thường. Phần C sẽ kiểm tra và chỉnh lại.

---

## Phần C: Kiểm tra và hoàn thiện trong Configure

### Bước 5: Kiểm tra Name, Description và Instructions

1. Chọn **Configure**
2. Kiểm tra từng trường:

| Trường | Cần thấy | Nếu chưa đúng |
|--------|----------|---------------|
| **Name** | Policy Assistant | Sửa trực tiếp trong ô Name |
| **Description** | Một câu mô tả agent giúp nhân viên tra cứu chính sách và quy trình nội bộ | Sửa trực tiếp |
| **Instructions** | Có đủ: phạm vi, giọng điệu, dẫn mục Sổ tay, không cam kết thay cấp phê duyệt, không tư vấn về cá nhân cụ thể, nhắc không nhập dữ liệu cá nhân | Bổ sung câu còn thiếu vào cuối ô Instructions |

> [!TIP]
> Từ đây trở đi, nên chỉnh trực tiếp trong **Configure** thay vì quay lại gõ prompt mô tả. Prompt mô tả mới có thể khiến Agent Builder viết lại toàn bộ Instructions và làm mất phần anh/chị đã sửa tay.

### Bước 6: Thêm Sổ tay làm knowledge source

1. Kéo xuống phần **Knowledge**
2. Thêm file [Sổ tay Chính sách Nội bộ.docx](#file-handbook): chọn file đã lưu trên **OneDrive**, hoặc tải file lên trực tiếp
3. Bật toggle **Only use specified sources** để agent chỉ dùng Sổ tay, không dùng kiến thức chung của mô hình hay nội dung web

> [!NOTE]
> Với agent trả lời về chính sách, nên luôn bật **Only use specified sources**: câu trả lời kiểm chứng được và agent không tự "bịa" định mức hay quy trình. Đổi lại, agent sẽ không trả lời được câu hỏi nằm ngoài Sổ tay, và đó chính là hành vi mong muốn.

### Bước 7: Chỉnh starter prompts

Kéo xuống phần **Starter prompts**. Giữ hoặc thay để có các câu hỏi nhân viên hay hỏi nhất, ví dụ:

| Title | Message |
|-------|---------|
| Ngày phép | Tôi làm 6 năm thì được bao nhiêu ngày phép năm? |
| Công tác phí | Đi công tác trong nước thì khách sạn và phụ cấp ăn tối đa bao nhiêu? |
| Thẩm quyền phê duyệt | Mua sắm trị giá bao nhiêu thì cần cấp nào phê duyệt và mấy báo giá? |
| Sử dụng AI | Những thông tin nào không được nhập vào Copilot? |

---

## Phần D: Test agent trước khi tạo

### Bước 8: Thử agent trong khung chat thử nghiệm

Nhập lần lượt các câu hỏi dưới đây vào khung chat thử nghiệm bên phải, nhấn **Send**, và so sánh với cột **Câu trả lời đúng**.

> **PROMPT:**
>
> Tôi đã làm việc tại công ty 6 năm thì có bao nhiêu ngày phép năm? Phép chưa dùng hết có được chuyển sang năm sau không?

> **PROMPT:**
>
> Tôi là chuyên viên, đi công tác Đà Nẵng 3 đêm. Khách sạn và phụ cấp ăn tối đa bao nhiêu, và tôi phải quyết toán trong bao lâu?

> **PROMPT:**
>
> Phòng tôi cần mua phần mềm trị giá 650 triệu đồng. Cần mấy báo giá và ai có thẩm quyền phê duyệt?

> **PROMPT:**
>
> Nhà cung cấp đề nghị tạm ứng 40% giá trị hợp đồng. Có được không, và nếu được thì cần điều kiện gì?

> **PROMPT:**
>
> Giá vàng tuần tới có tăng không? Tôi có nên mua vàng không?

| Câu hỏi | Câu trả lời đúng (theo Sổ tay) |
|---------|--------------------------------|
| Phép năm, 6 năm thâm niên | **15 ngày** (từ 5 đến dưới 10 năm). Phép chưa dùng được chuyển **tối đa 5 ngày**, phải dùng trước **31/03**. Nguồn: Mục 2.2 |
| Công tác Đà Nẵng, chuyên viên | Khách sạn tối đa **1,2 triệu đồng/đêm**, phụ cấp ăn **250.000 đồng/ngày**; quyết toán trong **10 ngày làm việc** sau chuyến đi, kèm hóa đơn hợp lệ. Nguồn: Mục 4 |
| Mua phần mềm 650 triệu | Thuộc mức trên 500 triệu đến 2 tỷ: cần **3 báo giá**, **Giám đốc Tài chính** phê duyệt. Nguồn: Mục 5.1 |
| Tạm ứng 40% | Vượt mức tối đa 30% nên là **ngoại lệ**: cần **Giám đốc Tài chính** phê duyệt và nhà cung cấp có **bảo lãnh tạm ứng của ngân hàng**. Nguồn: Mục 5.2 |
| Giá vàng | Agent **từ chối** vì ngoài phạm vi Sổ tay |

Nếu câu trả lời chưa đạt (không dẫn mục, sai số liệu, vẫn trả lời câu hỏi giá vàng), quay lại **Configure**: kiểm tra toggle **Only use specified sources** đã bật chưa, và bổ sung vào ô **Instructions** quy tắc còn thiếu. Sau đó test lại.

---

## Phần E: Tạo và chia sẻ agent

### Bước 9: Tạo agent và lấy link chia sẻ

1. Khi đã hài lòng với kết quả test, chọn **Create**
2. Khi tạo xong, màn hình hiện liên kết tới agent. Nhấn **Copy** để sao chép liên kết
3. Chọn **Change sharing settings** và chọn phạm vi chia sẻ. Vì agent dùng file trên OneDrive/SharePoint làm knowledge source, nên chọn **Specific users in your organization** và nhập tên đồng nghiệp hoặc nhóm cần dùng
4. Nhấn **Save**
5. Dán liên kết vào email hoặc Teams chat để gửi cho đồng nghiệp
6. Mở agent từ mục **Agents** ở thanh điều hướng bên trái và hỏi lại một câu trong Bước 8

> [!NOTE]
> - Người nhận chỉ dùng được agent, **không sửa được**; chỉ chủ sở hữu agent mới chỉnh sửa được.
> - Agent tôn trọng phân quyền: người không có **quyền đọc** file Sổ tay thì agent không trả lời từ file đó cho người ấy. Trong môi trường thật, nên đặt Sổ tay trong một **thư mục hoặc site SharePoint** do phòng ban phụ trách quản lý và cấp quyền đọc cho đúng nhóm nhân viên; khi tài liệu được cập nhật, agent tự dùng phiên bản mới.

> [!TIP]
> Để chia sẻ lại sau này: chọn **Policy Assistant** ở thanh điều hướng bên trái → **... (More)** → **Share**. Menu **...** này cũng là nơi mở lại agent để chỉnh sửa.

---

## Lưu ý tuân thủ

> [!NOTE]
> - Agent tự tạo chỉ chia sẻ trong nội bộ công ty; knowledge source phải là thư mục SharePoint có phân quyền.
> - Agent phục vụ khách hàng bên ngoài phải được Phòng Công nghệ Thông tin và Pháp chế phê duyệt.
> - Bật **Only use specified sources** với mọi agent trả lời về chính sách, quy trình và định mức.

---

## Tự thực hành: Tạo agent cho công việc của anh/chị

Lặp lại quy trình trên với một chủ đề của riêng anh/chị:

1. **Chủ đề** - Agent hỗ trợ việc gì? (hướng dẫn nhân viên mới, FAQ quy trình của phòng, tra cứu sản phẩm và dịch vụ, hỏi đáp quy trình IT, mẫu văn bản thường dùng...)
2. **Người dùng và giọng điệu** - Dành cho ai? Trang trọng hay thân thiện?
3. **Knowledge sources** - Thư mục hoặc site SharePoint nào làm nguồn? Ai đang có quyền đọc?
4. **Giới hạn** - Agent không được trả lời hoặc cam kết điều gì?
5. **Starter prompts** - 3-4 câu hỏi người dùng hay hỏi nhất
6. **Bộ câu test** - 3 câu có đáp án rõ trong tài liệu và 1 câu ngoài phạm vi để kiểm tra agent có từ chối không

---

## Tổng kết

| Anh/chị đã làm được | Ở bước |
|---------------------|--------|
| Mô tả agent bằng ngôn ngữ tự nhiên, không cần code | Mô tả bằng prompt (Bước 2-4) |
| Kiểm tra và chỉnh Name, Description, Instructions | Configure (Bước 5) |
| Gắn Sổ tay làm knowledge source, giới hạn agent chỉ dùng nguồn này | Configure (Bước 6) |
| Thiết kế starter prompts | Configure (Bước 7) |
| Test bằng bộ câu hỏi có đáp án, kể cả câu ngoài phạm vi | Khung chat thử nghiệm (Bước 8) |
| Tạo agent và chia sẻ link cho đồng nghiệp | Create (Bước 9) |
