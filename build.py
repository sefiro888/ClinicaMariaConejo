"""Genera todas las páginas HTML de la web de Fisioterapia María Conejo.

Uso:  python build.py
Los textos están en content.py; los estilos en assets/css/style.css y la
interacción en assets/js/site.js. No edites los .html a mano: se sobrescriben.
"""
import json
from html import escape
from pathlib import Path
from urllib.parse import quote

from content import (ADDRESS, AMENITIES, ANNOUNCEMENTS, CATEGORIES, CITY, COLLABORATIONS,
                     EXERCISE_BENEFITS, FINDER, HOME_FAQS, HOURS, NICA, PHONE, PHONE_INTL,
                     PILLARS, POLICY, RATING, REELS, REVIEWS, REVIEWS_COUNT, SERVICES, TEAM,
                     WINBACK_LEVELS)

ROOT = Path(__file__).resolve().parent
SITE_URL = "https://sefiro888.github.io/ClinicaMariaConejo/"
SHARE_IMG = SITE_URL + "assets/brand/share.jpg?v=1"
VERSION = "3.3"

WA_BASE = f"https://wa.me/{PHONE_INTL}"
WA = WA_BASE + "?text=" + quote("Hola, María 👋 Me gustaría pedir información o una cita en Fisioterapia María Conejo.")
IG = "https://www.instagram.com/fisiomariacm/"
FB = "https://www.facebook.com/p/Fisioterapia-Mar%C3%ADa-Conejo-61560371157858/"
MAP = "https://www.google.com/maps/search/?api=1&query=" + quote("Clínica Fisioterapia María Conejo, C. Fuente Toril, 24, 29312 Villanueva del Rosario, Málaga")
REVIEWS_URL = "https://www.google.com/maps/place/Cl%C3%ADnica+Fisioterapia+Mar%C3%ADa+Conejo/@37.0026564,-4.3687152,17z/data=!4m8!3m7!1s0xd7263121ad990bb:0xd9c6a05a087b7f2d!8m2!3d37.0026564!4d-4.3687152!9m1!1b1"
MAP_EMBED = "https://www.google.com/maps?q=" + quote("Clínica Fisioterapia María Conejo, Villanueva del Rosario") + "&output=embed"

ILLUSTRATIVE = set()  # ya no se usa ninguna imagen generada

BY_SLUG = {s["slug"]: s for s in SERVICES}


def e(value):
    return escape(str(value), quote=True)


def wa(text):
    return WA_BASE + "?text=" + quote(text)


def wa_service(item):
    return wa(f"Hola, María 👋 Me gustaría pedir información sobre «{item['title']}».")


def tag(name):
    return '<span class="illus">Imagen ilustrativa</span>' if name in ILLUSTRATIVE else ''


def img(name, alt, cls="", loading="lazy", sizes=""):
    folder = "assets/images/"
    return f'<img class="{e(cls)}" src="{folder}{e(name)}.webp" alt="{e(alt)}" loading="{loading}" decoding="async">'


def visual(item, alt=None, cls=""):
    """Foto real del servicio o, si no hay foto real adecuada, tarjeta gráfica de marca."""
    if item.get("tile"):
        area = CATEGORIES[item["category"]]["title"]
        return f'<div class="brand-tile {cls}" role="img" aria-label="{e(alt or item["title"])}"><img class="bt-mono" src="assets/brand/monogram-light.png" alt=""><span class="bt-ic">{icon(item["tile"])}</span><span class="bt-area">{area}</span><span class="bt-title">{e(item["title"])}</span></div>'
    return img(item["image"], alt or item["title"], cls)


# ───────────────────────────── ICONOS ─────────────────────────────
ICONS = {
    "arrow": '<path d="M5 12h14m-6-6 6 6-6 6"/>',
    "arrow-up-right": '<path d="M7 17 17 7M8 7h9v9"/>',
    "chevron": '<path d="m6 9 6 6 6-6"/>',
    "left": '<path d="m15 18-6-6 6-6"/>',
    "right": '<path d="m9 18 6-6-6-6"/>',
    "menu": '<path d="M4 8h16M4 16h10"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "check": '<path d="m5 12.5 4.2 4.2L19 7"/>',
    "phone": '<path d="M6.6 3.5H5a1.9 1.9 0 0 0-1.9 2c.4 8 7.4 15 15.4 15.4a1.9 1.9 0 0 0 2-1.9v-1.6a1.2 1.2 0 0 0-.9-1.2l-3.4-1a1.2 1.2 0 0 0-1.2.3l-1.4 1.4a13 13 0 0 1-5.6-5.6L9.4 9.9a1.2 1.2 0 0 0 .3-1.2l-1-3.4a1.2 1.2 0 0 0-1.2-.9Z"/>',
    "whatsapp": '<path d="M4 20l1.2-3.8A8 8 0 1 1 8 19z"/><path d="M9.2 8.6c.2-.5.5-.6.8-.6h.5c.2 0 .4.1.5.4l.7 1.6c.1.2 0 .5-.1.6l-.5.6c.6 1.1 1.5 2 2.6 2.6l.6-.5c.2-.2.4-.2.6-.1l1.6.7c.3.1.4.3.4.5v.5c0 .3-.2.6-.6.8-.6.3-1.5.4-2.6 0a8 8 0 0 1-4.4-4.4c-.4-1.1-.3-2 0-2.7Z"/>',
    "pin": '<path d="M20 10c0 5.5-8 12-8 12S4 15.5 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.6"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "insta": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>',
    "facebook": '<path d="M15 21v-8h3l.5-4H15V7c0-1 .5-1.5 1.5-1.5H19V2.2A20 20 0 0 0 16.5 2C13 2 11 4 11 7v2H8v4h3v8"/>',
    "star": '<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9Z"/>',
    "leaf": '<path d="M5 19c0-8 5-14 15-14 0 10-6 15-14 15"/><path d="M5 19c3-4 6-6 10-8"/>',
    "wave": '<path d="M3 12c2-4 4-4 6 0s4 4 6 0 4-4 6 0"/><path d="M3 17c2-3 4-3 6 0s4 3 6 0 4-3 6 0" opacity=".5"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7Z"/>',
    "gift": '<rect x="3" y="8" width="18" height="13" rx="1.5"/><path d="M12 8v13M3 12h18M12 8S10.5 3 8 3.5 7 8 12 8Zm0 0s1.5-5 4-4.5S17 8 12 8Z"/>',
    "baby": '<circle cx="12" cy="8" r="4.5"/><path d="M10.5 8h.01M13.5 8h.01M10.8 9.8c.7.5 1.7.5 2.4 0M5 21c1-4 4-6 7-6s6 2 7 6"/>',
    "home": '<path d="m3 11 9-7 9 7"/><path d="M5 10v10h14V10M10 20v-6h4v6"/>',
    "heart": '<path d="M12 20s-7.5-4.6-9.2-9.3C1.6 7.3 3.8 4 7.2 4c2 0 3.6 1.1 4.8 2.8C13.2 5.1 14.8 4 16.8 4c3.4 0 5.6 3.3 4.4 6.7C19.5 15.4 12 20 12 20Z"/>',
    "card": '<rect x="2.5" y="5" width="19" height="14" rx="2"/><path d="M2.5 10h19M6 15h4"/>',
    "car": '<path d="M5 17h14M4 17v-4l2-5h12l2 5v4M4 17v2M20 17v2"/><circle cx="7.5" cy="14" r=".8"/><circle cx="16.5" cy="14" r=".8"/>',
    "access": '<circle cx="12" cy="4.5" r="1.8"/><path d="M8 8.5h8M12 8.5V14l-3 6M12 14l3 6"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>',
    "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>',
    "quote": '<path d="M9 7H5v6h4v-2c0 2-1 4-3 4M19 7h-4v6h4v-2c0 2-1 4-3 4"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "bag": '<path d="M5 8h14l-1 13H6Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>',
    "map": '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2Z"/><path d="M9 4v14M15 6v14"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    "shield": '<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.4 7.5 9.5 4.3-1.1 7.5-4.9 7.5-9.5V6Z"/><path d="m8.8 12 2.2 2.2 4.4-4.4"/>',
    "hand": '<path d="M8 12V5.5a1.5 1.5 0 0 1 3 0V11M11 10V4a1.5 1.5 0 0 1 3 0v6M14 10V5.5a1.5 1.5 0 0 1 3 0V13c0 4.5-2.5 8-7 8-3 0-4.5-1.5-6-4l-1.6-3a1.5 1.5 0 0 1 2.6-1.5L8 15"/>',
    "foot": '<path d="M8 21c-2.5 0-3.5-2-3-5 .4-2.6 2-4 2-7 0-2.5 1.5-4 3.5-4S13 7 13 10c0 3-2 4-2 7 0 2.5-.5 4-3 4Z"/><circle cx="15" cy="5" r="1.2"/><circle cx="17.5" cy="7.5" r="1"/><circle cx="19" cy="10.5" r=".9"/>',
    "apple": '<path d="M12 7c-2-2-7-1.5-7 4 0 4 3 10 5 10 1 0 1.5-.6 2-.6s1 .6 2 .6c2 0 5-6 5-10 0-5.5-5-6-7-4Z"/><path d="M12 7c0-2 1-4 3-4"/>',
    "pulse": '<path d="M3 12h4l2-5 4 10 2-5h6"/>',
    "play": '<path d="M8 5.5v13l11-6.5Z" fill="currentColor"/>',
    "sound": '<path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4Z"/><path d="M16 9a4 4 0 0 1 0 6M18.5 6.5a7.5 7.5 0 0 1 0 11"/>',
}


def icon(name, cls=""):
    return f'<svg class="ic {cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'


AREA_ICON = {"fisioterapia": "hand", "nutricion": "apple", "podologia": "foot"}


def stars(n=5):
    return '<span class="stars" aria-label="5 de 5 estrellas">' + ''.join(icon('star') for _ in range(n)) + '</span>'


# ───────────────────────────── CABECERA ─────────────────────────────
def announcement():
    items = ''.join(f'<span class="ann-item">{icon(ic)}{e(t)}</span><span class="ann-dot" aria-hidden="true">✦</span>' for ic, t in ANNOUNCEMENTS)
    return f'''<div class="announce" role="region" aria-label="Avisos de la clínica">
  <div class="announce-status" data-open-status><span class="pulse-dot"></span><b>Consultando horario…</b></div>
  <div class="announce-track"><div class="announce-move">{items}{items}</div></div>
  <a class="announce-cta" href="{WA}" target="_blank" rel="noopener">Pedir cita {icon('arrow')}</a>
</div>'''


def mega_menu():
    cols = []
    for slug, cat in CATEGORIES.items():
        links = ''.join(
            f'<a href="servicio-{s["slug"]}.html" data-preview="{s["image"]}" data-preview-title="{e(s["title"])}" data-preview-text="{e(s["short"])}"><span>{e(s["title"])}</span><small>{e(s["short"])}</small></a>'
            for s in SERVICES if s["category"] == slug)
        cols.append(f'<div class="mega-col"><a class="mega-cat" href="{slug}.html" data-preview="{cat["image"]}" data-preview-title="{e(cat["title"])}" data-preview-text="{e(cat["eyebrow"])}">{icon(AREA_ICON[slug])}<span>{cat["title"]}</span>{icon("arrow")}</a><div class="mega-links">{links}</div></div>')
    first = SERVICES[0]
    return f'''<div class="mega" id="mega-servicios" role="region" aria-label="Servicios">
  <div class="mega-inner">
    <div class="mega-grid">{''.join(cols)}</div>
    <aside class="mega-preview">
      <div class="mega-preview-media">{img(CATEGORIES["fisioterapia"]["image"], "", "mega-img", "lazy")}</div>
      <div class="mega-preview-copy"><span class="eyebrow light" data-mp-text>Movimiento, recuperación y prevención</span><strong data-mp-title>Fisioterapia</strong></div>
      <a class="mega-all" href="servicios.html">Ver los 22 servicios {icon("arrow")}</a>
    </aside>
  </div>
</div>'''


