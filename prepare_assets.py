from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "Fotos para usar en la WEB"
TARGET = ROOT / "assets" / "images"
TARGET.mkdir(parents=True, exist_ok=True)

names = {
    "Bolsa de fisioterapia sobre soporte de madera-6.png": "bolsa",
    "Clínica luminosa con dos salas abiertas-2.png": "salas",
    "Dispositivo de fisioterapia en primer plano-5.png": "dispositivo",
    "Ejercicio de fisioterapia con bandas-5.png": "bandas",
    "Ejercicios de fisioterapia en clínica-3.png": "ejercicios",
    "Equipo de fisioterapia con pantalla-3.png": "winback",
    "Fachada de clínica en alta definición-2.png": "fachada",
    "Fisioterapeuta aplicando tratamiento-2.png": "tratamiento",
    "Fisioterapeuta con modelo anatómico-4.png": "modelo",
    "Fisioterapeuta junto al equipo de tratamiento-2.png": "ecografia",
    "Fotografía clínica en alta resolución-3.png": "consulta",
    "Infografía de fisioterapia en alta definición-7.png": "infografia",
    "Interior de clínica de fisioterapia-1.png": "interior",
    "Logotipo de clínica en primer plano-3.png": "logo-escena",
    "Logotipo nítido en alta definición-1.png": "logo",
    "Manos en fisioterapia manual-6.png": "manual",
    "Mujer con laptop en la clínica-1.png": "recepcionista",
    "Pasillo clínico en alta definición-4.png": "pasillo",
    "Pilates clínico con equipo-4.png": "pilates",
    "Pilates terapéutico al aire libre-1.png": "pilates-exterior-1",
    "Pilates terapéutico al aire libre-4.png": "pilates-exterior-2",
    "Póster de políticas clínicas en alta definición-1.png": "normativa-original",
    "Recepción clínica con plantas y logo-2.png": "recepcion",
    "Retrato clínico en alta definición-2.png": "maria",
    "Sesión de fisioterapia en clínica-1.png": "sesion",
    "Tarjeta de clínica entre flores-7.png": "tarjeta",
    "Terapia de hombro con sonda-3.png": "hombro",
}

for original, slug in names.items():
    source = SOURCE / original
    if not source.exists():
        raise FileNotFoundError(source)
    image = ImageOps.exif_transpose(Image.open(source)).convert("RGB")
    image.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
    image.save(TARGET / f"{slug}.webp", "WEBP", quality=83, method=6)
print(f"Preparadas {len(names)} fotografías en {TARGET}")
