# -*- coding: utf-8 -*-
"""把 src/template.html 內的素材佔位符換成 base64 data URI，輸出單一檔案 index.html。
用法： python build.py
"""
import base64, io, os, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))

MAP = {
    '{{CITY_FULL}}': ('assets/city_full.jpg', 'image/jpeg'),
    '{{CITY_RUIN}}': ('assets/city_ruin.jpg', 'image/jpeg'),
    '{{G_GUANYU}}':  ('assets/g_guanyu.png',  'image/png'),
    '{{G_ZHUGE}}':   ('assets/g_zhuge.png',   'image/png'),
    '{{G_HUANG}}':   ('assets/g_huang.png',   'image/png'),
    '{{LOGO}}':      ('assets/logo.png',      'image/png'),
    '{{IOS}}':       ('assets/ios.png',       'image/png'),
    '{{GP}}':        ('assets/gp.png',        'image/png'),
}

with open(os.path.join(HERE, 'src', 'template.html'), encoding='utf-8') as f:
    html = f.read()

for token, (path, mime) in MAP.items():
    p = os.path.join(HERE, path)
    with open(p, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('ascii')
    n = html.count(token)
    html = html.replace(token, 'data:%s;base64,%s' % (mime, b64))
    print('inlined %-22s %6.1f KB  x%d' % (path, os.path.getsize(p) / 1024, n))

out = os.path.join(HERE, 'index.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print('\nOK ->', out)
print('total %.2f MB' % (os.path.getsize(out) / 1024 / 1024))
