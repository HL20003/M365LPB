param([string]$Path, [string]$OutDir)
# Xuất ảnh từng slide (để kiểm tra nhanh giao diện), không dùng trong site
$pp = New-Object -ComObject PowerPoint.Application
try {
    $pres = $pp.Presentations.Open((Resolve-Path $Path).Path, $true, $false, $false)
    New-Item -ItemType Directory -Force $OutDir | Out-Null
    $i = 1
    foreach ($s in $pres.Slides) { $s.Export((Join-Path $OutDir "s$i.png"), "PNG", 960, 540); $i++ }
    $pres.Close()
} finally { $pp.Quit() }
