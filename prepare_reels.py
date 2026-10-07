"""Prepara los reels de Instagram para la web: vídeo completo optimizado, bucle corto
sin sonido para la vista previa, portada y fotogramas (recortados por encima de los subtítulos)."""
import subprocess
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT.parent / "Instagram descargas" / "reels"
VID = ROOT / "assets" / "video"; VID.mkdir(parents=True, exist_ok=True)
IMG = ROOT / "assets" / "images"
import imageio_ffmpeg  # pip install imageio-ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()

# nombre: (inicio del bucle, duración)
REELS = {"tecnologia": (20, 8), "familia": (11.5, 8), "fisiopilates-clases": (0.5, 8)}
# fotograma: (reel, segundo)
STILLS = {"reel-bebe": ("familia", 16), "reel-bebe-2": ("familia", 13), "reel-banda": ("familia", 24),
          "reel-fisiopilates": ("familia", 21), "reel-manual": ("tecnologia", 31), "reel-tratamiento": ("tecnologia", 27),
          "reel-electro": ("tecnologia", 57), "reel-eco-pantalla": ("tecnologia", 13), "reel-eco-rodilla": ("tecnologia", 8),
          "reel-winback": ("tecnologia", 41)}

def run(*a):
    subprocess.run([FF, "-loglevel", "error", "-y", *map(str, a)], check=True)

for name, (ss, dur) in REELS.items():
    src = SRC / f"{name}.mp4"
    run("-i", src, "-c:v", "libx264", "-crf", 26, "-preset", "slow", "-vf", "scale=720:-2", "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", VID / f"{name}.mp4")
    run("-ss", ss, "-t", dur, "-i", src, "-an", "-c:v", "libx264", "-crf", 30, "-preset", "slow", "-vf", "scale=360:-2", "-movflags", "+faststart", VID / f"{name}-loop.mp4")
    run("-ss", ss, "-i", src, "-frames:v", 1, "-q:v", 2, VID / f"{name}.jpg")
    Image.open(VID / f"{name}.jpg").save(VID / f"{name}.webp", "WEBP", quality=80); (VID / f"{name}.jpg").unlink()

Image.open(SRC / "pilates-naturaleza-portada.jpg").convert("RGB").save(VID / "pilates-naturaleza.webp", "WEBP", quality=85)

for name, (reel, t) in STILLS.items():
    tmp = VID / "tmp.png"
    run("-ss", t, "-i", SRC / f"{reel}.mp4", "-frames:v", 1, tmp)
    im = Image.open(tmp).convert("RGB")
    w, h = im.size
    im.crop((0, 0, w, int(w * 1.25))).save(IMG / f"{name}.webp", "WEBP", quality=86, method=6)
    tmp.unlink()
print("Reels preparados")
