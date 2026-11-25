# Lab 7 - Agent Builder: tạo agent và đưa vào Teams

## Sau lab này

> [!OUTCOME]
> **Làm được**
>
> - Tự tạo agent **Policy Assistant** chỉ bằng tiếng Việt, không cần lập trình
> - Kiểm tra agent bằng bộ câu hỏi có đáp án, kể cả câu ngoài phạm vi, trước khi chia sẻ
> - Chia sẻ agent cho đồng nghiệp và dùng agent ngay trong **Teams**
>
> **Biết được**
>
> - Agent chuẩn hóa cách trả lời từ tài liệu nội bộ có kiểm soát, thay vì mỗi người tự viết prompt
> - Agent tôn trọng phân quyền: người hỏi chỉ nhận được nội dung từ tài liệu họ có quyền xem
> - Agent chỉ thật sự có giá trị khi đến được nơi mọi người làm việc: **Teams**

## Tình huống

> Nhân viên liên tục hỏi Phòng Hành chính - Nhân sự, Kế toán và quản lý trực tiếp cùng những câu hỏi: được bao nhiêu ngày phép, công tác phí tối đa bao nhiêu, mua sắm cần mấy báo giá và ai duyệt. Anh/chị tạo **Policy Assistant**, trợ lý giúp mọi nhân viên tự tra cứu chính sách, chỉ trả lời dựa trên Sổ tay Chính sách Nội bộ, rồi đưa trợ lý này vào Teams cho đồng nghiệp dùng.

