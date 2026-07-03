# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: playwright\citizen_portal.spec.js >> Modul 1: Otorisasi & Sesi (AUTH-04, AUTH-05, AUTH-06) >> AUTH-05: Token kadaluarsa → interceptor menangani 401 dan redirect ke #login
- Location: playwright\citizen_portal.spec.js:399:5

# Error details

```
TimeoutError: page.waitForFunction: Timeout 10000ms exceeded.
```

# Page snapshot

```yaml
- generic [active] [ref=e1]:
  - navigation [ref=e2]:
    - link " Smart City Portal" [ref=e4] [cursor=pointer]:
      - /url: "#"
      - generic [ref=e5]: 
      - text: Smart City Portal
  - main [ref=e6]:
    - generic [ref=e7]:
      - complementary [ref=e8]:
        - generic [ref=e9]:
          - button " Laporan Baru" [ref=e10] [cursor=pointer]:
            - generic [ref=e11]: 
            - text: Laporan Baru
          - separator [ref=e12]
          - heading "Statistik Laporan Saya" [level=6] [ref=e13]
          - generic [ref=e14]:
            - generic [ref=e15]:
              - generic [ref=e16]: 
              - text: "Draft:"
            - generic [ref=e17]: "0"
          - generic [ref=e18]:
            - generic [ref=e19]:
              - generic [ref=e20]: 
              - text: "Reported:"
            - generic [ref=e21]: "0"
          - generic [ref=e22]:
            - generic [ref=e23]:
              - generic [ref=e24]: 
              - text: "Verified:"
            - generic [ref=e25]: "0"
          - generic [ref=e26]:
            - generic [ref=e27]:
              - generic [ref=e28]: 
              - text: "In Progress:"
            - generic [ref=e29]: "0"
          - generic [ref=e30]:
            - generic [ref=e31]:
              - generic [ref=e32]: 
              - text: "Resolved:"
            - generic [ref=e33]: "0"
      - generic [ref=e34]:
        - list [ref=e35]:
          - listitem [ref=e36]:
            - button "Laporan Saya" [ref=e37] [cursor=pointer]
          - listitem [ref=e38]:
            - button "Feed Kota" [ref=e39] [cursor=pointer]
        - generic [ref=e41]:
          - generic [ref=e42]: 
          - paragraph [ref=e43]: Gagal memuat data laporan.
      - complementary [ref=e44]:
        - generic [ref=e45]:
          - heading " Pengumuman" [level=6] [ref=e46]:
            - generic [ref=e47]: 
            - text: Pengumuman
          - paragraph [ref=e48]: Gunakan portal ini untuk melaporkan masalah infrastruktur dan layanan kota secara langsung.
  - text:  
```

# Test source

