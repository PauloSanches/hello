# Una semana en la playa. Un incidente de seguridad el segundo día.

[Volver al portafolio — AI/Agent](https://paulosanches.github.io/hello/es/agent/)

Language: es

Fuente: https://paulosanches.github.io/hello/es/field-notes/security-at-the-beach/agent/

[English](https://paulosanches.github.io/hello/field-notes/security-at-the-beach/story.md) · [Português do Brasil](https://paulosanches.github.io/hello/pt/field-notes/security-at-the-beach/story.md) · [Italiano](https://paulosanches.github.io/hello/it/field-notes/security-at-the-beach/story.md) · [Español](https://paulosanches.github.io/hello/es/field-notes/security-at-the-beach/story.md)

---

SEGURIDAD Y LIDERAZGO

Fui a trabajar una semana en una casa de playa, con la idea de pasar más tiempo con mi familia. El segundo día, un incidente de seguridad en producción cambió los planes.

4 min de lectura

![Vista costera pixelada con palmeras, una playa de arena y agua turquesa.](https://paulosanches.github.io/hello/assets/field-notes-beach.png?v=cfb755a41222)

Acababan de ascenderme a Manager. Entre mis nuevas responsabilidades, había asumido los roles de Delivery Lead y Solution Architect de un proyecto de marketing y CMS para una de las principales empresas del agronegocio de Brasil.

La solución utilizaba Liferay Portal y llevaba tres años en producción. El equipo del proyecto tenía solo dos personas, no había problemas relevantes registrados y el cliente estaba negociando la renovación del contrato. Era un proyecto pequeño por el tamaño del equipo, pero importante para la cuenta.

Con todo aparentemente bajo control, trabajar desde la casa de la playa parecía sencillo. Esperaba una semana normal de trabajo con más tiempo cerca de mi familia.

## Cuando la inestabilidad se convirtió en un incidente de seguridad

El segundo día identificamos un proceso sospechoso en el servidor de producción. El consumo de memoria seguía aumentando, sobrecargaba el entorno y provocaba reinicios. Lo que al principio parecía un problema de estabilidad se convirtió en un incidente de seguridad.

Activamos los protocolos de incidentes de la empresa, escalamos el caso y organizamos una sala de crisis. Mi responsabilidad era coordinar la respuesta técnica, organizar las siguientes acciones y mantener al cliente y a los responsables informados sobre el problema y nuestros avances.

## Encontrar la corrección era solo una parte del trabajo

Durante la investigación encontramos algo que complicaba la respuesta. En la fase de venta, el proyecto se había diseñado con la edición Community de Liferay. En ese contexto, no contábamos con el soporte ni con las correcciones disponibles que necesitábamos para responder con rapidez.

Identificamos vulnerabilidades conocidas en la versión que utilizábamos, pero no encontramos un paquete de actualización listo para instalar que las corrigiera.

Después de buscar en foros y abrir solicitudes de soporte con especialistas, descubrimos que la comunidad había publicado una corrección. Pero había un paso adicional: teníamos que descargar varios gigabytes de archivos y compilar la aplicación antes de instalar la versión actualizada en el servidor.

Fue entonces cuando la conexión de la casa de playa dejó de ser un detalle menor. Las descargas y la compilación nos llevaron dos noches completas.

## Mantener a todos informados

A medida que avanzaban las descargas, aumentaba la presión. El incidente ya estaba siendo seguido por líderes de toda América Latina, que solicitaban actualizaciones varias veces al día.

Tenía que trabajar en dos frentes: ayudar al equipo a llegar a una solución y explicar con claridad a las partes interesadas lo que sabíamos, lo que seguía en investigación y cuáles serían los siguientes pasos.

> Tenía que dejar claros los siguientes pasos sin prometer un plazo que todavía no podíamos respaldar.

Resolver el problema técnico y comunicar nuestros avances formaban parte de la respuesta. Todavía había incertidumbres y necesitaba ser transparente al respecto.

Finalmente compilamos e instalamos la versión actualizada, corregimos las vulnerabilidades que habíamos identificado y cerramos el incidente.

Apenas pude disfrutar de la playa. Gran parte de la semana transcurrió entre reuniones, investigación técnica y noches de trabajo, en un entorno que no estaba preparado para esa rutina. Fue una de las experiencias más intensas de mi carrera.

## Lo que me llevé

### El mantenimiento y el soporte forman parte de la propuesta

El coste de una solución debe contemplar el mantenimiento, las actualizaciones y el soporte. En este proyecto, la elección de la edición Community creó una dificultad que solo se hizo evidente cuando tuvimos que responder a una crisis. Si esas capacidades son necesarias para atender al cliente, deben formar parte de la propuesta desde el principio.

### Liderar es organizar toda la respuesta

La solución técnica es solo una parte del trabajo. También hay que organizar la respuesta, apoyar al equipo y comunicar los avances con transparencia, incluso cuando aún quedan preguntas sin respuesta.

### Trabajar desde cualquier lugar exige preparación

Poder trabajar desde cualquier lugar también exige pensar en las condiciones necesarias para afrontar lo inesperado. La conexión y el entorno de trabajo importan cuando un día normal se convierte en una crisis.

Acababa de asumir un puesto de gestión y esperaba una semana tranquila. En cambio, desde una casa de playa, recibí una lección práctica sobre responsabilidad, toma de decisiones y liderazgo bajo presión.

## Más sobre la parte técnica

Si te gustaría conocer los detalles técnicos de este incidente y crees que podrían serte útiles, estaré encantado de conversar sobre ellos.

[Escríbeme en LinkedIn](https://www.linkedin.com/in/paulosanches)
