"""Tạo 2 file PowerPoint cho Lab 4.

1) Town hall Q3 2026 (bản nháp).pptx - bộ slide "có sẵn": theme Office mặc định, nhiều chữ, tiêu đề chỉ là tên chủ đề.
   Học viên áp mẫu thương hiệu, nhờ Copilot rút gọn, dùng Visualize this slide, interactive slide và speaker notes.
2) Mẫu thương hiệu (giả định).pptx - mẫu thương hiệu của công ty giả định: bảng màu, font, slide master có dải màu
   và nhãn "Nội bộ", layout tiêu đề nền tối. Không dùng tên công ty thật.

Nền là base-16x9.pptx (tạo bằng make_base_pptx.ps1 qua PowerPoint COM) để có đủ layout 16:9 chuẩn.
Số liệu khớp với Báo cáo Kết quả Kinh doanh Q3 2026.xlsx và Kế hoạch Hoạt động 2027 (dự thảo).docx.
"""
import copy
from pathlib import Path

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.oxml.ns import qn
from pptx.oxml.shapes.autoshape import CT_Shape
from pptx.util import Emu, Pt

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
BASE = HERE / "base-16x9.pptx"

FICTION = "Tài liệu nháp dùng cho đào tạo. Số liệu và tình huống là giả định."

# ------------------------------------------------------------------ Bộ slide có sẵn (bản nháp, nhiều chữ)
DECK = [
    ("title", "HỌP TOÀN CÔNG TY QUÝ 3/2026",
     "Kết quả 9 tháng và định hướng Kế hoạch Hoạt động 2027\nPhòng Truyền thông nội bộ - bản nháp ngày 14/10/2026"),
    ("bullets", "Kết quả kinh doanh quý 3", [
        "Doanh thu quý 3 đạt 432 tỷ đồng, tăng 3,3% so với quý 2 và đạt 99,1% kế hoạch quý, trong đó mảng Triển khai giải pháp "
        "đạt 178 tỷ đồng nhờ ba dự án lớn nghiệm thu sớm trong tháng 9",
        "Tuy nhiên lợi nhuận trước thuế chỉ đạt 84 tỷ đồng, giảm 16,8% so với quý 2 và đạt 79% kế hoạch, nguyên nhân chính là chi phí "
        "thuê thầu phụ lên tới 50 tỷ đồng, vượt kế hoạch 39% do phải thuê ngoài bù nhân sự nghỉ việc",
        "Mảng Đào tạo doanh nghiệp chỉ đạt 29 tỷ đồng so với kế hoạch 36 tỷ đồng vì hai khóa đào tạo lớn bị khách hàng hoãn sang quý 4",
        "Khách hàng lớn nhất chiếm 36% doanh thu, cao hơn mức khoảng 20% của các doanh nghiệp cùng ngành",
        "Điểm hài lòng khách hàng (NPS) giảm từ 41 xuống 36, thấp hơn kế hoạch 45",
    ]),
    ("bullets", "Tình hình nhân sự", [
        "Cuối quý 3 công ty có 1.162 nhân viên tại 6 văn phòng, trong quý có 58 người nghỉ việc, tập trung ở văn phòng TP. Hồ Chí Minh "
        "(27 người); tỷ lệ nghỉ việc năm hóa là 20%, cao hơn nhiều so với kế hoạch 11,5% và trung vị ngành 13,5%",
        "Giờ làm thêm bình quân 14,2 giờ/người/tháng so với kế hoạch 8 giờ; giờ đào tạo bình quân chỉ 4,8 giờ/người trong quý",
        "Khảo sát nhân viên quý 3 cho thấy ba lý do chính khiến nhân viên muốn nghỉ: không thấy lộ trình phát triển, khối lượng "
        "làm thêm giờ lớn và thiếu thời gian đào tạo",
    ]),
    ("bullets", "Bốn sáng kiến trọng tâm năm 2027", [
        "Sáng kiến 1 - Con người: lộ trình nghề nghiệp rõ ràng cho từng vị trí, chương trình mentor, tăng ngân sách đào tạo, "
        "đánh giá 1:1 hằng tháng giữa quản lý và nhân viên",
        "Sáng kiến 2 - Khách hàng: phản hồi mọi yêu cầu của khách hàng trong 24 giờ làm việc, khảo sát sau mỗi giai đoạn dự án, "
        "họp đánh giá chất lượng dịch vụ hằng quý với 30 khách hàng lớn nhất",
        "Sáng kiến 3 - Làm việc thông minh với AI: triển khai Microsoft 365 Copilot cho toàn bộ nhân viên, đào tạo theo vai trò, "
        "xây dựng agent nội bộ tra cứu chính sách và quy trình",
        "Sáng kiến 4 - Tăng trưởng: mở văn phòng Huế trong quý 3/2027, tăng doanh thu mảng Đào tạo doanh nghiệp thêm 30%",
    ]),
    ("bullets", "Chương trình Phát triển và Phúc lợi 2027", [
        "Áp dụng từ 01/01/2027 cho nhân viên chính thức. Ngân sách đào tạo mỗi năm là 8 triệu đồng với nhân viên, 12 triệu đồng với "
        "chuyên viên và trưởng nhóm, 25 triệu đồng với quản lý",
        "Làm việc từ xa tối đa 2 ngày/tuần với nhân viên, chuyên viên và trưởng nhóm; quản lý linh hoạt theo lịch công tác. "
        "Mọi người được nghỉ sinh nhật 1 ngày",
        "Khám sức khỏe: gói cơ bản cho nhân viên, gói nâng cao cho chuyên viên và trưởng nhóm, gói nâng cao thêm 1 người thân cho quản lý",
        "Nhân viên mới được ghép mentor trong 6 tháng đầu; chuyên viên, trưởng nhóm làm mentor được phụ cấp 1 triệu đồng/tháng; "
        "thưởng giới thiệu ứng viên 8 triệu đồng (quản lý 15 triệu đồng)",
    ]),
    ("bullets", "Lộ trình triển khai", [
        "Tháng 11/2026: phê duyệt kế hoạch và công bố khung lộ trình nghề nghiệp (Phòng Nhân sự)",
        "Tháng 12/2026: cấp licence Microsoft 365 Copilot, đào tạo nhóm Copilot Champion (Phòng Công nghệ Thông tin)",
        "Tháng 01/2027: áp dụng Chương trình Phát triển và Phúc lợi 2027 và trao đổi 1:1 (Phòng Nhân sự, các phòng ban)",
        "Quý 1/2027: đào tạo Copilot theo vai trò cho toàn bộ nhân viên (Phòng Công nghệ Thông tin)",
        "Quý 3/2027: mở văn phòng Huế (Ban Giám đốc); hằng quý: đánh giá tiến độ và điều chỉnh kế hoạch (Phòng Kế hoạch và Chiến lược)",
    ]),
    ("bullets", "Mỗi người cần làm gì", [
        "Tháng 1/2027 trao đổi 1:1 với quản lý để thống nhất lộ trình nghề nghiệp và kế hoạch đào tạo cá nhân",
        "Mỗi quý hoàn thành tối thiểu 8 giờ đào tạo, trong đó có 2 giờ về sử dụng AI an toàn và hiệu quả",
        "Quản lý rà soát giờ làm thêm của đội hằng tháng và điều chỉnh phân công khi một người vượt 12 giờ/tháng",
        "Chỉ sử dụng công cụ AI được công ty phê duyệt, không đưa dữ liệu cá nhân hay dữ liệu khách hàng vào công cụ AI công cộng",
    ]),
    ("title", "HỎI ĐÁP", "Gửi câu hỏi trước qua kênh Teams \"Town hall\""),
]