```ts
  371 |     // =========================================================================
  372 |     // TEST CASE: AUTH-05
  373 |     // =========================================================================
  374 |     // JUDUL:
  375 |     //   Token Interceptor: Access token kadaluarsa → SPA menangani 401 error
  376 |     //
  377 |     // SKENARIO:
  378 |     //   Pengguna memiliki access_token yang sudah kadaluarsa (expired) namun
  379 |     //   refresh_token masih valid. Saat SPA melakukan API call dan mendapat
  380 |     //   respons 401, interceptor di api.js harus membersihkan localStorage
  381 |     //   dan mengarahkan pengguna ke halaman login.
  382 |     //
  383 |     // CATATAN TEKNIS:
  384 |     //   Dalam kode api.js (baris 28-33), interceptor sederhana diimplementasikan:
  385 |     //     if(response.status == 401){
  386 |     //         alert('Sesi Anda telah habis atau Anda belum login.');
  387 |     //         localStorage.clear();
  388 |     //         window.location.hash = '#login';
  389 |     //         return null;
  390 |     //     }
  391 |     //
  392 |     //   Perhatikan bahwa SPA ini TIDAK memiliki mekanisme auto-refresh token.
  393 |     //   Jadi ketika access_token expired, SPA langsung redirect ke login.
  394 |     //
  395 |     // STRATEGI TESTING:
  396 |     //   Kita menggunakan page.route() untuk mock respons 401 dari API server,
  397 |     //   sehingga kita tidak perlu benar-benar mengirim expired token ke server.
  398 |     // =========================================================================
  399 |     test('AUTH-05: Token kadaluarsa → interceptor menangani 401 dan redirect ke #login', async ({ page }) => {
  400 |         // -------------------------------------------------------------------
  401 |         // LANGKAH 1: Setup token di localStorage (simulasi user yang sudah login
  402 |         //            tapi tokennya sudah kadaluarsa)
  403 |         // -------------------------------------------------------------------
  404 |         await setupAuthTokens(page, EXPIRED_ACCESS_TOKEN, EXPIRED_REFRESH_TOKEN);
  405 | 
  406 |         // Verifikasi token tersimpan dengan benar
  407 |         const storedToken = await page.evaluate(() => localStorage.getItem('access_token'));
  408 |         expect(storedToken).toBe(EXPIRED_ACCESS_TOKEN);
  409 | 
  410 |         // -------------------------------------------------------------------
  411 |         // LANGKAH 2: Mock respons API untuk mensimulasikan 401 Unauthorized
  412 |         // -------------------------------------------------------------------
  413 |         // page.route() dapat menginterceptsi request HTTP
  414 |         // dan memberikan respons buatan (mock response).
  415 |         //
  416 |         // Pola URL '**\/api/report/**' akan mencocokkan semua request
  417 |         // ke endpoint report API (termasuk query parameters).
  418 |         //
  419 |         // -------------------------------------------------------------------
  420 | 
  421 |         // Hapus interceptor URL sebelumnya yang meredirect ke localhost
  422 |         // Agar mock kita yang prioritas
  423 |         await page.unroute('http://103.151.63.71:8013/api/**');
  424 | 
  425 |         // Mock SEMUA request ke API endpoint agar mengembalikan 401
  426 |         await page.route('**/api/**', async (route) => {
  427 |             // route.fulfill() langsung mengembalikan respons tanpa mengirim
  428 |             // request ke server asli. Ini sangat berguna untuk testing.
  429 |             await route.fulfill({
  430 |                 status: 401,
  431 |                 contentType: 'application/json',
  432 |                 body: JSON.stringify({
  433 |                     detail: 'Given token not valid for any token type',
  434 |                     code: 'token_not_valid'
  435 |                 })
  436 |             });
  437 |         });
  438 | 
  439 |         // -------------------------------------------------------------------
  440 |         // LANGKAH 3: Handle dialog alert yang muncul dari interceptor api.js
  441 |         // -------------------------------------------------------------------
  442 |         // Kode api.js menampilkan alert('Sesi Anda telah habis...') saat
  443 |         // menerima respons 401. Playwright akan error jika dialog tidak ditangani.
  444 |         //
  445 |         // page.on('dialog') mendaftarkan event handler untuk dialog browser
  446 |         // (alert, confirm, prompt). Kita harus accept/dismiss dialog.
  447 |         page.on('dialog', async (dialog) => {
  448 |             // Verifikasi pesan alert sesuai dengan yang ada di api.js
  449 |             console.log(`[AUTH-05] Dialog muncul: "${dialog.message()}"`);
  450 |             await dialog.accept();
  451 |         });
  452 | 
  453 |         // -------------------------------------------------------------------
  454 |         // LANGKAH 4: Navigasi ke #dashboard (router.js akan mengizinkan karena
  455 |         //            ada token di localStorage, meskipun token sudah expired)
  456 |         // -------------------------------------------------------------------
  457 |         // Auth guard di router.js HANYA memeriksa keberadaan token (ada/tidak),
  458 |         // BUKAN validitas token. Validitas dicek saat API call dilakukan.
  459 |         //
  460 |         await page.goto(`${SPA_URL}#dashboard`);
  461 | 
  462 |         // Tunggu hingga dashboard ter-render dan API call dilakukan
  463 |         // Saat dashboard dimuat, setupDashboardEvents() dan loadDashboardData()
  464 |         // akan dipanggil, yang akan memicu requestAPI() → mendapat 401 → redirect
  465 |         //
  466 |         await page.waitForTimeout(2000);
  467 | 
  468 |         // -------------------------------------------------------------------
  469 |         // LANGKAH 5: Verifikasi redirect ke #login setelah 401
  470 |         // -------------------------------------------------------------------
