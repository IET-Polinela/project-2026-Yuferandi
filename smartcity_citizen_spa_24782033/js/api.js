const BASE_URL = 'http://localhost:8000';

async function requestAPI(endpoint, method = 'GET', bodyData = null) {
    const url = `${BASE_URL}${endpoint}`;
    const headers = { 'Content-Type': 'application/json' };
    const accessToken = localStorage.getItem('access_token');
    
    if (accessToken) { 
        headers['Authorization'] = `Bearer ${accessToken}`; 
    }
    
    const options = { method: method, headers: headers };
    
    if (bodyData && (method === 'POST' || method === 'PUT' || method === 'PATCH')) {
        options.body = JSON.stringify(bodyData);
    }
    
    try {
        const response = await fetch(url, options);
        // Parse JSON response if possible
        let data = null;
        try {
            data = await response.json();
        } catch (err) {
            data = null;
        }

        // Interceptor: jika server mengembalikan 401, lakukan tindakan
        // sesuai ekspektasi test (alert, clear localStorage, redirect)
        if (response.status === 401) {
            try {
                alert('Sesi Anda telah habis atau Anda belum login. Silakan masuk kembali.');
            } catch (e) {
                // ignore in non-browser contexts
            }
            try { localStorage.clear(); } catch (e) {}
            try { window.location.hash = '#login'; } catch (e) {}
            return { status: response.status, data: data };
        }

        return { status: response.status, data: data };
    } catch (error) {
        console.error('Error saat menghubungi API:', error);
        return { status: 500, data: { detail: 'Koneksi ke server terputus.' } };
    }
}