def build_draft_deck():
    prs = Presentation(BASE)
    title_layout, content_layout = prs.slide_layouts[0], prs.slide_layouts[1]
    for kind, title, body in DECK:
        if kind == "title":
            s = prs.slides.add_slide(title_layout)
            s.shapes.title.text = title
            s.placeholders[1].text = body
            continue
        s = prs.slides.add_slide(content_layout)
        s.shapes.title.text = title
        tf = s.placeholders[1].text_frame
        for i, line in enumerate(body):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = line
            p.font.size = Pt(16)
        s.notes_slide.notes_text_frame.text = ""  # chưa có speaker notes
    prs.core_properties.title = "Town hall Q3 2026 (bản nháp)"
    prs.core_properties.comments = FICTION
    prs.save(OUT / "Town hall Q3 2026 (bản nháp).pptx")


# ------------------------------------------------------------------ Mẫu thương hiệu
NAVY, TEAL, ORANGE = "0A2A4E", "00A3A1", "F28C28"
COLORS = {  # bảng màu thương hiệu giả định
    "dk2": NAVY, "lt2": "EEF3F8",
    "accent1": NAVY, "accent2": TEAL, "accent3": ORANGE, "accent4": "5B6B7F", "accent5": "7FC8C6", "accent6": "C0392B",
    "hlink": "1C5FB0", "folHlink": "6B4FA0",
}
A = "http://schemas.openxmlformats.org/drawingml/2006/main"


