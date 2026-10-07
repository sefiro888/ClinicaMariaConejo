from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

root = Path(__file__).resolve().parent


class Refs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.h1 = 0
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        if tag == "img":
            self.images.append(attrs)
        for key in ("src", "href"):
            if key in attrs:
                self.refs.append(attrs[key])


errors = []
pages = list(root.glob("*.html"))
for page in pages:
    parser = Refs()
    parser.feed(page.read_text(encoding="utf-8"))
    if parser.h1 != 1:
        errors.append(f"{page.name}: {parser.h1} encabezados H1")
    for image in parser.images:
        if "alt" not in image:
            errors.append(f"{page.name}: imagen sin alt")
    for ref in parser.refs:
        parsed = urlparse(ref)
        if parsed.scheme or ref.startswith(("#", "//")):
            continue
        target = root / parsed.path
        if not target.exists():
            errors.append(f"{page.name}: enlace roto {ref}")

print(f"{len(pages)} páginas verificadas; {len(errors)} incidencias")
for error in errors:
    print(error)
raise SystemExit(1 if errors else 0)
