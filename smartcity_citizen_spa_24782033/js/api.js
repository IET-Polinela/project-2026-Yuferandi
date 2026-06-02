const BASE_URL = 'http://127.0.0.1:8000';

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
        const data = await response.json();
        return { status: response.status, data: data };
    } catch (error) {
        console.error('Error saat menghubungi API:', error);
        return { status: 500, data: { detail: 'Koneksi ke server terputus.' } };
    }
}