# Jogo da Vida - Magnólia

[Volver al portafolio — AI/Agent](https://paulosanches.github.io/hello/es/agent/)

Language: es

Fuente: https://paulosanches.github.io/hello/es/portfolio/jogo-da-vida-magnolia/agent/

[English](https://paulosanches.github.io/hello/portfolio/jogo-da-vida-magnolia/case.md) · [Português do Brasil](https://paulosanches.github.io/hello/pt/portfolio/jogo-da-vida-magnolia/case.md) · [Italiano](https://paulosanches.github.io/hello/it/portfolio/jogo-da-vida-magnolia/case.md) · [Español](https://paulosanches.github.io/hello/es/portfolio/jogo-da-vida-magnolia/case.md)

---

Portfolio / Side Quests

Un juego de mesa interactivo basado en historias y reflexión.

[![Captura de pantalla de Jogo da Vida - Magnólia, con el tablero ilustrado en la casilla final.](https://paulosanches.github.io/hello/assets/side-quest-magnolia.png)](https://paulosanches.github.io/hello/assets/side-quest-magnolia.png)

El tablero ilustrado al final del juego. [Ver la captura a tamaño completo](https://paulosanches.github.io/hello/assets/side-quest-magnolia.png)

## El producto

Jogo da Vida - Magnólia reúne 12 casillas ilustradas, historias de personajes y 10 preguntas para reflexionar en un juego de navegador para ordenador y móvil. Los jugadores controlan el ritmo. No hay puntuación ni formulario de respuestas; las preguntas están pensadas para debatir fuera de la aplicación.

## La experiencia

Cada casilla conecta una posición del tablero con una historia. El texto aparece de forma progresiva, seguido de una pregunta que mantiene la historia visible como referencia.

Los jugadores pueden avanzar, volver a una casilla anterior, pausar la aparición del texto o reiniciar el juego. Pasar a la siguiente casilla es siempre una decisión manual.

## Diseño técnico

### Arquitectura en ejecución

HTML, CSS y SVG definen la interfaz y el tablero ilustrado. JavaScript gestiona la casilla activa, el estado de la historia y la pregunta y las transiciones en el navegador. GitHub Pages sirve la aplicación estática; el juego no necesita un backend de aplicación ni una base de datos.

### Reproducción y navegación

Un controlador de reproducción dedicado gestiona la tarea actual, el temporizador y los estados de escritura, espera y pausa. Utiliza un intervalo de 24 ms y una espera de lectura de 3.000 ms antes de presentar una pregunta. La presentación automática espera mientras hay texto seleccionado, el panel de lectura tiene el foco del teclado o queda contenido sin leer por debajo de la posición de desplazamiento.

La navegación cancela el trabajo de reproducción pendiente, mientras que las comprobaciones del estado de ejecución evitan transiciones superpuestas. Pausar u ocultar la pestaña suspende la programación de tareas. El avance entre las casillas sigue siendo manual.

### Diseño de lectura y accesibilidad

El texto completo reserva su espacio en el diseño antes de que empiece el efecto de escritura, en lugar de cambiar el tamaño del globo con cada carácter. Una capa visual separada controla la aparición progresiva, mientras el texto completo sigue disponible para las tecnologías de asistencia.

La interfaz admite navegación con teclado y prefers-reduced-motion. La historia y la pregunta permanecen visibles a la vez.

### Contenido y control de versiones

Google Sheets permitió la edición colaborativa durante la preparación. Tras la aprobación editorial, se eliminó esa dependencia y el contenido final se publicó junto con el código. Esto mantiene la narrativa vinculada a una versión, pero exige un nuevo despliegue para cambiar el contenido.

### Pruebas y publicaciones

Las comprobaciones automatizadas cubren contenido, navegación, imágenes y diseño, y se complementan con verificaciones en el navegador con distintos tamaños de pantalla.

Un script de publicación escribe la misma marca de tiempo UTC en la página y en version.json, y añade parámetros de versión derivados de SHA-256 a las URL de JavaScript y CSS. Su modo de comprobación verifica la coherencia de las marcas de tiempo; no vuelve a calcular los hashes de los archivos. Los archivos publicados y el comportamiento en el navegador se comprueban por separado para confirmar la versión entregada.

### Herramientas de desarrollo

Hermes Agent y Codex apoyaron la implementación y las pruebas en un MacBook Air M1, con solicitudes y revisiones a través de Telegram. ChatGPT generó las ilustraciones de los personajes a partir de las fotografías proporcionadas; Hermes preparó e integró los archivos. Skills reutilizables guiaron el diseño, las pruebas, la depuración y la revisión. Estas herramientas forman parte del flujo de desarrollo, no de la ejecución del juego.

## Explora el proyecto

- [Abrir el juego](https://paulosanches.github.io/magnolia-jogo-da-vida/)
- [Código en GitHub](https://github.com/PauloSanches/magnolia-jogo-da-vida)
- [Ver cómo se hizo](https://paulosanches.github.io/magnolia-jogo-da-vida/backstage/)

Juego y detalles de su creación en portugués.
