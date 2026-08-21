/* ==========================================================================
   LÓGICA INTERACTIVA DE PÁGINA POR PÁGINA - INVITACIÓN DE VALERIA
   ========================================================================== */

// --- PANTALLA DE CARGA (LOADER) ---
function hideLoader() {
    const loader = document.getElementById('loader-wrapper');
    if (loader && !loader.classList.contains('fade-out')) {
        loader.classList.add('fade-out');
    }
}
window.addEventListener('load', () => setTimeout(hideLoader, 300));
setTimeout(hideLoader, 1500); // Respaldo automático si la carga de fuentes o audio tarda

document.addEventListener('DOMContentLoaded', () => {
    
    // --- CONFIGURACIÓN DE GOOGLE SHEETS ---
    const GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzB503DbZjbetlHBroDe2wyFDsJotT-yeQ3YArjm7G2__NC8DQunEn9GObL2AmUhPDv1A/exec'; 

    // --- VARIABLES DE ELEMENTOS DEL DOM ---
    const bgMusic = document.getElementById('bg-music');
    const audioToggle = document.getElementById('audio-toggle');
    const musicOnIcon = document.getElementById('music-on-icon');
    const musicOffIcon = document.getElementById('music-off-icon');
    const rsvpForm = document.getElementById('rsvp-form');
    const rsvpSuccess = document.getElementById('rsvp-success');
    const rsvpError = document.getElementById('rsvp-error');
    const submitBtn = document.getElementById('submit-btn');

    // --- 1. CONTROL DE NAVEGACIÓN CENTRALIZADO (BOTONES Y SWIPE) ---
    let currentPage = 1;
    const totalPages = 7;
    let isAnimating = false;

    function setActivePage(pageNum) {
        // Quitar active-page de todas las páginas
        document.querySelectorAll('.page').forEach(p => p.classList.remove('active-page'));
        // Marcar solo la página actual como activa
        const activePage = document.getElementById(`page-${pageNum}`);
        if (activePage) activePage.classList.add('active-page');
    }

    // Al inicio, página 1 es la activa
    setActivePage(1);

    function goNext() {
        if (isAnimating) return;
        if (currentPage < totalPages) {
            isAnimating = true;
            if (currentPage === 1) {
                playAudio();
                startPetalsEffect();
                setTimeout(() => {
                    if(audioToggle) audioToggle.style.display = 'flex';
                }, 800);
            }
            const page = document.getElementById(`page-${currentPage}`);
            if (page) page.classList.add('flipped');
            currentPage++;
            setActivePage(currentPage);
            setTimeout(() => { isAnimating = false; }, 900); // Mayor al tiempo de animación CSS (0.8s)
        }
    }

    function goPrev() {
        if (isAnimating) return;
        if (currentPage > 1) {
            isAnimating = true;
            currentPage--;
            const page = document.getElementById(`page-${currentPage}`);
            if (page) page.classList.remove('flipped');
            setActivePage(currentPage);
            setTimeout(() => { isAnimating = false; }, 900);
        }
    }

    // Botones Universales (Delegación de Eventos)
    document.querySelectorAll('.btn-next').forEach(btn => btn.addEventListener('click', goNext));
    document.querySelectorAll('.btn-prev').forEach(btn => btn.addEventListener('click', goPrev));
    
    // Botón de Portada especial
    const btnOpen = document.getElementById('btn-open');
    if (btnOpen) btnOpen.addEventListener('click', goNext);

    // Lógica de Swipe (Deslizamiento Táctil Móvil)
    let touchStartX = 0;
    let touchEndX = 0;
    
    const bookContainer = document.querySelector('.book-wrapper');
    if (bookContainer) {
        bookContainer.addEventListener('touchstart', e => {
            touchStartX = e.changedTouches[0].screenX;
        }, {passive: true});

        bookContainer.addEventListener('touchend', e => {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        }, {passive: true});
    }

    function handleSwipe() {
        const threshold = 40;
        if (touchStartX - touchEndX > threshold) goNext();
        if (touchEndX - touchStartX > threshold) goPrev();
    }
    // --- 2. CONTROL DE AUDIO (REPRODUCTOR ELEGANTE) ---
    let isMuted = false;

    function playAudio() {
        bgMusic.volume = 0.4; // Volumen sutil no invasivo
        bgMusic.play().then(() => {
            isMuted = false;
            updateAudioIcons();
        }).catch(err => {
            console.log("Auto-play bloqueado por el navegador. Esperando interacción.");
        });
    }

    function toggleAudio() {
        if (isMuted) {
            bgMusic.play();
            isMuted = false;
        } else {
            bgMusic.pause();
            isMuted = true;
        }
        updateAudioIcons();
    }

    function updateAudioIcons() {
        if (isMuted) {
            musicOnIcon.style.display = 'none';
            musicOffIcon.style.display = 'block';
        } else {
            musicOnIcon.style.display = 'block';
            musicOffIcon.style.display = 'none';
        }
    }

    if (audioToggle) {
        audioToggle.addEventListener('click', toggleAudio);
    }


    // --- 3. EFECTO DE PÉTALOS DE ROSA CAYENDO ---
    const petalsContainer = document.getElementById('petals-container');
    
    function startPetalsEffect() {
        setInterval(createPetal, 400);
    }

    function createPetal() {
        if (!petalsContainer) return;
        
        // Limitar la cantidad máxima de pétalos en pantalla para optimizar rendimiento móvil
        if (petalsContainer.children.length > 20) {
            return;
        }

        const petal = document.createElement('div');
        petal.classList.add('petal');
        
        // Parámetros de tamaño aleatorio (de 25px a 45px) para mostrar el detalle
        const size = Math.random() * 20 + 25;
        petal.style.width = `${size}px`;
        petal.style.height = `${size}px`;
        
        // Posición horizontal inicial aleatoria
        petal.style.left = `${Math.random() * 100}%`;
        
        // Tiempo de animación aleatorio (duración de la caída)
        const duration = Math.random() * 5 + 5; 
        petal.style.animation = `fall ${duration}s linear forwards`;
        petal.style.animationDelay = `${Math.random() * 2}s`;

        // Seleccionar aleatoriamente entre los dos diseños de pétalos PNG transparentes
        const petalImages = [
            'url("assets/petal.png")',
            'url("assets/petal_white.png")'
        ];
        petal.style.backgroundImage = petalImages[Math.floor(Math.random() * petalImages.length)];
        
        // Opcionalmente podemos voltear algunos pétalos aleatoriamente para mayor variedad
        if (Math.random() > 0.5) {
            petal.style.transform = `scaleX(-1)`;
        }

        petalsContainer.appendChild(petal);
        setTimeout(() => {
            petal.remove();
        }, (duration + 2) * 1000);
    }


    // --- 4. CUENTA REGRESIVA EN TIEMPO REAL ---
    const targetDate = new Date('2026-11-07T18:00:00').getTime();

    function updateCountdown() {
        const now = new Date().getTime();
        const difference = targetDate - now;

        if (difference <= 0) {
            document.getElementById('days').innerText = '00';
            document.getElementById('hours').innerText = '00';
            document.getElementById('minutes').innerText = '00';
            document.getElementById('seconds').innerText = '00';
            return;
        }

        const days = Math.floor(difference / (1000 * 60 * 60 * 24));
        const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((difference % (1000 * 60)) / 1000);

        document.getElementById('days').innerText = days < 10 ? '0' + days : days;
        document.getElementById('hours').innerText = hours < 10 ? '0' + hours : hours;
        document.getElementById('minutes').innerText = minutes < 10 ? '0' + minutes : minutes;
        document.getElementById('seconds').innerText = seconds < 10 ? '0' + seconds : seconds;
    }

    updateCountdown();
    setInterval(updateCountdown, 1000);


    // --- 5. LÓGICA DE FORMULARIO RSVP CON RATE LIMIT (MÁX. 3 INTENTOS) ---
    const addCompanionBtn = document.getElementById('add-companion-btn');
    const companionsContainer = document.getElementById('companions-container');
    const rsvpLimitMsg = document.getElementById('rsvp-limit');
    const maxCompanions = 2; // 1 titular + 2 acompañantes = 3 personas máximo
    const MAX_RSVP_ATTEMPTS = 3;

    function getRsvpAttempts() {
        try {
            return parseInt(localStorage.getItem('valeria_rsvp_attempts') || '0', 10);
        } catch (e) {
            return 0;
        }
    }

    function checkRsvpLimit() {
        if (getRsvpAttempts() >= MAX_RSVP_ATTEMPTS) {
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.style.opacity = '0.6';
                submitBtn.style.cursor = 'not-allowed';
            }
            if (rsvpLimitMsg) rsvpLimitMsg.style.display = 'block';
            return true;
        }
        return false;
    }

    checkRsvpLimit();

    if (addCompanionBtn && companionsContainer) {
        addCompanionBtn.addEventListener('click', () => {
            const currentCompanions = companionsContainer.querySelectorAll('.companion-row').length;
            if (currentCompanions < maxCompanions) {
                const companionIndex = currentCompanions + 1;
                const row = document.createElement('div');
                row.className = 'companion-row';
                row.style.cssText = 'display: flex; gap: 0.35rem; margin-top: 0.4rem; align-items: center;';
                
                row.innerHTML = `
                    <input type="text" class="form-input companion-input" style="width: 100%;" placeholder="Nombre de acompañante ${companionIndex}" required>
                    <button type="button" class="btn-remove-companion" style="background: none; border: none; color: #b71c1c; font-size: 1.2rem; cursor: pointer; padding: 0 0.35rem; line-height: 1; font-weight: bold;" title="Eliminar">✕</button>
                `;

                // Botón para eliminar este acompañante
                row.querySelector('.btn-remove-companion').addEventListener('click', () => {
                    row.remove();
                    updateCompanionButton();
                });

                companionsContainer.appendChild(row);
                updateCompanionButton();
            }
        });

        function updateCompanionButton() {
            const count = companionsContainer.querySelectorAll('.companion-row').length;
            if (count >= maxCompanions) {
                addCompanionBtn.style.display = 'none';
            } else {
                addCompanionBtn.style.display = 'inline';
            }
        }
    }

    if (rsvpForm) {
        rsvpForm.addEventListener('submit', (e) => {
            e.preventDefault();

            if (checkRsvpLimit()) return;

            submitBtn.disabled = true;
            submitBtn.innerText = 'Enviando...';
            if (rsvpSuccess) rsvpSuccess.style.display = 'none';
            if (rsvpError) rsvpError.style.display = 'none';
            if (rsvpLimitMsg) rsvpLimitMsg.style.display = 'none';

            const guestName = document.getElementById('guest-name').value.trim();
            const companionInputs = document.querySelectorAll('.companion-input');
            const companionNames = Array.from(companionInputs).map(inp => inp.value.trim()).filter(Boolean);

            let formattedName = guestName;
            if (companionNames.length > 0) {
                formattedName += ` (Acompañantes: ${companionNames.join(', ')})`;
            }

            // Incrementar contador de intentos (Rate limit)
            try {
                const newAttempts = getRsvpAttempts() + 1;
                localStorage.setItem('valeria_rsvp_attempts', newAttempts.toString());
            } catch(e) {}

            // Simulación si no está configurada la URL
            if (!GOOGLE_SCRIPT_URL) {
                setTimeout(() => {
                    submitBtn.disabled = false;
                    submitBtn.innerText = 'Confirmar Asistencia';
                    if (rsvpSuccess) rsvpSuccess.style.display = 'block';
                    rsvpForm.reset();
                    if (companionsContainer) {
                        companionsContainer.innerHTML = '';
                        if (addCompanionBtn) addCompanionBtn.style.display = 'inline';
                    }
                    checkRsvpLimit();
                }, 1200);
                return;
            }

            const params = new URLSearchParams();
            // Campos principales que registra Google Apps Script en la hoja
            params.append('nombre', formattedName);
            params.append('asistencia', 'Sí');
            // Campos adicionales por compatibilidad con múltiples formatos de Apps Script
            params.append('name', formattedName);
            params.append('titular', guestName);
            params.append('companion', companionNames.join(', '));
            params.append('companions', companionNames.join(', '));
            params.append('acompaniante', companionNames.join(', '));
            params.append('acompaniantes', companionNames.join(', '));
            companionNames.forEach((comp, idx) => {
                params.append(`acompaniante_${idx + 1}`, comp);
                params.append(`companion_${idx + 1}`, comp);
            });
            params.append('attendance', 'Sí');

            fetch(GOOGLE_SCRIPT_URL, {
                method: 'POST',
                mode: 'no-cors',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: params
            })
            .then(() => {
                submitBtn.disabled = false;
                submitBtn.innerText = 'Confirmar Asistencia';
                if (rsvpSuccess) rsvpSuccess.style.display = 'block';
                rsvpForm.reset();
                if (companionsContainer) {
                    companionsContainer.innerHTML = '';
                    if (addCompanionBtn) addCompanionBtn.style.display = 'inline';
                }
                checkRsvpLimit();
            })
            .catch(err => {
                console.error("Error:", err);
                submitBtn.disabled = false;
                submitBtn.innerText = 'Confirmar Asistencia';
                if (rsvpError) rsvpError.style.display = 'block';
            });
        });
    }

    // --- 6. CERRAR INVITACIÓN (VENTANA O PESTAÑA) ---
    const btnCloseBook = document.getElementById('btn-close-book');
    if (btnCloseBook) {
        btnCloseBook.addEventListener('click', () => {
            // Intentar cerrar la ventana/pestaña
            window.close();
            setTimeout(() => {
                try {
                    window.open('', '_self', '');
                    window.close();
                } catch(e) {}
            }, 100);
        });
    }
});