**Tài liệu nguồn:** [Sổ tay Chính sách Nội bộ.docx](#file-handbook). Dùng file trên **site SharePoint của workshop** nếu người hướng dẫn đã chia sẻ, hoặc tải lên **OneDrive** của anh/chị trước khi bắt đầu.

| Khái niệm | Nghĩa |
|-----------|-------|
| **Instructions** | Lời dặn cho agent: làm gì, giọng điệu nào, không được làm gì |
| **Knowledge** | Tài liệu agent dùng để trả lời, giúp câu trả lời chính xác và có nguồn |
| **Starter prompts** | Câu hỏi gợi ý hiện sẵn để người dùng bấm vào |
| **Describe / Configure** | Hai cách làm việc trong Agent Builder: mô tả bằng lời để Agent Builder tự điền, hoặc chỉnh trực tiếp từng trường |

## Thực hành trong buổi học

### Bài tập 1: Mô tả agent bằng lời

1. Vào [https://m365.cloud.microsoft/](https://m365.cloud.microsoft/) bằng **tài khoản công ty**, mở **Copilot**
2. Ở thanh bên trái, chọn **Agents** > **New Agent**. Màn hình Agent Builder có ô mô tả ở giữa, nút **Configure** và khung chat thử bên phải
3. Gửi lần lượt 2 prompt dưới đây, đợi Agent Builder trả lời xong mới gửi prompt tiếp theo:

> **PROMPT:**
>
> Tạo trợ lý nội bộ tên "Policy Assistant" cho toàn bộ nhân viên, giúp tra cứu nhanh chính sách nội bộ: thời gian làm việc, nghỉ phép, làm việc từ xa, công tác phí, mua sắm và thẩm quyền phê duyệt, tạm ứng, đào tạo, bảo mật thông tin và phúc lợi. Giọng điệu thân thiện, ngắn gọn, dễ hiểu với cả nhân viên mới. Trình bày định mức và cấp phê duyệt dạng bảng khi có thể, có ví dụ tính cụ thể khi người hỏi nêu thâm niên, chức danh hoặc giá trị. Cuối mỗi câu trả lời ghi mục tương ứng, ví dụ "(Nguồn: Sổ tay, Mục 4)".

> **PROMPT:**
>
> Giới hạn: chỉ trả lời dựa trên Sổ tay Chính sách Nội bộ; nếu Sổ tay không có thông tin, nói rõ và đề nghị liên hệ đầu mối theo Mục 10. Không trả lời câu hỏi ngoài chính sách nội bộ. Không tự phê duyệt hay cam kết thay cấp có thẩm quyền, không tư vấn kỷ luật hay lương thưởng của cá nhân cụ thể; khi cần ngoại lệ, chỉ ra đúng cấp phê duyệt. Nếu người dùng nhập số CCCD, số tài khoản, mật khẩu hoặc lương cá nhân, nhắc họ không chia sẻ dữ liệu này.

**Kết quả mong đợi:** Agent Builder tự điền **Name**, **Description**, **Instructions** và **Starter prompts**. Nội dung tự sinh có thể hơi khác giữa các học viên, điều này là bình thường.

> [!NOTE]
> Không thấy **New Agent**? Nhấn `Ctrl + F5` để tải lại trang. Giao diện Copilot đang được cập nhật nên vị trí nút có thể hơi khác hướng dẫn.

### Bài tập 2: Hoàn thiện trong Configure

1. Chọn **Configure** và kiểm tra:

| Trường | Cần thấy |
|--------|----------|
| **Name** | Policy Assistant |
| **Description** | Một câu: agent giúp nhân viên tra cứu chính sách và quy trình nội bộ |
| **Instructions** | Đủ phạm vi, giọng điệu, dẫn mục Sổ tay, không cam kết thay cấp phê duyệt, nhắc không nhập dữ liệu cá nhân. Thiếu câu nào thì gõ thêm vào cuối ô |

2. Ở **Knowledge**, thêm [Sổ tay Chính sách Nội bộ.docx](#file-handbook) (chọn từ SharePoint hoặc OneDrive)
3. Bật **Only use specified sources** để agent chỉ dùng Sổ tay, không dùng kiến thức chung hay nội dung web
4. Ở **Starter prompts**, giữ hoặc sửa để có 3-4 câu hay hỏi nhất, ví dụ *"Tôi làm 6 năm thì được bao nhiêu ngày phép?"*, *"Mua sắm bao nhiêu tiền thì cần ai duyệt?"*

> [!TIP]
> Từ bước này, chỉ chỉnh trong **Configure**. Gõ thêm prompt mô tả có thể khiến Agent Builder viết lại toàn bộ Instructions và mất phần anh/chị đã sửa.

### Bài tập 3: Test agent trước khi tạo

Trong khung chat thử bên phải, hỏi lần lượt 4 câu và so với đáp án:

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
> Giá vàng tuần tới có tăng không? Tôi có nên mua vàng không?

**Kết quả mong đợi:**

| Câu hỏi | Câu trả lời đúng |
|---------|------------------|
| Phép năm, 6 năm | **15 ngày**; chuyển sang năm sau **tối đa 5 ngày**, dùng trước **31/03** (Mục 2.2) |
| Công tác Đà Nẵng | Khách sạn tối đa **1,2 triệu đồng/đêm**, ăn **250.000 đồng/ngày**, quyết toán trong **10 ngày làm việc** (Mục 4) |
| Mua phần mềm 650 triệu | **3 báo giá**, **Giám đốc Tài chính** phê duyệt (Mục 5.1) |
| Giá vàng | Agent **từ chối** vì ngoài phạm vi Sổ tay |

Câu trả lời chưa đạt (không dẫn mục, sai số liệu, vẫn trả lời câu giá vàng)? Vào **Configure**, kiểm tra **Only use specified sources** đã bật chưa, bổ sung quy tắc còn thiếu vào **Instructions**, rồi test lại.

### Bài tập 4: Tạo, chia sẻ và dùng agent trong Teams

**Tạo và chia sẻ:**

1. Chọn **Create**. Khi tạo xong, nhấn **Copy** để sao chép link agent
2. Chọn **Change sharing settings** > **Specific users in your organization**, nhập tên 1-2 đồng nghiệp ngồi cạnh, nhấn **Save**
3. Gửi link agent cho các đồng nghiệp đó trong một nhóm chat **Teams**

**Dùng agent trong Teams:**

4. Mở **Teams**, chọn **Copilot** ở thanh bên trái, chọn **Policy Assistant** trong danh sách agent
5. Hỏi một câu:

> **PROMPT:**
>
> Nhà cung cấp đề nghị tạm ứng 40% giá trị hợp đồng. Có được không, và nếu được thì cần điều kiện gì?

6. Mở link agent đồng nghiệp gửi cho anh/chị và hỏi thử một câu

**Kết quả mong đợi:** Policy Assistant trả lời ngay trong Teams như trong Copilot Chat: tạm ứng 40% vượt mức tối đa 30% nên là **ngoại lệ**, cần **Giám đốc Tài chính** phê duyệt và **bảo lãnh tạm ứng của ngân hàng** (Mục 5.2). Agent đồng nghiệp chia sẻ cũng dùng được trong Teams.

> [!NOTE]
> - Người được chia sẻ chỉ **dùng** agent, không sửa được. Muốn chia sẻ lại hoặc chỉnh sửa: chọn agent ở thanh bên trái Copilot > **...** > **Share** hoặc **Edit**.
> - Agent trả lời theo quyền của **người hỏi**. Nếu Sổ tay nằm trên OneDrive cá nhân của anh/chị, đồng nghiệp không có quyền đọc file sẽ **không nhận được câu trả lời**. Với agent dùng thật, đặt tài liệu nguồn trên **site SharePoint** do phòng ban quản lý và cấp quyền đọc cho đúng nhóm; khi tài liệu cập nhật, agent tự dùng bản mới.

## Ba cấp độ agent

| | SharePoint agent | Agent Builder | Copilot Studio |
|---|------------------|---------------|----------------|
| **Dùng khi** | Hỏi đáp tài liệu của một site, thư viện | Agent nghiệp vụ đơn giản: lời dặn, tài liệu nguồn, câu hỏi gợi ý | Tích hợp hệ thống nghiệp vụ, thực hiện hành động, quản trị và phân phối quy mô lớn |
| **Ai tạo** | Người có quyền chỉnh sửa site | Người dùng, ngay trong Copilot Chat | Nhóm IT hoặc người phát triển |
| **Đưa đến người dùng** | Thêm vào nhóm chat, kênh Teams | Chia sẻ link, dùng trong Copilot Chat và Teams | Teams, Copilot Chat, website và các kênh khác |

## Lưu ý tuân thủ

> [!NOTE]
> - Agent tự tạo chỉ chia sẻ trong nội bộ công ty; tài liệu nguồn phải nằm ở thư mục hoặc site SharePoint có phân quyền đúng.
> - Bật **Only use specified sources** với mọi agent trả lời về chính sách, quy trình và định mức.
> - Agent phục vụ khách hàng bên ngoài phải được Phòng Công nghệ Thông tin và Pháp chế phê duyệt.
> - Không ghi mật khẩu, dữ liệu khách hàng hay dữ liệu cá nhân vào Instructions hay tài liệu nguồn.

## Tự thực hành thêm

### Tạo skill trong Copilot Chat [MỚI]

Agent ở các bài tập trên giúp **nhiều người hỏi đáp** từ một bộ tài liệu. **Skill** giải quyết một nhu cầu khác: dạy Copilot **một quy trình làm việc** của anh/chị (các bước, mẫu trình bày, quy tắc), để lần sau chỉ cần gọi tên là Copilot làm đúng như vậy. Ở bài này, anh/chị biến việc viết báo cáo tuần thành skill.

> [!NOTE]
> Skills trong Copilot Chat cần licence **Microsoft 365 Copilot**. Nếu không thấy mục **Agents**, hãy tìm trong nút **Plugins**.

**Mô tả skill bằng lời:**

1. Trong [Copilot Chat](https://m365.cloud.microsoft/chat), mở cuộc trò chuyện mới (Work IQ **bật**)
2. Nhập prompt:

> **PROMPT:**
>
> Tạo cho tôi một skill cá nhân tên "bao-cao-tuan". Mục đích: soạn báo cáo tuần gửi quản lý trực tiếp từ email, cuộc họp, chat Teams và tài liệu của tôi trong 7 ngày qua. Các bước: (1) nếu tôi chưa nói, hỏi lại báo cáo gửi ai và cần tập trung dự án nào; (2) tìm thông tin 7 ngày gần nhất; (3) trình bày đúng 4 phần: Kết quả đã hoàn thành (tối đa 5 ý), Đang thực hiện (bảng Việc | Tiến độ | Hạn chót | Rủi ro), Cần hỗ trợ hoặc cần quyết định (cần ai, việc gì, trước ngày nào), Kế hoạch tuần tới; (4) mỗi ý ghi nguồn; (5) cuối báo cáo liệt kê các ý chưa có nguồn rõ ràng. Quy tắc: tối đa một trang, không tự thêm số liệu hay thời hạn, thiếu thông tin thì ghi [CẦN XÁC NHẬN], không đưa dữ liệu cá nhân vào báo cáo.

3. Copilot mở trình tạo skill với các phần **Name**, **Description**, **Instructions**, **Workflow**, **Included files**. Kiểm tra:

| Phần | Cần thấy |
|------|----------|
| **Name** | bao-cao-tuan (chỉ chữ thường, số và dấu gạch ngang) |
| **Description** | Nói rõ skill làm gì và **khi nào dùng**, ví dụ "dùng khi người dùng nhờ viết báo cáo tuần". Copilot dựa vào mô tả này để tự chọn skill |
| **Workflow** | Đủ 5 bước như prompt |

4. Lưu skill

> [!TIP]
> **Không tạo được skill bằng lời?** Tải [Skill Copilot Chat - bao-cao-tuan.zip](#file-skill-chat). Trong Copilot Chat chọn **Agents** > **More agents**, bấm mũi tên cạnh **Add** > **Upload skill**, chọn file zip và bấm **Upload**. Mở file zip để xem: một skill thực chất là một file **SKILL.md** gồm tên, mô tả và các bước viết bằng lời thường.

**Gọi skill:**

1. Mở cuộc trò chuyện mới, bấm **+** và chọn skill **bao-cao-tuan** trong mục **Agents and Skills** (hoặc gõ "/" rồi chọn skill)
2. Nhập:

> **PROMPT:**
>
> Viết báo cáo tuần này gửi trưởng phòng của tôi, tập trung vào việc chuẩn bị báo cáo quản lý quý 3.

3. Bật tùy chọn **Let Copilot use this skill automatically** trong phần cài đặt của skill, rồi thử gõ *"Tổng kết tuần giúp tôi"* mà không chọn skill. Copilot tự nhận ra và dùng **bao-cao-tuan**

**Kết quả mong đợi:** Báo cáo luôn có đúng 4 phần theo mẫu, mỗi ý có nguồn, cuối báo cáo có danh sách ý cần tự xác nhận. Tuần sau gọi lại skill, cấu trúc vẫn y như vậy, không cần viết lại prompt dài.

**Skill hay agent?** Skill là quy trình làm việc nhiều bước Copilot làm theo, chủ yếu cho cá nhân và việc lặp lại (báo cáo tuần, làm sạch dữ liệu, soạn tờ trình theo mẫu). Agent là trợ lý có lời dặn và tài liệu nguồn riêng, để nhiều người cùng hỏi đáp.

### Tạo agent cho công việc của anh/chị

Lặp lại quy trình trên với một chủ đề của riêng anh/chị:

1. **Chủ đề** - Agent hỗ trợ việc gì? (hướng dẫn nhân viên mới, FAQ quy trình của phòng, tra cứu sản phẩm và dịch vụ, hỏi đáp quy trình IT...)
2. **Người dùng và giọng điệu** - Dành cho ai? Trang trọng hay thân thiện?
3. **Knowledge** - Thư mục hoặc site SharePoint nào làm nguồn? Ai đang có quyền đọc?
4. **Giới hạn** - Agent không được trả lời hoặc cam kết điều gì?
5. **Starter prompts** - 3-4 câu hỏi người dùng hay hỏi nhất
6. **Bộ câu test** - 3 câu có đáp án rõ trong tài liệu và 1 câu ngoài phạm vi
