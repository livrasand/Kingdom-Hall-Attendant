import { sveltekit } from "@sveltejs/kit/vite";

/** @type {import('vite').UserConfig} */
const config = {
    plugins: [sveltekit()],

    server: {
        port: 3000
    },

    build: {
        cssCodeSplit: true, // Para dividir el CSS en archivos separados
        sourcemap: true,    // Para generar mapas de origen
    },
};

export default config;
