"""Genera logotipos transparentes (color y claro), monograma, favicons e imágenes de Instagram optimizadas."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT.parent / "Fotos para usar en la WEB" / "Logotipo nítido en alta definición-1.png"
OUT = ROOT / "assets" / "brand"
OUT.mkdir(parents=True, exist_ok=True)

im = Image.open(SRC).convert("RGBA")
px = im.load()
w, h = im.size
for y in range(h):
    for x in range(w):
        r, g, b, a = px[x, y]
        lum = (r + g + b) / 3
        # fondo blanco -> transparente con borde suavizado
        alpha = max(0, min(255, int((250 - lum) * 255 / 70)))
        px[x, y] = (r, g, b, alpha)
im = im.crop(im.getbbox())
color = im.copy()
color.thumbnail((900, 900), Image.Resampling.LANCZOS)
color.save(OUT / "logo-color.png", optimize=True)

light = im.copy()
lp = light.load()
for y in range(light.height):
    for x in range(light.width):
        r, g, b, a = lp[x, y]
        lp[x, y] = (255, 250, 244, a)
light.thumbnail((900, 900), Image.Resampling.LANCZOS)
light.save(OUT / "logo-light.png", optimize=True)

# monograma (parte superior: "MC" + figura)
mono_box = (0, 0, im.width, int(im.height * 0.60))
mono = im.crop(mono_box)
mono = mono.crop(mono.getbbox())
mono_c = mono.copy(); mono_c.thumbnail((400, 400), Image.Resampling.LANCZOS); mono_c.save(OUT / "monogram.png", optimize=True)
mono_l = mono.copy(); ml = mono_l.load()
for y in range(mono_l.height):
    for x in range(mono_l.width):
        r, g, b, a = ml[x, y]; ml[x, y] = (255, 250, 244, a)
mono_l.thumbnail((400, 400), Image.Resampling.LANCZOS); mono_l.save(OUT / "monogram-light.png", optimize=True)

for size in (32, 180, 192, 512):
    canvas = Image.new("RGBA", (size, size), (250, 246, 241, 255))
    m = mono.copy(); m.thumbnail((int(size * .78), int(size * .78)), Image.Resampling.LANCZOS)
    canvas.alpha_composite(m, ((size - m.width) // 2, (size - m.height) // 2))
    canvas.convert("RGB").save(OUT / f"icon-{size}.png")

ig_src = ROOT.parent / "Instagram descargas"
ig_out = ROOT / "assets" / "images" / "ig"
ig_out.mkdir(parents=True, exist_ok=True)
for f in sorted(ig_src.glob("*.jpg")):
    Image.open(f).convert("RGB").save(ig_out / f"{f.stem}.webp", "WEBP", quality=84, method=6)
print("Marca e Instagram preparados")
