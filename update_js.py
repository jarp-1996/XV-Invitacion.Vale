import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace btn-close-book and add-companion logic at the bottom of DOMContentLoaded, right before `// --- 4. FORMULARIO RSVP ---`
add_logic = r'''
    // --- 3.5. LOGICA DE CERRAR LIBRO Y ACOMPAÑANTES ---
    const btnCloseBook = document.getElementById('btn-close-book');
    if (btnCloseBook) {
        btnCloseBook.addEventListener('click', () => {
            document.querySelectorAll('.page').forEach(p => p.classList.remove('flipped'));
            currentPage = 1;
        });
    }

    const addCompBtn = document.getElementById('add-companion-btn');
    const compField = document.getElementById('companion-field');
    if (addCompBtn && compField) {
        addCompBtn.addEventListener('click', () => {
            compField.style.display = 'block';
            addCompBtn.style.display = 'none';
        });
    }

    // --- 4. FORMULARIO RSVP ---'''

js = js.replace('// --- 4. FORMULARIO RSVP ---', add_logic)

# Replace the data encoding in the fetch request
old_fetch_logic = r'''            const name = document.getElementById('guest-name').value;
            const attendance = document.querySelector('input[name="attendance"]:checked').value;
            
            // Convertimos a URL encoded para Google Apps Script
            const data = new URLSearchParams();
            data.append('nombre', name);
            data.append('asistencia', attendance);'''

new_fetch_logic = r'''            const rawName = document.getElementById('guest-name').value;
            const comp = document.getElementById('companion-name') ? document.getElementById('companion-name').value : '';
            const diet = document.getElementById('diet-req') ? document.getElementById('diet-req').value : '';
            
            let finalName = rawName;
            let extras = [];
            if(comp) extras.push(`Acomp: ${comp}`);
            if(diet) extras.push(`Dieta: ${diet}`);
            if(extras.length > 0) finalName += ` (${extras.join(', ')})`;

            const attendance = document.querySelector('input[name="attendance"]:checked').value;
            
            // Convertimos a URL encoded para Google Apps Script
            const data = new URLSearchParams();
            data.append('nombre', finalName);
            data.append('asistencia', attendance);'''

js = js.replace(old_fetch_logic, new_fetch_logic)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
