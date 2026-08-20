import re

# Read index.html to extract all 6 pages' contents
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

pages = []
for i in range(1, 7):
    # Match everything inside <div class="page" id="page-X"> ... </div> (but stopping before the next page)
    # The safest way is to find the opening <div class="page-content" and capture until the matching closing div of the page.
    # But regex is tricky for nested divs.
    # Instead, let's use a simpler approach.
    pass

# We will just construct the HTML manually using the known structure
new_views = ''

# Page 1
p1 = re.search(r'(<div class="page-content-front".*?</div>\s*</div>)', index_html, re.DOTALL).group(1)
new_views += f'''
                <div class="ds-page-frame">
                    <h4>Página 1: Portada</h4>
                    <div class="ds-page-container">
                        {p1}
                    </div>
                </div>
'''

# Pages 2 to 6
for i in range(2, 7):
    title = ""
    if i == 2: title = "Prólogo Animado"
    elif i == 3: title = "Cuándo & Dónde"
    elif i == 4: title = "Detalles (Dress Code & Regalos)"
    elif i == 5: title = "RSVP"
    elif i == 6: title = "Contratapa"
    
    # Capture <div class="page-content...
    # Since page-nav is inside, we can just grab from <div class="page-content to the div before <!-- PÁGINA
    pattern = f'<!-- PÁGINA {i}.*?(<div class="page-content.*?)<!-- PÁGINA {i+1}'
    if i == 6:
        pattern = f'<!-- PÁGINA 6.*?(<div class="page-content.*?)(?=</div>\s*</div>\s*</div>\s*<!-- Elemento de Audio)'
    
    match = re.search(pattern, index_html, re.DOTALL | re.IGNORECASE)
    if match:
        content = match.group(1).strip()
        # Remove the closing </div> of the page wrapper which we might have grabbed
        if content.endswith('</div>\n                </div>'):
            content = content[:-13].strip()
        
        new_views += f'''
                <div class="ds-page-frame">
                    <h4>Página {i}: {title}</h4>
                    <div class="ds-page-container">
                        {content}
                    </div>
                </div>
'''

# Now inject into design-system.html
with open('design-system.html', 'r', encoding='utf-8') as f:
    ds_html = f.read()

ds_html = re.sub(r'<div class="ds-book-preview-grid">.*?</div>\s*</section>', f'<div class="ds-book-preview-grid">{new_views}            </div>\n        </section>', ds_html, flags=re.DOTALL)

with open('design-system.html', 'w', encoding='utf-8') as f:
    f.write(ds_html)
