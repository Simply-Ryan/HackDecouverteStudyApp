// Service Worker for StudyFlow Push Notifications
// Version 1.0.0

const CACHE_NAME = 'studyflow-v1';
const urlsToCache = [
    '/',
    '/static/css/style.css',
    '/static/js/main.js'
];

// Install service worker and cache resources
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
});

// Fetch cached resources when offline
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                // Return cached version or fetch from network
                return response || fetch(event.request);
            })
    );
});

// Handle push notifications
self.addEventListener('push', event => {
    console.log('Push notification received:', event);
    
    let data = {};
    if (event.data) {
        try {
            data = event.data.json();
        } catch (e) {
            data = {
                title: 'StudyFlow Notification',
                body: event.data.text(),
                icon: '/static/images/logo.png',
                badge: '/static/images/badge.png'
            };
        }
    }
    
    const title = data.title || 'StudyFlow';
    const options = {
        body: data.body || 'You have a new notification',
        icon: data.icon || '/static/images/logo.png',
        badge: data.badge || '/static/images/badge.png',
        vibrate: [200, 100, 200],
        tag: data.tag || 'studyflow-notification',
        requireInteraction: data.requireInteraction || false,
        data: {
            url: data.url || '/',
            notificationId: data.notificationId
        },
        actions: data.actions || [
            {
                action: 'open',
                title: 'View',
                icon: '/static/images/view-icon.png'
            },
            {
                action: 'close',
                title: 'Dismiss',
                icon: '/static/images/close-icon.png'
            }
        ]
    };
    
    event.waitUntil(
        self.registration.showNotification(title, options)
    );
});

// Handle notification clicks
self.addEventListener('notificationclick', event => {
    console.log('Notification clicked:', event);
    
    event.notification.close();
    
    if (event.action === 'close') {
        // User dismissed notification
        return;
    }
    
    // Get the URL from notification data
    const urlToOpen = event.notification.data.url || '/';
    
    event.waitUntil(
        clients.matchAll({
            type: 'window',
            includeUncontrolled: true
        }).then(clientList => {
            // Check if there's already a window open
            for (let client of clientList) {
                if (client.url === urlToOpen && 'focus' in client) {
                    return client.focus();
                }
            }
            // Open new window if none found
            if (clients.openWindow) {
                return clients.openWindow(urlToOpen);
            }
        })
    );
});

// Handle notification close
self.addEventListener('notificationclose', event => {
    console.log('Notification closed:', event);
    
    // Track notification dismissal if needed
    const notificationId = event.notification.data.notificationId;
    if (notificationId) {
        // Could send to analytics or mark as read
        fetch('/api/notifications/' + notificationId + '/dismiss', {
            method: 'POST'
        });
    }
});

// Clean up old caches on activation
self.addEventListener('activate', event => {
    const cacheWhitelist = [CACHE_NAME];
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (!cacheWhitelist.includes(cacheName)) {
                        console.log('Deleting old cache:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});
