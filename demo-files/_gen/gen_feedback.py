"""Tạo Phản hồi khách hàng T9-T10 2026 (xuất từ hệ thống).xlsx cho Lab 3 Bài tập 4-5.

Mô phỏng file xuất từ hệ thống CRM: dòng tiêu đề rác phía trên, dòng trống, dòng trùng, tên văn phòng / mức độ / nhóm vấn đề
viết không thống nhất, ngày lẫn kiểu ngày và kiểu chữ. Hai sheet T9 và T10 cùng cấu trúc để học viên tạo skill trên T9
rồi chạy lại trên T10.

Số dòng hợp lệ (sau khi bỏ trùng, bỏ trống) được cố định theo QUOTA; văn phòng phân bổ theo trọng số có seed.
Chạy xong in đáp án cho người hướng dẫn.
"""
import random
from collections import Counter
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font

OUT = Path(__file__).resolve().parent.parent / "Phản hồi khách hàng T9-T10 2026 (xuất từ hệ thống).xlsx"
random.seed(1009)

OFFICES = ["Hà Nội", "TP. Hồ Chí Minh", "Đà Nẵng", "Hải Phòng", "Cần Thơ", "Bình Dương"]
OFFICE_VARIANTS = {
    "Hà Nội": ["Hà Nội", "HN", "Ha Noi", "hà nội"],
    "TP. Hồ Chí Minh": ["TP. Hồ Chí Minh", "TP.HCM", "HCM", "Hồ Chí Minh", "tp hcm"],
    "Đà Nẵng": ["Đà Nẵng", "Da Nang", "ĐN"],
    "Hải Phòng": ["Hải Phòng", "HP", "Hai Phong"],
    "Cần Thơ": ["Cần Thơ", "Can Tho", "CT"],
    "Bình Dương": ["Bình Dương", "BD", "Binh Duong"],
}
ISSUES = ["Chậm tiến độ", "Thay đổi nhân sự dự án", "Phản hồi chậm", "Chất lượng bàn giao", "Hóa đơn - thanh toán", "Khen ngợi"]
ISSUE_VARIANTS = {
    "Chậm tiến độ": ["Chậm tiến độ", "chậm tiến độ", "Cham tien do", "Chậm tiến độ "],
    "Thay đổi nhân sự dự án": ["Thay đổi nhân sự dự án", "Thay đổi nhân sự", "thay doi nhan su du an"],
    "Phản hồi chậm": ["Phản hồi chậm", "phản hồi chậm", "Phan hoi cham"],
    "Chất lượng bàn giao": ["Chất lượng bàn giao", "chất lượng bàn giao", "CL bàn giao"],
    "Hóa đơn - thanh toán": ["Hóa đơn - thanh toán", "Hoá đơn/thanh toán", "hoa don - thanh toan"],
    "Khen ngợi": ["Khen ngợi", "khen ngợi", "Khen"],
}
LEVEL_VARIANTS = {"Cao": ["Cao", "cao", "CAO", "High"], "Trung bình": ["Trung bình", "TB", "trung bình", "Medium"],
                  "Thấp": ["Thấp", "thấp", "Low"]}
LINES = ["Tư vấn", "Triển khai giải pháp", "Dịch vụ vận hành", "Đào tạo doanh nghiệp"]
LINE_VARIANTS = {"Tư vấn": ["Tư vấn", "tu van"], "Triển khai giải pháp": ["Triển khai giải pháp", "Trien khai", "TKGP"],
                 "Dịch vụ vận hành": ["Dịch vụ vận hành", "Vận hành"], "Đào tạo doanh nghiệp": ["Đào tạo doanh nghiệp", "Đào tạo"]}

