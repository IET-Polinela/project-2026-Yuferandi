let currentTab = 'my_reports';
let currentPage = 1;
let allReports = [];
let totalPages = 1;
let editingReportId = null; 
let reportModalInstance = null;

// ==========================================
// 1. Fetching API Terpaginasi
// ==========================================
async function loadDashboardData(tab = currentTab, page = currentPage) {
    currentTab = tab;
    currentPage = page;

    const response = await requestAPI(`/api/report/?tab=${tab}&page=${page}`, 'GET');

    if (response && response.status === 200) {
        allReports = response.data.results || [];
        const totalCount = response.data.count || 0;
        totalPages = Math.ceil(totalCount / 10) || 1;

        renderList();
        renderPagination();
        loadSummaryStats(); 
    } else {
        const listContainer = document.getElementById('listContainer');
        if (listContainer) {
            listContainer.innerHTML = `
                <div class="col-12 text-center text-muted p-5">
                    <i class="bi bi-exclamation-triangle fs-1"></i><p>Gagal memuat data laporan.</p>
                </div>
            `;
        }
        const paginationContainer = document.getElementById('paginationContainer');
        if (paginationContainer) paginationContainer.innerHTML = '';
    }
}

// ==========================================
// 2. Bypass Kalkulasi Rekap di Sidebar
// ==========================================
async function loadSummaryStats() {
    const response = await requestAPI('/api/report/?tab=my_reports&page_size=1000', 'GET');
    
    if (response && response.status === 200) {
        const allMyReports = response.data.results || [];
        
        const totalDraft = allMyReports.filter(r => r.status === 'DRAFT').length;
        const totalProses = allMyReports.filter(r => r.status === 'IN_PROGRESS' || r.status === 'VERIFIED' || r.status === 'REPORTED').length;
        const totalSelesai = allMyReports.filter(r => r.status === 'RESOLVED').length;

        const statDraft = document.getElementById('statDraft');
        const statProses = document.getElementById('statProses');
        const statSelesai = document.getElementById('statSelesai');

        if(statDraft) statDraft.innerText = totalDraft;
        if(statProses) statProses.innerText = totalProses;
        if(statSelesai) statSelesai.innerText = totalSelesai;
    }
}

// ==========================================
// 3. Render List & Progress Bar
// ==========================================
function renderList() {
    const listContainer = document.getElementById('listContainer');
    if (!listContainer) return;

    if (allReports.length === 0) {
        listContainer.innerHTML = `<div class="col-12 text-center p-5 text-muted card border-0 shadow-sm"><i class="bi bi-inbox fs-1"></i><h5 class="mt-3">Belum ada laporan</h5></div>`;
        return;
    }

    let html = '';
    allReports.forEach(report => {
        let progressPercent = 0;
        let progressColor = 'bg-secondary';
        let statusBadgeColor = 'bg-secondary';

        if (report.status === 'DRAFT') {
            progressPercent = 15;
            progressColor = 'bg-secondary';
            statusBadgeColor = 'bg-secondary';
        } else if (report.status === 'REPORTED') {
            progressPercent = 40;
            progressColor = 'bg-info';
            statusBadgeColor = 'bg-info text-dark';
        } else if (report.status === 'VERIFIED') {
            progressPercent = 60;
            progressColor = 'bg-warning';
            statusBadgeColor = 'bg-warning text-dark';
        } else if (report.status === 'IN_PROGRESS') {
            progressPercent = 80;
            progressColor = 'bg-primary'; 
            statusBadgeColor = 'bg-primary';
        } else if (report.status === 'RESOLVED') {
            progressPercent = 100;
            progressColor = 'bg-success';
            statusBadgeColor = 'bg-success';
        }

        const editBtn = (report.status === 'DRAFT' && report.is_owner) 
            ? `<button class="btn btn-sm btn-outline-secondary" onclick="editDraft(${report.id})"><i class="bi bi-pencil"></i> Edit</button>` 
            : '';

        html += `
            <div class="card mb-3 shadow-sm border-0">
                <div class="card-body">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                         <span class="badge ${statusBadgeColor}">${report.status}</span>
                         <small class="text-muted">${new Date(report.updated_at).toLocaleDateString()}</small>
                    </div>
                    <h5 class="card-title fw-bold">${report.title}</h5>
                    <h6 class="card-subtitle mb-3 text-muted"><i class="bi bi-geo-alt"></i> ${report.location}</h6>
                    <p class="card-text">${report.description}</p>
                    
                    <div class="mb-3 mt-4">
                        <div class="d-flex justify-content-between small text-muted mb-1">
                            <span>Status Penanganan</span>
                            <span>${progressPercent}%</span>
                        </div>
                        <div class="progress" style="height: 8px;">
                            <div class="progress-bar ${progressColor}" role="progressbar" style="width: ${progressPercent}%"></div>
                        </div>
                    </div>
                    
                    <div class="d-flex justify-content-between align-items-center mt-3 pt-2 border-top">
                        <span class="small text-muted"><i class="bi bi-person"></i> ${report.reporter}</span>
                        ${editBtn}
                    </div>
                </div>
            </div>
        `;
    });
    listContainer.innerHTML = html;
}

