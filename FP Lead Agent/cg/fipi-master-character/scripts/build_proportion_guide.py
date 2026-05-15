from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
TURNAROUND = ROOT / "turnaround-references" / "fipi_turnaround_draft_approved_2026-05-15.png"
OUT_DIR = ROOT / "expression-material-stage"
OUT_PATH = OUT_DIR / "fipi_proportion_guide_candidate.png"


def line(draw, xy, fill, width=5):
    draw.line(xy, fill=fill, width=width)


def label(draw, xy, text, font, fill=(20, 32, 48), bg=(255, 255, 255)):
    x, y = xy
    box = draw.textbbox((x, y), text, font=font)
    pad = 6
    draw.rounded_rectangle(
        (box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad),
        radius=6,
        fill=bg,
        outline=(190, 198, 208),
    )
    draw.text((x, y), text, font=font, fill=fill)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    src = Image.open(TURNAROUND).convert("RGB")
    # Keep the image readable while adding a footer notes area.
    max_w = 1800
    if src.width > max_w:
        ratio = max_w / src.width
        src = src.resize((max_w, int(src.height * ratio)), Image.Resampling.LANCZOS)

    footer_h = 260
    canvas = Image.new("RGB", (src.width, src.height + footer_h), (246, 248, 250))
    canvas.paste(src, (0, 0))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()

    # Approximate zones for the first/front character in the turnaround sheet.
    # Coordinates are proportional to the resized image and intentionally simple:
    # this is a sculpt planning guide, not a precise measurement drawing.
    w, h = src.size
    x0 = int(w * 0.055)
    x1 = int(w * 0.255)
    y_top = int(h * 0.205)
    y_foot = int(h * 0.875)
    y_eye = int(h * 0.365)
    y_belly_top = int(h * 0.535)
    y_belly_bottom = int(h * 0.785)
    y_hand = int(h * 0.595)
    y_spine_top = int(h * 0.185)
    y_spine_back = int(h * 0.415)

    red = (225, 70, 70)
    blue = (34, 102, 220)
    green = (40, 150, 80)
    amber = (230, 150, 30)
    purple = (130, 80, 190)

    # Overall height.
    line(draw, [(x0, y_top), (x0, y_foot)], red, 6)
    line(draw, [(x0 - 18, y_top), (x0 + 18, y_top)], red, 6)
    line(draw, [(x0 - 18, y_foot), (x0 + 18, y_foot)], red, 6)
    label(draw, (x0 + 24, y_top + 10), "overall height", font)

    # Face/eye band.
    line(draw, [(int(w * 0.095), y_eye), (int(w * 0.238), y_eye)], blue, 5)
    label(draw, (int(w * 0.105), y_eye - 36), "eye band / gaze", font)

    # Belly patch.
    bx = int(w * 0.170)
    line(draw, [(bx, y_belly_top), (bx, y_belly_bottom)], green, 5)
    line(draw, [(bx - 70, y_belly_top), (bx + 70, y_belly_top)], green, 4)
    line(draw, [(bx - 70, y_belly_bottom), (bx + 70, y_belly_bottom)], green, 4)
    label(draw, (bx + 84, y_belly_top + 20), "belly patch only on torso", font)

    # Hand/arm length.
    line(draw, [(int(w * 0.086), y_hand), (int(w * 0.120), int(h * 0.700))], amber, 5)
    label(draw, (int(w * 0.045), int(h * 0.705)), "soft short arms", font)

    # Crown/back spines.
    line(draw, [(int(w * 0.135), y_spine_top), (int(w * 0.248), y_spine_back)], purple, 5)
    label(draw, (int(w * 0.150), y_spine_top - 36), "blue plush spine mass", font)

    # Side/back silhouette callout on second/back views.
    line(draw, [(int(w * 0.710), int(h * 0.255)), (int(w * 0.710), int(h * 0.800))], purple, 5)
    label(draw, (int(w * 0.725), int(h * 0.280)), "back spine volume", font)

    # Footer.
    fy = src.height + 24
    draw.text((32, fy), "Fipi Proportion Guide Candidate", font=font, fill=(18, 52, 86))
    notes = [
        "Use as sculpt planning reference, not exact CAD measurement.",
        "Preserve: green face, torso-only belly patch, compact plush body, short limbs, big eyes, small glossy nose, blue spine shell.",
        "Do not start manual sculpt until FP Lead/user approves this guide with turnaround + expressions + materials.",
    ]
    for i, note in enumerate(notes):
        draw.text((32, fy + 38 + i * 34), f"- {note}", font=font, fill=(35, 45, 58))

    canvas.save(OUT_PATH)
    print(OUT_PATH)


if __name__ == "__main__":
    main()
