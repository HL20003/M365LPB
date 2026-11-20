"""Xuất "Huong dan speaker.md" thành PDF (A4, font Segoe UI) để gửi cho speaker.

Chạy: python make_pdf.py  (cần reportlab; Windows có sẵn font Segoe UI)
Hỗ trợ phần Markdown dùng trong file: #, ##, ###, đoạn văn, gạch đầu dòng (kể cả lùi 2 dấu cách),
danh sách số, bảng | ... |, **in đậm**.
"""
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

HERE = Path(__file__).resolve().parent
SRC = HERE / "Huong dan speaker.md"
OUT = HERE / "Hướng dẫn speaker - Copilot Workshop (bản general v2).pdf"

F = r"C:\Windows\Fonts"
for name, file in (("Seg", "segoeui"), ("SegB", "segoeuib"), ("SegI", "segoeuii"), ("SegBI", "segoeuiz")):
    pdfmetrics.registerFont(TTFont(name, f"{F}\\{file}.ttf"))
pdfmetrics.registerFontFamily("Seg", normal="Seg", bold="SegB", italic="SegI", boldItalic="SegBI")

NAVY, BLUE, GREY = colors.HexColor("#0A2A4E"), colors.HexColor("#1C5FB0"), colors.HexColor("#55606E")
LINE, TINT = colors.HexColor("#CCD5DF"), colors.HexColor("#EEF4FB")
base = ParagraphStyle("b", fontName="Seg", fontSize=9.6, leading=13.6, textColor=colors.HexColor("#16202C"), spaceAfter=4)
cell = ParagraphStyle("c", parent=base, fontSize=8.6, leading=11.8, spaceAfter=0)
cellb = ParagraphStyle("cb", parent=cell, fontName="SegB")
h0 = ParagraphStyle("h0", parent=base, fontName="SegB", fontSize=18, leading=23, textColor=NAVY, spaceAfter=2)
h1 = ParagraphStyle("h1", parent=base, fontName="SegB", fontSize=13, leading=17, textColor=NAVY, spaceBefore=12, spaceAfter=5)
h2 = ParagraphStyle("h2", parent=base, fontName="SegB", fontSize=10.8, leading=14.5, textColor=BLUE, spaceBefore=8, spaceAfter=3)
bul = ParagraphStyle("bl", parent=base, leftIndent=12, bulletIndent=3, spaceAfter=2)
bul2 = ParagraphStyle("bl2", parent=bul, leftIndent=24, bulletIndent=15)
W = A4[0] - 36 * mm


def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)


def make_table(rows):
    rows = [r for r in rows if not re.fullmatch(r"\|[\s\-|:]+\|", r.strip())]
    data = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    ncol = len(data[0])
    # độ rộng cột theo độ dài chữ, có giới hạn trên/dưới
    lens = [max(len(r[i]) if i < len(r) else 0 for r in data) for i in range(ncol)]
    # không để cột hẹp hơn từ dài nhất trong cột (tránh cắt đôi từ như "Copilot", "PowerPoint")
    words = [max((len(w) for r in data if i < len(r) for w in r[i].replace("**", "").split()), default=1) for i in range(ncol)]
    weights = [min(max(l, 20, wl * 3.8), 90) for l, wl in zip(lens, words)]
    widths = [W * w / sum(weights) for w in weights]
    body = [[Paragraph(inline(c), cellb if r == 0 else cell) for c in row] for r, row in enumerate(data)]
    t = Table(body, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("BACKGROUND", (0, 0), (-1, 0), TINT),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def build():
    lines = SRC.read_text(encoding="utf-8").splitlines()
    story, i = [], 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            i += 1
            continue
        if s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i])
                i += 1
            story += [make_table(rows), Spacer(1, 6)]
            continue
        if s.startswith("### "):
            story.append(Paragraph(inline(s[4:]), h2))
        elif s.startswith("## "):
            story.append(Paragraph(inline(s[3:]), h1))
        elif s.startswith("# "):
            story.append(Paragraph(inline(s[2:]), h0))
        elif re.match(r"^\s{2,}- ", ln):
            story.append(Paragraph(inline(s[2:]), bul2, bulletText="–"))
        elif s.startswith("- "):
            story.append(Paragraph(inline(s[2:]), bul, bulletText="•"))
        elif re.match(r"^\d+\. ", s):
            num, rest = s.split(". ", 1)
            story.append(Paragraph(inline(rest), bul, bulletText=f"{num}."))
        else:
            story.append(Paragraph(inline(s), base))
        i += 1
    return story


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Seg", 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(18 * mm, 10 * mm, "Hướng dẫn speaker - Copilot Overview Workshop (bản general v2) - tài liệu nội bộ")
    canvas.drawRightString(A4[0] - 18 * mm, 10 * mm, f"Trang {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=15 * mm, bottomMargin=16 * mm,
                        title="Hướng dẫn speaker - Copilot Overview Workshop (bản general v2)")
doc.build(build(), onFirstPage=footer, onLaterPages=footer)
print(OUT)
