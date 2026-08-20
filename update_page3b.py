import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the map URL
html = html.replace(
    'https://www.google.com/maps/search/?api=1&query=Calle+Hawai+297,+Sol+de+la+Molina',
    'https://maps.app.goo.gl/kRPghWoH3Lv5T87EA'
)

# 2. Make the oso bigger and shift it more to cover the right half
html = html.replace(
    'style="position: absolute; bottom: -5px; right: -15px; max-width: 175px; opacity: 1; z-index: 5; pointer-events: none;"',
    'style="position: absolute; bottom: -5px; right: -20px; max-width: 230px; opacity: 1; z-index: 5; pointer-events: none;"'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
