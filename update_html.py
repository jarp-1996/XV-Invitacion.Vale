import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_pages = r'''                <!-- PÁGINA 2: BIENVENIDA E INSPIRACIÓN -->
                <div class="page" id="page-2">
                    <div class="page-content parchment-bg ornate-box">
                        <p class="text-serif" style="font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--color-gold-dark);">Valeria</p>
                        <div class="photo-placeholder" style="width: 140px; height: 140px; border-radius: 50%; border: 3px solid var(--color-gold); margin: 0.8rem auto; overflow: hidden; background: rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center;">
                            <span class="text-serif" style="color: var(--color-gold-dark); opacity: 0.7; font-size: 0.75rem; text-align: center;">[Tu Foto<br>Aquí]</span>
                        </div>
                        <div class="gold-separator" style="margin: 0.5rem auto;"></div>
                        <p class="text-serif text-story" style="font-size: 0.95rem; font-style: italic; margin: 1rem 0; line-height: 1.5; padding: 0 10px;">
                            "Hay momentos inolvidables que se atesoran en el corazón para siempre. Gracias por ser parte de mi historia y compartir esta noche mágica conmigo."
                        </p>
                        <div class="gold-separator" style="margin: 0.5rem auto;"></div>
                        
                        <div class="page-nav">
                            <button class="btn-nav btn-prev">&#10094;</button>
                            <button class="btn-nav btn-next">&#10095;</button>
                        </div>
                    </div>
                </div>

                <!-- PÁGINA 3: EL CUÁNDO Y EL DÓNDE -->
                <div class="page" id="page-3">
                    <div class="page-content parchment-bg ornate-box">
                        <h3 class="text-serif-dec" style="font-size: 1.4rem; color: var(--color-rose-dark); margin-bottom: 0.4rem;">Cuándo & Dónde</h3>
                        <p class="text-serif" style="font-size: 1.1rem; font-weight: 600; color: var(--color-gold-dark); margin-bottom: 0.2rem;">Sábado, 7 de Noviembre 2026</p>
                        <p class="text-serif" style="font-size: 1rem; margin-bottom: 1rem;">6:00 PM</p>
                        
                        <div class="countdown-container" id="countdown" style="margin-bottom: 1.2rem;">
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
                        
                        <p class="text-serif" style="font-size: 0.9rem; font-weight: bold; margin-bottom: 0.2rem;">Recepción</p>
                        <p style="font-size: 0.8rem; opacity: 0.85; max-width: 90%; margin: 0 auto 0.8rem; line-height: 1.3;">
                            Calle Hawai 297, Sol de la Molina
                        </p>
                        <a href="https://www.google.com/maps/search/?api=1&query=Calle+Hawai+297,+Sol+de+la+Molina" target="_blank" rel="noopener" class="btn btn-gold" style="padding: 0.5rem 1.2rem; font-size: 0.75rem; letter-spacing: 0.1em; margin-bottom: 0.5rem;">Ver en el Mapa</a>
                        
                        <div class="page-nav">
                            <button class="btn-nav btn-prev">&#10094;</button>
                            <button class="btn-nav btn-next">&#10095;</button>
                        </div>
                    </div>
                </div>

                <!-- PÁGINA 4: DETALLES DEL EVENTO -->
                <div class="page" id="page-4">
                    <div class="page-content parchment-bg ornate-box">
                        <div style="margin-top: 0.5rem; width: 100%;">
                            <h3 class="text-serif-dec" style="font-size: 1.3rem; color: var(--color-rose-dark); margin-bottom: 0.2rem;">Dress Code</h3>
                            <p class="text-serif" style="font-size: 1.1rem; font-weight: 700; color: var(--color-gold-dark); letter-spacing: 0.1em;">Elegante / Formal</p>
                            <div style="display: flex; justify-content: center; gap: 0.5rem; margin: 0.6rem 0;">
                                <div style="width: 20px; height: 20px; border-radius: 50%; background: #000; border: 1px solid var(--color-gold);" title="Negro"></div>
                                <div style="width: 20px; height: 20px; border-radius: 50%; background: #1a2942; border: 1px solid var(--color-gold);" title="Azul Noche"></div>
                                <div style="width: 20px; height: 20px; border-radius: 50%; background: #5a1818; border: 1px solid var(--color-gold);" title="Vino"></div>
                            </div>
                            <p style="font-size: 0.75rem; opacity: 0.9; line-height: 1.3; max-width: 90%; margin: 0 auto;">
                                *Color reservado: Amarillo/Dorado
                            </p>
                        </div>
                        
                        <div class="gold-separator" style="margin: 1rem auto;"></div>
                        
                        <div style="width: 100%;">
                            <h3 class="text-serif-dec" style="font-size: 1.3rem; color: var(--color-rose-dark); margin-bottom: 0.2rem;">Mesa de Regalos</h3>
                            <p class="text-serif" style="font-size: 1rem; font-weight: 600; color: var(--color-gold-dark);">Lluvia de Sobres</p>
                            <p style="font-size: 0.8rem; opacity: 0.9; line-height: 1.3; max-width: 90%; margin: 0.3rem auto 0.6rem;">
                                Tu presencia es mi mejor regalo. Si deseas tener un detalle, habrá un buzón en la recepción o puedes hacerlo aquí:
                            </p>
                            <button class="btn btn-rose" style="padding: 0.4rem 1rem; font-size: 0.7rem;" onclick="alert('Aquí puedes enlazar tu cuenta bancaria o QR.')">Ver Datos Bancarios</button>
                        </div>
                        
                        <div class="page-nav">
                            <button class="btn-nav btn-prev">&#10094;</button>
                            <button class="btn-nav btn-next">&#10095;</button>
                        </div>
                    </div>
                </div>

                <!-- PÁGINA 5: RSVP -->
                <div class="page" id="page-5">
                    <div class="page-content parchment-bg ornate-box">
                        <h3 class="text-serif-dec" style="font-size: 1.3rem; color: var(--color-rose-dark); margin-bottom: 0.2rem;">Confirmación</h3>
                        <p class="text-serif" style="font-size: 0.8rem; font-style: italic; margin-bottom: 0.6rem; color: var(--color-text-dark);">
                            Por favor confirma tu asistencia
                        </p>
                        
                        <form id="rsvp-form" class="rsvp-form" style="width: 100%; text-align: left;">
                            <div class="form-group" style="margin-bottom: 0.5rem;">
                                <label style="font-size: 0.7rem; font-weight: bold; color: var(--color-text-dark);">Tu Nombre</label>
                                <input type="text" id="guest-name" class="form-input" style="padding: 0.4rem; font-size: 0.8rem; background: rgba(0,0,0,0.03); border-color: rgba(170,140,44,0.4); color: var(--color-text-dark);" required>
                            </div>
                            
                            <div class="form-group" style="margin-bottom: 0.5rem; display: none;" id="companion-field">
                                <label style="font-size: 0.7rem; font-weight: bold; color: var(--color-text-dark);">Acompañante(s)</label>
                                <input type="text" id="companion-name" class="form-input" style="padding: 0.4rem; font-size: 0.8rem; background: rgba(0,0,0,0.03); border-color: rgba(170,140,44,0.4); color: var(--color-text-dark);" placeholder="Nombre(s)">
                            </div>
                            <div style="text-align: right; margin-bottom: 0.5rem;">
                                <span id="add-companion-btn" style="font-size: 0.7rem; color: var(--color-rose-dark); cursor: pointer; text-decoration: underline; font-weight: 600;">+ Añadir acompañante</span>
                            </div>
                            
                            <div class="form-group" style="margin-bottom: 0.5rem;">
                                <label style="font-size: 0.7rem; font-weight: bold; color: var(--color-text-dark);">Dieta / Alergias (Opcional)</label>
                                <input type="text" id="diet-req" class="form-input" style="padding: 0.4rem; font-size: 0.8rem; background: rgba(0,0,0,0.03); border-color: rgba(170,140,44,0.4); color: var(--color-text-dark);" placeholder="Ej. Ninguna, Vegano">
                            </div>
                            
                            <div class="form-group" style="margin-bottom: 0.8rem; text-align: center;">
                                <label style="font-size: 0.75rem; font-weight: bold; margin-bottom: 0.2rem; display: block; color: var(--color-text-dark);">¿Asistirás?</label>
                                <div class="radio-group" style="justify-content: center;">
                                    <label class="radio-label" style="font-size: 0.75rem; color: var(--color-text-dark);"><input type="radio" name="attendance" value="si" required checked><span class="radio-custom" style="border-color: var(--color-gold-dark);"></span> Sí</label>
                                    <label class="radio-label" style="font-size: 0.75rem; color: var(--color-text-dark);"><input type="radio" name="attendance" value="no" required><span class="radio-custom" style="border-color: var(--color-gold-dark);"></span> No</label>
                                </div>
                            </div>
                            
                            <button type="submit" class="btn btn-rose" id="submit-btn" style="padding: 0.5rem; font-size: 0.8rem; width: 100%; border-radius: 4px;">Enviar RSVP</button>
                            
                            <div id="rsvp-success" class="form-message success" style="display:none; font-size: 0.7rem; padding: 0.4rem;">¡Gracias por confirmar!</div>
                            <div id="rsvp-error" class="form-message error" style="display:none; font-size: 0.7rem; padding: 0.4rem;">Error al enviar.</div>
                        </form>
                        
                        <div class="page-nav">
                            <button class="btn-nav btn-prev">&#10094;</button>
                            <button class="btn-nav btn-next">&#10095;</button>
                        </div>
                    </div>
                </div>

                <!-- PÁGINA 6: CONTRATAPA -->
                <div class="page" id="page-6">
                    <div class="page-content parchment-bg ornate-box" style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
                        <h2 class="text-cursive" style="font-size: 3.5rem; color: var(--color-gold-dark); margin-bottom: 0.5rem;">Gracias</h2>
                        <p class="text-serif text-story" style="font-size: 1.2rem; font-style: italic; max-width: 80%; text-align: center; color: var(--color-text-dark);">
                            ¡No faltes!<br>Nos vemos en la pista de baile.
                        </p>
                        <div class="gold-separator" style="margin: 1.5rem auto;"></div>
                        <button class="btn btn-gold" id="btn-close-book" style="margin-top: 1rem;">Cerrar Invitación</button>
                        
                        <div class="page-nav">
                            <button class="btn-nav btn-prev">&#10094;</button>
                        </div>
                    </div>
                </div>'''

pattern = re.compile(r'<!-- PÁGINA 2.*?</div>\s*</div>\s*</div>', re.DOTALL)
html = pattern.sub(new_pages, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
