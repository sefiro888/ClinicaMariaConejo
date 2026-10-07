"""Imagen para compartir en WhatsApp y redes (Open Graph, 1200x630)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "assets" / "brand" / "share.jpg"
W, H = 1200, 630

photo = Image.open(ROOT / "assets" / "images" / "maria.webp").convert("RGB")
pw, ph = photo.size
crop_h = int(pw * H / W)
top = int((ph - crop_h) * 0.35)
img = photo.crop((0, top, pw, top + crop_h)).resize((W, H), Image.LANCZOS)

shade = Image.new("L", (W, H), 0)
d = ImageDraw.Draw(shade)
for y in range(H):
    v = int(max(0, (y - H * 0.38) / (H * 0.62)) ** 1.3 * 235)
    d.line([(0, y), (W, y)], fill=v)
img = Image.composite(Image.new("RGB", (W, H), (40, 30, 25)), img, shade)

draw = ImageDraw.Draw(img)
F = Path("C:/Windows/Fonts")
serif = ImageFont.truetype(str(F / "georgia.ttf"), 54)
serif_i = ImageFont.truetype(str(F / "georgiai.ttf"), 54)
sans = ImageFont.truetype(str(F / "segoeui.ttf"), 26)
sans_b = ImageFont.truetype(str(F / "seguisb.ttf"), 22)

x = 56
draw.text((x, 420), "Fisioterapia, nutrición", font=serif, fill=(255, 250, 244))
w = draw.textlength("y ", font=serif)
draw.text((x, 482), "y", font=serif, fill=(255, 250, 244))
draw.text((x + w, 482), "podología", font=serif_i, fill=(233, 201, 153))
sym = ImageFont.truetype(str(F / "seguisym.ttf"), 24)
t1 = "Villanueva del Rosario, Málaga  ·  "
draw.text((x, 560), t1, font=sans, fill=(255, 248, 240))
sx = x + draw.textlength(t1, font=sans)
draw.text((sx, 563), "★★★★★", font=sym, fill=(233, 190, 120))
draw.text((sx + draw.textlength("★★★★★ ", font=sym), 560), "5,0 en Google", font=sans, fill=(255, 248, 240))

img.save(OUT, "JPEG", quality=85, optimize=True, progressive=True)
print(OUT, OUT.stat().st_size // 1024, "KB")
