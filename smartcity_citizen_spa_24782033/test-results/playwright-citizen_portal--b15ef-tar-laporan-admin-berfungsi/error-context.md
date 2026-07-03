# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: playwright\citizen_portal.spec.js >> Modul 5: Interaktivitas UI (UI-01 through UI-06) >> UI-02: Live Search pada daftar laporan admin berfungsi
- Location: playwright\citizen_portal.spec.js:729:5

# Error details

```
TimeoutError: page.waitForSelector: Timeout 10000ms exceeded.
Call log:
  - waiting for locator('form') to be visible

```

# Page snapshot

```yaml
- generic [active] [ref=e1]:
  - banner [ref=e2]:
    - heading "Page not found (404)" [level=1] [ref=e3]
    - table [ref=e4]:
      - rowgroup [ref=e5]:
        - 'row "Request Method: GET" [ref=e6]':
          - rowheader "Request Method:" [ref=e7]
          - cell "GET" [ref=e8]
        - 'row "Request URL: http://localhost:8000/login/" [ref=e9]':
          - rowheader "Request URL:" [ref=e10]
          - cell "http://localhost:8000/login/" [ref=e11]
  - main [ref=e12]:
    - paragraph [ref=e13]:
      - text: Using the URLconf defined in
      - code [ref=e14]: smartcity_app.urls
      - text: ", Django tried these URL patterns, in this order:"
    - list [ref=e15]:
      - listitem [ref=e16]:
        - code [ref=e17]: admin/
      - listitem [ref=e18]:
        - code
        - code [ref=e19]: "[name='home']"
      - listitem [ref=e20]:
        - code
        - code [ref=e21]: reports/ [name='report_list']
      - listitem [ref=e22]:
        - code
        - code [ref=e23]: reports/create/ [name='report_create']
      - listitem [ref=e24]:
        - code
        - code [ref=e25]: reports/add/ [name='add_report']
      - listitem [ref=e26]:
        - code
        - code [ref=e27]: reports/<int:pk>/update/ [name='report_update']
      - listitem [ref=e28]:
        - code
        - code [ref=e29]: reports/<int:pk>/edit/ [name='update_report']
      - listitem [ref=e30]:
        - code
        - code [ref=e31]: reports/<int:pk>/delete/ [name='report_delete']
      - listitem [ref=e32]:
        - code
        - code [ref=e33]: reports/<int:pk>/remove/ [name='delete_report']
      - listitem [ref=e34]:
        - code
        - code [ref=e35]: reports/<int:pk>/ [name='report_detail']
      - listitem [ref=e36]:
        - code
        - code [ref=e37]: reports/<int:pk>/status/ [name='update_status']
      - listitem [ref=e38]:
        - code
        - code [ref=e39]: api/reports/
      - listitem [ref=e40]:
        - code
        - code [ref=e41]: api/reports/<int:pk>/
      - listitem [ref=e42]:
        - code
        - code [ref=e43]: api/search/ [name='api_search_reports']
      - listitem [ref=e44]:
        - code
        - code [ref=e45]: reports/search/ [name='report_search']
      - listitem [ref=e46]:
        - code
        - code [ref=e47]: reports/detail-api/<int:pk>/ [name='report_detail_api']
      - listitem [ref=e48]:
        - code
        - code [ref=e49]: api/detail/<int:pk>/ [name='api_detail_modal']
      - listitem [ref=e50]:
        - code
        - code [ref=e51]: api/
      - listitem [ref=e52]:
        - code [ref=e53]: about/
      - listitem [ref=e54]:
        - code [ref=e55]: contacts/
      - listitem [ref=e56]:
        - code [ref=e57]: auth/
      - listitem [ref=e58]:
        - code [ref=e59]: dashboard/
      - listitem [ref=e60]:
        - code [ref=e61]: api/token/ [name='token_obtain_pair']
      - listitem [ref=e62]:
        - code [ref=e63]: api/token/refresh/ [name='token_refresh']
      - listitem [ref=e64]:
        - code [ref=e65]: api/register/ [name='api_register']
      - listitem [ref=e66]:
        - code [ref=e67]: api/schema/ [name='schema']
      - listitem [ref=e68]:
        - code [ref=e69]: api/docs/swagger/ [name='swagger-ui']
      - listitem [ref=e70]:
        - code [ref=e71]: api/docs/scalar/ [name='scalar-ui']
    - paragraph [ref=e72]:
      - text: The current path,
      - code [ref=e73]: login/
      - text: ", didn’t match any of these."
  - contentinfo [ref=e74]:
    - paragraph [ref=e75]:
      - text: You’re seeing this error because you have
      - code [ref=e76]: DEBUG = True
      - text: in your Django settings file. Change that to
      - code [ref=e77]: "False"
      - text: ", and Django will display a standard 404 page."
```

