/* ==========================================================================
   LÓGICA INTERACTIVA DE PÁGINA POR PÁGINA - INVITACIÓN DE VALERIA
   ========================================================================== */

// --- PANTALLA DE CARGA (LOADER) ---
window.addEventListener('load', () => {
    const loader = document.getElementById('loader-wrapper');
    if (loader) {
        setTimeout(() => {
            loader.classList.add('fade-out');
        }, 500); // Pequeño retraso para asegurar carga de tipografías pesadas
    }
});

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
    const totalPages = 6;
    let isAnimating = false; // Bloqueo anti-doble-click durante la animación

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
            setTimeout(() => { isAnimating = false; }, 700); // Duración de la transición CSS
        }
    }

    function goPrev() {
        if (isAnimating) return;
        if (currentPage > 1) {
            isAnimating = true;
            currentPage--;
            const page = document.getElementById(`page-${currentPage}`);
            if (page) page.classList.remove('flipped');
            setTimeout(() => { isAnimating = false; }, 700);
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
        const threshold = 40; // Distancia mínima en píxeles
        if (touchStartX - touchEndX > threshold) {
            goNext(); // Swipe a la izquierda
        }
        if (touchEndX - touchStartX > threshold) {
            goPrev(); // Swipe a la derecha
        }
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


    // --- 5. LÓGICA DE FORMULARIO RSVP ---
    if (rsvpForm) {
        rsvpForm.addEventListener('submit', (e) => {
            e.preventDefault();

            submitBtn.disabled = true;
            submitBtn.innerText = 'Enviando...';
            rsvpSuccess.style.display = 'none';
            rsvpError.style.display = 'none';

            const guestName = document.getElementById('guest-name').value;
            const attendanceValue = document.querySelector('input[name="attendance"]:checked').value;

            const rsvpData = {
                name: guestName,
                attendance: attendanceValue === 'si' ? 'Sí' : 'No'
            };

            // Simulación si no está configurada la URL
            if (!GOOGLE_SCRIPT_URL) {
                setTimeout(() => {
                    submitBtn.disabled = false;
                    submitBtn.innerText = 'Confirmar Asistencia';
                    rsvpSuccess.style.display = 'block';
                    rsvpForm.reset();
                }, 1200);
                return;
            }

            const params = new URLSearchParams();
            for (const key in rsvpData) {
                params.append(key, rsvpData[key]);
            }

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
                rsvpSuccess.style.display = 'block';
                rsvpForm.reset();
            })
            .catch(err => {
                console.error("Error:", err);
                submitBtn.disabled = false;
                submitBtn.innerText = 'Confirmar Asistencia';
                rsvpError.style.display = 'block';
            });
        });
    }
});
