import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I need to replace the bottom part of Page 3.
# From `<p class="text-serif" style="font-size: 0.9rem; font-weight: bold; margin-bottom: 0.2rem;">Ubicación del Evento</p>`
# to before `<div class="page-nav">`

old_part = r'<p class="text-serif" style="font-size: 0.9rem; font-weight: bold; margin-bottom: 0.2rem;">Ubicación del Evento</p>.*?<div class="page-nav">'

new_part = '''
                        <div style="display: flex; width: 100%; justify-content: space-between; align-items: flex-end; margin-top: 1rem; position: relative; z-index: 10;">
                            <div style="width: 55%; text-align: center; padding-left: 0.5rem; padding-bottom: 1rem;">
                                <p class="text-serif" style="font-size: 0.95rem; font-weight: bold; margin-bottom: 0.3rem;">Ubicación del Evento</p>
                                <p style="font-size: 0.8rem; opacity: 0.85; margin: 0 auto 0.8rem; line-height: 1.3;">
                                    Calle Hawai 297, Sol de la Molina
                                </p>
                                <a href="https://www.google.com/maps/search/?api=1&query=Calle+Hawai+297,+Sol+de+la+Molina" target="_blank" rel="noopener" class="btn btn-rose" style="padding: 0.6rem 1rem; font-size: 0.75rem; letter-spacing: 0.05em;">📍 VER EN EL MAPA</a>
                            </div>
                            <div style="width: 45%;"></div>
                        </div>
                        
                        <!-- Ilustración pegada al fondo derecho -->
                        <img src="assets/oso_principe.png" alt="Oso Príncipe" style="position: absolute; bottom: -5px; right: -15px; max-width: 175px; opacity: 1; z-index: 5; pointer-events: none;">
                        
                        <div class="page-nav">'''

html = re.sub(old_part, new_part.strip(), html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
