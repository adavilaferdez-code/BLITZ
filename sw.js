// BLIZT PRO - SMART NETWORK-FIRST SERVICE WORKER
const CACHE_VERSION = 'blizt-pro-v2026-10-03-auto';

// Install: Activate immediately
self.addEventListener('install', (event) => {
    self.skipWaiting();
});

// Activate: Clean up any old caches and claim all clients immediately
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keys) => {
            return Promise.all(
                keys.map((key) => {
                    if (key !== CACHE_VERSION) {
                        return caches.delete(key);
                    }
                })
            );
        }).then(() => self.clients.claim())
    );
});

// Fetch: Network First for all HTML and data to ensure GitHub updates are instant
self.addEventListener('fetch', (event) => {
    if (event.request.method !== 'GET') return;

    // For HTML navigation, always fetch freshest from GitHub / server
    if (event.request.mode === 'navigate' || event.request.destination === 'document' || event.request.url.includes('.html')) {
        event.respondWith(
            fetch(event.request)
                .then((networkResponse) => {
                    if (networkResponse && networkResponse.status === 200) {
                        const clone = networkResponse.clone();
                        caches.open(CACHE_VERSION).then((cache) => cache.put(event.request, clone));
                    }
                    return networkResponse;
                })
                .catch(() => caches.match(event.request))
        );
        return;
    }

    // For other assets, try network first, fallback to cache
    event.respondWith(
        fetch(event.request)
            .then((networkResponse) => {
                if (networkResponse && networkResponse.status === 200) {
                    const clone = networkResponse.clone();
                    caches.open(CACHE_VERSION).then((cache) => cache.put(event.request, clone));
                }
                return networkResponse;
            })
            .catch(() => caches.match(event.request))
    );
});
