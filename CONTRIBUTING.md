# Guía de contribución

¡Gracias por tu interés en contribuir a Kingdom Hall Attendant! Nos alegra contar con tu apoyo. Aquí te proporcionamos algunas directrices para ayudarte a comenzar.

## Tecnologías utilizadas

- **Lenguajes y Frameworks**: Python, Flask, HTML, SQLite
- **Traducciones**: PyBabel
- **Hosting**: PythonAnywhere
- **Dominio**: GoDaddy
- **Financiamiento**: OpenCollective
- **Desktop Client**: Electron (renderiza la URL pública getkha.org) _github.com/livrasand/kingdom_hall_attendant_binaries_

## Cómo contribuir

### 1. Reportar Problemas

Si encuentras un problema, por favor abre un issue en GitHub. Asegúrate de proporcionar la mayor cantidad de información posible para que podamos entender y reproducir el problema.

### 2. Solicitudes de extracción (Pull Requests)

Para realizar cambios en el código, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y añade comentarios descriptivos.
4. Asegúrate de que los tests pasen (`python -m unittest discover`).
5. Realiza un commit de tus cambios (`git commit -am 'Añadir nueva funcionalidad'`).
6. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
7. Abre una solicitud de extracción (pull request) desde tu rama al repositorio principal.

### 3. Donaciones

Puedes apoyar el proyecto monetariamente a través de [OpenCollective](https://opencollective.com/kingdom-hall-attendant/).

### 4. Desktop Client

Si deseas contribuir al cliente de escritorio hecho en Electron, sigue el mismo proceso de pull requests descrito anteriormente pero en este repositorio: https://github.com/livrasand/kingdom_hall_attendant_binaries.

## Etiquetas para Issues

Para organizar y priorizar los issues, utilizamos las siguientes etiquetas:

- **Tipo de tarea**:
  - `backend`: Relacionado con el backend.
  - `bug`: Something isn't working.
  - `database`: Relacionado con la base de datos.
  - `documentation`: Improvements or additions to documentation.
  - `enhancement`: New feature or request.
  - `feature`: Nueva funcionalidad.
  - `frontend`: Relacionado con el frontend.
  - `integration`: Integración con otras aplicaciones.
  - `new translation`: Incidents related to the creation of new translations.
  - `refactor`: Mejoras de código sin cambiar la funcionalidad.
  - `test`: Relacionado con pruebas y cobertura de tests.
  - `translations`: Identify incidents related to the translation of text or code.
  - `ui/ux`: Relacionado con la interfaz de usuario y la experiencia de usuario.

- **Prioridad**:
  - `priority: high`: Alta prioridad.
  - `priority: medium`: Prioridad media.
  - `priority: low`: Baja prioridad.

- **Dificultad**:
  - `difficulty: easy`: Fácil.
  - `difficulty: medium`: Media.
  - `difficulty: hard`: Difícil.

- **Estado**:
  - `blocked`: Bloqueado por algún motivo.
  - `completed`: Completado.
  - `in progress`: En progreso.
  - `review needed`: Necesita revisión.
  - `solved`: The problem has been resolved.

- **Colaboración**:
  - `good first issue`: Good for newcomers.
  - `help wanted`: Extra attention is needed.

- **Otros**:
  - `dependencies`: Pull requests that update a dependency file.
  - `duplicate`: This issue or pull request already exists.
  - `ignore top-ranking issues`: [ignored label].
  - `invalid`: This doesn't seem right.
  - `platform support`: Una etiqueta paraguas para todas las plataformas.
  - `question`: Further information is requested.
  - `wontfix`: No se solucionará.

## Contacto

Si tienes alguna pregunta o necesitas más información, no dudes en abrir un issue con la etiqueta `question` o contactar conmigo directamente en **livrasand@outlook.com**.

¡Gracias por tu colaboración!

## Uso de ChatGPT para nuevos programadores

Si estás comenzando en la programación y deseas practicar con Kingdom Hall Attendant, te recomendamos utilizar ChatGPT como una herramienta de apoyo. ChatGPT puede ayudarte a entender conceptos básicos, resolver problemas y proporcionarte ejemplos de código. Aquí te damos algunas recomendaciones para que saques el máximo provecho:

### Recomendaciones de uso

1. **Aprender conceptos básicos**: Usa ChatGPT para obtener explicaciones sobre conceptos básicos de Python, Flask y otras tecnologías utilizadas en el proyecto.
2. **Resolver problemas comunes**: Pregunta a ChatGPT sobre errores comunes y cómo resolverlos. Esto puede ayudarte a avanzar más rápido en tu aprendizaje.
3. **Ejemplos de código**: Solicita ejemplos de código para entender cómo se implementan ciertas funcionalidades. Esto puede ser útil para ver cómo se estructuran los proyectos en Python y Flask.

### Consejos para usar ChatGPT con precaución

- **Verifica la información**: Aunque ChatGPT puede proporcionar información valiosa, siempre es importante verificar las respuestas y buscar fuentes adicionales cuando sea necesario.
- **Prueba y experimenta**: No te limites a copiar y pegar el código. Prueba el código, experimenta con él y entiende cómo funciona.
- **Consulta documentación oficial**: Utiliza la documentación oficial de las tecnologías que estás aprendiendo para obtener información precisa y detallada.
- **Participa en la comunidad**: No dudes en unirte a foros y comunidades de desarrolladores donde puedes hacer preguntas y obtener consejos de programadores más experimentados.

Al utilizar ChatGPT de manera informada, puedes mejorar tus habilidades de programación y contribuir de manera más efectiva al proyecto Kingdom Hall Attendant. ¡Buena código y feliz codificación!

