import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_img = 'style="position: absolute; bottom: 0px; left: 50%; transform: translateX(-50%); max-width: 90px;'
new_img = 'style="position: absolute; bottom: 0px; right: 15px; max-width: 160px;'

html = html.replace(old_img, new_img)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