# Test source

```ts
  51  | // BASE_URL: Alamat server backend Django. Semua request API diarahkan ke sini.
  52  | //
  53  | // SPA_URL: Alamat di mana SPA Citizen Portal di-serve. Jika tidak ada local
  54  | //          web server, Playwright akan membuka file HTML langsung dari disk.
  55  | //          Gunakan environment variable PLAYWRIGHT_SPA_URL untuk override.
  56  | //
  57  | // CATATAN PENTING :
  58  | //   - file:// URL akan bekerja tanpa server jika semua asset JS/CSS ada di disk
  59  | //     dan SPA tidak memerlukan CORS untuk local file access.
  60  | //   - Untuk frontend yang membutuhkan web server, jalankan `python -m http.server`
  61  | //     atau `npx http-server` di folder root SPA lalu set PLAYWRIGHT_SPA_URL.
  62  | // ---------------------------------------------------------------------------
  63  | const BASE_URL = 'http://localhost:8000';
  64  | const DEFAULT_SPA_FILE = path.resolve(__dirname, '..', 'index.html').replace(/\\/g, '/');
  65  | const SPA_URL = process.env.PLAYWRIGHT_SPA_URL || `file://${DEFAULT_SPA_FILE}`;
  66  | 
  67  | // ---------------------------------------------------------------------------
  68  | // KREDENSIAL TEST 
  69  | // ---------------------------------------------------------------------------
  70  | // Kredensial untuk akun test yang sudah terdaftar di database Django.
  71  | // Pastikan akun ini ada sebelum menjalankan test, atau gunakan mock API.
  72  | // ---------------------------------------------------------------------------
  73  | const TEST_CITIZEN_USERNAME = 'testwarga';
  74  | const TEST_CITIZEN_PASSWORD = 'testpassword123';
  75  | const TEST_ADMIN_USERNAME  = 'admin';
  76  | const TEST_ADMIN_PASSWORD  = 'admin123';
  77  | 
  78  | // ---------------------------------------------------------------------------
  79  | // FAKE JWT TOKENS UNTUK TESTING
  80  | // ---------------------------------------------------------------------------
  81  | // Token JWT palsu yang digunakan untuk simulasi sesi kadaluarsa.
  82  | //
  83  | // Struktur JWT: header.payload.signature (base64url encoded)
  84  | //
  85  | // Token di bawah sengaja dibuat dengan 'exp' (expiry) yang sudah lewat
  86  | // sehingga server akan menolaknya dengan status 401 Unauthorized.
  87  | // ---------------------------------------------------------------------------
  88  | const EXPIRED_ACCESS_TOKEN  = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwMDAwMDAwLCJpYXQiOjE2MDAwMDAwMDAsImp0aSI6ImZha2VfYWNjZXNzX2lkIiwidXNlcl9pZCI6MX0.fake_signature_for_testing';
  89  | const EXPIRED_REFRESH_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMDAwMDAwMCwiaWF0IjoxNjAwMDAwMDAwLCJqdGkiOiJmYWtlX3JlZnJlc2hfaWQiLCJ1c2VyX2lkIjoxfQ.fake_signature_for_testing';
  90  | const VALID_ACCESS_TOKEN    = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjo5OTk5OTk5OTk5LCJpYXQiOjE2MDAwMDAwMDAsImp0aSI6InZhbGlkX2FjY2Vzc19pZCIsInVzZXJfaWQiOjF9.fake_valid_signature';
  91  | 
  92  | // =============================================================================
  93  | // FUNGSI HELPER 
  94  | // =============================================================================
  95  | // Fungsi-fungsi pembantu (helper) yang digunakan berulang kali di berbagai test.
  96  | // Memisahkan logika ke helper function membuat kode test lebih bersih dan DRY
  97  | // (Don't Repeat Yourself).
  98  | //
  99  | // =============================================================================
  100 | 
  101 | /**
  102 |  * loginSPA - Melakukan login ke Portal Warga (Citizen SPA)
  103 |  *
  104 |  * Langkah-langkah / Steps:
  105 |  *   1. Navigasi ke halaman SPA dengan hash #login
  106 |  *   2. Tunggu form login muncul (id='loginForm')
  107 |  *   3. Isi username dan password
  108 |  *   4. Klik tombol submit
  109 |  *   5. Tunggu navigasi ke #dashboard (jika login berhasil)
  110 |  *
  111 |  * @param {import('@playwright/test').Page} page - Objek halaman Playwright 
  112 |  * @param {string} username - Username untuk login 
  113 |  * @param {string} password - Password untuk login 
  114 |  */
  115 | async function loginSPA(page, username, password) {
  116 |     // Navigasi ke halaman login SPA
  117 |     await page.goto(`${SPA_URL}#login`);
  118 | 
  119 |     // Tunggu hingga form login ter-render di DOM
  120 |     // Catatan: SPA menggunakan hash-routing, jadi router.js akan meng-inject
  121 |     //          HTML form login ke dalam div #app-content saat hash = #login
  122 |     await page.waitForSelector('#loginForm', { state: 'visible', timeout: 10000 });
  123 | 
  124 |     // Isi field username - menggunakan locator dengan id selector
  125 |     await page.locator('#loginUsername').fill(username);
  126 | 
  127 |     // Isi field password
  128 |     await page.locator('#loginPassword').fill(password);
  129 | 
  130 |     // Klik tombol submit pada form login
  131 |     // Selector: cari button type="submit" di dalam form #loginForm
  132 |     await page.locator('#loginForm button[type="submit"]').click();
  133 | }
  134 | 
  135 | /**
  136 |  * loginAdmin - Melakukan login ke Portal Admin (Django server-side)
  137 |  *
  138 |  * Portal Admin menggunakan Django's built-in authentication dengan
  139 |  * form POST + CSRF token. Berbeda dengan SPA yang menggunakan JWT API.
  140 |  *
  141 |  *
  142 |  * @param {import('@playwright/test').Page} page - Objek halaman Playwright 
  143 |  * @param {string} username - Username admin 
  144 |  * @param {string} password - Password admin 
  145 |  */
  146 | async function loginAdmin(page, username, password) {
  147 |     // Navigasi ke halaman login admin Django
  148 |     await page.goto(`${BASE_URL}/login/`);
  149 | 
  150 |     // Tunggu form login muncul
> 151 |     await page.waitForSelector('form', { state: 'visible', timeout: 10000 });
      |                ^ TimeoutError: page.waitForSelector: Timeout 10000ms exceeded.
  152 | 
  153 |     // Isi username & password
  154 |     await page.locator('input[name="username"]').fill(username);
  155 |     await page.locator('input[name="password"]').fill(password);
  156 | 
  157 |     // Klik tombol submit login dan tunggu hingga navigasi/redirect selesai
  158 |     await Promise.all([
  159 |         page.waitForNavigation({ waitUntil: 'networkidle', timeout: 15000 }),
  160 |         page.locator('button[type="submit"]').click()
  161 |     ]);
  162 | }
  163 | 
  164 | /**
  165 |  * setupAuthTokens - Menyimpan token otentikasi ke localStorage browser
  166 |  *
  167 |  * Fungsi ini menggunakan page.evaluate() untuk menjalankan JavaScript
  168 |  * langsung di konteks browser (bukan di Node.js).
  169 |  * Ini berguna untuk mensimulasikan state login tanpa benar-benar
  170 |  * melakukan proses login via API.
  171 |  *
  172 |  *
  173 |  * PENTING:
  174 |  *   page.evaluate() menjalankan kode di dalam browser yang sedang diuji.
  175 |  *   Variabel dari Node.js harus di-pass sebagai argumen kedua.
  176 |  *
  177 |  *
  178 |  * @param {import('@playwright/test').Page} page - Objek halaman Playwright 
  179 |  * @param {string} accessToken  - JWT access token
  180 |  * @param {string} refreshToken - JWT refresh token
  181 |  * @param {string} [username]   - Opsional: username untuk disimpan 
  182 |  */
  183 | async function setupAuthTokens(page, accessToken, refreshToken, username = 'testwarga') {
  184 |     await page.evaluate(
  185 |         // Arrow function ini dieksekusi di dalam browser (V8 engine)
  186 |         ({ access, refresh, user }) => {
  187 |             // localStorage.setItem() menyimpan data key-value di browser
  188 |             localStorage.setItem('access_token', access);
  189 |             localStorage.setItem('refresh_token', refresh);
  190 |             localStorage.setItem('username', user);
  191 |         },
  192 |         // Argumen kedua: objek data yang di-pass ke browser context
  193 |         { access: accessToken, refresh: refreshToken, user: username }
  194 |     );
  195 | }
  196 | 
  197 | /**
  198 |  * clearAuthTokens - Menghapus semua token dari localStorage
  199 |  *
  200 |  * Digunakan di beforeEach untuk memastikan setiap test dimulai
  201 |  * dari state bersih (tidak ada sesi login tersisa).
  202 |  *
  203 |  * @param {import('@playwright/test').Page} page - Objek halaman Playwright 
  204 |  */
  205 | async function clearAuthTokens(page) {
  206 |     await page.evaluate(() => {
  207 |         // localStorage.clear() menghapus SEMUA data di localStorage domain ini
  208 |         localStorage.clear();
  209 |     });
  210 | }
  211 | 
  212 | /**
  213 |  * mockSPAApiUrl - Memastikan SEMUA request API di SPA mengarah ke localhost:8000
  214 |  *
  215 |  * Menggunakan pola wildcard "** /api/**" (dua bintang lalu slash api slash dua bintang),
  216 |  * fungsi ini akan mencegat request ke domain apapun
  217 |  * (misal: http://103.151.63.71:8013/api, http://192.168.1.5/api, dll)
  218 |  * dan membelokkannya secara paksa ke server Django lokal di http://localhost:8000/api.
  219 |  *
  220 |  * @param {import('@playwright/test').Page} page - Objek halaman Playwright
  221 |  */
  222 | async function mockSPAApiUrl(page) {
  223 |     const BASE_URL = 'http://localhost:8000';
  224 | 
  225 |     // Gunakan wildcard **/api/** untuk menangkap dari host/domain mana saja
  226 |     await page.route('**/api/**', async (route) => {
  227 |         const originalUrl = route.request().url();
  228 | 
  229 |         // [PENTING] Mencegah infinite loop: 
  230 |         // Jika request sudah benar mengarah ke localhost:8000, biarkan saja lewat.
  231 |         if (originalUrl.startsWith(BASE_URL)) {
  232 |             return route.continue();
  233 |         }
  234 | 
  235 |         // Parsing URL asli menggunakan objek URL bawaan JavaScript
  236 |         const urlObj = new URL(originalUrl);
  237 |         
  238 |         // urlObj.pathname akan mengambil "/api/endpoint/"
  239 |         // urlObj.search akan mengambil query string (misal: "?search=jalan") jika ada
  240 |         const newUrl = `${BASE_URL}${urlObj.pathname}${urlObj.search}`;
  241 | 
  242 |         // Lanjutkan request dengan URL yang sudah dibelokkan ke localhost
  243 |         await route.continue({ url: newUrl });
  244 |     });
  245 | }
  246 | 
  247 | 
  248 | // #############################################################################
  249 | // #                                                                           #
  250 | // #   MODUL 1: OTORISASI & SESI (AUTH-04, AUTH-05, AUTH-06)                   #
  251 | // #                                                                           #
```