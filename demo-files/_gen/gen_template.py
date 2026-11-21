"""Tạo "Mẫu tờ trình (giả định).docx" cho Lab 2 - Bài tập 2.

Mẫu có cấu trúc cố định và các chỗ trống trong [ngoặc vuông, chữ nghiêng màu xám] kèm hướng dẫn điền.
Học viên mở mẫu, gõ "/" chọn Báo cáo quản lý Q3 2026 (bản nháp) và Sổ tay Chính sách Nội bộ,
rồi nhờ Copilot điền tờ trình xin phê duyệt hợp đồng khung thuê thầu phụ 3,2 tỷ đồng.
Mục 3 "Căn cứ quy định" buộc Copilot đối chiếu với Sổ tay (Mục 5.1, 5.2, 5.3), nên đề xuất sai
trong bản nháp báo cáo (Giám đốc Tài chính duyệt, không lấy báo giá, tạm ứng 45%) phải được sửa.
"""
from pathlib import Path

from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor

from docx_common import NAVY, footer_note, new_doc, shade, table

OUT = Path(__file__).resolve().parent.parent
GREY = RGBColor(0x6B, 0x75, 0x80)
FICTION = "Mẫu giả định dùng cho mục đích đào tạo. Mã văn bản, đơn vị và quy định là giả định."


def hint(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(f"[{text}]")
    r.italic = True
    r.font.color.rgb = GREY
    return p


def build():
    doc = new_doc()
    footer_note(doc, FICTION)

    t = doc.add_table(rows=1, cols=2)
    left, right = t.rows[0].cells
    left.text = ""
    r = left.paragraphs[0].add_run("CÔNG TY (GIẢ ĐỊNH)\n")
    r.bold = True
    r.font.size = Pt(10)
    r = left.paragraphs[0].add_run("Đơn vị đề xuất: [Tên phòng ban]\nSố: ......../TTr-[Mã đơn vị]")
    r.font.size = Pt(9.5)
    right.text = ""
    right.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = right.paragraphs[0].add_run("Phân loại: [Nội bộ / Mật]\nNgày ...... tháng ...... năm ......")
    r.font.size = Pt(9.5)
    r.italic = True

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(14)
    r = p.add_run("TỜ TRÌNH")
    r.bold = True
    r.font.size = Pt(17)
    r.font.color.rgb = NAVY
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run("V/v: ").bold = True
    r = p.add_run("[Tên việc cần phê duyệt, tối đa 1 dòng]")
    r.italic = True
    r.font.color.rgb = GREY
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run("Kính gửi: ").bold = True
    r = p.add_run("[Cấp có thẩm quyền phê duyệt theo Sổ tay Chính sách Nội bộ, Mục 5.1]")
    r.italic = True
    r.font.color.rgb = GREY

    doc.add_heading("1. Sự cần thiết", 1)
    hint(doc, "Bối cảnh và vấn đề cần giải quyết, có số liệu cụ thể và nguồn số liệu. Tối đa 5 dòng.")

    doc.add_heading("2. Nội dung đề xuất", 1)
    table(doc, ["Hạng mục", "Nội dung"], [
        ["Đối tượng / nhà cung cấp", "[Tên hoặc mô tả nhà cung cấp]"],
        ["Giá trị (chưa VAT)", "[Số tiền]"],
        ["Thời hạn", "[Thời hạn hợp đồng]"],
        ["Phương thức lựa chọn nhà cung cấp", "[Số báo giá đã có / cần có]"],
        ["Tạm ứng và thanh toán", "[Tỷ lệ tạm ứng, điều kiện thanh toán]"],
        ["Đơn vị thực hiện", "[Phòng ban chủ trì, đầu mối]"],
    ], [5.5, 11])

    doc.add_heading("3. Căn cứ quy định", 1)
    hint(doc, "Đối chiếu từng nội dung đề xuất với Sổ tay Chính sách Nội bộ. Nếu đề xuất chưa đúng quy định, ghi rõ cách điều chỉnh "
              "hoặc nêu đây là ngoại lệ cần phê duyệt.")
    table(doc, ["Nội dung", "Quy định áp dụng (ghi mục)", "Đề xuất đáp ứng thế nào"], [
        ["[Cấp phê duyệt]", "", ""],
        ["[Số báo giá]", "", ""],
        ["[Tạm ứng]", "", ""],
        ["[Điều khoản bắt buộc trong hợp đồng]", "", ""],
    ], [4.5, 5.5, 6.5])

    doc.add_heading("4. Rủi ro và biện pháp kiểm soát", 1)
    table(doc, ["Rủi ro", "Biện pháp kiểm soát", "Đơn vị phụ trách"], [
        ["", "", ""],
        ["", "", ""],
    ], [5.5, 7, 4])

    doc.add_heading("5. Kiến nghị", 1)
    hint(doc, "Nội dung đề nghị cấp có thẩm quyền phê duyệt, viết thành 2-3 gạch đầu dòng.")

    doc.add_heading("Ý kiến và phê duyệt", 1)
    sig = doc.add_table(rows=2, cols=4)
    sig.style = "Table Grid"
    for i, h in enumerate(["Người đề xuất", "[Đơn vị rà soát]", "[Đơn vị rà soát]", "[Cấp phê duyệt]"]):
        c = sig.rows[0].cells[i]
        c.text = ""
        r = c.paragraphs[0].add_run(h)
        r.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shade(c, "0B3D5C")
    for c in sig.rows[1].cells:
        c.text = "\n\n\n"
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    r = p.add_run("Hướng dẫn: giữ nguyên cấu trúc 5 mục. Thay toàn bộ nội dung trong [ngoặc vuông]. Tờ trình không quá 2 trang.")
    r.italic = True
    r.font.size = Pt(9)
    r.font.color.rgb = GREY
    doc.save(OUT / "Mẫu tờ trình (giả định).docx")


if __name__ == "__main__":
    build()
    print("Mẫu tờ trình ->", OUT)
