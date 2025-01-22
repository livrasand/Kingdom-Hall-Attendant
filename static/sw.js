// static/sw.js

const CACHE_NAME = 'mi-cache-v1';
const urlsToCache = [
    '/',
    '/static/styles.css',
    '/static/primer.css',
    '/static/style.css',
    '/static/en-línea-1.css',
    '/static/jw-icons.css',
    '/static/favicon.ico',
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