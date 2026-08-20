import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the end of Page 3 content, before <div class="page-nav">
insertion = '''📍 Ver en el Mapa</a>
                        
                        <!-- Ilustración pegada al fondo -->
                        <img src="assets/oso_principe.png" alt="Oso Príncipe" style="position: absolute; bottom: 0px; left: 50%; transform: translateX(-50%); max-width: 90px; opacity: 0.95; z-index: 5; pointer-events: none; mix-blend-mode: multiply;">
                        
                        <div class="page-nav">'''

html = html.replace('📍 Ver en el Mapa</a>\n                        \n                        <div class="page-nav">', insertion)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
