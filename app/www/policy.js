// Bundle JS for /policy page

console.log('📋 Privacy Policy bundle loaded');

document.addEventListener('DOMContentLoaded', () => {
    // Smooth scroll for TOC links
    document.querySelectorAll('.toc a').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const target = document.getElementById(targetId);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                // Update URL without scroll jump
                history.pushState(null, null, `#${targetId}`);
            }
        });
    });

    // Highlight active section on scroll
    const sections = document.querySelectorAll('.section');
    const tocLinks = document.querySelectorAll('.toc a');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                tocLinks.forEach(link => {
                    link.style.color = '';
                    link.style.fontWeight = '';
                    if (link.getAttribute('href') === `#${entry.target.id}`) {
                        link.style.color = '#1d4ed8';
                        link.style.fontWeight = 'bold';
                    }
                });
            }
        });
    }, { threshold: 0.3, rootMargin: '-100px 0px -50% 0px' });

    sections.forEach(section => observer.observe(section));

    // Policy acknowledgment tracking
    const acknowledgeBtn = document.getElementById('policy-acknowledge');
    const confirmedMsg = document.getElementById('policy-confirmed');
    
    if (acknowledgeBtn && confirmedMsg) {
        // Check localStorage
        const acknowledged = localStorage.getItem('policyAcknowledged');
        const ackDate = localStorage.getItem('policyAcknowledgedDate');
        
        if (acknowledged === 'true' && ackDate) {
            acknowledgeBtn.style.display = 'none';
            confirmedMsg.style.display = 'block';
            confirmedMsg.textContent = `✓ Acknowledged on ${new Date(ackDate).toLocaleDateString()}`;
        }
        
        acknowledgeBtn.addEventListener('click', function() {
            const now = new Date().toISOString();
            localStorage.setItem('policyAcknowledged', 'true');
            localStorage.setItem('policyAcknowledgedDate', now);
            
            this.style.display = 'none';
            confirmedMsg.style.display = 'block';
            confirmedMsg.textContent = '✓ Thank you for acknowledging!';
            
            // Optional: Send acknowledgment to server
            // App.ajax('/api/policy-acknowledge', 'POST', { acknowledged: true });
            
            console.log('✅ Policy acknowledged at', now);
        });
    }

    // Add reading progress indicator
    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        height: 4px;
        background: linear-gradient(90deg, #2563eb, #764ba2);
        z-index: 9999;
        transition: width 0.1s;
    `;
    document.body.insertBefore(progressBar, document.body.firstChild);
    
    window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = (scrollTop / docHeight) * 100;
        progressBar.style.width = `${progress}%`;
    });

    // Print button (optional)
    const printBtn = document.createElement('button');
    printBtn.textContent = '🖨️ Print Policy';
    printBtn.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: #2563eb;
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 4px;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        z-index: 1000;
    `;
    printBtn.addEventListener('click', () => window.print());
    document.body.appendChild(printBtn);

    // Hide print button when printing
    const style = document.createElement('style');
    style.textContent = '@media print { .print-btn { display: none; } }';
    document.head.appendChild(style);
});

// Track policy view analytics (optional)
window.addEventListener('load', () => {
    console.log('📊 Policy page viewed:', {
        path: window.location.pathname,
        timestamp: new Date().toISOString(),
        referrer: document.referrer || 'direct'
    });
});