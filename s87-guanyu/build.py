# -*- coding: utf-8 -*-
"""把 src/template.html 內的素材佔位符換成 base64 data URI，輸出單一檔案 HTML。
用法： python build.py
"""
import base64, io, os, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))

MAP = {
    '{{BG}}':   ('assets/bg.jpg',     'image/jpeg'),
    '{{HERO}}': ('assets/guanyu.png', 'image/png'),
    '{{LOGO}}': ('assets/logo.png',   'image/png'),
    '{{IOS}}':  ('assets/ios.png',    'image/png'),
    '{{GP}}':   ('assets/gp.png',     'image/png'),
}

with open(os.path.join(HERE, 'src', 'template.html'), encoding='utf-8') as f:
    html = f.read()

for token, (path, mime) in MAP.items():
    with open(os.path.join(HERE, path), 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('ascii')
    html = html.replace(token, 'data:%s;base64,%s' % (mime, b64))
    print('inlined %-14s %6.1f KB -> base64 %6.1f KB' % (path, os.path.getsize(os.path.join(HERE, path)) / 1024, len(b64) / 1024))

out = os.path.join(HERE, 'index.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print('\nOK ->', out)
print('total %.2f MB' % (os.path.getsize(out) / 1024 / 1024))
