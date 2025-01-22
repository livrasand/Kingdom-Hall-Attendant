# Guía de contribución

¡Gracias por tu interés en contribuir a Kingdom Hall Attendant! Nos alegra contar con tu apoyo. Aquí te proporcionamos algunas directrices para ayudarte a comenzar.

## Índice
1. [Tecnologías utilizadas](#1-tecnologías-utilizadas)
2. [Cómo contribuir](#2-cómo-contribuir)
   - [Reportar Problemas](#21-reportar-problemas)
   - [Solicitudes de extracción (Pull Requests)](#22-solicitudes-de-extracción-pull-requests)
   - [Donaciones](#23-donaciones)
   - [Contribuir a la traducción](#24-contribuir-a-la-traducción)
   - [Desktop Client](#25-desktop-client)
3. [Etiquetas para Issues](#3-etiquetas-para-issues)
4. [Contacto](#4-contacto)
5. [Uso de ChatGPT para nuevos programadores](#5-uso-de-chatgpt-para-nuevos-programadores)
   - [Recomendaciones de uso](#51-recomendaciones-de-uso)
   - [Consejos para usar ChatGPT con precaución](#52-consejos-para-usar-chatgpt-con-precaución)
6. [Bases de datos](#6-bases-de-datos)

## 1. Tecnologías utilizadas

- **Lenguajes y Frameworks**: Python, Flask, HTML, SQLite
- **Traducciones**: PyBabel
- **Hosting**: PythonAnywhere
- **Dominio**: GoDaddy
- **Financiamiento**: Solo aceptamos donaciones mediante [OpenCollective](https://opencollective.com/kingdom-hall-attendant/).
- **Desktop Client**: Electron (renderiza la URL pública getkha.org) _github.com/livrasand/kingdom_hall_attendant_binaries_

## 2. Cómo contribuir

### 2.1 Configuración del archivo .env

Para ejecutar localmente Kingdom Hall Attendant (KHA), es necesario configurar un archivo `.env`. Este archivo contiene variables de entorno que son esenciales para el funcionamiento de la aplicación. Puedes encontrar un ejemplo de este archivo llamado `.env-example` en el repositorio. A continuación, se detallan las variables que debes incluir y cómo obtener sus valores:

- **Secret keys**:
  - `JWT_SECRET_KEY`: Esta es la clave secreta utilizada para firmar los tokens JWT. 
  - `SECRET_KEY`: Esta clave se utiliza para proteger sesiones y datos sensibles. Al igual que con `JWT_SECRET_KEY`, asegúrate de que sea única y segura.

Puedes generar una clave segura y única utilizando el siguiente script de Python:

```python
import secrets

def generate_secret_key(length):
    """Genera una clave secreta aleatoria."""
    return secrets.token_hex(length)

def main():
    jwt_secret_key = generate_secret_key(64)  
    app_secret_key = generate_secret_key(48)  

    print(f"JWT_SECRET_KEY = '{jwt_secret_key}'")
    print(f"SECRET_KEY = '{app_secret_key}'")

if __name__ == "__main__":
    main()
```

Puedes usar este script para generar tus claves secretas.

- **Configuración de correo electrónico**:
  - `MAIL_USERNAME`: Tu dirección de correo electrónico que se utilizará para enviar correos desde la aplicación. Por ejemplo, `your_email@gmail.com`.
  - `MAIL_PASSWORD`: La contraseña de tu cuenta de correo electrónico. Si usas Gmail, es recomendable generar una contraseña de aplicación para mayor seguridad.
  - `MAIL_SERVER`: El servidor SMTP que utilizarás para enviar correos. Para Gmail, este valor es `smtp.gmail.com`.
  - `MAIL_PORT`: El puerto que se utilizará para la conexión SMTP. Para Gmail, el puerto por defecto es `587`, que se utiliza con TLS.
  - `MAIL_USE_TLS`: Debe establecerse en `True` para usar TLS, que es un protocolo de seguridad.
  - `MAIL_USE_SSL`: Debe establecerse en `False` si estás utilizando TLS. Si decides usar SSL en su lugar, cámbialo a `True`.

Si ejecutas KHA localmente, puedes omitir toda esta configuración de correo electrónico. En su lugar, puedes modificar el código para evitar llamar a los correos. Para crear tu cuenta, simplemente crea un nuevo Row en la base de datos `cavea`, y manualmente copia la base `kha.db`, cambiándole el nombre por el que tú elijas. Sin embargo, este nombre debe ser el mismo que el de la columna `database` en tu Row de `cavea` en la tabla `emptor`. 

Asegúrate de replicar estas configuraciones en tu archivo `.env` para que la aplicación funcione correctamente.

### 2.2 Reportar Problemas

Si encuentras un problema, por favor abre un issue en GitHub. Asegúrate de proporcionar la mayor cantidad de información posible para que podamos entender y reproducir el problema.

### 2.3 Solicitudes de extracción (Pull Requests)

Para realizar cambios en el código, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y añade comentarios descriptivos.
4. Asegúrate de que los tests pasen (`python -m unittest discover`).
5. Realiza un commit de tus cambios (`git commit -am 'Añadir nueva funcionalidad'`).
6. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
7. Abre una solicitud de extracción (pull request) desde tu rama al repositorio principal.

### 2.4 Donaciones

Puedes apoyar el proyecto monetariamente a través de [OpenCollective](https://opencollective.com/kingdom-hall-attendant/). Solo aceptamos donaciones mediante OpenCollective, por ningún otro medio.

### 2.5 Contribuir a la traducción

Si deseas contribuir a la traducción de la aplicación, puedes hacerlo a través de [Crowdin](https://crowdin.com/project/kingdom-hall-attendant).

### 2.6 Desktop Client

Si deseas contribuir al cliente de escritorio hecho en Electron, sigue el mismo proceso de pull requests descrito anteriormente pero en este repositorio: https://github.com/livrasand/kingdom_hall_attendant_binaries.

## 3. Etiquetas para Issues

Para organizar y priorizar los issues, utilizamos las siguientes etiquetas:

- **Tipo de tarea**:
  - `backend`: Relacionado con el backend.
  - `bug`: Algo no está funcionando.
  - `database`: Relacionado con la base de datos.
  - `documentation`: Mejoras o adiciones a la documentación.
  - `enhancement`: Nueva funcionalidad o solicitud.
  - `feature`: Nueva funcionalidad.
  - `frontend`: Relacionado con el frontend.
  - `integration`: Integración con otras aplicaciones.
  - `new translation`: Incidentes relacionados con la creación de nuevas traducciones.
  - `refactor`: Mejoras de código sin cambiar la funcionalidad.
  - `test`: Relacionado con pruebas y cobertura de tests.
  - `translations`: Identificar incidentes relacionados con la traducción de texto o código.
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
  - `solved`: El problema ha sido resuelto.

- **Colaboración**:
  - `good first issue`: Bueno para principiantes.
  - `help wanted`: Se necesita atención extra.

- **Otros**:
  - `dependencies`: Pull requests que actualizan un archivo de dependencia.
  - `duplicate`: Este issue o pull request ya existe.
  - `ignore top-ranking issues`: [etiqueta ignorada].
  - `invalid`: Esto no parece correcto.
  - `platform support`: Una etiqueta paraguas para todas las plataformas.
  - `question`: Se solicita más información.
  - `wontfix`: No se solucionará.

## 4. Contacto

Si tienes alguna pregunta o necesitas más información, no dudes en abrir un issue con la etiqueta `question` o contactar conmigo directamente en **livrasand@outlook.com**.

¡Gracias por tu colaboración!

## 5. Uso de ChatGPT para nuevos programadores

Si estás comenzando en la programación y deseas practicar con Kingdom Hall Attendant, te recomendamos utilizar ChatGPT como una herramienta de apoyo. ChatGPT puede ayudarte a entender conceptos básicos, resolver problemas y proporcionarte ejemplos de código. Aquí te damos algunas recomendaciones para que saques el máximo provecho:

### 5.1 Recomendaciones de uso

1. **Aprender conceptos básicos**: Usa ChatGPT para obtener explicaciones sobre conceptos básicos de Python, Flask y otras tecnologías utilizadas en el proyecto.
2. **Resolver problemas comunes**: Pregunta a ChatGPT sobre errores comunes y cómo resolverlos. Esto puede ayudarte a avanzar más rápido en tu aprendizaje.
3. **Ejemplos de código**: Solicita ejemplos de código para entender cómo se implementan ciertas funcionalidades. Esto puede ser útil para ver cómo se estructuran los proyectos en Python y Flask.

### 5.2 Consejos para usar ChatGPT con precaución

- **Verifica la información**: Aunque ChatGPT puede proporcionar información valiosa, siempre es importante verificar las respuestas y buscar fuentes adicionales cuando sea necesario.
- **Prueba y experimenta**: No te limites a copiar y pegar el código. Prueba el código, experimenta con él y entiende cómo funciona.
- **Consulta documentación oficial**: Utiliza la documentación oficial de las tecnologías que estás aprendiendo para obtener información precisa y detallada.
- **Participa en la comunidad**: No dudes en unirte a foros y comunidades de desarrolladores donde puedes hacer preguntas y obtener consejos de programadores más experimentados.

Al utilizar ChatGPT de manera informada, puedes mejorar tus habilidades de programación y contribuir de manera más efectiva al proyecto Kingdom Hall Attendant. 

## 6. Bases de datos

Para arrancar localmente, es correcto que haya dos bases de datos: `cavea.db` y `kha.db`. Sin embargo, solo se usa una de ellas, pero ambas están presentes. Esto podría ser confuso para algunos. La base de datos `cavea` es la base de datos principal de **Kingdom Hall Attendant**, donde se registran los usuarios, las contraseñas, los identicons y todo lo relacionado con la aplicación y los usuarios. La base de datos `kha` es solo para copiar y crear la base de datos del usuario final, donde el usuario guardará sus datos de la aplicación.

¡Buena código y feliz codificación!
