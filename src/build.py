#!/usr/bin/env python3
"""Build index.html from src/app.html (inlines the logo, adds PWA tags)."""
import base64, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'src' / 'app.html').read_text(encoding='utf-8')
logo = 'data:image/png;base64,' + base64.b64encode((root / 'src' / 'logo.png').read_bytes()).decode()
out = src.replace('__LOGO__', logo)
pwa = ('<meta name="theme-color" content="#141415">\n<link rel="manifest" href="manifest.webmanifest">\n'
       '<link rel="apple-touch-icon" href="icon-180.png">\n<link rel="icon" type="image/png" href="icon-192.png">\n'
       '<meta name="apple-mobile-web-app-title" content="VISION 조감도">\n<meta name="mobile-web-app-capable" content="yes">')
out = out.replace('<meta name="theme-color" content="#141415">', pwa, 1)
(root / 'index.html').write_text(out, encoding='utf-8')
print('built index.html', len(out), 'bytes')