// ==========================================
// 4. Render Tombol Paginasi
// ==========================================
function renderPagination() {
    const paginationContainer = document.getElementById('paginationContainer');
    if (!paginationContainer) return;
    
    let html = `<nav><ul class="pagination justify-content-center">`;
    
    html += `
        <li class="page-item ${currentPage === 1 ? 'disabled' : ''}">
            <button class="page-link" onclick="loadDashboardData('${currentTab}', ${currentPage - 1})">&laquo;</button>
        </li>
    `;
    
    for (let i = 1; i <= totalPages; i++) {
        html += `
            <li class="page-item ${currentPage === i ? 'active' : ''}">
                <button class="page-link" onclick="loadDashboardData('${currentTab}', ${i})">${i}</button>
            </li>
        `;
    }
    
    html += `
        <li class="page-item ${currentPage === totalPages ? 'disabled' : ''}">
            <button class="page-link" onclick="loadDashboardData('${currentTab}', ${currentPage + 1})">&raquo;</button>
        </li>
    `;
    
    html += `</ul></nav>`;
    paginationContainer.innerHTML = html;
}

// ==========================================
// 5. Manajemen Modal & Submit API
// ==========================================
function openModalNewReport() {
    editingReportId = null; 
    document.getElementById('reportForm').reset();
    document.getElementById('reportModalLabel').innerHTML = '<i class="bi bi-pencil-square me-2"></i>Buat Laporan Baru';
    reportModalInstance.show();
}

function editDraft(id) {
    const report = allReports.find(r => r.id === id);
    if (report) {
        editingReportId = id; 
        
        document.getElementById('title').value = report.title;
        document.getElementById('category').value = report.category;
        document.getElementById('location').value = report.location;
        document.getElementById('description').value = report.description;
        
        document.getElementById('reportModalLabel').innerHTML = '<i class="bi bi-pencil me-2"></i>Edit Draft Laporan';
        reportModalInstance.show();
    }
}

async function submitReportData(statusTarget) {
    const payload = {
        title: document.getElementById('title').value,
        category: document.getElementById('category').value,
        location: document.getElementById('location').value,
        description: document.getElementById('description').value,
        status: statusTarget 
    };

    if (!payload.title || !payload.category || !payload.location || !payload.description) {
        alert('Mohon lengkapi semua field laporan!');
        return;
    }

    let endpoint = '/api/report/';
    let method = 'POST';

    if (editingReportId !== null) {
        endpoint = `/api/report/${editingReportId}/`;
        method = 'PUT';
    }

    const response = await requestAPI(endpoint, method, payload);

    if (response.status === 201 || response.status === 200) {
        reportModalInstance.hide();
        document.getElementById('reportForm').reset();
        editingReportId = null;
        alert('Data berhasil disimpan!');
        loadDashboardData(currentTab, 1);
    } else {
        alert('Gagal menyimpan laporan. Cek konsol untuk detail.');
        console.error(response.data);
    }
}

// ==========================================
// 6. Inisialisasi
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
    if (typeof handleRouting === 'function') handleRouting();

    const modalEl = document.getElementById('reportModal');
    if (modalEl) {
         reportModalInstance = new bootstrap.Modal(modalEl);
    }

    const btnDraft = document.getElementById('btnDraft');
    const btnSubmit = document.getElementById('btnSubmit');

    if (btnDraft) btnDraft.addEventListener('click', () => submitReportData('DRAFT'));
    if (btnSubmit) btnSubmit.addEventListener('click', () => submitReportData('REPORTED'));
});