# Guía de Hacking para Kingdom Hall Attendant

## Configuración del entorno de desarrollo

Para comenzar con el desarrollo y pruebas de seguridad de Kingdom Hall Attendant, sigue estos pasos:

1. **Clonar el repositorio:**
   ```sh
   git clone https://github.com/livrasand/Kingdom-Hall-Attendant
   cd Kingdom-Hall-Attendant
   ```
2. **Instalar dependencias:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Iniciar la aplicación localmente:**
   ```sh
   python app.py
   ```
4. **Configurar entorno de pruebas:** Puedes crear cuentas de prueba y modificar datos localmente sin afectar la versión en producción.

## Pruebas de seguridad permitidas

Siguiendo el **[Contrato Permisivo para Hackers](https://www.getkha.org/terms)**, puedes realizar las siguientes pruebas:

### 1. Exploración de vulnerabilidades
- **Inyecciones SQL**: Verifica si los formularios y consultas pueden ser explotadas mediante inyecciones SQL.
- **XSS (Cross-Site Scripting)**: Intenta inyectar scripts maliciosos en los campos de entrada.
- **CSRF (Cross-Site Request Forgery)**: Prueba si es posible realizar peticiones no autorizadas en nombre de otro usuario.

### 2. Revisión de código
- Inspecciona el código fuente en busca de vulnerabilidades comunes.
- Analiza la implementación de la autenticación y cifrado de datos.

### 3. Pruebas de autenticación
- Evalúa la seguridad del inicio de sesión y el almacenamiento de contraseñas.
- Prueba mecanismos de recuperación de cuenta para detectar posibles debilidades.

### 4. Análisis de configuración de seguridad
- Verifica que no haya claves API o credenciales expuestas en el repositorio.
- Asegúrate de que las cookies y tokens estén protegidos contra secuestros.

## Pruebas avanzadas

### 1. Pruebas de rendimiento
- Modifica los tiempos de polling en el código para optimizar el rendimiento:
  ```java
  long POLLING_INTERVAL_MS = SECONDS.toMillis(10);
  ```

### 2. Simulación de ataques en entorno local
- Usa herramientas como **Burp Suite** o **OWASP ZAP** para interceptar y modificar peticiones.
- Emplea **sqlmap** para detectar inyecciones SQL en las consultas.

## Acciones NO permitidas

- **No realizar ataques de denegación de servicio (DoS) al sitio web real `www.getkha.org`.**
- **No intentar acceder a cuentas ajenas o datos sensibles.**
- **No modificar el sistema en producción.**
- **No usar malware o exploits en la versión en línea.**

## Reporte de vulnerabilidades

Si encuentras una vulnerabilidad, repórtala siguiendo las medidas de [SECURITY.md](https://github.com/livrasand/Kingdom-Hall-Attendant/blob/main/SECURITY.md)

