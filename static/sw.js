const CACHE_NAME = 'kingdom-hall-attendant-cache-v1';
const urlsToCache = [
  '/',
  '/welcome.html',
  '/static/styles.css',
  '/static/style.css',
  '/static/primer.css',
  '/static/print-styles.css',
  '/static/loading-splash.css',
  '/static/sw.js',
  '/static/manifest.json',
  '/static/favicon.png',
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
  );
});