TEXTS = {
    "Chậm tiến độ": ["Giai đoạn 2 trễ hơn kế hoạch 2 tuần, chưa có lịch mới", "Bàn giao module báo cáo chậm so với cam kết",
                     "Mốc nghiệm thu bị lùi lần thứ hai", "Tiến độ chậm, khách hàng đề nghị họp với cấp quản lý"],
    "Thay đổi nhân sự dự án": ["Đổi quản lý dự án lần thứ hai, khách hàng phải giải thích lại yêu cầu",
                               "Chuyên viên phụ trách nghỉ việc, người mới chưa nắm hệ thống",
                               "Đội dự án thay người giữa giai đoạn, thiếu bàn giao"],
    "Phản hồi chậm": ["Yêu cầu hỗ trợ sau 3 ngày chưa có phản hồi", "Email hỏi tiến độ không được trả lời",
                      "Hotline không gặp được người phụ trách"],
    "Chất lượng bàn giao": ["Tài liệu hướng dẫn bàn giao thiếu phần vận hành", "Lỗi phát sinh sau khi bàn giao 1 tuần",
                            "Báo cáo bàn giao chưa đúng mẫu đã thống nhất"],
    "Hóa đơn - thanh toán": ["Hóa đơn ghi sai thông tin đơn vị", "Đề nghị thanh toán gửi chậm so với hợp đồng",
                             "Chưa nhận được biên bản đối chiếu công nợ"],
    "Khen ngợi": ["Đội dự án hỗ trợ nhiệt tình ngoài giờ", "Buổi đào tạo người dùng rất dễ hiểu",
                  "Quản lý dự án chủ động báo cáo rủi ro sớm"],
}
STATUS = ["Đã xử lý", "Đang xử lý", "Mới", "đã xử lý"]

# (tháng, số dòng hợp lệ theo nhóm vấn đề, số dòng trùng, số dòng trống)
MONTHS = [
    ("T9", 9, {"Chậm tiến độ": 38, "Thay đổi nhân sự dự án": 24, "Phản hồi chậm": 20, "Chất lượng bàn giao": 16,
               "Hóa đơn - thanh toán": 10, "Khen ngợi": 12}, 8, 3),
    ("T10", 10, {"Chậm tiến độ": 41, "Thay đổi nhân sự dự án": 33, "Phản hồi chậm": 19, "Chất lượng bàn giao": 15,
                 "Hóa đơn - thanh toán": 11, "Khen ngợi": 15}, 6, 3),
]
# Trọng số văn phòng theo nhóm vấn đề: chậm tiến độ và thay đổi nhân sự dồn vào TP. Hồ Chí Minh (khớp số nghỉ việc, dự án rủi ro)
W_DEFAULT = [30, 30, 12, 9, 8, 11]
W_HCM = [24, 52, 6, 6, 6, 6]
LEVEL_W = {"Chậm tiến độ": [55, 35, 10], "Thay đổi nhân sự dự án": [45, 45, 10], "Phản hồi chậm": [30, 50, 20],
           "Chất lượng bàn giao": [40, 45, 15], "Hóa đơn - thanh toán": [10, 50, 40], "Khen ngợi": [0, 0, 100]}


def make_rows(month, quota):
    rows = []
    for issue, n in quota.items():
        w = W_HCM if issue in ("Chậm tiến độ", "Thay đổi nhân sự dự án") else W_DEFAULT
        for _ in range(n):
            office = random.choices(OFFICES, weights=w)[0]
            level = random.choices(["Cao", "Trung bình", "Thấp"], weights=LEVEL_W[issue])[0]
            line = random.choices(LINES, weights=[3, 5, 3, 1] if issue != "Khen ngợi" else [3, 3, 3, 3])[0]
            day = date(2026, month, random.randint(1, 30 if month == 9 else 31))
            rows.append(dict(day=day, office=office, issue=issue, level=level, line=line,
                             kh=f"KH-{random.randint(1, 291):03d}", text=random.choice(TEXTS[issue]),
                             status=random.choice(STATUS)))
    rows.sort(key=lambda r: r["day"])
    return rows


