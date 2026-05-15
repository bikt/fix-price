from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT / "reference" / "fipi_master_reference.png"
OUT = ROOT / "reference-pack"


def crop_pct(img, name, box):
    w, h = img.size
    x1, y1, x2, y2 = box
    crop = img.crop((int(w * x1), int(h * y1), int(w * x2), int(h * y2)))
    path = OUT / name
    crop.save(path)
    return path


def fit(img, size):
    canvas = Image.new("RGB", size, "white")
    copy = img.copy()
    copy.thumbnail((size[0] - 24, size[1] - 74), Image.Resampling.LANCZOS)
    x = (size[0] - copy.width) // 2
    y = 64 + (size[1] - 74 - copy.height) // 2
    canvas.paste(copy, (x, y))
    return canvas


def mean_color(img, box):
    w, h = img.size
    x1, y1, x2, y2 = box
    crop = img.crop((int(w * x1), int(h * y1), int(w * x2), int(h * y2))).convert("RGB")
    pixels = list(crop.getdata())
    r = sum(p[0] for p in pixels) // len(pixels)
    g = sum(p[1] for p in pixels) // len(pixels)
    b = sum(p[2] for p in pixels) // len(pixels)
    return (r, g, b)


def hex_color(rgb):
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def make_contact_sheet(items):
    font = ImageFont.load_default()
    tile_w, tile_h = 420, 420
    cols = 3
    rows = (len(items) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tile_w, rows * tile_h), (242, 245, 248))
    draw = ImageDraw.Draw(sheet)

    for index, (title, path) in enumerate(items):
        x = (index % cols) * tile_w
        y = (index // cols) * tile_h
        draw.rectangle((x + 10, y + 10, x + tile_w - 10, y + tile_h - 10), fill="white", outline=(210, 218, 226))
        tile = fit(Image.open(path).convert("RGB"), (tile_w - 20, tile_h - 20))
        sheet.paste(tile, (x + 10, y + 10))
        draw.rectangle((x + 18, y + 18, x + tile_w - 18, y + 50), fill="white")
        draw.text((x + 24, y + 28), title, fill=(18, 52, 86), font=font)

    path = OUT / "fipi_reference_pack_contact_sheet.png"
    sheet.save(path)
    return path


def make_swatches(img):
    swatches = [
        # Manual guide swatches from the approved visual canon. Pixel averages
        # are too noisy here because the source image has strong light, shadows,
        # sky spill, and plush texture.
        ("body green guide", (116, 205, 38)),
        ("belly light green guide", (213, 233, 91)),
        ("spines blue guide", (0, 84, 196)),
        ("nose black guide", (18, 20, 20)),
        ("mouth dark guide", (45, 8, 8)),
        ("tongue red guide", (226, 87, 68)),
    ]

    font = ImageFont.load_default()
    w, h = 900, 320
    sheet = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(sheet)
    draw.text((24, 18), "Fipi canonical color guide swatches from approved reference", fill=(18, 52, 86), font=font)

    x, y = 24, 62
    for name, rgb in swatches:
        draw.rectangle((x, y, x + 105, y + 105), fill=rgb, outline=(40, 40, 40))
        draw.text((x, y + 116), name, fill=(20, 20, 20), font=font)
        draw.text((x, y + 136), hex_color(rgb), fill=(20, 20, 20), font=font)
        x += 145

    path = OUT / "fipi_reference_color_swatches.png"
    sheet.save(path)

    return path, swatches


def write_manifest(crops, contact, swatch_path, swatches):
    lines = [
        "# Fipi Sculpt Reference Pack",
        "",
        "Status: ready for manual sculpt blockout.",
        "",
        "## Source Of Truth",
        "",
        f"- Canonical reference: `{REFERENCE}`",
        "",
        "## Crops",
        "",
    ]

    for title, path in crops:
        lines.append(f"- {title}: `{path}`")

    lines += [
        "",
        "## Review Sheets",
        "",
        f"- Contact sheet: `{contact}`",
        f"- Color swatches: `{swatch_path}`",
        "",
        "## Color Guide Swatches",
        "",
    ]

    for name, rgb in swatches:
        lines.append(f"- {name}: `{hex_color(rgb)}`")

    lines += [
        "",
        "## Sculpt Priorities",
        "",
        "1. Match facial identity before scene quality.",
        "2. Match silhouette before materials.",
        "3. Match spines pattern before accessory/scenery work.",
        "4. Do not use the rejected procedural model as visual truth.",
        "5. Show blockout preview before detailed texture/rig work.",
    ]

    (OUT / "REFERENCE_PACK_MANIFEST.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    img = Image.open(REFERENCE).convert("RGB")
    (OUT / "fipi_full_canonical_reference.png").write_bytes(REFERENCE.read_bytes())

    crop_specs = [
        ("Full canonical reference", OUT / "fipi_full_canonical_reference.png"),
        ("Face identity", crop_pct(img, "crop_face_identity.png", (0.24, 0.20, 0.78, 0.55))),
        ("Eyes nose smile", crop_pct(img, "crop_eyes_nose_smile.png", (0.35, 0.32, 0.67, 0.52))),
        ("Crown spines", crop_pct(img, "crop_crown_spines.png", (0.23, 0.17, 0.77, 0.34))),
        ("Side spines", crop_pct(img, "crop_side_spines.png", (0.15, 0.27, 0.86, 0.63))),
        ("Hands and fingers", crop_pct(img, "crop_hands_fingers.png", (0.13, 0.29, 0.86, 0.47))),
        ("Belly patch", crop_pct(img, "crop_belly_patch.png", (0.35, 0.50, 0.66, 0.73))),
        ("Feet and toes", crop_pct(img, "crop_feet_toes.png", (0.30, 0.61, 0.72, 0.77))),
    ]

    contact = make_contact_sheet(crop_specs)
    swatch_path, swatches = make_swatches(img)
    write_manifest(crop_specs, contact, swatch_path, swatches)

    print("REFERENCE_PACK_READY")
    print(contact)
    print(swatch_path)


if __name__ == "__main__":
    main()
