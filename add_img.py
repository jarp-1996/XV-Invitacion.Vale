import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

img_tag = '<img src="assets/princesa_bailando.png" alt="Princesa" class="prologue-illustration">'
html = html.replace('<div class="animated-quote">\n                            <p class="text-serif text-story"', 
                    f'<div class="animated-quote">\n                            {img_tag}\n                            <p class="text-serif text-story"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* Ilustración del prólogo */
.prologue-illustration {
    display: block;
    margin: 0 auto 1.5rem;
    max-width: 140px;
    height: auto;
    opacity: 0;
    filter: drop-shadow(0 0 10px rgba(212, 175, 55, 0));
}

.page.active-page .prologue-illustration {
    animation: blurGlowReveal 1.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
    animation-delay: 0.6s; /* Aparece un poquito antes que el texto */
}
'''
with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(new_css)
