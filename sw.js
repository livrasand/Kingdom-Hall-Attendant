const CACHE_NAME = 'kha-v0.26.0';
const urlsToCache = [
  '/',
  '/home',
  '/index.html',
  '/static/images/313010479-cfab1393-8ae1-4b3f-9895-7022272f1262.jpeg',
  '/pwa.html',
  '/login-mobile-client.html',
  '/login-desktop-client',
  '/congregacion.html',
  '/publicadores.html',
  '/vida-ministerio.html',
  '/estudio-atalaya.html',
  '/oradores.html',
  '/bosquejos.html',
  '/grupos-predicacion.html',
  '/informes-predicacion',
  '/audio-video-acomodadores',
  '/predicacion-publica',
  '/servicio-campo',
  '/territorios',
  '/visita-superint-circuito.html',
  '/literatura',
  '/asistencia-reuniones',
  '/copias-seguridad',
  '/configuracion.html',
  '/static/styles.css',
  '/static/primer.css',
  '/static/style.css',
  '/static/en-línea-1.css',
  '/static/jw-icons.css',
  '/static/icons/icon-256x256.png',
  '/static/icons/icon-512x512.png'
];

// Instalación del Service Worker
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                return cache.addAll(urlsToCache);
            })
    );
});

// Manejo de las solicitudes de red
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
    );
});

self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cache => {
                    if (cache !== CACHE_NAME) {
                        return caches.delete(cache); // Elimina cachés antiguas
                    }
                })
            );
        }).then(() => self.clients.claim()) // Toma el control de las pestañas abiertas
    );
});

// Escucha mensajes para activar la nueva versión
self.addEventListener('message', event => {
    if (event.data === 'skipWaiting') {
        self.skipWaiting(); // Activa la nueva versión inmediatamente
    }
});