def header(active=""):
    def link(name, href):
        cur = ' aria-current="page"' if active == href else ''
        return f'<a href="{href}" class="nav-link"{cur}><span data-text="{name}">{name}</span></a>'

    m_areas = ''
    for slug, cat in CATEGORIES.items():
        subs = ''.join(f'<a href="servicio-{s["slug"]}.html">{e(s["title"])}</a>' for s in SERVICES if s["category"] == slug)
        m_areas += f'<details class="m-acc"><summary><span class="m-acc-ic">{icon(AREA_ICON[slug])}</span><span><b>{cat["title"]}</b><small>{e(cat["eyebrow"])}</small></span>{icon("plus", "m-plus")}</summary><div class="m-acc-body"><a class="m-acc-all" href="{slug}.html">Ver área de {cat["title"].lower()} {icon("arrow")}</a>{subs}</div></details>'

    return f'''<a class="skip-link" href="#contenido">Saltar al contenido</a>
{announcement()}
<header class="site-header" id="cabecera">
  <div class="header-inner">
    <a class="brand" href="index.html" aria-label="Fisioterapia María Conejo, inicio">
      <img class="brand-color" src="assets/brand/logo-color.png" alt="Fisioterapia María Conejo" width="150" height="110">
      <img class="brand-light" src="assets/brand/logo-light.png" alt="" width="150" height="110">
    </a>
    <nav class="desktop-nav" aria-label="Navegación principal">
      {link('Inicio', 'index.html')}
      <div class="nav-drop">
        <button type="button" class="nav-link nav-drop-btn" aria-expanded="false" aria-controls="mega-servicios"><span data-text="Servicios">Servicios</span>{icon('chevron')}</button>
        {mega_menu()}
      </div>
      {link('La clínica', 'clinica.html')}
      {link('Información', 'informacion.html')}
      {link('Contacto', 'contacto.html')}
    </nav>
    <div class="header-actions">
      <a class="header-phone" href="tel:+{PHONE_INTL}" aria-label="Llamar al {PHONE}">{icon('phone')}<span>{PHONE}</span></a>
      <a class="btn btn-primary btn-sm magnetic" href="contacto.html#reserva">Pedir cita {icon('arrow')}</a>
      <button class="menu-toggle" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu" aria-hidden="true">
  <div class="m-backdrop" data-close-menu></div>
  <div class="m-panel" role="dialog" aria-modal="true" aria-label="Menú">
    <div class="m-top"><img src="assets/brand/logo-color.png" alt="Fisioterapia María Conejo" class="m-logo"><button type="button" class="m-close" data-close-menu aria-label="Cerrar menú">{icon('close')}</button></div>
    <div class="m-status" data-open-status><span class="pulse-dot"></span><b>Consultando horario…</b></div>
    <nav class="m-nav" aria-label="Navegación móvil">
      <a href="index.html" class="m-link"><span>01</span>Inicio</a>
      <a href="servicios.html" class="m-link"><span>02</span>Todos los servicios</a>
      <div class="m-areas">{m_areas}</div>
      <a href="clinica.html" class="m-link"><span>03</span>La clínica y el equipo</a>
      <a href="informacion.html" class="m-link"><span>04</span>Información útil</a>
      <a href="contacto.html" class="m-link"><span>05</span>Contacto</a>
    </nav>
    <div class="m-quick">
      <a href="{WA}" target="_blank" rel="noopener">{icon('whatsapp')}<span>WhatsApp</span></a>
      <a href="tel:+{PHONE_INTL}">{icon('phone')}<span>Llamar</span></a>
      <a href="{MAP}" target="_blank" rel="noopener">{icon('pin')}<span>Cómo llegar</span></a>
    </div>
    <a class="btn btn-primary btn-block" href="contacto.html#reserva">Reservar cita {icon('arrow')}</a>
    <div class="m-foot"><span>{ADDRESS} · Villanueva del Rosario</span><div class="socials"><a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{icon('insta')}</a><a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{icon('facebook')}</a></div></div>
  </div>
</div>'''


# ───────────────────────────── PIE ─────────────────────────────
def hours_list(cls="hours"):
    rows = ''
    for i, (day, spans) in enumerate(HOURS):
        txt = ' · '.join(f'{a:02d}:00–{b:02d}:00' for a, b in spans) if spans else 'Cerrado'
        rows += f'<li data-day="{i}"><span>{day}</span><b>{txt}</b></li>'
    return f'<ul class="{cls}">{rows}</ul>'


def footer():
    cats = ''.join(f'<a href="{s}.html">{v["title"]}</a>' for s, v in CATEGORIES.items())
    popular = ''.join(f'<a href="servicio-{s}.html">{BY_SLUG[s]["title"]}</a>' for s in ["fisiopilates", "ecografia-musculoesqueletica", "tecnicas-invasivas", "fisioterapia-pediatrica", "estudio-pisada"])
    return f'''<section class="pre-footer">
  <div class="container pre-footer-inner reveal">
    <img src="assets/brand/monogram.png" alt="" class="pf-mono" aria-hidden="true">
    <p class="script">Te acompañamos en el proceso</p>
    <h2>¿Empezamos a cuidarte?</h2>
    <p>Escríbenos y te ayudamos a encontrar la atención que necesitas. Respondemos lo antes posible.</p>
    <div class="pf-actions"><a class="btn btn-primary magnetic" href="contacto.html#reserva">Reservar mi cita {icon('arrow')}</a><a class="btn btn-ghost" href="tel:+{PHONE_INTL}">{icon('phone')} {PHONE}</a></div>
  </div>
</section>
<footer class="footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <img src="assets/brand/logo-light.png" alt="Fisioterapia María Conejo" class="footer-logo" loading="lazy">
      <p>Clínica de fisioterapia, nutrición y podología en Villanueva del Rosario. Un lugar para escucharte, comprender tu proceso y acompañarte en cada paso.</p>
      <div class="footer-rating">{stars()}<span><b>{RATING}</b> en Google · {REVIEWS_COUNT} opiniones</span></div>
      <div class="socials"><a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{icon('insta')}</a><a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{icon('facebook')}</a><a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{icon('whatsapp')}</a></div>
    </div>
    <div class="footer-col"><h3>Áreas</h3>{cats}<a href="servicios.html">Todos los servicios</a></div>
    <div class="footer-col"><h3>Destacados</h3>{popular}</div>
    <div class="footer-col"><h3>Clínica</h3><a href="clinica.html">Conoce a María</a><a href="clinica.html#equipo">Equipo</a><a href="clinica.html#tecnologia">Tecnología</a><a href="informacion.html#normativa">Normativa</a><a href="informacion.html#bonos">Bonos y tarjetas regalo</a><a href="contacto.html">Contacto</a></div>
    <div class="footer-col footer-hours"><h3>Horario</h3>{hours_list('hours hours-dark')}<p class="footer-addr">{icon('pin')}<span>{ADDRESS}<br>{CITY}</span></p><a class="footer-map" href="{MAP}" target="_blank" rel="noopener">Cómo llegar {icon('arrow-up-right')}</a></div>
  </div>
  <div class="container footer-bottom"><span>© <span data-year>2026</span> Fisioterapia María Conejo · Centro sanitario NICA {NICA}</span><span>Web de demostración · Diseño a medida</span></div>
</footer>
<nav class="action-bar" aria-label="Acciones rápidas">
  <a href="tel:+{PHONE_INTL}">{icon('phone')}<span>Llamar</span></a>
  <a href="{WA}" target="_blank" rel="noopener">{icon('whatsapp')}<span>WhatsApp</span></a>
  <a href="contacto.html#reserva" class="ab-main">{icon('calendar')}<span>Cita</span></a>
  <a href="{MAP}" target="_blank" rel="noopener">{icon('pin')}<span>Llegar</span></a>
  <button type="button" data-open-menu>{icon('menu')}<span>Menú</span></button>
</nav>
<a class="float-ig" href="{IG}" target="_blank" rel="noopener" aria-label="Seguir a la clínica en Instagram">{icon('insta')}<span>Síguenos</span></a>
<a class="float-wa" href="{WA}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">{icon('whatsapp')}<span>¿Hablamos?</span></a>
<div class="reel-modal" id="reel-modal" role="dialog" aria-modal="true" aria-label="Vídeo" hidden>
  <div class="rm-backdrop" data-close-reel></div>
  <div class="rm-box">
    <button type="button" class="rm-close" data-close-reel aria-label="Cerrar vídeo">{icon('close')}</button>
    <div class="rm-phone"><video controls playsinline preload="none"></video></div>
    <div class="rm-copy"><span class="eyebrow light">Reel · @fisiomariacm</span><h3 data-rm-title></h3><p data-rm-text></p><small data-rm-credit></small><a class="btn btn-light btn-sm" data-rm-url href="{IG}" target="_blank" rel="noopener">{icon('insta')} Ver en Instagram</a></div>
  </div>
</div>
<button class="to-top" type="button" aria-label="Volver arriba"><svg viewBox="0 0 44 44" aria-hidden="true"><circle cx="22" cy="22" r="20" class="tt-track"/><circle cx="22" cy="22" r="20" class="tt-bar"/></svg>{icon('arrow')}</button>'''


