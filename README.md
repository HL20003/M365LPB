# Copilot Overview Workshop - bản general v2

Bản v2 (tách từ `m365copilot-overview-lab-general` ngày 20/11/2026): agenda 8 phần theo hướng dẫn speaker, tính năng mới 2026, bố cục bài tập dạng thẻ, mỗi lab một use case riêng. Bản gốc giữ làm dự phòng.

Site lab Microsoft 365 Copilot dùng chung cho mọi phòng ban và mọi vai trò, dựng theo mẫu `m365copilot-overview-lab-mkg`
(cùng cấu trúc module/lab, giao diện và cách host), nhưng nội dung và file demo dùng một công ty dịch vụ giả định thay vì một phòng ban cố định.

## Cấu trúc

| Đường dẫn | Nội dung |
|---|---|
| `public/` | Site tĩnh: `index.html`, `js/app.js` (danh sách module và file demo), `css/style.css`, `labs/*/index.md`, `files/` |
| `demo-files/` | Bản gốc các file demo và script tạo lại (`_gen/`), kèm đáp án cho người hướng dẫn |
| `wrangler.jsonc` | Cấu hình Cloudflare Workers (static assets từ `public/`) |

## Chạy thử và deploy lên Cloudflare Workers

```bash
npx wrangler dev        # chạy thử tại http://localhost:8787
npx wrangler deploy     # deploy, Worker tên m365copilot-general-lab-v2
```

Lần đầu deploy, wrangler sẽ yêu cầu đăng nhập Cloudflare (`npx wrangler login`).
Không mở trực tiếp `index.html` bằng file:// vì trang tải nội dung lab bằng fetch; hãy chạy qua wrangler dev hoặc một web server bất kỳ.

## Sửa nội dung

- Thêm hoặc đổi lab: sửa file markdown trong `public/labs/`, cập nhật `modules` trong `public/js/app.js` và bảng lịch trình trong `public/index.html`.
- Đổi file demo: xem `demo-files/README.md`. Trong markdown, `[tên file](#file-<id>)` tự thành link tải file có id tương ứng trong `demoFiles` của `app.js`.

## Mật khẩu lớp học

Site được khóa bằng một mật khẩu chung (`src/worker.js`). Người truy cập thấy trang **Đăng nhập**, nhập đúng mật khẩu thì vào được site trong 7 ngày; nút **Đăng xuất** ở thanh trên cùng.

- **Đặt hoặc đổi mật khẩu:** Cloudflare dashboard > Workers & Pages > `m365copilot-general-lab-v2` > Settings > **Variables and Secrets** > Add, chọn loại **Secret**, tên `LAB_PASSWORD`. Hoặc chạy `npx wrangler secret put LAB_PASSWORD`. Đổi mật khẩu thì mọi người phải đăng nhập lại.
- **Không ghi mật khẩu vào code**: repo GitHub đang public.
- Chưa đặt `LAB_PASSWORD` thì site báo "chưa sẵn sàng" thay vì mở công khai.
- **Logo trên trang đăng nhập:** đặt file logo SoftwareOne chính thức tại `public/brand/softwareone-logo.svg` (thư mục `public/brand/` xem được khi chưa đăng nhập, chỉ để file thương hiệu ở đây). Chưa có file thì trang hiện chữ "SoftwareOne" thay thế.
- Chạy thử trên máy: tạo file `.dev.vars` (đã có trong .gitignore) với dòng `LAB_PASSWORD=<mật khẩu thử>`, rồi `npx wrangler dev`.
