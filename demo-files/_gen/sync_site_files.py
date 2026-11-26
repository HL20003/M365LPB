"""Chép file demo vào thư mục files/ của site (đường dẫn ASCII) và đóng gói zip để tải một lần.

Chạy lại sau mỗi lần tạo lại file demo. Tên tiếng Việt đầy đủ được giữ khi tải về
nhờ thuộc tính download trong app.js, nên tên ở đây chỉ cần ổn định và không dấu.

Hai skill mẫu trong demo-files/skills được đóng gói thành zip:
- Skill Excel: zip chứa thư mục <tên skill>/SKILL.md, giải nén rồi chép cả thư mục vào thư mục skills trên OneDrive
- Skill Copilot Chat: zip có SKILL.md ở gốc, tải lên trực tiếp bằng Upload skill
"""
import shutil
import zipfile
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent
DST = SRC.parent / "public" / "files"
SKILLS = SRC / "skills"

FILES = {  # đường dẫn trên site: tên file gốc
    "so-tay-chinh-sach-noi-bo.docx": "Sổ tay Chính sách Nội bộ.docx",
    "sample-chinh-sach-bao-mat-thong-tin.docx": "SAMPLE Chính sách Bảo mật Thông tin.docx",
    "bao-cao-ket-qua-kinh-doanh-q3-2026.xlsx": "Báo cáo Kết quả Kinh doanh Q3 2026.xlsx",
    "phan-hoi-khach-hang-t9-t10-2026.xlsx": "Phản hồi khách hàng T9-T10 2026 (xuất từ hệ thống).xlsx",
    "ke-hoach-hoat-dong-2027.docx": "Kế hoạch Hoạt động 2027 (dự thảo).docx",
    "bao-cao-quan-ly-q3-2026-ban-nhap.docx": "Báo cáo quản lý Q3 2026 (bản nháp).docx",
    "mau-to-trinh-gia-dinh.docx": "Mẫu tờ trình (giả định).docx",
    "transcript-hop-giao-ban-q3-mau.docx": "Transcript họp giao ban quý 3 (mẫu).docx",
    "town-hall-q3-2026-ban-nhap.pptx": "Town hall Q3 2026 (bản nháp).pptx",
    "mau-thuong-hieu-gia-dinh.pptx": "Mẫu thương hiệu (giả định).pptx",
}
SKILL_ZIPS = {  # đường dẫn trên site: (tên khi tải về, thư mục skill, có bọc thư mục không)
    "skill-excel-bao-cao-phan-hoi-khach-hang.zip": ("Skill Excel - bao-cao-phan-hoi-khach-hang.zip", "bao-cao-phan-hoi-khach-hang", True),
    "skill-ppt-slide-tom-tat.zip": ("Skill PowerPoint - slide-tom-tat.zip", "slide-tom-tat", True),
    "skill-chat-bao-cao-tuan.zip": ("Skill Copilot Chat - bao-cao-tuan.zip", "bao-cao-tuan", False),
}
ZIP_NAME = "copilot-workshop-demo-files.zip"

if DST.exists():
    shutil.rmtree(DST)
DST.mkdir(parents=True)
for site_name, src_name in FILES.items():
    shutil.copy2(SRC / src_name, DST / site_name)
for site_name, (_, folder, wrap) in SKILL_ZIPS.items():
    with zipfile.ZipFile(DST / site_name, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(SKILLS / folder / "SKILL.md", arcname=f"{folder}/SKILL.md" if wrap else "SKILL.md")
with zipfile.ZipFile(DST / ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as z:
    for src_name in FILES.values():
        z.write(SRC / src_name, arcname=src_name)
    for site_name, (download_name, _, _) in SKILL_ZIPS.items():
        z.write(DST / site_name, arcname=f"Skill mẫu/{download_name}")
total = sum(p.stat().st_size for p in DST.iterdir())
print(f"{len(FILES)} file + {len(SKILL_ZIPS)} skill + zip -> {DST} ({total / 1024:.0f} KB)")
