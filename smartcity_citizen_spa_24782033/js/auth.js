function setupLoginForm() {
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', async function(event) {
            event.preventDefault(); 
            
            const usernameInput = document.getElementById('loginUsername').value;
            const passwordInput = document.getElementById('loginPassword').value;
            const payload = { username: usernameInput, password: passwordInput };
            
            const response = await requestAPI('/api/token/', 'POST', payload);
            
            if (response.status === 200) {
                localStorage.setItem('access_token', response.data.access);
                localStorage.setItem('refresh_token', response.data.refresh);
                alert('Login berhasil! Mengalihkan ke Dashboard...');
                window.location.hash = '#dashboard'; 
            } else {
                alert('Login Gagal: Cek kembali username dan password Anda.');
            }
        });
    }
}