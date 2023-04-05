

# Bienvenido a la Guía de contribución de Kingdom Hall Attendant

¡Gracias por invertir su tiempo en contribuir con nuestro proyecto! Cualquier contribución que haga se reflejará en [docs.goattendant.com](https://docs.goattendant.com) :sparkles:.

Lea nuestro [Código de conducta](./CODE_OF_CONDUCT.md) para mantener nuestra comunidad accesible y respetable.

En esta guía, obtendrá una descripción general del flujo de trabajo de contribución desde la apertura de un problema, la creación de un RP, la revisión y la fusión del RP.

Use el ícono de la tabla de contenido en la esquina superior izquierda de este documento para acceder rápidamente a una sección específica de esta guía.

## Empezando

Verifique qué tipos de contribuciones aceptamos antes de realizar cambios. Algunos de ellos ni siquiera requieren escribir una sola línea de código :sparkles:.

### Asuntos

#### Crear un nuevo problema

Si detecta un problema con los documentos, busque si ya existe un problema. Si no existe un problema relacionado, puede abrir un nuevo problema utilizando un [formulario de problema] relevante (https://github.com/github/docs/issues/new/choose).

#### Resolver un problema

Explore nuestros problemas existentes para encontrar uno que le interese. Puede restringir la búsqueda utilizando "etiquetas" como filtros.

### Hacer cambios

#### Hacer cambios en la interfaz de usuario

Haz clic en **Hacer una contribución** en la parte inferior de cualquier página de documentos para hacer pequeños cambios, como un error tipográfico, corregir una oración o un enlace roto. Esto lo lleva al archivo `.md` donde puede realizar sus cambios y [crear una solicitud de extracción](#pull-request) para una revisión.

 

#### Hacer cambios en un espacio de código

Para obtener más información sobre el uso de un espacio de código para trabajar en la documentación de GitHub, consulte "[Trabajar en un espacio de código](https://github.com/github/docs/blob/main/contributing/codespace.md)".

#### Hacer cambios localmente

1. Bifurcar el repositorio.
- Usando el escritorio de GitHub:
  - [Primeros pasos con GitHub Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/getting-started-with-github-desktop) lo guiará a través de la configuración de Desktop .
  - Una vez que Desktop está configurado, puede usarlo para [bifurcar el repositorio] (https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/cloning-and-forking- repositorios-desde-github-desktop)!

- Usando la línea de comando:
  - [Fork the repo](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository) para que pueda realizar sus cambios sin afectar el proyecto original hasta que esté listo para fusionarlos.

2. Instale o actualice a **Node.js**, en la versión especificada en `.node-version`. Para obtener más información, consulte [la guía de desarrollo](contributing/development.md).

3. ¡Cree una rama de trabajo y comience con sus cambios!

### Confirma tu actualización

Confirme los cambios una vez que esté satisfecho con ellos. No olvide auto-revisar para acelerar el proceso de revisión:zap:.

### Solicitud de extracción

Cuando haya terminado con los cambios, cree una solicitud de incorporación de cambios, también conocida como PR.
- Complete la plantilla "Listo para revisión" para que podamos revisar su PR. Esta plantilla ayuda a los revisores a comprender sus cambios, así como el propósito de su solicitud de extracción.
- No se olvide de [vincular PR al problema](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue ) si está resolviendo uno.
- Active la casilla de verificación para [permitir ediciones del mantenedor](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/allowing-changes-to-a-pull-request-branch -created-from-a-fork) para que la rama se pueda actualizar para una fusión.
Una vez que envíe su PR, un miembro del equipo de Docs revisará su propuesta. Podemos hacer preguntas o solicitar información adicional.
- Es posible que solicitemos que se realicen cambios antes de que se pueda fusionar un RP, ya sea mediante [cambios sugeridos](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/incorporating -feedback-in-your-pull-request) o comentarios de solicitud de extracción. Puede aplicar los cambios sugeridos directamente a través de la interfaz de usuario. Puede realizar cualquier otro cambio en su bifurcación y luego confirmarlo en su rama.
- A medida que actualice su PR y aplique los cambios, marque cada conversación como [resuelta](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a- pull-request#resolving-conversations).
- Si se encuentra con algún problema de combinación, consulte este [tutorial de git] (https://github.com/skills/resolve-merge-conflicts) para ayudarlo a resolver conflictos de combinación y otros problemas.

### ¡Su PR está fusionado!

Felicidades :tada::tada: El equipo de GoAttendant te agradece :sparkles:.

Una vez que se fusione su RP, sus contribuciones serán visibles públicamente en los documentos de Kingdom Hall Attendant (https://docs.goattendant.com).