def page(title, description, body, active="", cls="", extra_head="", filename="index.html"):
    url = SITE_URL + ("" if filename == "index.html" else filename)
    og_title = "Fisioterapia María Conejo · Villanueva del Rosario" if filename == "index.html" else f"{title} · Fisioterapia María Conejo"
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)} · Fisioterapia María Conejo</title>
<meta name="description" content="{e(description)}">
<meta name="theme-color" content="#4a3a30">
<meta name="robots" content="noindex">
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="Fisioterapia María Conejo">
<meta property="og:locale" content="es_ES">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(og_title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:image" content="{SHARE_IMG}">
<meta property="og:image:secure_url" content="{SHARE_IMG}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="María Conejo en la recepción de su clínica de fisioterapia, nutrición y podología">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(og_title)}">
<meta name="twitter:description" content="{e(description)}">
<meta name="twitter:image" content="{SHARE_IMG}">
<link rel="icon" href="assets/brand/icon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/brand/icon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Allura&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={VERSION}">
<script>document.documentElement.classList.add('js');try{{if(!sessionStorage.getItem('mc-intro')&&!matchMedia('(prefers-reduced-motion: reduce)').matches){{document.documentElement.classList.add('show-intro');sessionStorage.setItem('mc-intro','1')}}}}catch(e){{}}</script>
<script src="assets/js/site.js?v={VERSION}" defer></script>
{extra_head}
</head>
<body class="{cls}{' has-hero' if cls != 'nf-page' else ''}">
<div class="intro" aria-hidden="true"><div class="intro-inner"><img src="assets/brand/monogram.png" alt=""><span class="intro-line"></span><p>Fisioterapia · Nutrición · Podología</p></div></div>
{header(active)}
<main id="contenido">
{body}
</main>
{footer()}
</body>
</html>'''


# ───────────────────────────── BLOQUES ─────────────────────────────
def head(eyebrow, title, text="", center=False, light=False):
    return f'''<div class="sec-head{' center' if center else ''}{' on-dark' if light else ''} reveal"><span class="eyebrow{' light' if light else ''}">{e(eyebrow)}</span><h2>{title}</h2>{f'<p>{e(text)}</p>' if text else ''}</div>'''


def service_card(item, index=None):
    n = f'<span class="sc-num">{index:02d}</span>' if index else ''
    cat = CATEGORIES[item["category"]]
    return f'''<a class="s-card reveal" href="servicio-{item["slug"]}.html">
  <div class="s-card-media">{visual(item)}<span class="s-card-cat">{icon(AREA_ICON[item["category"]])}{cat["title"]}</span></div>
  <div class="s-card-body">{n}<h3>{e(item["title"])}</h3><p>{e(item["lead"])}</p><span class="s-card-link">Descubrir {icon("arrow")}</span></div>
</a>'''


def area_card(slug, cat, i):
    items = [s for s in SERVICES if s["category"] == slug]
    lis = ''.join(f'<li><a href="servicio-{s["slug"]}.html">{e(s["title"])}</a></li>' for s in items)
    return f'''<article class="area-card reveal" style="--d:{i * 120}ms">
  <a href="{slug}.html" class="area-media" aria-label="{cat['title']}">{img(cat["image"], cat["title"])}{tag(cat["image"])}</a>
  <div class="area-body">
    <div class="area-top"><span class="area-ic">{icon(AREA_ICON[slug])}</span><span class="area-count">{len(items):02d} servicios</span></div>
    <h3><a href="{slug}.html">{cat["title"]}</a></h3>
    <p>{e(cat["lead"])}</p>
    <ul class="area-list">{lis}</ul>
    <a class="link-arrow" href="{slug}.html">Explorar {cat["title"].lower()} {icon("arrow")}</a>
  </div>
</article>'''


def page_hero(eyebrow, title, text, image, crumbs="", actions="", extra=""):
    crumb = f'<nav class="crumbs" aria-label="Ruta"><a href="index.html">Inicio</a>{crumbs}</nav>' if crumbs is not None else ''
    return f'''<section class="page-hero">
  <div class="ph-media">{img(image, "", "", "eager")}</div>
  <div class="ph-shade"></div>
  <div class="container ph-content">
    {crumb}
    <span class="eyebrow light ph-eyebrow">{e(eyebrow)}</span>
    <h1 class="ph-title split">{title}</h1>
    <p class="ph-lead">{e(text)}</p>
    {f'<div class="ph-actions">{actions}</div>' if actions else ''}
    {extra}
  </div>
  {tag(image)}
  <div class="ph-scroll" aria-hidden="true"><span></span></div>
</section>'''


def faq_list(faqs, open_first=True):
    return '<div class="faq-list">' + ''.join(
        f'<details class="faq"{" open" if (i == 0 and open_first) else ""}><summary><span class="faq-n">{i + 1:02d}</span><span class="faq-q">{e(q)}</span><span class="faq-ic">{icon("plus")}</span></summary><div class="faq-a"><p>{e(a)}</p></div></details>'
        for i, (q, a) in enumerate(faqs)) + '</div>'


def reviews_block(title="Lo que dicen nuestros pacientes", dark=False):
    cards = ''.join(f'''<figure class="review">
  <div class="review-top">{stars()}<span class="g-badge">Google</span></div>
  <blockquote>{e(t)}</blockquote>
  <figcaption><span class="avatar">{n[0]}</span><span><b>{e(n)}</b><small>{e(w)} · Reseña verificada en Google Maps</small></span></figcaption>
</figure>''' for n, w, t in REVIEWS)
    return f'''<section class="section reviews-sec{' dark' if dark else ''}" id="opiniones">
  <div class="container">
    <div class="reviews-head reveal">
      <div><span class="eyebrow">Opiniones reales</span><h2>{title}</h2></div>
      <div class="rating-box"><b class="rating-num" data-count="5" data-decimals="1">{RATING}</b><div>{stars()}<span>{REVIEWS_COUNT} opiniones en Google</span></div></div>
    </div>
    <div class="reviews-track" data-carousel>{cards}</div>
    <div class="reviews-foot reveal"><div class="car-btns"><button type="button" data-car-prev aria-label="Opinión anterior">{icon('left')}</button><button type="button" data-car-next aria-label="Opinión siguiente">{icon('right')}</button></div><a class="link-arrow" href="{REVIEWS_URL}" target="_blank" rel="noopener">Ver todas las opiniones en Google {icon('arrow-up-right')}</a></div>
  </div>
</section>'''


def booking_block(preset_area="", preset_service="", title="Reserva tu cita en 1 minuto"):
    areas = ''.join(f'<button type="button" class="chip" data-area="{s}">{icon(AREA_ICON[s])}{c["title"]}</button>' for s, c in CATEGORIES.items())
    return f'''<section class="section booking-sec" id="reserva">
  <div class="container booking-grid">
    <div class="booking-copy reveal">
      <span class="eyebrow">Reserva guiada</span>
      <h2>{title}</h2>
      <p>Responde tres preguntas y te preparamos el mensaje para enviarlo por WhatsApp. No guardamos ningún dato: tú decides si lo envías.</p>
      <ul class="booking-points"><li>{icon('check')}Respuesta en horario de clínica</li><li>{icon('check')}Sin compromiso</li><li>{icon('check')}Te orientamos si no sabes qué servicio elegir</li></ul>
      <div class="booking-alt"><span>¿Prefieres hablar?</span><a href="tel:+{PHONE_INTL}">{icon('phone')} {PHONE}</a></div>
    </div>
    <form class="booking reveal" data-booking data-preset-area="{preset_area}" data-preset-service="{preset_service}" novalidate>
      <div class="bk-progress"><span class="is-on">1</span><i></i><span>2</span><i></i><span>3</span></div>
      <fieldset class="bk-step is-active" data-step="1">
        <legend>¿Qué necesitas?</legend>
        <div class="chips">{areas}<button type="button" class="chip" data-area="orientacion">{icon('search')}No lo sé, oriéntame</button></div>
        <label class="field" data-service-field hidden><span>Servicio</span><select name="servicio"></select></label>
        <div class="bk-nav"><span></span><button type="button" class="btn btn-primary btn-sm" data-next disabled>Siguiente {icon('arrow')}</button></div>
      </fieldset>
      <fieldset class="bk-step" data-step="2">
        <legend>¿Cuándo te viene mejor?</legend>
        <div class="chips" data-group="franja"><button type="button" class="chip" data-value="por la mañana (11:00–14:00)">Mañana</button><button type="button" class="chip" data-value="por la tarde (15:00–21:00)">Tarde</button><button type="button" class="chip" data-value="cuando haya hueco">Me da igual</button></div>
        <div class="chips small" data-group="modalidad"><button type="button" class="chip is-on" data-value="en la clínica">{icon('home')}En la clínica</button><button type="button" class="chip" data-value="a domicilio">{icon('car')}A domicilio</button></div>
        <div class="bk-nav"><button type="button" class="btn-text" data-prev>{icon('left')} Atrás</button><button type="button" class="btn btn-primary btn-sm" data-next disabled>Siguiente {icon('arrow')}</button></div>
      </fieldset>
      <fieldset class="bk-step" data-step="3">
        <legend>Último paso</legend>
        <label class="field"><span>Tu nombre</span><input name="nombre" autocomplete="given-name" placeholder="¿Cómo te llamas?"></label>
        <label class="field"><span>Cuéntanos brevemente (opcional)</span><textarea name="detalle" rows="3" placeholder="Ej.: dolor de hombro desde hace dos semanas"></textarea></label>
        <div class="bk-preview"><span>Vista previa del mensaje</span><p data-preview-msg></p></div>
        <div class="bk-nav"><button type="button" class="btn-text" data-prev>{icon('left')} Atrás</button><a class="btn btn-wa" data-send href="{WA}" target="_blank" rel="noopener">{icon('whatsapp')} Abrir WhatsApp</a></div>
      </fieldset>
    </form>
  </div>
</section>'''


def map_block():
    return f'''<div class="map-box reveal" data-map="{MAP_EMBED}">
  <div class="map-placeholder">
    {img('fachada', 'Fachada de la clínica en C. Fuente Toril, 24')}
    <div class="map-ph-copy"><span class="map-pin">{icon('pin')}</span><b>{ADDRESS}</b><span>{CITY}</span><button type="button" class="btn btn-light btn-sm" data-load-map>Ver mapa interactivo {icon('map')}</button><a href="{MAP}" target="_blank" rel="noopener" class="link-arrow light">Abrir en Google Maps {icon('arrow-up-right')}</a></div>
  </div>
</div>'''


def hours_card():
    return f'''<div class="hours-card reveal">
  <div class="hc-head"><span class="hc-ic">{icon('clock')}</span><div><span class="eyebrow">Horario</span><div class="hc-status" data-open-status><span class="pulse-dot"></span><b>Consultando…</b></div></div></div>
  {hours_list()}
  <p class="muted">Atención con cita previa. Festivos: consultar.</p>
</div>'''


def ig_strip():
    items = [("ig-compromiso", "Tu visita, nuestro compromiso"), ("ig-movimiento", "Tu recuperación empieza con movimiento"), ("ig-detalle", "Cuidamos cada detalle"),
             ("ig-dedicacion", "Detrás de cada tratamiento hay dedicación"), ("ig-fisiopilates-naturaleza", "Muévete, respira y reconecta contigo"), ("ig-winback-precision", "Fisioterapia basada en precisión y cuidado"),
             ("ig-precision", "Trabajamos con precisión para cuidar de ti"), ("ig-aire-libre", "FisioPilates al aire libre")]
    tiles = ''.join(f'<a class="ig-tile reveal" style="--d:{i * 60}ms" href="{IG}" target="_blank" rel="noopener"><img src="assets/images/ig/{n}.webp" alt="{e(t)}" loading="lazy"><span class="ig-over">{icon("insta")}<em>{e(t)}</em></span></a>' for i, (n, t) in enumerate(items))
    return f'''<section class="section ig-sec">
  <div class="container">
    <div class="ig-head reveal"><div><span class="eyebrow">@fisiomariacm</span><h2>Síguenos en <em>Instagram</em></h2><p>Consejos, novedades, FisioPilates al aire libre y el día a día de la clínica.</p></div><a class="btn btn-outline" href="{IG}" target="_blank" rel="noopener">{icon('insta')} Seguir en Instagram</a></div>
    <div class="ig-grid">{tiles}</div>
  </div>
</section>'''


def exercise_wheel():
    pts = ''.join(f'<li class="wheel-item" style="--i:{i}"><span class="wheel-n">0{i + 1}</span><p>{e(t)}</p></li>' for i, t in enumerate(EXERCISE_BENEFITS))
    return f'''<section class="section wheel-sec">
  <div class="container wheel-grid">
    <div class="reveal">
      <span class="eyebrow light">Recuperación activa</span>
      <h2>El ejercicio en tu <em>recuperación</em></h2>
      <p>El movimiento es una de las herramientas más poderosas de la fisioterapia. Por eso, en casi todos los tratamientos, te enseñamos ejercicios adaptados y comprobamos que los haces bien.</p>
      <a class="btn btn-light magnetic" href="servicio-ejercicio-terapeutico.html">Ejercicio terapéutico {icon('arrow')}</a>
    </div>
    <div class="wheel reveal" aria-label="Beneficios del ejercicio">
      <div class="wheel-core"><img src="assets/brand/monogram-light.png" alt=""><b>6 razones</b><span>para moverte</span></div>
      <svg class="wheel-ring" viewBox="0 0 400 400" aria-hidden="true"><circle cx="200" cy="200" r="150"/><circle cx="200" cy="200" r="190" class="ring2"/></svg>
      <ol>{pts}</ol>
    </div>
  </div>
</section>'''


def winback_block():
    tabs = ''.join(f'<button type="button" class="wb-tab{" is-on" if i == 0 else ""}" data-wb="{i}" role="tab" aria-selected="{"true" if i == 0 else "false"}"><b>{e(n)}</b><span>Nivel {e(d.lower())}</span></button>' for i, (n, d, t, p) in enumerate(WINBACK_LEVELS))
    panels = ''.join(f'<p class="wb-text{" is-on" if i == 0 else ""}" data-wb-text="{i}">{e(t)}</p>' for i, (n, d, t, p) in enumerate(WINBACK_LEVELS))
    return f'''<div class="winback reveal">
  <div class="wb-visual" data-level="0" aria-hidden="true">
    <div class="wb-layer l1"><span>Piel</span></div><div class="wb-layer l2"><span>Músculo</span></div><div class="wb-layer l3"><span>Tendón · articulación</span></div>
    <div class="wb-beam"></div><div class="wb-head"></div>
  </div>
  <div class="wb-ui"><div class="wb-tabs" role="tablist">{tabs}</div>{panels}</div>
</div>'''


# ───────────────────────────── REELS ─────────────────────────────
def reel_card(key, i=0, cls=""):
    r = REELS[key]
    if r["video"]:
        return f'''<button type="button" class="reel-card reveal {cls}" style="--d:{i * 100}ms" data-reel="{key}" data-title="{e(r['title'])}" data-text="{e(r['text'])}" data-url="{r['url']}" data-credit="{e(r.get('credit', ''))}" aria-label="Ver vídeo: {e(r['title'])}">
  <video class="reel-vid" data-autoplay src="assets/video/{key}-loop.mp4" poster="assets/video/{key}.webp" muted loop playsinline preload="none" aria-hidden="true"></video>
  <span class="reel-shade"></span><span class="reel-tag">{icon('insta')}{e(r['tag'])}</span><span class="reel-play">{icon('play')}</span>
  <span class="reel-copy"><b>{e(r['title'])}</b><small>{icon('sound')} Ver con sonido</small></span>
</button>'''
    return f'''<a class="reel-card reveal {cls}" style="--d:{i * 100}ms" href="{r['url']}" target="_blank" rel="noopener" aria-label="Ver en Instagram: {e(r['title'])}">
  <img class="reel-vid" src="assets/video/{key}.webp" alt="" loading="lazy">
  <span class="reel-shade"></span><span class="reel-tag">{icon('insta')}{e(r['tag'])}</span><span class="reel-play">{icon('arrow-up-right')}</span>
  <span class="reel-copy"><b>{e(r['title'])}</b><small>{icon('insta')} Ver en Instagram</small></span>
</a>'''


def reels_strip(title="La clínica <em>en vídeo</em>", text="Reels reales de la clínica: pulsa en cualquiera para verlo con sonido."):
    cards = ''.join(reel_card(k, i) for i, k in enumerate(REELS))
    return f'''<section class="section reels-sec">
  <div class="container">
    <div class="ig-head reveal"><div><span class="eyebrow light">Reels · @fisiomariacm</span><h2>{title}</h2><p>{e(text)}</p></div><a class="btn btn-light" href="{IG}" target="_blank" rel="noopener">{icon('insta')} Ver más en Instagram</a></div>
    <div class="reels-grid">{cards}</div>
  </div>
</section>'''


def reel_feature(keys, heading="Míralo <em>en vídeo</em>"):
    main = REELS[keys[0]]
    cards = ''.join(reel_card(k, i, "phone") for i, k in enumerate(keys))
    return f'''<section class="section reel-feature">
  <div class="container rf-grid">
    <div class="rf-copy">
      <span class="eyebrow light reveal">Desde nuestro Instagram</span>
      <h2 class="reveal">{heading}</h2>
      <p class="rf-title reveal">{e(main['title'])}</p>
      <p class="reveal">{e(main['text'])}</p>
      <div class="hs-actions reveal"><a class="btn btn-light" href="{main['url']}" target="_blank" rel="noopener">{icon('insta')} Ver en Instagram</a><a class="btn btn-glass" href="{IG}" target="_blank" rel="noopener">Seguir a @fisiomariacm</a></div>
    </div>
    <div class="rf-phones n{len(keys)}">{cards}</div>
  </div>
</section>'''


# ───────────────────────────── PORTADA ─────────────────────────────
def home():
    slides = [
        ("Clínica de fisioterapia en Villanueva del Rosario", "Tu salud merece <em>tiempo</em> y escucha", "Fisioterapia, nutrición y podología con un enfoque cercano, una valoración completa y tecnología de última generación.", "maria", "clinica.html", "Conoce la clínica", "24% 30%"),
        ("FisioPilates · Movimiento con propósito", "Recupera la <em>confianza</em> en tu movimiento", "Grupos reducidos o sesiones individuales guiadas por una fisioterapeuta titulada. También al aire libre.", "pilates-exterior-2", "servicio-fisiopilates.html", "Descubrir FisioPilates", "50% 50%"),
        ("Ecografía musculoesquelética", "Ver más allá de los <em>síntomas</em>", "Imágenes en tiempo real para valorar tus tejidos, personalizar el tratamiento y seguir tu evolución. Sin radiación e indolora.", "ecografia", "servicio-ecografia-musculoesqueletica.html", "Saber más", "40% 50%"),
        ("Tecnología Winback", "Terapia inteligente, <em>resultados</em> reales", "Radiofrecuencia de alta, media y baja frecuencia para aliviar el dolor y acelerar tu recuperación.", "tratamiento", "servicio-tecarterapia-diatermia.html", "Conocer Winback", "50% 50%"),
    ]
    slide_html = ''
    rail = ''
    for i, (eb, title, text, im, link, cta_txt, pos) in enumerate(slides):
        h = 'h1' if i == 0 else 'h2'
        load = 'eager' if i == 0 else 'lazy'
        slide_html += f'''<article class="hero-slide{' is-current' if i == 0 else ''}" aria-hidden="{'false' if i == 0 else 'true'}" data-index="{i}">
  <div class="hs-media"><img src="assets/images/{im}.webp" alt="" loading="{load}" style="object-position:{pos}"{' fetchpriority="high"' if i == 0 else ''}></div>
  <div class="container hs-content">
    <span class="eyebrow light hs-eyebrow"><span class="eb-line"></span>{e(eb)}</span>
    <{h} class="hs-title">{title}</{h}>
    <p class="hs-text">{e(text)}</p>
    <div class="hs-actions"><a class="btn btn-light magnetic" href="{link}">{cta_txt} {icon('arrow')}</a><a class="btn btn-glass" href="contacto.html#reserva">{icon('calendar')} Pedir cita</a></div>
  </div>
</article>'''
        rail += f'<button type="button" class="rail-item{" is-active" if i == 0 else ""}" data-slide-to="{i}" aria-label="Ver: {e(eb)}"><span class="rail-n">0{i + 1}</span><span class="rail-t">{e(eb.split(" · ")[0])}</span><span class="rail-bar"><i></i></span></button>'

    ticker_words = ["Fisioterapia", "FisioPilates", "Ecografía", "Punción seca", "Winback", "Pediatría", "Nutrición", "Podología", "Estudio de la pisada", "Ejercicio terapéutico", "Terapia manual", "A domicilio"]
    ticker = ''.join(f'<span>{w}</span><img src="assets/brand/monogram.png" alt="" aria-hidden="true">' for w in ticker_words)

    finder_btns = ''.join(f'<button type="button" class="f-chip{" is-on" if i == 0 else ""}" data-finder="{i}" role="tab" aria-selected="{"true" if i == 0 else "false"}">{e(label)}</button>' for i, (label, _, _) in enumerate(FINDER))
    finder_panels = ''
    for i, (label, text, slugs) in enumerate(FINDER):
        cards = ''.join(f'<a class="f-card" href="servicio-{s}.html">{visual(BY_SLUG[s], cls="mini")}<span><small>{CATEGORIES[BY_SLUG[s]["category"]]["title"]}</small><b>{e(BY_SLUG[s]["title"])}</b></span>{icon("arrow")}</a>' for s in slugs)
        finder_panels += f'<div class="f-panel{" is-on" if i == 0 else ""}" data-finder-panel="{i}" role="tabpanel"><p class="f-text">{e(text)}</p><div class="f-cards">{cards}</div><a class="link-arrow" href="{wa("Hola, María 👋 Os escribo porque: " + label.lower() + ". ¿Me podéis orientar?")}" target="_blank" rel="noopener">Consultar mi caso por WhatsApp {icon("arrow")}</a></div>'

    areas = ''.join(area_card(s, c, i) for i, (s, c) in enumerate(CATEGORIES.items()))
    pillars = ''.join(f'<div class="pillar reveal" style="--d:{i * 120}ms"><span class="pillar-n">0{i + 1}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(PILLARS))
    steps = [("Te escuchamos", "Conocemos tu historia, tus hábitos y lo que te preocupa."), ("Valoramos", "Exploración completa y ecografía cuando aporta información."), ("Diseñamos tu plan", "Elegimos contigo las técnicas y los objetivos."), ("Avanzamos juntos", "Ejercicios para casa, seguimiento y ajustes.")]
    steps_html = ''.join(f'<li class="step reveal" style="--d:{i * 120}ms"><span class="step-dot">0{i + 1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(steps))
    collab = ''.join(f'<li><b>{e(n)}</b><span>{e(d)}</span></li>' for n, d in COLLABORATIONS)
    faqs = faq_list(HOME_FAQS[:6])

    return f'''<section class="home-hero" data-slider>
  {slide_html}
  <div class="hero-grain" aria-hidden="true"></div>
  <div class="hero-badge reveal-late"><span class="hb-g">G</span><div><b>{RATING}</b>{stars()}<small>{REVIEWS_COUNT} opiniones en Google</small></div></div>
  <div class="hero-bottom container"><div class="hero-rail">{rail}</div><div class="hero-nav"><span class="hero-count"><b data-current>01</b> / 0{len(slides)}</span><button type="button" data-prev aria-label="Anterior">{icon('left')}</button><button type="button" data-next aria-label="Siguiente">{icon('right')}</button></div></div>
</section>

<div class="ticker" aria-hidden="true"><div class="ticker-move">{ticker}{ticker}</div></div>

<section class="section welcome">
  <div class="container welcome-grid">
    <div class="welcome-media reveal">
      <div class="wm-main">{img('recepcion', 'Recepción de la Clínica Fisioterapia María Conejo')}</div>
      <div class="wm-small">{img('modelo', 'María Conejo explicando con un modelo anatómico')}</div>
      <div class="wm-card"><img src="assets/brand/monogram.png" alt=""><span>Atención integral<br><b>Villanueva del Rosario</b></span></div>
    </div>
    <div class="welcome-copy">
      <span class="eyebrow reveal">Bienvenida a la clínica</span>
      <h2 class="reveal">Cada persona es <em>única</em>. Tu tratamiento, también.</h2>
      <p class="lead reveal">En Clínica María Conejo trabajamos para que cada persona reciba una atención integral en su proceso de recuperación. La fisioterapia va más allá: se trata de comprender a fondo tu estado y acompañarte de manera cercana y segura.</p>
      <p class="reveal">Por eso comenzamos siempre con una valoración completa y personalizada —tu historial, tus hábitos y tus necesidades— para diseñar un plan adaptado a ti, con el objetivo de mejorar tu bienestar, recuperar tu movilidad y prevenir futuras lesiones.</p>
      <div class="stats reveal">
        <div><b data-count="5" data-decimals="1">5,0</b><span>Valoración en Google</span></div>
        <div><b data-count="{REVIEWS_COUNT}">{REVIEWS_COUNT}</b><span>Opiniones de pacientes</span></div>
        <div><b data-count="3">3</b><span>Áreas de salud</span></div>
        <div><b data-count="{len(SERVICES)}">{len(SERVICES)}</b><span>Servicios</span></div>
      </div>
      <a class="link-arrow reveal" href="clinica.html">Conoce nuestra forma de trabajar {icon('arrow')}</a>
    </div>
  </div>
</section>

<section class="section finder-sec" id="que-te-ocurre">
  <div class="container">
    {head('Encuentra tu tratamiento', '¿Qué te <em>ocurre</em>?', 'Elige lo que mejor describe tu situación y te mostramos por dónde empezar.', center=True)}
    <div class="finder reveal">
      <div class="f-chips" role="tablist">{finder_btns}</div>
      <div class="f-panels">{finder_panels}</div>
    </div>
  </div>
</section>

<section class="section areas-sec">
  <div class="container">
    {head('Tres formas de cuidarte', 'Fisioterapia, nutrición y <em>podología</em>', 'Un mismo centro, tres áreas coordinadas para cuidarte de forma integral.')}
    <div class="areas">{areas}</div>
    <div class="center-end reveal"><a class="btn btn-outline" href="servicios.html">Ver los {len(SERVICES)} servicios {icon('arrow')}</a></div>
  </div>
</section>

<section class="section method-sec">
  <div class="container">
    {head('Nuestro método', 'Primero, tu historia. <em>Después</em>, un plan.', 'Así es el camino que recorremos contigo desde la primera visita.', center=True)}
    <ol class="steps">{steps_html}</ol>
    <div class="pillars">{pillars}</div>
  </div>
</section>

<section class="section tech-sec" id="tecnologia">
  <div class="container">
    {head('Tecnología al servicio del cuidado', 'Precisión que se <em>nota</em>', 'Incorporamos tecnología de última generación porque aporta seguridad, optimiza los resultados y te ayuda a sentirte confiado en todo momento.', light=True)}
    <div class="tech-grid">
      <article class="tech-card reveal">
        <div class="tech-media">{img('ecografia', 'Ecógrafo de la clínica mostrando una imagen musculoesquelética')}<span class="tech-live"><i></i>Imagen en tiempo real</span></div>
        <div class="tech-body">
          <span class="eyebrow light">Ecógrafo de última generación</span>
          <h3>Ecografía musculoesquelética</h3>
          <p>Nos permite ver más allá de los síntomas y personalizar tu tratamiento al máximo.</p>
          <ul class="ticks light"><li>{icon('check')}Visualización en tiempo real de músculos, tendones y articulaciones</li><li>{icon('check')}Mayor precisión en punción seca e infiltraciones</li><li>{icon('check')}Seguimiento detallado de tu recuperación</li><li>{icon('check')}Sin radiación, seguro y totalmente indoloro</li></ul>
          <a class="link-arrow light" href="servicio-ecografia-musculoesqueletica.html">Más sobre la ecografía {icon('arrow')}</a>
        </div>
      </article>
      <article class="tech-card reveal" style="--d:150ms">
        <div class="tech-body">
          <span class="eyebrow light">Diatermia Winback</span>
          <h3>Radiofrecuencia en tres niveles</h3>
          <p>Combina alta, media y baja frecuencia para actuar a nivel superficial, medio y profundo. Pulsa cada nivel:</p>
          {winback_block()}
          <a class="link-arrow light" href="servicio-tecarterapia-diatermia.html">Más sobre Winback {icon('arrow')}</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="pilates-band">
  <div class="pb-media">{img('pilates-exterior-1', 'Sesión de FisioPilates al aire libre en la sierra')}</div>
  <div class="pb-shade"></div>
  <div class="container pb-content">
    <div class="pb-copy reveal">
      <span class="script light">Muévete, respira y reconecta contigo</span>
      <h2>FisioPilates, también <em>al aire libre</em></h2>
      <p>Siente cómo tu cuerpo gana fuerza, equilibrio y bienestar en contacto con la naturaleza. Y en la sala, sesiones guiadas para mejorar tu postura, fortalecer tu core y prevenir lesiones.</p>
      <ul class="ticks light inline"><li>{icon('check')}Grupo reducido</li><li>{icon('check')}Adaptado a cada persona</li><li>{icon('check')}Guiado por fisioterapeuta</li></ul>
      <div class="hs-actions"><a class="btn btn-light magnetic" href="servicio-fisiopilates.html">Descubrir FisioPilates {icon('arrow')}</a><a class="btn btn-glass" href="{wa('Hola, María 👋 Me interesa reservar plaza en FisioPilates. ¿Qué horarios tenéis?')}" target="_blank" rel="noopener">{icon('whatsapp')} Reservar plaza</a></div>
    </div>
    <div class="pb-phone">{reel_card('fisiopilates-clases', 0, 'phone')}</div>
  </div>
</section>

{exercise_wheel()}

<section class="section maria-sec">
  <div class="container maria-grid">
    <div class="maria-media reveal">
      <div class="maria-frame">{img('maria', 'María Conejo Martín, fisioterapeuta y directora del centro')}</div>
      <span class="maria-sign">María Conejo</span>
    </div>
    <div class="maria-copy">
      <span class="eyebrow reveal">¡Te presentamos a María!</span>
      <h2 class="reveal">Ciencia, técnica y <em>empatía</em></h2>
      <p class="lead reveal">Graduada en Fisioterapia y con un Máster en Fisioterapia Manual e Invasiva para el Tratamiento del Dolor y de la Disfunción por la Universidad de Granada.</p>
      <p class="reveal">Especializada además en fisioterapia pediátrica, atención temprana, neonatología y educación, María cree firmemente en el poder del acompañamiento terapéutico, la educación en salud y la escucha activa como pilares de una recuperación efectiva.</p>
      <ul class="creds reveal"><li><b>Máster · UGR</b><span>Fisioterapia manual e invasiva</span></li><li><b>Pediatría</b><span>Atención temprana y neonatología</span></li><li><b>Ecografía</b><span>Valoración musculoesquelética</span></li></ul>
      <a class="btn btn-outline reveal" href="clinica.html#equipo">Conoce al equipo {icon('arrow')}</a>
    </div>
  </div>
</section>

{reels_strip()}

<section class="kids-band">
  <div class="container kids-grid">
    <div class="kids-media reveal">{img('reel-bebe', 'Fisioterapia pediátrica: manos de la fisioterapeuta sujetando el pie de un bebé')}</div>
    <div class="kids-copy reveal">
      <span class="eyebrow">Fisioterapia pediátrica</span>
      <h2>Para los más <em>pequeños</em>, desde sus primeros días</h2>
      <div class="kids-tags"><span>🍼 Cólico del lactante</span><span>👶🏼 Deformidades craneales</span><span>🚼 Trastornos del desarrollo</span><span>👦🏼 Patologías pediátricas</span><span>🔎 Valoración y prevención</span><span>👩🏼‍🍼 Asesoramiento de lactancia</span></div>
      <a class="link-arrow" href="servicio-fisioterapia-pediatrica.html">Conocer la atención pediátrica {icon('arrow')}</a>
    </div>
  </div>
</section>

{reviews_block()}

<section class="section gift-sec">
  <div class="container gift-grid">
    <div class="gift-card reveal">
      <div class="gift-media">{img('tarjeta', 'Tarjeta de la clínica Fisioterapia María Conejo')}</div>
      <div class="gift-body"><span class="eyebrow">Bonos y tarjetas regalo</span><h3>Regala bienestar</h3><p>Bonos de sesiones de fisioterapia y tarjetas regalo con 1 año de validez. Pregúntanos sin compromiso.</p><a class="link-arrow" href="{wa('Hola, María 👋 Me gustaría información sobre bonos o tarjetas regalo.')}" target="_blank" rel="noopener">Pedir información {icon('arrow')}</a></div>
    </div>
    <div class="collab-card reveal" style="--d:150ms">
      <span class="eyebrow">Creemos en el poder de los vínculos</span>
      <h3>Convenios con entidades locales</h3>
      <p>Colaboramos con agrupaciones de la zona para mejorar el acceso a la fisioterapia y compartir nuestra pasión por la salud y el bienestar.</p>
      <ul class="collab-list">{collab}</ul>
      <a class="link-arrow" href="{wa('Hola, María 👋 Pertenezco a una entidad/club y me gustaría información sobre convenios.')}" target="_blank" rel="noopener">¿Tu entidad quiere colaborar? {icon('arrow')}</a>
    </div>
  </div>
</section>

{ig_strip()}

<section class="section faq-home">
  <div class="container faq-grid">
    <div>
      {head('Resolvemos tus dudas', 'Preguntas <em>frecuentes</em>', 'Lo que más nos preguntáis antes de la primera visita.')}
      {hours_card()}
    </div>
    <div class="reveal">{faqs}<a class="link-arrow" href="informacion.html#preguntas">Ver más preguntas {icon('arrow')}</a></div>
  </div>
</section>

{booking_block()}

<section class="section visit-sec">
  <div class="container visit-grid">
    {map_block()}
    <div class="visit-copy reveal">
      <span class="eyebrow">Cómo llegar</span>
      <h2>Te esperamos en <em>Villanueva del Rosario</em></h2>
      <p>Estamos en {ADDRESS}, con aparcamiento gratuito en la calle y acceso adaptado para silla de ruedas.</p>
      <ul class="amen">{''.join(f'<li>{icon(i)}<span>{e(t)}</span></li>' for i, t in AMENITIES)}</ul>
    </div>
  </div>
</section>'''


# ───────────────────────────── SERVICIOS ─────────────────────────────
def all_services():
    jump = ''.join(f'<a href="#{s}" class="jump-link">{icon(AREA_ICON[s])}{c["title"]}<small>{sum(1 for x in SERVICES if x["category"] == s)}</small></a>' for s, c in CATEGORIES.items())
    parts = ''
    for slug, cat in CATEGORIES.items():
        cards = ''.join(service_card(x, i + 1) for i, x in enumerate(x for x in SERVICES if x['category'] == slug))
        parts += f'<section class="section svc-block" id="{slug}"><div class="container">{head(cat["eyebrow"], cat["title"], cat["lead"])}<div class="s-grid">{cards}</div><div class="center-end reveal"><a class="btn btn-outline" href="{slug}.html">Entrar en {cat["title"].lower()} {icon("arrow")}</a></div></div></section>'
    return page_hero('Todos los servicios', 'Un cuidado <em>pensado</em> para ti', 'Fisioterapia, nutrición y podología: explora cada servicio con información clara, preguntas frecuentes y reserva directa.', 'salas', '<span>Servicios</span>', f'<a class="btn btn-light" href="#que-te-ocurre">¿No sabes cuál elegir? {icon("arrow")}</a>') + f'<nav class="jump container reveal" aria-label="Ir a un área">{jump}</nav>' + parts + finder_section() + booking_block()


def finder_section():
    btns = ''.join(f'<button type="button" class="f-chip{" is-on" if i == 0 else ""}" data-finder="{i}" role="tab" aria-selected="{"true" if i == 0 else "false"}">{e(l)}</button>' for i, (l, _, _) in enumerate(FINDER))
    panels = ''
    for i, (label, text, slugs) in enumerate(FINDER):
        cards = ''.join(f'<a class="f-card" href="servicio-{s}.html">{visual(BY_SLUG[s], cls="mini")}<span><small>{CATEGORIES[BY_SLUG[s]["category"]]["title"]}</small><b>{e(BY_SLUG[s]["title"])}</b></span>{icon("arrow")}</a>' for s in slugs)
        panels += f'<div class="f-panel{" is-on" if i == 0 else ""}" data-finder-panel="{i}" role="tabpanel"><p class="f-text">{e(text)}</p><div class="f-cards">{cards}</div></div>'
    return f'<section class="section finder-sec" id="que-te-ocurre"><div class="container">{head("Encuentra tu tratamiento", "¿Qué te <em>ocurre</em>?", "Elige lo que mejor describe tu situación.", center=True)}<div class="finder reveal"><div class="f-chips" role="tablist">{btns}</div><div class="f-panels">{panels}</div></div></div></section>'


def category_page(slug):
    cat = CATEGORIES[slug]
    items = [x for x in SERVICES if x['category'] == slug]
    cards = ''.join(service_card(x, i + 1) for i, x in enumerate(items))
    hl = ''.join(f'<div class="hl reveal" style="--d:{i * 100}ms"><span class="hl-n">0{i + 1}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(cat['highlights']))
    member = next((m for m in TEAM if m['name'] == cat['pro']), None)
    pro = ''
    if member:
        photo = img(member['image'], member['name']) if member['image'] else '<div class="mono-avatar"><img src="assets/brand/monogram.png" alt=""></div>'
        pro = f'<aside class="pro-card reveal"><div class="pro-photo">{photo}</div><div><span class="eyebrow">Te atiende</span><h3>{e(member["name"])}</h3><p class="pro-role">{e(member["role"])}</p><p>{e(member["bio"][0])}</p><a class="link-arrow" href="clinica.html#equipo">Conocer al equipo {icon("arrow")}</a></div></aside>'
    else:
        pro = f'<aside class="pro-card reveal"><div class="pro-photo"><div class="mono-avatar"><img src="assets/brand/monogram.png" alt=""></div></div><div><span class="eyebrow">Te atiende</span><h3>Servicio de podología</h3><p>Profesional de podología del centro, en coordinación con el área de fisioterapia para abordar la pisada, la postura y el dolor de forma global.</p><a class="link-arrow" href="contacto.html">Pedir información {icon("arrow")}</a></div></aside>'
    extra = ''
    if slug == 'fisioterapia':
        extra = exercise_wheel() + reviews_block('Pacientes de fisioterapia')
    return page_hero(cat['eyebrow'], cat['title'], cat['lead'], cat['hero'], f'<a href="servicios.html">Servicios</a><span>{cat["title"]}</span>', f'<a class="btn btn-light" href="#servicios-area">Ver servicios {icon("arrow")}</a><a class="btn btn-glass" href="contacto.html#reserva">{icon("calendar")} Pedir cita</a>') + f'''
<section class="section cat-intro">
  <div class="container cat-intro-grid">
    <div><span class="eyebrow reveal">Nuestra atención</span><h2 class="reveal">Un plan que parte de <em>ti</em></h2>{''.join(f'<p class="reveal{" lead" if i == 0 else ""}">{e(p)}</p>' for i, p in enumerate(cat['intro']))}</div>
    {pro}
  </div>
  <div class="container hl-grid">{hl}</div>
</section>
<section class="section section-soft" id="servicios-area"><div class="container">{head('Explora esta área', f'Servicios de {cat["title"].lower()}', 'Entra en cada página para saber para quién es, cómo es la sesión, qué traer y las respuestas a las dudas más habituales.')}<div class="s-grid">{cards}</div></div></section>
{extra}
<section class="section"><div class="container faq-grid"><div>{head('Dudas frecuentes', f'Sobre {cat["title"].lower()}', 'Si tu pregunta no está aquí, escríbenos.')}{hours_card()}</div><div class="reveal">{faq_list(cat['faqs'])}</div></div></section>
{booking_block(preset_area=slug)}'''


def service_page(item):
    cat = CATEGORIES[item['category']]
    slug = item['slug']
    crumbs = f'<a href="servicios.html">Servicios</a><a href="{item["category"]}.html">{cat["title"]}</a><span>{e(item["title"])}</span>'
    facts = ''.join(f'<div class="fact"><small>{e(l)}</small><b>{e(v)}</b></div>' for l, v in item['facts'])
    actions = f'<a class="btn btn-light magnetic" href="#reserva">{icon("calendar")} Reservar</a><a class="btn btn-glass" href="{wa_service(item)}" target="_blank" rel="noopener">{icon("whatsapp")} Preguntar</a>'
    hero = page_hero(item['kicker'], e(item['title']), item['lead'], item['hero'], crumbs, actions, f'<div class="facts">{facts}</div>')

    subnav = '<nav class="subnav" aria-label="En esta página"><div class="container subnav-inner"><a href="#resumen" class="is-active">Resumen</a><a href="#beneficios">Beneficios</a><a href="#para-quien">Para quién</a><a href="#sesion">La sesión</a><a href="#preguntas">Preguntas</a><a href="#reserva" class="subnav-cta">Reservar</a></div></nav>'

    member = next((m for m in TEAM if m['name'] == cat['pro']), None)
    pro_name = member['name'] if member else 'Servicio de podología'
    pro_role = member['role'] if member else 'Profesional de podología del centro'
    pro_photo = (img(member['image'], member['name']) if member and member['image'] else '<div class="mono-avatar sm"><img src="assets/brand/monogram.png" alt=""></div>')

    aside = f'''<aside class="side-card reveal">
  <div class="side-pro">{pro_photo}<div><small>Te atiende</small><b>{e(pro_name)}</b><span>{e(pro_role)}</span></div></div>
  <ul class="side-list"><li>{icon('pin')}<span>{e(item['place'])}</span></li><li>{icon('clock')}<span>L–J 11–14 · 15–21 h<br>V 11–14 · 15–20 h</span></li><li>{icon('shield')}<span>Valoración individual antes de empezar</span></li></ul>
  <a class="btn btn-primary btn-block" href="#reserva">Reservar cita {icon('arrow')}</a>
  <a class="btn btn-ghost-dark btn-block" href="{wa_service(item)}" target="_blank" rel="noopener">{icon('whatsapp')} Consultar por WhatsApp</a>
</aside>'''

    benefits = ''.join(f'<div class="benefit reveal" style="--d:{i * 100}ms"><span class="benefit-ic">{icon(["spark", "target", "heart", "shield"][i % 4])}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(item['benefits']))
    audience = ''.join(f'<li class="reveal" style="--d:{i * 60}ms">{icon("check")}<span>{e(x)}</span></li>' for i, x in enumerate(item['audience']))
    process = ''.join(f'<li class="tl-item reveal" style="--d:{i * 120}ms"><span class="tl-dot">0{i + 1}</span><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>' for i, (t, d) in enumerate(item['process']))
    prepare = ''.join(f'<li>{icon("bag")}<span>{e(x)}</span></li>' for x in item['prepare'])
    note = f'<div class="note-card reveal"><span class="script">Para tener en cuenta</span><p>{e(item["note"])}</p></div>' if item['note'] else ''

    # Extras visuales por servicio
    extras = ''
    gallery_map = {
        'fisiopilates': [('pilates', 'FisioPilates en la sala con fitball'), ('pilates-exterior-1', 'FisioPilates al aire libre'), ('ejercicios', 'Grupo reducido de FisioPilates'), ('pilates-exterior-2', 'Estiramientos en la naturaleza')],
        'ecografia-musculoesqueletica': [('ecografia', 'Ecógrafo de la clínica'), ('hombro', 'Ecografía de hombro'), ('consulta', 'María junto al ecógrafo'), ('reel-eco-rodilla', 'Ecografía de rodilla en consulta')],
        'tecarterapia-diatermia': [('winback', 'Equipo Winback'), ('tratamiento', 'Aplicación de diatermia en el brazo'), ('dispositivo', 'Cabezal del equipo Winback'), ('sesion', 'Sesión con tecnología Winback')],
        'terapia-manual': [('reel-tratamiento', 'Terapia manual en camilla'), ('modelo', 'María explicando la columna con un modelo anatómico')],
        'ejercicio-terapeutico': [('reel-banda', 'Ejercicio con banda elástica'), ('bandas', 'Trabajo de fuerza con bandas'), ('reel-fisiopilates', 'Ejercicio guiado por la fisioterapeuta'), ('ejercicios', 'Ejercicio terapéutico en grupo reducido')],
        'fisioterapia-pediatrica': [('reel-bebe-2', 'Fisioterapia pediátrica con un bebé'), ('recepcionista', 'María Conejo, especializada en pediatría y neonatología')],
        'rehabilitacion-postquirurgica': [('reel-electro', 'Electroestimulación durante la recuperación'), ('reel-tratamiento', 'Tratamiento tras una lesión')],
        'tecnicas-invasivas': [('reel-eco-pantalla', 'Imagen ecográfica para guiar la técnica'), ('consulta', 'María junto al ecógrafo')],
    }
    if slug in gallery_map:
        g = ''.join(f'<figure class="gal-item reveal" style="--d:{i * 80}ms" data-lightbox="{n}" data-caption="{e(c)}">{img(n, c)}{tag(n)}<figcaption>{e(c)}</figcaption></figure>' for i, (n, c) in enumerate(gallery_map[slug]))
        extras += f'<section class="section section-soft"><div class="container">{head("Galería", "Así lo <em>vivimos</em> en la clínica", center=True)}<div class="gallery g{len(gallery_map[slug])}">{g}</div></div></section>'
    if slug == 'tecarterapia-diatermia':
        extras += f'<section class="section tech-sec"><div class="container tech-solo">{head("¿Cómo actúa esta tecnología?", "Tres frecuencias, tres <em>profundidades</em>", "Pulsa cada nivel para ver en qué capa actúa y qué efecto tiene.", light=True)}{winback_block()}</div></section>'
    if slug == 'ejercicio-terapeutico':
        extras += exercise_wheel()

    reel_html = ''
    if item['reel']:
        keys = [item['reel']] + (['pilates-naturaleza'] if slug == 'fisiopilates' else [])
        reel_html = reel_feature(keys)

    is_fisio = item['category'] == 'fisioterapia'
    review = ''
    if is_fisio:
        n, w, t = REVIEWS[sum(map(ord, slug)) % len(REVIEWS)]
        review = f'<section class="section quote-sec"><div class="container"><figure class="big-quote reveal">{icon("quote", "q-ic")}<blockquote>{e(t)}</blockquote><figcaption>{stars()}<b>{e(n)}</b><span>Opinión en Google · {e(w)}</span></figcaption></figure></div></section>'

    others = [x for x in SERVICES if x['category'] == item['category'] and x['slug'] != slug]
    related = ''.join(service_card(x) for x in others)
    other_areas = ''.join(f'<a class="oa-link" href="{s}.html">{icon(AREA_ICON[s])}<span><b>{c["title"]}</b><small>{e(c["eyebrow"])}</small></span>{icon("arrow")}</a>' for s, c in CATEGORIES.items() if s != item['category'])

    return hero + subnav + f'''
<section class="section detail" id="resumen">
  <div class="container detail-grid">
    <div class="detail-main">
      <span class="eyebrow reveal">{e(cat['title'])} · {e(item['kicker'])}</span>
      <h2 class="reveal">{e(item['title'])}, <em>explicado</em> con calma</h2>
      {''.join(f'<p class="reveal{" lead" if i == 0 else ""}">{e(p)}</p>' for i, p in enumerate(item['intro']))}
      {note}
    </div>
    {aside}
  </div>
</section>
<section class="section section-soft" id="beneficios"><div class="container">{head('Beneficios', '¿Qué puede <em>aportarte</em>?', center=True)}<div class="benefits">{benefits}</div></div></section>
{reel_html}
<section class="section" id="para-quien">
  <div class="container audience-grid">
    <div class="audience-media reveal">{visual(item)}<div class="am-badge">{icon('heart')}<span>Valoración individual<br><b>antes de empezar</b></span></div></div>
    <div>{head('¿Cuándo consultar?', 'Puede ser para ti <em>si…</em>')}<ul class="check-grid">{audience}</ul><p class="muted reveal">La indicación concreta se determina siempre tras valorar tu caso.</p></div>
  </div>
</section>
<section class="section section-dark" id="sesion">
  <div class="container session-grid">
    <div>{head('¿Qué puedes esperar?', 'Así es el <em>proceso</em>', 'Paso a paso, para que sepas en todo momento qué hacemos y por qué.', light=True)}<ol class="timeline">{process}</ol></div>
    <div class="prepare-card reveal"><span class="eyebrow">Antes de venir</span><h3>Qué traer o tener en cuenta</h3><ul class="prepare">{prepare}</ul><div class="prepare-foot">{icon('clock')}<span>Si no puedes acudir, avísanos con al menos <b>12 horas</b> de antelación.</span></div></div>
  </div>
</section>
{extras}
{review}
<section class="section" id="preguntas"><div class="container faq-grid"><div>{head('Resolvemos tus dudas', 'Preguntas <em>frecuentes</em>', 'Información útil antes de dar el primer paso.')}<div class="faq-help reveal"><p>¿No encuentras tu respuesta?</p><a class="btn btn-outline btn-sm" href="{wa_service(item)}" target="_blank" rel="noopener">{icon('whatsapp')} Pregúntanos</a></div></div><div class="reveal">{faq_list(item['faqs'])}</div></div></section>
{booking_block(preset_area=item['category'], preset_service=slug, title=f'Reserva: {item["title"]}')}
<section class="section section-soft related"><div class="container">{head('Sigue explorando', f'Más en <em>{cat["title"].lower()}</em>')}<div class="rel-track" data-carousel>{related}</div><div class="reviews-foot"><div class="car-btns"><button type="button" data-car-prev aria-label="Anterior">{icon('left')}</button><button type="button" data-car-next aria-label="Siguiente">{icon('right')}</button></div><a class="link-arrow" href="{item['category']}.html">Ver toda el área {icon('arrow')}</a></div><div class="other-areas reveal"><span class="eyebrow">Otras áreas del centro</span>{other_areas}</div></div></section>'''


# ───────────────────────────── LA CLÍNICA ─────────────────────────────
def clinic_page():
    maria, ana = TEAM
    tl = ''.join(f'<li class="reveal" style="--d:{i * 100}ms"><span class="tl-year">{e(a)}</span><p>{e(b)}</p></li>' for i, (a, b) in enumerate(maria['milestones']))
    ana_tl = ''.join(f'<li><b>{e(a)}</b><span>{e(b)}</span></li>' for a, b in ana['milestones'])
    gal = [('recepcion', 'Recepción con el logotipo de la clínica'), ('salas', 'Salas de tratamiento luminosas'), ('fachada', 'Fachada en C. Fuente Toril, 24'), ('interior', 'Interior de la clínica'),
           ('pasillo', 'Pasillo y sala 2'), ('logo-escena', 'Logotipo en la pared de la clínica'), ('recepcionista', 'Atención en recepción'), ('consulta', 'Consulta con ecógrafo'), ('bolsa', 'Detalles de la marca'), ('tarjeta', 'Tarjeta de la clínica')]
    g = ''.join(f'<figure class="gal-item reveal" style="--d:{(i % 4) * 80}ms" data-lightbox="{n}" data-caption="{e(c)}">{img(n, c)}<figcaption>{e(c)}</figcaption></figure>' for i, (n, c) in enumerate(gal))
    pillars = ''.join(f'<div class="pillar reveal" style="--d:{i * 120}ms"><span class="pillar-n">0{i + 1}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(PILLARS))
    collab = ''.join(f'<li><b>{e(n)}</b><span>{e(d)}</span></li>' for n, d in COLLABORATIONS)
    return page_hero('Nuestra clínica', 'Un cuidado cercano, <em>con criterio</em>', 'Un espacio luminoso en Villanueva del Rosario para escucharte, valorar tu situación y avanzar contigo.', 'logo-escena', '<span>La clínica</span>', f'<a class="btn btn-light" href="#equipo">Conocer al equipo {icon("arrow")}</a>') + f'''
<section class="section welcome">
  <div class="container welcome-grid">
    <div class="welcome-media reveal"><div class="wm-main">{img('interior', 'Interior de la clínica')}</div><div class="wm-small">{img('salas', 'Salas de tratamiento')}</div></div>
    <div class="welcome-copy">
      <span class="eyebrow reveal">Nuestra filosofía</span>
      <h2 class="reveal">La fisioterapia va <em>más allá</em></h2>
      <p class="lead reveal">En Clínica María Conejo trabajamos para que cada persona reciba una atención integral en su proceso de recuperación. Se trata de comprender a fondo el estado de cada paciente y acompañarlo de manera cercana y segura.</p>
      <p class="reveal">Creemos que cada persona es única. Por eso comenzamos siempre con una valoración completa y personalizada, analizando tu historial, tus hábitos y tus necesidades específicas. Solo así podemos diseñar un plan de tratamiento adaptado a ti.</p>
      <p class="script reveal">¡gracias siempre!</p>
    </div>
  </div>
  <div class="container pillars">{pillars}</div>
</section>
<section class="section section-soft" id="equipo">
  <div class="container">
    {head('El equipo', 'Las personas detrás de <em>cada paso</em>', center=True)}
    <article class="team-feature">
      <div class="tf-media reveal"><div class="maria-frame">{img('maria', maria['name'])}</div><span class="maria-sign">María Conejo</span></div>
      <div class="tf-copy">
        <span class="eyebrow reveal">{e(maria['role'])}</span>
        <h3 class="reveal">{e(maria['name'])}</h3>
        {''.join(f'<p class="reveal{" lead" if i == 0 else ""}">{e(p)}</p>' for i, p in enumerate(maria['bio']))}
        <ol class="milestones">{tl}</ol>
      </div>
    </article>
    <div class="team-row">
      <article class="team-card reveal"><div class="mono-avatar"><img src="assets/brand/monogram.png" alt=""></div><div><span class="eyebrow">{e(ana['role'])}</span><h3>{e(ana['name'])}</h3>{''.join(f'<p>{e(p)}</p>' for p in ana['bio'])}<ul class="mini-creds">{ana_tl}</ul><a class="link-arrow" href="nutricion.html">Área de nutrición {icon('arrow')}</a></div></article>
      <article class="team-card reveal" style="--d:120ms"><div class="mono-avatar"><img src="assets/brand/monogram.png" alt=""></div><div><span class="eyebrow">Podología</span><h3>Servicio de podología</h3><p>Estudio de la pisada, plantillas personalizadas, órtesis de silicona, quiropodia, reconstrucción ungueal y podología general, también a domicilio.</p><p>Trabaja en coordinación con fisioterapia para abordar la pisada, la postura y el dolor de forma global.</p><a class="link-arrow" href="podologia.html">Área de podología {icon('arrow')}</a></div></article>
    </div>
  </div>
</section>
{reels_strip('Así somos, <em>en vídeo</em>', 'Conoce la clínica, a María y nuestras clases a través de los reels de Instagram.')}
<section class="section tech-sec" id="tecnologia">
  <div class="container">
    {head('Tecnología', 'Herramientas que aportan <em>precisión</em>', 'Ecógrafo de última generación y diatermia Winback, siempre al servicio de la valoración y del tratamiento.', light=True)}
    <div class="tech-grid">
      <article class="tech-card reveal"><div class="tech-media">{img('hombro', 'Ecografía de hombro')}<span class="tech-live"><i></i>Ecografía en consulta</span></div><div class="tech-body"><h3>Ecografía musculoesquelética</h3><p>Imágenes claras y detalladas de músculos, tendones y ligamentos para valorar mejor, personalizar el tratamiento y seguir tu evolución con precisión.</p><a class="link-arrow light" href="servicio-ecografia-musculoesqueletica.html">Saber más {icon('arrow')}</a></div></article>
      <article class="tech-card reveal" style="--d:150ms"><div class="tech-media">{img('winback', 'Equipo Winback')}<span class="tech-live"><i></i>Winback</span></div><div class="tech-body"><h3>Diatermia Winback</h3><p>Radiofrecuencia de alta, media y baja frecuencia para actuar a distintos niveles del cuerpo: un tratamiento personalizado, potente y no invasivo.</p><a class="link-arrow light" href="servicio-tecarterapia-diatermia.html">Saber más {icon('arrow')}</a></div></article>
    </div>
  </div>
</section>
<section class="section"><div class="container">{head('El espacio', 'Pensado para que te sientas <em>cómodo</em>', 'Pulsa en cualquier imagen para verla en grande.', center=True)}<div class="gallery masonry">{g}</div></div></section>
{reviews_block()}
<section class="section section-soft"><div class="container gift-grid">
  <div class="collab-card reveal"><span class="eyebrow">Colaboraciones</span><h3>Convenios con entidades locales</h3><p>Creemos en el poder de los vínculos. Por eso colaboramos en nuestras sesiones de fisioterapia con agrupaciones de la zona para mejorar el acceso a la fisioterapia.</p><ul class="collab-list">{collab}</ul></div>
  <div class="collab-card reveal" style="--d:150ms"><span class="eyebrow">Accesibilidad y servicios</span><h3>Un centro para todas las personas</h3><ul class="amen">{''.join(f'<li>{icon(i)}<span>{e(t)}</span></li>' for i, t in AMENITIES)}</ul><p class="muted">Centro sanitario registrado · NICA {NICA}</p></div>
</div></section>
{ig_strip()}'''


# ───────────────────────────── INFORMACIÓN ─────────────────────────────
def info_page():
    pol = ''.join(f'<li class="reveal" style="--d:{i * 80}ms"><span class="pol-n">0{i + 1}</span><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>' for i, (t, d) in enumerate(POLICY))
    steps = [("Escríbenos", "Por WhatsApp o por teléfono, cuéntanos brevemente qué necesitas."), ("Te orientamos", "Te indicamos el servicio adecuado y te proponemos día y hora."), ("Primera visita", "Valoración completa: historia, exploración y, si procede, ecografía."), ("Tu plan", "Te explicamos qué ocurre y empezamos a trabajar juntos.")]
    st = ''.join(f'<li class="step reveal" style="--d:{i * 120}ms"><span class="step-dot">0{i + 1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(steps))
    quick = ''.join(f'<a href="#{a}" class="jump-link">{icon(i)}{t}</a>' for a, i, t in [("horario", "clock", "Horario"), ("primera-visita", "calendar", "Primera visita"), ("bonos", "gift", "Bonos"), ("normativa", "shield", "Normativa"), ("preguntas", "search", "Preguntas")])
    return page_hero('Información para tu visita', 'Todo un poco más <em>claro</em>', 'Horario, cómo pedir cita, qué esperar de la primera visita, bonos, normativa y respuestas a las dudas más habituales.', 'pasillo', '<span>Información</span>') + f'''
<nav class="jump container reveal" aria-label="En esta página">{quick}</nav>
<section class="section" id="horario"><div class="container info-top">
  {hours_card()}
  <div class="info-cards">
    <article class="i-card reveal"><span class="i-ic">{icon('whatsapp')}</span><h3>Cita por WhatsApp</h3><p>La forma más rápida. Te respondemos en horario de clínica.</p><a class="link-arrow" href="{WA}" target="_blank" rel="noopener">Escribir ahora {icon('arrow')}</a></article>
    <article class="i-card reveal" style="--d:100ms"><span class="i-ic">{icon('phone')}</span><h3>Por teléfono</h3><p>Llámanos al {PHONE}. Si estamos en sesión, te devolvemos la llamada.</p><a class="link-arrow" href="tel:+{PHONE_INTL}">Llamar {icon('arrow')}</a></article>
    <article class="i-card reveal" style="--d:200ms"><span class="i-ic">{icon('home')}</span><h3>A domicilio</h3><p>Fisioterapia y podología en casa para movilidad reducida. Consulta cobertura.</p><a class="link-arrow" href="{wa('Hola, María 👋 Quería consultar la atención a domicilio en mi localidad: ')}" target="_blank" rel="noopener">Consultar {icon('arrow')}</a></article>
    <article class="i-card reveal" style="--d:300ms"><span class="i-ic">{icon('card')}</span><h3>Formas de pago</h3><p>Tarjeta de crédito o débito y pago con el móvil (NFC).</p></article>
  </div>
</div></section>
<section class="section section-soft method-sec" id="primera-visita"><div class="container">{head('Paso a paso', 'Cómo es tu <em>primera visita</em>', 'Sin prisas: el primer día está pensado para conocerte y entender qué te ocurre.', center=True)}<ol class="steps">{st}</ol>
  <div class="tips reveal"><div><h3>{icon('bag')} Qué traer</h3><p>Ropa cómoda, informes o pruebas de imagen si los tienes y la lista de medicación que tomas.</p></div><div><h3>{icon('clock')} Llega con tiempo</h3><p>Unos minutos antes, para empezar a la hora y aprovechar toda la sesión.</p></div><div><h3>{icon('heart')} Pregunta todo</h3><p>Queremos que entiendas tu proceso. Ninguna duda es pequeña.</p></div></div>
</div></section>
<section class="section" id="bonos"><div class="container gift-grid">
  <div class="gift-card reveal"><div class="gift-media">{img('tarjeta', 'Tarjeta regalo de la clínica')}</div><div class="gift-body"><span class="eyebrow">Bonos de fisioterapia</span><h3>Ahorra y sé constante</h3><p>Los bonos de sesiones te ayudan a mantener la continuidad del tratamiento. Pregúntanos sin compromiso por las modalidades disponibles.</p><a class="link-arrow" href="{wa('Hola, María 👋 Me gustaría información sobre los bonos de fisioterapia.')}" target="_blank" rel="noopener">Consultar bonos {icon('arrow')}</a></div></div>
  <div class="gift-card reveal" style="--d:150ms"><div class="gift-media">{img('bolsa', 'Bolsa con el logotipo de la clínica')}</div><div class="gift-body"><span class="eyebrow">Tarjetas regalo</span><h3>Regala salud y bienestar</h3><p>Una sesión de fisioterapia, FisioPilates, nutrición o podología: el regalo perfecto para alguien que se cuida. Validez de 1 año.</p><a class="link-arrow" href="{wa('Hola, María 👋 Quiero regalar una tarjeta regalo. ¿Qué opciones hay?')}" target="_blank" rel="noopener">Pedir tarjeta regalo {icon('arrow')}</a></div></div>
</div></section>
<section class="section section-dark" id="normativa"><div class="container policy-grid">
  <div>{head('Normativa del centro', 'Para cuidarnos <em>entre todos</em>', 'Aplicamos estas normas para garantizar que otra persona que lo necesite pueda beneficiarse de su cita.', light=True)}<p class="script light reveal">¡gracias siempre!</p></div>
  <ol class="policy">{pol}</ol>
</div></section>
<section class="section" id="preguntas"><div class="container faq-grid"><div>{head('Resolvemos tus dudas', 'Preguntas <em>frecuentes</em>', 'Todo lo que necesitas saber antes de venir.')}<div class="faq-help reveal"><p>¿Tienes otra pregunta?</p><a class="btn btn-outline btn-sm" href="{WA}" target="_blank" rel="noopener">{icon('whatsapp')} Escríbenos</a></div></div><div class="reveal">{faq_list(HOME_FAQS)}</div></div></section>
{booking_block()}'''


# ───────────────────────────── CONTACTO ─────────────────────────────
def contact_page():
    return page_hero('Hablemos', 'Estamos aquí para <em>escucharte</em>', 'Pide tu cita o resuelve cualquier duda por WhatsApp, teléfono o en persona.', 'fachada', '<span>Contacto</span>', f'<a class="btn btn-light" href="#reserva">{icon("calendar")} Reservar cita</a><a class="btn btn-glass" href="tel:+{PHONE_INTL}">{icon("phone")} {PHONE}</a>') + f'''
<section class="section"><div class="container contact-cards">
  <a class="c-card reveal" href="{WA}" target="_blank" rel="noopener"><span class="c-ic wa">{icon('whatsapp')}</span><small>WhatsApp</small><b>{PHONE}</b><span class="link-arrow">Abrir chat {icon('arrow')}</span></a>
  <a class="c-card reveal" style="--d:100ms" href="tel:+{PHONE_INTL}"><span class="c-ic">{icon('phone')}</span><small>Teléfono</small><b>{PHONE}</b><span class="link-arrow">Llamar {icon('arrow')}</span></a>
  <a class="c-card reveal" style="--d:200ms" href="{MAP}" target="_blank" rel="noopener"><span class="c-ic">{icon('pin')}</span><small>Dirección</small><b>{ADDRESS}</b><span class="link-arrow">Cómo llegar {icon('arrow')}</span></a>
  <a class="c-card reveal" style="--d:300ms" href="{IG}" target="_blank" rel="noopener"><span class="c-ic">{icon('insta')}</span><small>Instagram</small><b>@fisiomariacm</b><span class="link-arrow">Seguir {icon('arrow')}</span></a>
</div></section>
{booking_block(title='Pide tu cita sin complicaciones')}
<section class="section visit-sec"><div class="container visit-grid">{map_block()}<div class="visit-copy">{hours_card()}<ul class="amen reveal">{''.join(f'<li>{icon(i)}<span>{e(t)}</span></li>' for i, t in AMENITIES)}</ul></div></div></section>
<section class="section section-soft"><div class="container faq-grid"><div>{head('Antes de escribirnos', 'Dudas <em>rápidas</em>')}</div><div class="reveal">{faq_list(HOME_FAQS[:5])}</div></div></section>'''


def not_found():
    return f'''<section class="nf"><div class="container nf-inner"><img src="assets/brand/monogram.png" alt=""><span class="eyebrow">Error 404</span><h1>Esta página se ha ido a <em>estirar</em></h1><p>No encontramos lo que buscas, pero podemos ayudarte a llegar donde querías.</p><div class="pf-actions"><a class="btn btn-primary" href="index.html">Volver al inicio {icon('arrow')}</a><a class="btn btn-outline" href="servicios.html">Ver servicios</a></div></div></section>'''


# ───────────────────────────── DATOS PARA JS ─────────────────────────────
def site_data():
    data = {
        "phone": PHONE_INTL,
        "hours": [[list(t) for t in spans] for _, spans in HOURS],
        "days": [d for d, _ in HOURS],
        "areas": {s: c["title"] for s, c in CATEGORIES.items()},
        "services": [{"slug": s["slug"], "title": s["title"], "area": s["category"]} for s in SERVICES],
    }
    return f'<script>window.MC={json.dumps(data, ensure_ascii=False)};</script>'


def jsonld():
    data = {
        "@context": "https://schema.org", "@type": "Physiotherapy", "name": "Clínica Fisioterapia María Conejo",
        "telephone": "+34 656 64 33 30", "image": SHARE_IMG, "url": SITE_URL,
        "address": {"@type": "PostalAddress", "streetAddress": ADDRESS, "postalCode": "29312", "addressLocality": "Villanueva del Rosario", "addressRegion": "Málaga", "addressCountry": "ES"},
        "geo": {"@type": "GeoCoordinates", "latitude": 37.0026564, "longitude": -4.3687152},
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "5.0", "reviewCount": REVIEWS_COUNT},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "11:00", "closes": "14:00"},
                                      {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "15:00", "closes": "21:00"},
                                      {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "11:00", "closes": "14:00"},
                                      {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "15:00", "closes": "20:00"}],
        "sameAs": [IG, FB],
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


DATA = site_data()

PAGES = {
    "index.html": ("Fisioterapia, nutrición y podología en Villanueva del Rosario", "Clínica de fisioterapia, nutrición y podología en Villanueva del Rosario (Málaga). Ecografía, punción seca, Winback, FisioPilates y pediatría. 5,0 en Google.", home(), "index.html", "home", DATA + jsonld()),
    "servicios.html": ("Servicios", "Los 22 servicios de fisioterapia, nutrición y podología de Fisioterapia María Conejo, con información detallada y reserva por WhatsApp.", all_services(), "", "", DATA),
    "clinica.html": ("La clínica y el equipo", "Conoce a María Conejo Martín, al equipo y la forma de trabajar de la clínica en Villanueva del Rosario.", clinic_page(), "clinica.html", "", DATA),
    "informacion.html": ("Información útil", "Horario, primera visita, bonos y tarjetas regalo, normativa de cancelación y preguntas frecuentes.", info_page(), "informacion.html", "", DATA),
    "contacto.html": ("Contacto y cita", "Pide cita en Fisioterapia María Conejo por WhatsApp o teléfono (656 64 33 30). C. Fuente Toril, 24, Villanueva del Rosario.", contact_page(), "contacto.html", "", DATA),
    "404.html": ("Página no encontrada", "La página que buscas no existe.", not_found(), "", "nf-page", DATA),
}
for slug, category in CATEGORIES.items():
    PAGES[f"{slug}.html"] = (category['title'], category['lead'], category_page(slug), "", "", DATA)
for item in SERVICES:
    PAGES[f"servicio-{item['slug']}.html"] = (item['title'], item['lead'], service_page(item), "", "service", DATA)

for filename, (title, description, body, active, cls, extra) in PAGES.items():
    (ROOT / filename).write_text(page(title, description, body, active, cls, extra, filename), encoding="utf-8")

print(f"Generadas {len(PAGES)} páginas HTML")
