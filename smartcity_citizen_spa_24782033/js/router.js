const routes = {
    '#login': `
        <div class="row justify-content-center mt-5">
            <div class="col-md-4 card shadow-sm border-0 p-4">
                <h4 class="text-center fw-bold mb-4">Login Warga</h4>
                <form id="loginForm">
                    <input type="text" id="loginUsername" class="form-control mb-3" placeholder="Username" required>
                    <input type="password" id="loginPassword" class="form-control mb-3" placeholder="Password" required>
                    <button type="submit" class="btn btn-primary w-100 fw-bold">Masuk</button>
                </form>
            </div>
        </div>
    `,
    '#dashboard': `
        <div class="row g-4">
            <aside class="col-12 col-lg-3">
                <div class="card border-0 p-3 shadow-sm sticky-top" style="top: 20px;">
                    <button class="btn btn-primary btn-lg w-100 fw-bold mb-3" onclick="openModalNewReport()">
                        <i class="bi bi-plus-circle-fill me-2"></i>Laporan Baru
                    </button>
                    <hr>
                    <h6 class="fw-bold mb-3 text-muted">Statistik Laporan Saya</h6>
                    
                    <div class="d-flex justify-content-between mb-2">
                        <span><i class="bi bi-file-earmark me-2"></i>Draft:</span> 
                        <span class="fw-bold text-secondary" id="statDraft">0</span>
                    </div>
                    <div class="d-flex justify-content-between mb-2">
                        <span><i class="bi bi-megaphone me-2"></i>Reported:</span> 
                        <span class="fw-bold text-info" id="statReported">0</span>
                    </div>
                    <div class="d-flex justify-content-between mb-2">
                        <span><i class="bi bi-patch-check me-2"></i>Verified:</span> 
                        <span class="fw-bold text-warning" id="statVerified">0</span>
                    </div>
                    <div class="d-flex justify-content-between mb-2">
                        <span><i class="bi bi-gear-wide-connected me-2"></i>In Progress:</span> 
                        <span class="fw-bold text-primary" id="statInProgress">0</span>
                    </div>
                    <div class="d-flex justify-content-between">
                        <span><i class="bi bi-check-circle me-2"></i>Resolved:</span> 
                        <span class="fw-bold text-success" id="statResolved">0</span>
                    </div>
                </div>
            </aside>
            
            <section class="col-12 col-lg-6">
                <ul class="nav nav-pills mb-4 nav-fill shadow-sm rounded bg-white p-2">
                    <li class="nav-item">
                        <button class="nav-link active" id="tabMyReports" onclick="switchTab('my_reports')">Laporan Saya</button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-link" id="tabFeed" onclick="switchTab('feed')">Feed Kota</button>
                    </li>
                </ul>

                <div id="listContainer">
                    <div class="text-center p-5"><div class="spinner-border text-primary" role="status"></div></div>
                </div>
                
                <div id="paginationContainer" class="mt-4"></div>
            </section>
            
            <aside class="col-lg-3 d-none d-lg-block">
                <div class="card border-0 p-3 shadow-sm sticky-top" style="top: 20px;">
                    <h6 class="fw-bold"><i class="bi bi-info-circle-fill text-primary me-2"></i>Pengumuman</h6>
                    <p class="small text-muted mt-2">Gunakan portal ini untuk melaporkan masalah infrastruktur dan layanan kota secara langsung.</p>
                </div>
            </aside>
        </div>
    `
};

function switchTab(tabName) {
    const btnMyReports = document.getElementById('tabMyReports');
    const btnFeed = document.getElementById('tabFeed');
    
    if (tabName === 'my_reports') {
        btnMyReports.classList.add('active');
        btnFeed.classList.remove('active');
    } else {
        btnFeed.classList.add('active');
        btnMyReports.classList.remove('active');
    }
    
    if (typeof loadDashboardData === 'function') {
        loadDashboardData(tabName, 1);
    }
}

function handleRouting() {
    const hash = window.location.hash || '#login'; 
    const appContent = document.getElementById('app-content');
    
    if (appContent) {
        appContent.innerHTML = routes[hash] || routes['#login'];
        
        if (hash === '#login' && typeof setupLoginForm === 'function') {
            setupLoginForm();
        } else if (hash === '#dashboard' && typeof loadDashboardData === 'function') {
            loadDashboardData('my_reports', 1);
        }
    }
}

window.addEventListener('hashchange', handleRouting);
window.addEventListener('DOMContentLoaded', handleRouting);