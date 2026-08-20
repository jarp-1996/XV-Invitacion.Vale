import re

with open('design-system.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_hoja_2 = '''<!-- HOJA 2: PRÓLOGO -->
                <div class="ds-page-frame">
                    <h4>Página 2: Prólogo Animado</h4>
                    <div class="ds-page-container">
                        <div class="page-content parchment-bg ornate-box" style="display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 2rem; position: relative;">
                            
                            <img src="assets/princesa_bailando.png" alt="Princesa" style="display: block; margin: 0 auto 1.5rem; max-width: 140px; height: auto;">
                            
                            <p class="text-serif text-story" style="font-size: 1.1rem; font-style: italic; margin-bottom: 0.8rem; line-height: 1.6; text-align: center; color: var(--color-text-dark);">
                                "Los que no creen en la magia nunca la encontrarán."
                            </p>
                            <p class="text-serif" style="font-size: 0.8rem; letter-spacing: 0.1em; color: var(--color-gold-dark); text-align: center; width: 100%;">
                                — Roald Dahl
                            </p>
                            
                            <div class="page-nav" style="position: absolute; bottom: 15px; left: 0; width: 100%; display: flex; justify-content: space-between; padding: 0 15px; opacity: 1; pointer-events: none;">
                                <button class="btn-nav btn-prev">&#10094;</button>
                                <button class="btn-nav btn-next">&#10095;</button>
                            </div>
                        </div>
                    </div>
                </div>

                '''

html = re.sub(r'<!-- HOJA 2: PRÓLOGO -->.*?<!-- HOJA 3:', new_hoja_2 + '<!-- HOJA 3:', html, flags=re.DOTALL)

with open('design-system.html', 'w', encoding='utf-8') as f:
    f.write(html)
