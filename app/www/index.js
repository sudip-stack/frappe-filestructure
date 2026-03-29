// Page-specific JavaScript for homepage
console.log('🏠 Homepage loaded');
document.addEventListener('DOMContentLoaded', function() {
    console.log('Page view tracked:', window.location.pathname);
    window.addEventListener('load', function() {
        const loadTime = performance.now().toFixed(2);
        console.log(`⚡ Page loaded in ${loadTime}ms`);
    });
});
