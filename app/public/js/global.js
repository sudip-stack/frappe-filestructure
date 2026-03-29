// Global JavaScript - loaded on all pages
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 App initialized:', window.appConfig || {});
    
    const currentPath = window.location.pathname;
    document.querySelectorAll('nav a').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.style.background = 'rgba(255,255,255,0.2)';
        }
    });
});

window.App = {
    notify: function(message, type = 'info') {
        console.log(`[${type.toUpperCase()}] ${message}`);
    },
    formatDate: function(date) {
        return new Date(date).toLocaleDateString();
    },
    ajax: async function(url, method = 'GET', data = null) {
        const options = { method, headers: { 'Content-Type': 'application/json' } };
        if (data) options.body = JSON.stringify(data);
        return fetch(url, options).then(res => res.json());
    }
};
