# SvelteKit + Electron

<p align="center">
  <img src="https://goattendant.com/GoAttendantLogo.png" width="256">
</p>
<p align="center">
  Una aplicación multiplataforma desarrollada especialmente para ancianos, siervos ministeriales y superintendentes de circuito, para elaborar y mantener muchas de las asignaciones para la congregación.
</p>


## Commands
- `npm run dev`: Runs SvelteKit in dev mode
- `npm run preview`: Runs SvelteKit in production mode
- `npm run electron`: Runs SvelteKit with electron in dev mode
- `npm run build`: Runs SvelteKit compiler
- `npm run dev:package`: Creates an Electron package (you can inspect the contents)
- `npm run package`: Creates a distributable Electron package

## Bootstrap 5 and FontAwesome support

Download the template and install the dependencies:

```
npx degit Dax89/electron-sveltekit
npm install --save bootstrap@next @fortawesome/fontawesome-free
```

Add these lines in `src/app.scss`:

```
@import "bootstrap/scss/bootstrap";
@import "@fortawesome/fontawesome-free/css/all.min.css";
```
