# Cómo usar Pybabel para gestionar traducciones de Kingdom Hall Attendant

Este documento proporciona instrucciones detalladas sobre cómo usar Pybabel para gestionar las traducciones en Kingdom Hall Attendant.

## Prerrequisitos

1. Asegúrate de tener Python instalado en tu sistema.
2. Instala Babel usando pip:
    ```sh
    pip install babel
    ```

## Configurar Pybabel

### 1. Crear el archivo de configuración `babel.cfg`

Crea un archivo llamado `babel.cfg` en la raíz de tu proyecto. Este archivo le dirá a Babel dónde buscar cadenas traducibles.

Ejemplo de `babel.cfg`:
```ini
[python: **.py]
[jinja2: templates/**.html]

```

### 2. Extraer cadenas traducibles
Ejecuta el siguiente comando para extraer las cadenas traducibles de tu código y plantillas:

```sh
pybabel extract -F babel.cfg -o messages.pot .
```

Este comando generará un archivo `messages.pot` que contiene todas las cadenas traducibles encontradas en tu proyecto.

### 3. Inicializar un archivo de mensajes para un idioma específico

Para crear un archivo `messages.po` para un idioma específico (por ejemplo, español), utiliza el siguiente comando:

```sh
pybabel init -i messages.pot -d locales -l es
```

Este comando crea el archivo `messages.po` en el directorio `locales/es/LC_MESSAGES`.

### 4. Traducir las cadenas

Abre el archivo `messages.po` en un editor de texto, Poedit, o visita nuestro servidor en Crowdin y traduce las cadenas necesarias.

### 5. Compilar las traducciones

Una vez que hayas traducido todas las cadenas, compila los archivos de mensajes `.po` en archivos binarios `.mo` que tu aplicación puede usar:

```sh
pybabel compile -d locales
```