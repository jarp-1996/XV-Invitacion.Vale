# Invitación Interactiva de Quince Años: La Bella y la Bestia 🥀✨

Un proyecto web de una invitación digital elegante, interactiva y con temática de *La Bella y la Bestia*, desarrollada para los Quince Años de Valeria. 
La aplicación simula un libro antiguo encuadernado en cuero y detalles dorados que se abre para revelar pergaminos, animaciones mágicas y un sistema de confirmación de asistencia (RSVP) integrado con Google Sheets.

## 🌟 Características Destacadas

* **Libro Interactivo 3D:** Animación CSS 3D personalizada que simula la apertura de la portada y el pase de páginas (`rotateY`), ofreciendo una experiencia inmersiva.
* **Diseño UI/UX Temático:** Inspirado en la magia de los cuentos de hadas. Paleta de colores basada en dorado (oro antiguo), azul marino y rojo rosa. Uso extensivo de Glassmorphism, pergaminos, texturas y sombras.
* **Animaciones "Mágicas":** Efectos de revelación con combinación de `filter: blur()`, `text-shadow` y escalado, logrando que el texto y las ilustraciones "aparezcan" mágicamente de la niebla como un encantamiento.
* **Lluvia de Pétalos Dinámica:** Partículas generadas de forma dinámica en JavaScript (`createPetal()`) con tamaños, duraciones y posiciones aleatorias que caen por toda la pantalla.
* **Sistema RSVP Serverless:** Formulario de confirmación de asistencia conectado a una API de Google Apps Script, que registra directamente a los invitados en un documento de Google Sheets sin necesidad de backend o base de datos pesada.
* **Música de Fondo Integrada:** Reproducción automática en bucle de la versión instrumental filarmónica del tema central para completar la inmersión del usuario al abrir el libro.
* **Mobile-First & Touch Swipe:** Totalmente adaptable (responsive) y programada para soportar navegación mediante gestos táctiles (Swipe L/R) en dispositivos móviles.

## 🛠️ Stack Tecnológico

* **Frontend:** HTML5 Semántico, CSS3 Moderno (Custom Properties, Flexbox, CSS Animations, 3D Transforms, Keyframes) y JavaScript Vanilla (ES6+).
* **Backend / Database:** Google Apps Script & Google Sheets (para recepción de formularios CORS-friendly).
* **Despliegue (CI/CD):** Vercel integrado con GitHub para despliegues automáticos (Push-to-Deploy).

## 🚀 Instalación y Despliegue Local

1. Clona este repositorio:
   ```bash
   git clone https://github.com/jarp-1996/XV-Invitacion.Vale.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd XV-Invitacion.Vale
   ```
3. Ejecuta un servidor local rápido con Python:
   ```bash
   python -m http.server 8000
   ```
4. Abre `http://localhost:8000` en tu navegador.

## 🎨 Sistema de Diseño (Design System)

El proyecto incluye un archivo `design-system.html` auto-documentado. Este archivo actúa como la fuente de la verdad para todos los componentes visuales:
- **Tipografía:** Playfair Display (Serif), Great Vibes (Cursive), Lora.
- **Botones y Nav:** Estados Hover con brillo metálico animado y transformaciones 3D.
- **Componentes:** Cajas de pergamino, separadores dorados, campos de formulario con estética royal.
- **Visuales:** Archivos de portada, texturas y rosas encantadas (`/assets`).

## 👨‍💻 Autor y Contribuciones

Desarrollado y conceptualizado para fines de celebración y como muestra de desarrollo Frontend moderno con énfasis en Micro-interacciones y UI inmersiva.

---
*«Los que no creen en la magia nunca la encontrarán.»*
