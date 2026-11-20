param([string]$Out = "base-16x9.pptx")
# Tạo file PowerPoint trống 16:9 (theme Office mặc định) làm nền cho gen_slides.py
$pp = New-Object -ComObject PowerPoint.Application
try {
    $pres = $pp.Presentations.Add(0)   # 0 = không hiện cửa sổ
    $pres.PageSetup.SlideWidth = 960
    $pres.PageSetup.SlideHeight = 540
    $full = Join-Path (Get-Location) $Out
    $pres.SaveAs($full)
    $pres.Close()
    "created: $full"
} finally {
    $pp.Quit()
    [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($pp)
}
