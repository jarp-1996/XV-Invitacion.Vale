import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Quitar el color forzado para permitir que la animación CSS lo controle
html = html.replace('color: var(--color-text-dark);"', '"')
html = html.replace('color: var(--color-gold-dark); text-align: center; width: 100%;"', 'text-align: center; width: 100%;"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove old animation block
old_anim_pattern = re.compile(r'/\*\s*Animación de la cita del prólogo\s*\*/.*', re.DOTALL)
css = old_anim_pattern.sub('', css)

new_anim = '''
/* Animación de la cita del prólogo (Opción 2: Resplandor Dorado) */
.animated-quote {
    opacity: 0;
}

.page.active-page .animated-quote {
    opacity: 1;
}

.page.active-page .animated-quote p {
    opacity: 0;
    animation: goldenGlowFade 3.5s cubic-bezier(0.25, 0.8, 0.25, 1) forwards;
    animation-delay: 0.8s;
}

.page.active-page .animated-quote p:nth-child(1) {
    color: var(--color-text-dark); /* Fallback */
}

.page.active-page .animated-quote p:nth-child(2) {
    color: var(--color-gold-dark); /* Fallback */
    animation-delay: 2.0s; /* El autor aparece un poco despues */
}

@keyframes goldenGlowFade {
    0% {
        opacity: 0;
        filter: brightness(2) drop-shadow(0 0 5px rgba(212, 175, 55, 0));
        transform: scale(0.95);
    }
    40% {
        opacity: 1;
        filter: brightness(3) drop-shadow(0 0 15px rgba(212, 175, 55, 1)) drop-shadow(0 0 30px rgba(212, 175, 55, 0.8));
        transform: scale(1.02);
    }
    100% {
        opacity: 1;
        filter: brightness(1) drop-shadow(0 0 0px rgba(212, 175, 55, 0));
        transform: scale(1);
    }
}
'''

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css + new_anim)
