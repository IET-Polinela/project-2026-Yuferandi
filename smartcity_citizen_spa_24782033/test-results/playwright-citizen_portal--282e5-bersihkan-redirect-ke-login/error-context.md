# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: playwright\citizen_portal.spec.js >> Modul 1: Otorisasi & Sesi (AUTH-04, AUTH-05, AUTH-06) >> AUTH-06: Kedua token kadaluarsa → localStorage dibersihkan, redirect ke #login
- Location: playwright\citizen_portal.spec.js:510:5

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
  471 |         await page.waitForFunction(
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
> 561 |         await page.waitForFunction(
      |                    ^ TimeoutError: page.waitForFunction: Timeout 10000ms exceeded.
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
  572 |         // 5c. localStorage harus bersih (refresh_token harus null)
  573 |         const refreshAfter = await page.evaluate(() => localStorage.getItem('refresh_token'));
  574 |         expect(refreshAfter).toBeNull();
  575 | 
  576 |         // 5d. Verifikasi username juga ikut terhapus
  577 |         const usernameAfter = await page.evaluate(() => localStorage.getItem('username'));
  578 |         expect(usernameAfter).toBeNull();
  579 | 
  580 |         // 5e. Form login harus terlihat (verifikasi visual)
  581 |         await expect(page.locator('#loginForm')).toBeVisible({ timeout: 5000 });
  582 | 
  583 |         console.log('[AUTH-06] ✅ Kedua token expired: localStorage bersih, redirect ke #login berhasil');
  584 |     });
  585 | });
  586 | 
  587 | 
  588 | // #############################################################################
  589 | // #                                                                           #
  590 | // #   MODUL 5: INTERAKTIVITAS UI (UI-01 through UI-06)                        #
  591 | // #                                                                           #
  592 | // #   Modul ini menguji fitur-fitur interaktif pada antarmuka pengguna,        #
  593 | // #   termasuk Chart.js rendering, live search, pagination, modal dialog,     #
  594 | // #   form submission, dan responsive design.                                 #
  595 | // #                                                                           #
  596 | // #############################################################################
  597 | 
  598 | test.describe('Modul 5: Interaktivitas UI (UI-01 through UI-06)', () => {
  599 |     // =========================================================================
  600 |     // PENGANTAR MODUL
  601 |     // =========================================================================
  602 |     // Test UI memverifikasi bahwa elemen-elemen antarmuka berfungsi dengan baik
  603 |     // dari perspektif pengguna akhir. Ini mencakup:
  604 |     //
  605 |     // 1. Rendering visual (chart, tabel, modal)
  606 |     // 2. Interaksi pengguna (klik, ketik, scroll)
  607 |     // 3. Respons dinamis (AJAX, filtering, pagination)
  608 |     // 4. Responsive design (tampilan mobile vs desktop)
  609 |     // =========================================================================
  610 | 
  611 |     // =========================================================================
  612 |     // TEST CASE: UI-01
  613 |     // =========================================================================
  614 |     // JUDUL:
  615 |     //   Chart.js Rendering: Grafik statistik dashboard admin ter-render
  616 |     //
  617 |     // SKENARIO:
  618 |     //   Admin login ke portal admin, navigasi ke halaman /dashboard/,
  619 |     //   tunggu Chart.js selesai merender, dan verifikasi bahwa elemen
  620 |     //   canvas chart (statusChart dan categoryChart) ada dan terlihat.
  621 |     //
  622 |     // KONSEP TEKNIS:
  623 |     //   - Chart.js merender grafik ke elemen <canvas> HTML5
  624 |     //   - Dashboard mengambil data dari /dashboard/api/data/ via fetch()
  625 |     //   - Chart diinisialisasi setelah data berhasil di-fetch
  626 |     //
  627 |     // REFERENSI KODE:
  628 |     //   Lihat dashboard.html baris 47-74:
  629 |     //     - <canvas id="statusChart"> → Chart.js doughnut chart
  630 |     //     - <canvas id="categoryChart"> → Chart.js bar chart
  631 |     //     - fetch('/dashboard/api/data/') → data source
  632 |     // =========================================================================
  633 |     test('UI-01: Chart.js di Dashboard Admin ter-render dengan benar', async ({ page }) => {
  634 |         // -------------------------------------------------------------------
  635 |         // LANGKAH 1: Login ke portal admin
  636 |         // -------------------------------------------------------------------
  637 |         // Menggunakan helper function loginAdmin yang sudah kita buat
  638 |         await loginAdmin(page, TEST_ADMIN_USERNAME, TEST_ADMIN_PASSWORD);
  639 | 
  640 |         // -------------------------------------------------------------------
  641 |         // LANGKAH 2: Navigasi ke halaman dashboard
  642 |         // -------------------------------------------------------------------
  643 |         await page.goto(`${BASE_URL}/dashboard/`);
  644 | 
  645 |         // Tunggu halaman selesai dimuat sepenuhnya
  646 |         await page.waitForLoadState('networkidle');
  647 | 
  648 |         // -------------------------------------------------------------------
  649 |         // LANGKAH 3: Tunggu Chart.js selesai merender
  650 |         // -------------------------------------------------------------------
  651 |         // Chart.js merender secara asinkron setelah data di-fetch dari API.
  652 |         // Kita perlu menunggu:
  653 |         //   1. Fetch ke /dashboard/api/data/ selesai
  654 |         //   2. new Chart() dipanggil dan canvas di-render
  655 |         //
  656 |         // Strategi: Tunggu elemen canvas terlihat di viewport
  657 |         // -------------------------------------------------------------------
  658 |         const statusChartCanvas  = page.locator('#statusChart');
  659 |         const categoryChartCanvas = page.locator('#categoryChart');
  660 | 
  661 |         // -------------------------------------------------------------------
```