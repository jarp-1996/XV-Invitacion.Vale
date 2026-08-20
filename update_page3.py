import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_page_3 = '''
                <div class="page" id="page-3">
                    <div class="page-content parchment-bg ornate-box" style="display: flex; flex-direction: column; justify-content: center;">
                        <h3 class="text-serif-dec" style="font-size: 1.4rem; color: var(--color-rose-dark); margin-bottom: 0.4rem;">Cuándo &amp; Dónde</h3>
                        
                        <p class="text-serif" style="font-size: 1.1rem; font-weight: 600; color: var(--color-gold-dark); margin-bottom: 0.2rem;">Sábado, 7 de Noviembre 2026</p>
                        <p class="text-serif" style="font-size: 1rem; margin-bottom: 1rem;">🕕 6:00 PM</p>
                        
                        <p class="text-serif" style="font-size: 0.85rem; font-style: italic; color: var(--color-gold-dark); margin-bottom: 0.4rem;">Faltan...</p>
                        <div class="countdown-container" id="countdown" style="margin-bottom: 1.5rem;">
                            <div class="countdown-box">
                                <span class="countdown-val" id="days">00</span><span class="countdown-lbl">Días</span>
                            </div>
                            <div class="countdown-box">
                                <span class="countdown-val" id="hours">00</span><span class="countdown-lbl">Hrs</span>
                            </div>
                            <div class="countdown-box">
                                <span class="countdown-val" id="minutes">00</span><span class="countdown-lbl">Min</span>
                            </div>
                            <div class="countdown-box">
                                <span class="countdown-val" id="seconds">00</span><span class="countdown-lbl">Seg</span>
                            </div>
                        </div>
                        
                        <p class="text-serif" style="font-size: 0.9rem; font-weight: bold; margin-bottom: 0.2rem;">Ubicación del Evento</p>
                        <p style="font-size: 0.8rem; opacity: 0.85; max-width: 90%; margin: 0 auto 0.8rem; line-height: 1.3;">
                            Calle Hawai 297, Sol de la Molina
                        </p>
                        <a href="https://www.google.com/maps/search/?api=1&query=Calle+Hawai+297,+Sol+de+la+Molina" target="_blank" rel="noopener" class="btn btn-rose" style="padding: 0.5rem 1.2rem; font-size: 0.75rem; letter-spacing: 0.1em; margin-bottom: 0.5rem;">📍 Ver en el Mapa</a>
                        
                        <div class="page-nav">
                            <button class="btn-nav btn-prev">&#10094;</button>
                            <button class="btn-nav btn-next">&#10095;</button>
                        </div>
                    </div>
                </div>
'''

html = re.sub(r'<div class="page" id="page-3">.*?<div class="page-nav">.*?</div>\s*</div>\s*</div>', new_page_3.strip(), html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