> 471 |         await page.waitForFunction(
      |                    ^ TimeoutError: page.waitForFunction: Timeout 10000ms exceeded.
  472 |             () => window.location.hash === '#login',
  473 |             null,
  474 |             { timeout: 10000 }
  475 |         );
  476 | 
  477 |         await expect(page).toHaveURL(/#login/);
  478 | 
  479 |         // -------------------------------------------------------------------
  480 |         // LANGKAH 6: Verifikasi localStorage sudah dibersihkan oleh interceptor
  481 |         // -------------------------------------------------------------------
  482 |         // Kode api.js baris 30: localStorage.clear()
  483 |         const tokenAfter = await page.evaluate(() => localStorage.getItem('access_token'));
  484 |         const refreshAfter = await page.evaluate(() => localStorage.getItem('refresh_token'));
  485 | 
  486 |         // Token harus null setelah interceptor membersihkan localStorage
  487 |         expect(tokenAfter).toBeNull();
  488 |         expect(refreshAfter).toBeNull();
  489 | 
  490 |         console.log('[AUTH-05] ✅ Interceptor 401 berhasil: localStorage dibersihkan, redirect ke #login');
  491 |     });
  492 | 
  493 |     // =========================================================================
  494 |     // TEST CASE: AUTH-06
  495 |     // =========================================================================
  496 |     // JUDUL:
  497 |     //   Kedua Token Kadaluarsa: Access + Refresh expired → redirect ke #login
  498 |     //
  499 |     // SKENARIO:
  500 |     //   Kedua token (access dan refresh) sudah kadaluarsa. Pengguna mencoba
  501 |     //   mengakses #dashboard. SPA harus mendeteksi kegagalan autentikasi
  502 |     //   dan mengarahkan pengguna kembali ke halaman login.
  503 |     //
  504 |     // PERBEDAAN DENGAN AUTH-05:
  505 |     //   AUTH-05 fokus pada interceptor menangani respons 401.
  506 |     //   AUTH-06 fokus pada state akhir: localStorage HARUS bersih dan
  507 |     //   pengguna HARUS berada di halaman login.
  508 |     //
  509 |     // =========================================================================
  510 |     test('AUTH-06: Kedua token kadaluarsa → localStorage dibersihkan, redirect ke #login', async ({ page }) => {
  511 |         // -------------------------------------------------------------------
  512 |         // LANGKAH 1: Simpan kedua token yang sudah kadaluarsa ke localStorage
  513 |         // -------------------------------------------------------------------
  514 |         await setupAuthTokens(page, EXPIRED_ACCESS_TOKEN, EXPIRED_REFRESH_TOKEN);
  515 | 
  516 |         // Verifikasi awal: kedua token tersimpan
  517 |         const accessBefore = await page.evaluate(() => localStorage.getItem('access_token'));
  518 |         const refreshBefore = await page.evaluate(() => localStorage.getItem('refresh_token'));
  519 |         expect(accessBefore).not.toBeNull();
  520 |         expect(refreshBefore).not.toBeNull();
  521 | 
  522 |         // -------------------------------------------------------------------
  523 |         // LANGKAH 2: Mock API untuk menolak semua request dengan 401
  524 |         // -------------------------------------------------------------------
  525 |         // Karena kedua token expired, server pasti menolak. Kita mock
  526 |         // agar test tidak bergantung pada koneksi server yang sebenarnya.
  527 |         await page.unroute('http://103.151.63.71:8013/api/**');
  528 | 
  529 |         await page.route('**/api/**', async (route) => {
  530 |             await route.fulfill({
  531 |                 status: 401,
  532 |                 contentType: 'application/json',
  533 |                 body: JSON.stringify({
  534 |                     detail: 'Token is invalid or expired',
  535 |                     code: 'token_not_valid'
  536 |                 })
  537 |             });
  538 |         });
  539 | 
  540 |         // -------------------------------------------------------------------
  541 |         // LANGKAH 3: Handle dialog alert agar test tidak terganggu
  542 |         // -------------------------------------------------------------------
  543 |         page.on('dialog', async (dialog) => {
  544 |             console.log(`[AUTH-06] Dialog muncul: "${dialog.message()}"`);
  545 |             await dialog.accept();
  546 |         });
  547 | 
  548 |         // -------------------------------------------------------------------
  549 |         // LANGKAH 4: Coba akses dashboard
  550 |         // -------------------------------------------------------------------
  551 |         await page.goto(`${SPA_URL}#dashboard`);
  552 | 
  553 |         // Tunggu proses redirect terjadi
  554 |         await page.waitForTimeout(2000);
  555 | 
  556 |         // -------------------------------------------------------------------
  557 |         // LANGKAH 5: Verifikasi TIGA hal sekaligus (Triple Assertion)
  558 |         // -------------------------------------------------------------------
  559 | 
  560 |         // 5a. URL harus mengarah ke #login
  561 |         await page.waitForFunction(
  562 |             () => window.location.hash === '#login',
  563 |             null,
  564 |             { timeout: 10000 }
  565 |         );
  566 |         await expect(page).toHaveURL(/#login/);
  567 | 
  568 |         // 5b. localStorage harus bersih (access_token harus null)
  569 |         const accessAfter = await page.evaluate(() => localStorage.getItem('access_token'));
  570 |         expect(accessAfter).toBeNull();
  571 | 
```