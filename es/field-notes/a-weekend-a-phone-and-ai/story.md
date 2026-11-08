# ¿Qué puedes crear en un fin de semana con un teléfono e IA?

[Volver al portafolio — AI/Agent](https://paulosanches.github.io/hello/es/agent/)

Language: es

Fuente: https://paulosanches.github.io/hello/es/field-notes/a-weekend-a-phone-and-ai/agent/

[English](https://paulosanches.github.io/hello/field-notes/a-weekend-a-phone-and-ai/story.md) · [Português do Brasil](https://paulosanches.github.io/hello/pt/field-notes/a-weekend-a-phone-and-ai/story.md) · [Italiano](https://paulosanches.github.io/hello/it/field-notes/a-weekend-a-phone-and-ai/story.md) · [Español](https://paulosanches.github.io/hello/es/field-notes/a-weekend-a-phone-and-ai/story.md)

---

IA E INGENIERÍA

Cómo utilicé Codex por texto y voz para construir, probar y publicar mi portafolio.

2 min de lectura

[![Diagrama del setup que muestra las instrucciones por texto y voz desde el teléfono, la implementación y las comprobaciones con Codex, los commits de GitHub, el alojamiento en GitHub Pages, tres versiones de idioma y un ciclo de revisión.](https://paulosanches.github.io/hello/assets/portfolio-build-setup.webp?v=f8526c37b759)](https://paulosanches.github.io/hello/assets/portfolio-build-setup.webp?v=f8526c37b759)

[Ver el diagrama a tamaño completo](https://paulosanches.github.io/hello/assets/portfolio-build-setup.webp?v=f8526c37b759)

En un fin de semana construí este portafolio guiando a Codex desde mi teléfono. Compartí mi currículum y mis fotos, aporté referencias visuales y definí cómo quería presentar mi experiencia. Algunas historias las escribí y otras las dicté.

Dirigía el trabajo con instrucciones breves y comprobaba el resultado en el navegador. Codex editaba los archivos y ejecutaba comandos en su entorno de desarrollo. Desde el teléfono revisaba el contenido, el diseño y el comportamiento, y después indicaba los siguientes ajustes.

Publiqué el portafolio con **alojamiento gratuito en GitHub Pages**, usando **HTML, CSS y JavaScript**, sin utilizar Vercel ni Supabase. Las páginas estáticas y las interacciones en el navegador cubrían lo que quería construir. Codex registraba los cambios en GitHub, y el flujo de compilación y despliegue de GitHub Pages publicaba los archivos.

Para ofrecer el contenido en **inglés, italiano y portugués de Brasil**, usamos un script de Python para generar las páginas a partir de los archivos de origen y las traducciones. Cada idioma tiene sus propias URL, metadatos y enlaces a las otras versiones. Añadimos un mapa del sitio, URL canónicas y datos estructurados para el perfil y los artículos.

Para las interacciones, incluí Easter eggs que reconocen `redbull`, `gameday` y `goodmorning`. JavaScript cambia el tema, la foto y una frase del banner. Las variables CSS aplican los colores, mientras que `sessionStorage` mantiene la selección mientras los visitantes navegan en la misma pestaña.

La validación formó parte de la entrega. Codex comprobó las páginas en Chromium y WebKit con distintos anchos de pantalla, verificando imágenes, enlaces, traducciones y componentes. Mis revisiones desde el móvil complementaban esas comprobaciones con ajustes de legibilidad, encuadre y organización.

Me centré en la experiencia de quien visita el sitio: una identidad visual propia, navegación adaptable, tarjetas y páginas dedicadas a las historias. Con una arquitectura sencilla y alojamiento gratuito, publiqué un portafolio con interacciones pensadas para mi perfil, dirigiendo el proyecto por texto y voz.

## Sigamos conversando

¿Estás usando IA y agentes en tus proyectos?

[Escríbeme por LinkedIn](https://www.linkedin.com/in/paulosanches)

Tomemos un café virtual para intercambiar experiencias.
