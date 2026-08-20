import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove old animation block (Option 2)
old_anim_pattern = re.compile(r'/\*\s*Animación de la cita del prólogo \(Opción 2: Resplandor Dorado\)\s*\*/.*', re.DOTALL)
css = old_anim_pattern.sub('', css)

new_anim = '''
/* Animación de la cita del prólogo (Opción 3: Pluma Invisible) */
.animated-quote {
    opacity: 0;
}

.page.active-page .animated-quote {
    opacity: 1;
}

.page.active-page .animated-quote p {
    clip-path: inset(0 100% 0 0);
    opacity: 0;
    animation: wipeReveal 3.5s cubic-bezier(0.4, 0.0, 0.2, 1) forwards;
    animation-delay: 0.8s;
}

.page.active-page .animated-quote p:nth-child(1) {
    color: var(--color-text-dark);
}

.page.active-page .animated-quote p:nth-child(2) {
    color: var(--color-gold-dark);
    animation-delay: 3.5s; /* El autor aparece justo cuando termina la frase */
    animation-duration: 2s; /* Se revela más rápido */
}

@keyframes wipeReveal {
    0% {
        clip-path: inset(0 100% 0 0);
        opacity: 0.2;
    }
    10% {
        opacity: 1;
    }
    100% {
        clip-path: inset(0 -5% 0 0); /* -5% por si acaso recorta itálicas */
        opacity: 1;
    }
}
'''

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css.strip() + '\n' + new_anim)
