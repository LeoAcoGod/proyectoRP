
const staticAssets = [
    '/',
    '/home.html',
    '/static/home.css',
    '/static/chatbot.css',
    '/static/login.css',
    
  ];
  
  self.addEventListener('install', async event => {
    const cache = await caches.open('staticAssets');
    await cache.addAll(staticAssets);
    console.log('service worker installed');
  });
  
  self.addEventListener('fetch', async event => {
    const request = event.request;
    const url = new URL(request.url);
  
    if (url.origin === location.origin) {
      event.respondWith(
        caches.match(request).then(cachedResponse=> {
          if (cachedResponse) {
            return cachedResponse;
          }
  
          return fetch(request).then(response => {
            const cache = caches.open('staticAssets');
            cache.put(request, response.clone());
            return response;
          });
        })
      );
    }
  });