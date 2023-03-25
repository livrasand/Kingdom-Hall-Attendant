# Instalar dependencias:

npm install

# KHA Alpha:

npm run dev

# Posibles errores detectados:

### npm WARN config global `--global`, `--local` are deprecated. Use `--location=global` instead.

i.   Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
ii.  npm install --global --production npm-windows-upgrade
iii. npm-windows-upgrade --npm-version latest

`<strong>`Recuerde volver a la política inicial:`</strong>`
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

### electron-builder

```bash
# gerar um .exe ('electron-builder --win')
yarn win;
npm run win;
```