def set_theme(prs):
    part = prs.slide_master.part.part_related_by(RT.THEME)
    root = etree.fromstring(part.blob)
    root.set("name", "Mau thuong hieu gia dinh")
    scheme = root.find(f".//{{{A}}}clrScheme")
    scheme.set("name", "Thuong hieu gia dinh")
    for key, hexval in COLORS.items():
        el = scheme.find(f"{{{A}}}{key}")
        for child in list(el):
            el.remove(child)
        etree.SubElement(el, f"{{{A}}}srgbClr", val=hexval)
    fonts = root.find(f".//{{{A}}}fontScheme")
    fonts.set("name", "Thuong hieu gia dinh")
    for tag, face in (("majorFont", "Segoe UI Semibold"), ("minorFont", "Segoe UI")):
        fonts.find(f"{{{A}}}{tag}/{{{A}}}latin").set("typeface", face)
    part._blob = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)


def add_master_shape(master, sp_id, name, x, y, cx, cy, fill=None, text=None, size=10, color="FFFFFF", bold=False):
    tree = master.shapes._spTree
    if text is None:
        sp = CT_Shape.new_autoshape_sp(sp_id, name, "rect", x, y, cx, cy)
    else:
        sp = CT_Shape.new_textbox_sp(sp_id, name, x, y, cx, cy)
    tree.append(sp)
    shape = master.shapes[-1]
    if fill:
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor.from_string(fill)
        shape.line.fill.background()
    if text is not None:
        tf = shape.text_frame
        tf.margin_left = tf.margin_right = 0
        tf.text = text
        r = tf.paragraphs[0].runs[0]
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.color.rgb = RGBColor.from_string(color)
    return shape


def dark_layout(layout):
    """Layout nền xanh đậm, chữ trắng (đảo bảng màu bằng clrMapOvr)."""
    layout.background.fill.solid()
    layout.background.fill.fore_color.rgb = RGBColor.from_string(NAVY)
    ovr = layout._element.find(qn("p:clrMapOvr"))
    if ovr is None:  # thứ tự trong sldLayout: cSld, clrMapOvr, ...
        ovr = etree.Element(qn("p:clrMapOvr"))
        layout._element.find(qn("p:cSld")).addnext(ovr)
    for child in list(ovr):
        ovr.remove(child)
    etree.SubElement(ovr, f"{{{A}}}overrideClrMapping", bg1="dk1", tx1="lt1", bg2="dk2", tx2="lt2",
                     accent1="accent1", accent2="accent2", accent3="accent3", accent4="accent4",
                     accent5="accent5", accent6="accent6", hlink="hlink", folHlink="folHlink")


def build_brand_template():
    prs = Presentation(BASE)
    set_theme(prs)
    W, H = prs.slide_width, prs.slide_height
    master = prs.slide_master
    # Dải màu chân trang, vạch nhấn cạnh tiêu đề, nhãn thương hiệu và mức phân loại
    add_master_shape(master, 901, "Brand band", 0, H - Emu(380000), W, Emu(380000), fill=NAVY)
    add_master_shape(master, 902, "Brand accent", Emu(457200), Emu(520000), Emu(90000), Emu(640000), fill=TEAL)
    add_master_shape(master, 903, "Brand name", Emu(457200), H - Emu(300000), Emu(4000000), Emu(230000),
                     text="◆ CÔNG TY GIẢ ĐỊNH", size=10, bold=True)
    add_master_shape(master, 904, "Classification", W - Emu(2900000), H - Emu(300000), Emu(2450000), Emu(230000),
                     text="Phân loại: Nội bộ", size=10, color="7FC8C6")
    for layout in prs.slide_layouts:
        if layout.name in ("Title Slide", "Section Header"):
            dark_layout(layout)

    s = prs.slides.add_slide(prs.slide_layouts[0])
    s.shapes.title.text = "Tiêu đề bài trình bày"
    s.placeholders[1].text = "Phòng ban  |  Ngày trình bày"
    s = prs.slides.add_slide(prs.slide_layouts[1])
    s.shapes.title.text = "Tiêu đề là một thông điệp, không chỉ là tên chủ đề"
    tf = s.placeholders[1].text_frame
    rules = [
        "Tối đa 4 ý mỗi slide, mỗi ý không quá 2 dòng",
        "Màu chính xanh đậm #0A2A4E; màu nhấn xanh ngọc #00A3A1 cho số liệu cần chú ý; cam #F28C28 cho cảnh báo",
        "Font Segoe UI Semibold cho tiêu đề, Segoe UI cho nội dung",
        "Số liệu quan trọng đưa lên biểu đồ hoặc hình minh họa thay vì viết thành câu dài",
    ]
    for i, line in enumerate(rules):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
    prs.core_properties.title = "Mẫu thương hiệu (giả định)"
    prs.core_properties.comments = FICTION
    prs.save(OUT / "Mẫu thương hiệu (giả định).pptx")


if __name__ == "__main__":
    build_draft_deck()
    build_brand_template()
    print("2 file PowerPoint ->", OUT)
