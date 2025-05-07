document.addEventListener('DOMContentLoaded', function() {
    // Initialize animated background elements
    initAnimatedBackground();
    
    // Add smooth scrolling to form sections
    document.querySelectorAll('.form-section h2').forEach(heading => {
        heading.addEventListener('click', function() {
            const section = this.parentElement;
            section.classList.toggle('expanded');
        });
    });
    
    // Print result functionality
    const printButton = document.getElementById('printResult');
    if (printButton) {
        printButton.addEventListener('click', function(e) {
            e.preventDefault();
            window.print();
        });
    }
    
    // Form validation
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const allSelects = form.querySelectorAll('select');
            let isValid = true;
            
            allSelects.forEach(select => {
                if (!select.value) {
                    isValid = false;
                    select.classList.add('error');
                } else {
                    select.classList.remove('error');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showToast('Please answer all questions');
            }
        });
    }
});

// Function to create more animated boxes for background
function initAnimatedBackground() {
    const background = document.querySelector('.animated-background');
    if (!background) return;
    
    // Add more animated elements dynamically
    for (let i = 0; i < 5; i++) {
        const box = document.createElement('div');
        box.className = 'animated-box dynamic';
        
        // Random positioning and sizing
        const size = Math.random() * 100 + 50;
        const top = Math.random() * 100;
        const left = Math.random() * 100;
        const delay = Math.random() * 10;
        const duration = Math.random() * 10 + 10;
        
        box.style.width = `${size}px`;
        box.style.height = `${size}px`;
        box.style.top = `${top}%`;
        box.style.left = `${left}%`;
        box.style.animationDelay = `${delay}s`;
        box.style.animationDuration = `${duration}s`;
        
        background.appendChild(box);
    }
}

// Toast notification function
function showToast(message) {
    // Check if toast container exists, create if not
    let toastContainer = document.querySelector('.toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.className = 'toast-container';
        document.body.appendChild(toastContainer);
    }
    
    // Create toast element
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    
    // Add to container
    toastContainer.appendChild(toast);
    
    // Animation
    setTimeout(() => {
        toast.classList.add('show');
    }, 10);
    
    // Remove after 3 seconds
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => {
            toastContainer.removeChild(toast);
        }, 300);
    }, 3000);
}