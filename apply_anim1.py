import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove old animation block (Option 3)
old_anim_pattern = re.compile(r'/\*\s*Animación de la cita del prólogo \(Opción 3: Pluma Invisible\)\s*\*/.*', re.DOTALL)
css = old_anim_pattern.sub('', css)

new_anim = '''
/* Animación de la cita del prólogo (Opción 1: Revelación Mágica) */
.animated-quote {
    opacity: 0;
}

.page.active-page .animated-quote {
    opacity: 1;
}

.page.active-page .animated-quote p {
    opacity: 0;
    animation: blurReveal 3s ease-out forwards;
    animation-delay: 0.8s;
}

.page.active-page .animated-quote p:nth-child(1) {
    color: var(--color-text-dark);
}

.page.active-page .animated-quote p:nth-child(2) {
    color: var(--color-gold-dark);
    animation-delay: 2.5s;
    animation-duration: 2s;
}

@keyframes blurReveal {
    0% {
        filter: blur(15px);
        opacity: 0;
        transform: scale(1.1) translateY(10px);
    }
    100% {
        filter: blur(0px);
        opacity: 1;
        transform: scale(1) translateY(0);
    }
}
'''

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css.strip() + '\n' + new_anim)
