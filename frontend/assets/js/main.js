// Main JavaScript for DermaAI

document.addEventListener("DOMContentLoaded", function () {
    initTheme();
    initMobileMenu();
    loadRecentScans();
    setupFormListeners();
});

// --- Dark Mode Logic ---
function initTheme() {
    const toggleBtn = document.getElementById('theme-toggle');
    if (!toggleBtn) return; // Guard clause if button not present

    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    updateToggleIcon(currentTheme);

    toggleBtn.addEventListener('click', () => {
        let theme = document.documentElement.getAttribute('data-theme');
        let newTheme = theme === 'light' ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateToggleIcon(newTheme);
    });
}

function updateToggleIcon(theme) {
    const toggleBtn = document.getElementById('theme-toggle');
    if (toggleBtn) {
        toggleBtn.innerHTML = theme === 'light'
            ? '<i class="fas fa-moon"></i>'
            : '<i class="fas fa-sun"></i>';
    }
}

// --- Mobile Menu ---
function initMobileMenu() {
    const menu = document.querySelector('#menu-bar');
    const nav = document.querySelector('.nav');

    if (menu && nav) {
        menu.addEventListener('click', () => {
            menu.classList.toggle('fa-times');
            nav.classList.toggle('active');
        });

        // Close menu when clicking a link
        nav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                menu.classList.remove('fa-times');
                nav.classList.remove('active');
            });
        });
    }
}

// --- Recent Scans (LocalStorage) ---
function savePrediction(result, severity) {
    const scan = {
        id: Date.now(),
        result: result,
        severity: severity || '',
        date: new Date().toLocaleDateString(),
    };

    let scans = JSON.parse(localStorage.getItem('recentScans') || '[]');
    scans.unshift(scan);
    if (scans.length > 5) scans.pop(); // Keep last 5
    localStorage.setItem('recentScans', JSON.stringify(scans));
}

function loadRecentScans() {
    const container = document.getElementById('recent-scans-list');
    if (!container) return;

    const scans = JSON.parse(localStorage.getItem('recentScans') || '[]');

    if (scans.length === 0) {
        container.innerHTML = '<p class="text-muted small">No recent scans yet. Upload an image to get started.</p>';
        return;
    }

    const severityClass = (s) => {
        if (!s) return 'mild';
        const sl = s.toLowerCase();
        if (sl === 'severe') return 'severe';
        if (sl === 'moderate') return 'moderate';
        return 'mild';
    };

    container.innerHTML = scans.map(scan => `
        <div class="scan-item d-flex justify-content-between align-items-center">
            <div class="d-flex align-items-center gap-2">
                <span class="fw-bold" style="color:var(--primary-color);">${scan.result}</span>
                ${scan.severity ? `<span class="severity-chip severity-${severityClass(scan.severity)}" style="font-size:0.78rem;padding:3px 12px;">${scan.severity}</span>` : ''}
            </div>
            <span class="small text-muted">${scan.date}</span>
        </div>
    `).join('');
}

// --- Loading State and Form Handling ---
function setupFormListeners() {
    const forms = document.querySelectorAll('form');
    const loadingOverlay = document.getElementById('loading-overlay');

    forms.forEach(form => {
        form.addEventListener('submit', function () {
            if (loadingOverlay) {
                loadingOverlay.style.display = 'flex';
            }
        });
    });
}


// --- Camera Logic (Existing but cleaned up) ---
let stream;

function startCamera() {
    const video = document.getElementById('video');
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(s => {
                stream = s;
                video.srcObject = stream;
            })
            .catch(err => {
                console.error("Error accessing camera: ", err);
                alert("Unable to access camera. Please allow permissions.");
            });
    }
}

function stopCamera() {
    const video = document.getElementById('video');
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
        video.srcObject = null;
    }
}

function captureAndAssign() {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    if (!video || !canvas) return;

    const ctx = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    canvas.toBlob(function (blob) {
        const file = new File([blob], "captured_image.png", { type: "image/png" });
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);

        const input = document.getElementById('real-file');
        if (input) {
            input.files = dataTransfer.files;
            input.dispatchEvent(new Event('change')); // Trigger change event
        }

        const fileNameSpan = document.getElementById('file-name');
        if (fileNameSpan) fileNameSpan.textContent = file.name;

        // Hide modal using Bootstrap API if available, else fallback
        const modalEl = document.getElementById('cameraModal');
        if (modalEl) {
            const modal = bootstrap.Modal.getInstance(modalEl);
            if (modal) modal.hide();
        }

        stopCamera();
    }, 'image/png');
}

// Global scope binding for inline onclicks (legacy support)
window.startCamera = startCamera;
window.stopCamera = stopCamera;
window.captureAndAssign = captureAndAssign;




