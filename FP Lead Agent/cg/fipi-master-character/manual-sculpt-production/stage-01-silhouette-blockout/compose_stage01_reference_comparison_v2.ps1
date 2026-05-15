Add-Type -AssemblyName System.Drawing

$Root = "C:\Users\mrbik\Desktop\AI projects\projects\fix-price\FP Lead Agent\cg\fipi-master-character"
$OutDir = Join-Path $Root "manual-sculpt-production\stage-01-silhouette-blockout"
$PreviewDir = Join-Path $OutDir "previews"

$Turnaround = Join-Path $Root "turnaround-references\fipi_turnaround_draft_approved_2026-05-15.png"
$Proportion = Join-Path $Root "expression-material-stage\fipi_proportion_guide_candidate.png"
$Front = Join-Path $PreviewDir "fipi_stage01_silhouette_front_v2.png"
$Side = Join-Path $PreviewDir "fipi_stage01_silhouette_side_v2.png"
$Back = Join-Path $PreviewDir "fipi_stage01_silhouette_back_v2.png"
$Output = Join-Path $PreviewDir "fipi_stage01_reference_comparison_v2.png"

$Bitmap = New-Object System.Drawing.Bitmap 2400, 1500
$Graphics = [System.Drawing.Graphics]::FromImage($Bitmap)
$Graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$Graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$Graphics.Clear([System.Drawing.Color]::FromArgb(238, 238, 235))

$TitleFont = New-Object System.Drawing.Font "Arial", 34, ([System.Drawing.FontStyle]::Bold)
$LabelFont = New-Object System.Drawing.Font "Arial", 20, ([System.Drawing.FontStyle]::Bold)
$BodyFont = New-Object System.Drawing.Font "Arial", 22, ([System.Drawing.FontStyle]::Regular)
$SmallFont = New-Object System.Drawing.Font "Arial", 16, ([System.Drawing.FontStyle]::Regular)
$BrushDark = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(28, 35, 42))
$BrushMuted = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(76, 84, 92))
$Pen = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(205, 205, 200)), 2

function Draw-ContainedImage {
    param(
        [System.Drawing.Graphics]$Graphics,
        [string]$Path,
        [System.Drawing.RectangleF]$Rect,
        [string]$Label
    )

    $Graphics.FillRectangle([System.Drawing.Brushes]::WhiteSmoke, $Rect)
    $Graphics.DrawRectangle($script:Pen, $Rect.X, $Rect.Y, $Rect.Width, $Rect.Height)

    $Image = [System.Drawing.Image]::FromFile($Path)
    $Scale = [Math]::Min($Rect.Width / $Image.Width, $Rect.Height / $Image.Height)
    $DrawW = $Image.Width * $Scale
    $DrawH = $Image.Height * $Scale
    $DrawX = $Rect.X + (($Rect.Width - $DrawW) / 2)
    $DrawY = $Rect.Y + (($Rect.Height - $DrawH) / 2)
    $Dest = New-Object System.Drawing.RectangleF $DrawX, $DrawY, $DrawW, $DrawH
    $Graphics.DrawImage($Image, $Dest)
    $Image.Dispose()

    $Graphics.DrawString($Label, $script:LabelFont, $script:BrushDark, $Rect.X, ($Rect.Y - 32))
}

$Graphics.DrawString("Stage 1 v2 silhouette comparison", $TitleFont, $BrushDark, 40, 28)
$Graphics.DrawString("Approved references vs revised temporary sculpt blockout candidate. Not production mesh.", $BodyFont, $BrushMuted, 40, 72)

Draw-ContainedImage $Graphics $Turnaround ([System.Drawing.RectangleF]::new(40, 150, 1040, 470)) "Approved turnaround reference"
Draw-ContainedImage $Graphics $Proportion ([System.Drawing.RectangleF]::new(40, 735, 1040, 470)) "Approved proportion guide"

Draw-ContainedImage $Graphics $Front ([System.Drawing.RectangleF]::new(1130, 150, 370, 370)) "Candidate front v2"
Draw-ContainedImage $Graphics $Side ([System.Drawing.RectangleF]::new(1545, 150, 370, 370)) "Candidate side v2"
Draw-ContainedImage $Graphics $Back ([System.Drawing.RectangleF]::new(1960, 150, 370, 370)) "Candidate back v2"

$Notes = "Revision focus:`n- closer head/body proportions`n- layered rounded spine masses instead of one smooth shell`n- less blob-like hands and feet`n- compact plush mascot volume`n`nStage 1 scope only: no face identity/detail, no final materials, no retopo, UV, rig, animation, or Figma insertion."
$NotesRect = New-Object System.Drawing.RectangleF 1130, 610, 1200, 365
$Graphics.FillRectangle([System.Drawing.Brushes]::WhiteSmoke, $NotesRect)
$Graphics.DrawRectangle($Pen, $NotesRect.X, $NotesRect.Y, $NotesRect.Width, $NotesRect.Height)
$Graphics.DrawString($Notes, $BodyFont, $BrushDark, $NotesRect)

$Risk = "Handoff verdict should be based on silhouette only. The candidate is still a temporary Blender blockout and must not be accepted as production topology or approved master."
$RiskRect = New-Object System.Drawing.RectangleF 1130, 1025, 1200, 170
$Graphics.DrawString($Risk, $SmallFont, $BrushMuted, $RiskRect)

$Bitmap.Save($Output, [System.Drawing.Imaging.ImageFormat]::Png)

$Graphics.Dispose()
$Bitmap.Dispose()
$TitleFont.Dispose()
$LabelFont.Dispose()
$BodyFont.Dispose()
$SmallFont.Dispose()
$BrushDark.Dispose()
$BrushMuted.Dispose()
$Pen.Dispose()
