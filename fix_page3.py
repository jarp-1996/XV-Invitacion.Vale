import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find and replace the bottom layout section of page 3
old_block = re.search(
    r'<div style="display: flex; width: 100%;.*?<!-- Ilustración pegada al fondo derecho -->.*?<div class="page-nav">',
    html, re.DOTALL
)

if old_block:
    new_block = '''<div class="page-nav">'''
    
    # We'll put location info and button above the bear, bear fills bottom-right
    # First replace the whole block
    replacement = '''
                        <p class="text-serif" style="font-size: 0.95rem; font-weight: bold; margin-bottom: 0.2rem;">Ubicación del Evento</p>
                        <p style="font-size: 0.8rem; opacity: 0.85; max-width: 55%; margin: 0 auto 1rem; line-height: 1.3;">
                            Calle Hawai 297, Sol de la Molina
                        </p>
                        
                        <div class="page-nav">'''
    
    html = html[:old_block.start()] + replacement + html[old_block.end():]

# Now update the oso image - remove old one and put it correctly
html = html.replace(
    '<!-- Ilustración pegada al fondo derecho -->\n                        <img src="assets/oso_principe.png" alt="Oso Príncipe" style="position: absolute; bottom: -5px; right: -20px; max-width: 230px; opacity: 1; z-index: 5; pointer-events: none;">',
    ''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