def messy(r):
    d = r["day"]
    fmt = random.random()
    if fmt < 0.55:
        day_val = d  # ô kiểu ngày
    elif fmt < 0.85:
        day_val = d.strftime("%d/%m/%Y")  # chữ dd/mm/yyyy
    else:
        day_val = d.isoformat()  # chữ yyyy-mm-dd
    return [day_val, random.choice(OFFICE_VARIANTS[r["office"]]), r["kh"], random.choice(LINE_VARIANTS[r["line"]]),
            random.choice(ISSUE_VARIANTS[r["issue"]]), random.choice(LEVEL_VARIANTS[r["level"]]), r["text"], r["status"]]


wb = Workbook()
wb.remove(wb.active)
answers = {}
for name, month, quota, n_dup, n_blank in MONTHS:
    rows = make_rows(month, quota)
    data = [messy(r) for r in rows]
    for i in random.sample(range(len(data)), n_dup):  # dòng trùng: chép y nguyên, chèn ngay sau dòng gốc
        data.insert(data.index(data[i]) + 1, list(data[i]))
    for _ in range(n_blank):
        data.insert(random.randint(5, len(data) - 5), [None] * 8)

    ws = wb.create_sheet(name)
    ws["A1"] = "BÁO CÁO XUẤT TỪ HỆ THỐNG CRM - PHẢN HỒI KHÁCH HÀNG"
    ws["A1"].font = Font(bold=True)
    ws["A2"] = f"Kỳ: tháng {month}/2026 | Ngày xuất: 0{1 if month == 9 else 3}/{month + 1}/2026 08:12 | Người xuất: system | Số liệu giả định dùng cho đào tạo"
    ws.append([])
    ws.append(["STT", "Ngày nhận", "Văn phòng", "Mã KH", "Mảng dịch vụ", "Nhóm vấn đề", "Mức độ", "Nội dung tóm tắt", "Trạng thái"])
    stt = 0
    for row in data:
        if row[0] is None:
            ws.append([None] * 9)
            continue
        stt += 1
        ws.append([stt] + row)
        c = ws.cell(row=ws.max_row, column=2)
        if isinstance(row[0], date):
            c.number_format = "dd/mm/yyyy"
    for col, w in zip("ABCDEFGHI", [6, 12, 16, 9, 20, 24, 11, 62, 12]):
        ws.column_dimensions[col].width = w

    by_issue = Counter(r["issue"] for r in rows)
    by_office = Counter(r["office"] for r in rows)
    late_hcm = sum(r["issue"] == "Chậm tiến độ" and r["office"] == "TP. Hồ Chí Minh" for r in rows)
    staff_hcm = sum(r["issue"] == "Thay đổi nhân sự dự án" and r["office"] == "TP. Hồ Chí Minh" for r in rows)
    high = sum(r["level"] == "Cao" for r in rows)
    answers[name] = dict(raw=len(data), dup=n_dup, blank=n_blank, valid=len(rows), by_issue=by_issue,
                         by_office=by_office, late_hcm=late_hcm, staff_hcm=staff_hcm, high=high)

wb.save(OUT)
print("Đã tạo", OUT.name)
for name, a in answers.items():
    v = a["valid"]
    print(f"\n{name}: {a['raw']} dòng dữ liệu (gồm {a['dup']} trùng, {a['blank']} trống) -> {v} dòng hợp lệ")
    print("  Theo nhóm:", ", ".join(f"{k} {n} ({n / v:.0%})" for k, n in a["by_issue"].most_common()))
    print("  Theo văn phòng:", ", ".join(f"{k} {n}" for k, n in a["by_office"].most_common()))
    print(f"  Chậm tiến độ ở TP. HCM: {a['late_hcm']}/{a['by_issue']['Chậm tiến độ']}; "
          f"Thay đổi nhân sự ở TP. HCM: {a['staff_hcm']}/{a['by_issue']['Thay đổi nhân sự dự án']}; "
          f"Mức độ Cao: {a['high']} ({a['high'] / v:.0%})")
