# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: playwright\citizen_portal.spec.js >> Modul 5: Interaktivitas UI (UI-01 through UI-06) >> UI-04: Klik tombol Buat Laporan → modal #reportModal muncul
- Location: playwright\citizen_portal.spec.js:982:5

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: locator('#btnBukaModal')
Expected: visible
Timeout: 10000ms
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 10000ms
  - waiting for locator('#btnBukaModal')

```

```yaml
- navigation:
  - link " Smart City Portal":
    - /url: "#"
- main:
  - complementary:
    - button " Laporan Baru"
    - separator
    - heading "Statistik Laporan Saya" [level=6]
    - text: " Draft: 0  Reported: 0  Verified: 0  In Progress: 0  Resolved: 0"
  - list:
    - listitem:
      - button "Laporan Saya"
    - listitem:
      - button "Feed Kota"
  - text: 
  - heading "Belum ada laporan" [level=5]
  - navigation:
    - list:
      - listitem:
        - button "«"
      - listitem:
        - button "1"
      - listitem:
        - button "»"
  - complementary:
    - heading " Pengumuman" [level=6]
    - paragraph: Gunakan portal ini untuk melaporkan masalah infrastruktur dan layanan kota secara langsung.
```

# Test source

```ts
  914  |         // -------------------------------------------------------------------
  915  |         // LANGKAH 4: Klik tab "Feed Kota (Publik)"
  916  |         // -------------------------------------------------------------------
  917  |         // Tab ini ada di router.js (template #dashboard), id='tabFeedKota'
  918  |         const tabFeedKota = page.locator('#tabFeedKota');
  919  |         await expect(tabFeedKota).toBeVisible();
  920  |         await tabFeedKota.click();
  921  | 
  922  |         // Tunggu data dimuat (AJAX call + render)
  923  |         await page.waitForTimeout(2000);
  924  | 
  925  |         // -------------------------------------------------------------------
  926  |         // LANGKAH 5: Hitung jumlah kartu laporan di listContainer
  927  |         // -------------------------------------------------------------------
  928  |         // Setiap laporan dirender sebagai <div class="col"> di dalam #listContainer
  929  |         // (lihat app.js renderList() baris 109: card.className = 'col')
  930  |         const listContainer = page.locator('#listContainer');
  931  |         await expect(listContainer).toBeVisible();
  932  | 
  933  |         const reportCards = listContainer.locator('.col');
  934  |         const cardCount = await reportCards.count();
  935  | 
  936  |         // Assertion: jumlah kartu tidak boleh lebih dari 10
  937  |         expect(cardCount).toBeLessThanOrEqual(10);
  938  |         expect(cardCount).toBeGreaterThan(0);
  939  | 
  940  |         console.log(`[UI-03] Jumlah kartu di Feed Kota: ${cardCount} (maks 10)`);
  941  | 
  942  |         // -------------------------------------------------------------------
  943  |         // LANGKAH 6: Verifikasi kontrol pagination muncul
  944  |         // -------------------------------------------------------------------
  945  |         // Karena ada 25 laporan dan 10 per halaman, harus ada 3 halaman.
  946  |         // renderPagination() (app.js baris 230) akan membuat navigasi halaman.
  947  |         const paginationContainer = page.locator('#paginationContainer');
  948  |         await expect(paginationContainer).toBeVisible();
  949  | 
  950  |         // Verifikasi ada tombol navigasi halaman (page numbers, prev, next)
  951  |         const paginationButtons = paginationContainer.locator('.page-item');
  952  |         const paginationCount = await paginationButtons.count();
  953  | 
  954  |         // Harus ada minimal 3 tombol: Sebelumnya, 1, 2, 3, Selanjutnya = 5 tombol
  955  |         expect(paginationCount).toBeGreaterThanOrEqual(3);
  956  | 
  957  |         console.log(`[UI-03] ✅ Pagination terverifikasi: ${cardCount} kartu, ${paginationCount} tombol navigasi`);
  958  |     });
  959  | 
  960  |     // =========================================================================
  961  |     // TEST CASE: UI-04
  962  |     // =========================================================================
  963  |     // JUDUL:
  964  |     //   Modal Dialog: Tombol "Buat Laporan Baru" membuka modal #reportModal
  965  |     //
  966  |     // SKENARIO:
  967  |     //   Login ke SPA, navigasi ke #dashboard, klik tombol #btnBukaModal,
  968  |     //   dan verifikasi bahwa modal Bootstrap #reportModal muncul (visible).
  969  |     //
  970  |     // REFERENSI KODE:
  971  |     //   - app.js baris 282-292: setupDashboardEvents() → pasang event listener
  972  |     //     btnBukaModal.addEventListener('click', function() {
  973  |     //         reportModalInstance.show();
  974  |     //     });
  975  |     //   - index.html baris 31: <div class="modal fade" id="reportModal">
  976  |     //
  977  |     // KONSEP TEKNIS:
  978  |     //   - Bootstrap Modal: overlay dialog yang dimunculkan dengan JS
  979  |     //   - Class 'show' ditambahkan ke modal saat ditampilkan
  980  |     //   - Modal instance dibuat dengan: new bootstrap.Modal(element)
  981  |     // =========================================================================
  982  |     test('UI-04: Klik tombol Buat Laporan → modal #reportModal muncul', async ({ page }) => {
  983  |         // -------------------------------------------------------------------
  984  |         // LANGKAH 1: Setup state login dan mock API
  985  |         // -------------------------------------------------------------------
  986  |         await page.goto(SPA_URL);
  987  | 
  988  |         // Hapus route interceptor sebelumnya
  989  |         await page.unroute('http://103.151.63.71:8013/api/**');
  990  | 
  991  |         // Mock semua API calls agar tidak gagal
  992  |         await page.route('**/api/**', async (route) => {
  993  |             // Untuk endpoint report, kembalikan data kosong
  994  |             await route.fulfill({
  995  |                 status: 200,
  996  |                 contentType: 'application/json',
  997  |                 body: JSON.stringify({ count: 0, results: [] })
  998  |             });
  999  |         });
  1000 | 
  1001 |         // Simpan token agar bisa akses dashboard
  1002 |         await setupAuthTokens(page, VALID_ACCESS_TOKEN, EXPIRED_REFRESH_TOKEN);
  1003 | 
  1004 |         // Handle dialog alert (jika muncul)
  1005 |         page.on('dialog', async (dialog) => await dialog.accept());
  1006 | 
  1007 |         // -------------------------------------------------------------------
  1008 |         // LANGKAH 2: Navigasi ke dashboard
  1009 |         // -------------------------------------------------------------------
  1010 |         await page.goto(`${SPA_URL}#dashboard`);
  1011 | 
  1012 |         // Tunggu tombol "Buat Laporan Baru" muncul
  1013 |         const btnBukaModal = page.locator('#btnBukaModal');
> 1014 |         await expect(btnBukaModal).toBeVisible({ timeout: 10000 });
       |                                    ^ Error: expect(locator).toBeVisible() failed
  1015 | 
  1016 |         // -------------------------------------------------------------------
  1017 |         // LANGKAH 3: Verifikasi modal belum terlihat sebelum diklik
  1018 |         // -------------------------------------------------------------------
  1019 |         const reportModal = page.locator('#reportModal');
  1020 | 
  1021 |         // Modal awalnya memiliki class "modal fade" (tanpa "show")
  1022 |         // Sehingga tidak terlihat oleh pengguna
  1023 |         await expect(reportModal).not.toBeVisible();
  1024 | 
  1025 |         // -------------------------------------------------------------------
  1026 |         // LANGKAH 4: Klik tombol "Buat Laporan Baru"
  1027 |         // -------------------------------------------------------------------
  1028 |         await btnBukaModal.click();
  1029 | 
  1030 |         // -------------------------------------------------------------------
  1031 |         // LANGKAH 5: Tunggu dan verifikasi modal muncul
  1032 |         // -------------------------------------------------------------------
  1033 |         // Bootstrap menambahkan class 'show' ke modal saat ditampilkan,
  1034 |         // dan mengubah style display dari 'none' ke 'block'.
  1035 |         //
  1036 |         // Kita gunakan toBeVisible() yang secara internal memeriksa apakah
  1037 |         // elemen memiliki ukuran > 0 dan tidak di-hidden.
  1038 |         //
  1039 |         await expect(reportModal).toBeVisible({ timeout: 5000 });
  1040 | 
  1041 |         // Verifikasi tambahan: cek class 'show' pada modal
  1042 |         const hasShowClass = await reportModal.evaluate(
  1043 |             (el) => el.classList.contains('show')
  1044 |         );
  1045 |         expect(hasShowClass).toBe(true);
  1046 | 
  1047 |         // -------------------------------------------------------------------
  1048 |         // LANGKAH 6: Verifikasi form dan elemen input ada di dalam modal
  1049 |         // -------------------------------------------------------------------
  1050 |         // Form laporan harus memiliki semua field yang diperlukan
  1051 |         await expect(page.locator('#reportForm')).toBeVisible();
  1052 |         await expect(page.locator('#inputTitle')).toBeVisible();
  1053 |         await expect(page.locator('#inputCategory')).toBeVisible();
  1054 |         await expect(page.locator('#inputLocation')).toBeVisible();
  1055 |         await expect(page.locator('#inputDescription')).toBeVisible();
  1056 |         await expect(page.locator('#btnDraft')).toBeVisible();
  1057 |         await expect(page.locator('#btnSubmit')).toBeVisible();
  1058 | 
  1059 |         // Verifikasi judul modal
  1060 |         const modalTitle = page.locator('#reportModalLabel');
  1061 |         await expect(modalTitle).toContainText('Buat Laporan Baru');
  1062 | 
  1063 |         console.log('[UI-04] ✅ Modal #reportModal berhasil dibuka dengan semua elemen form');
  1064 |     });
  1065 | 
  1066 |     // =========================================================================
  1067 |     // TEST CASE: UI-05
  1068 |     // =========================================================================
  1069 |     // JUDUL:
  1070 |     //   Form Submission: Simpan Draft laporan via modal form
  1071 |     //
  1072 |     // SKENARIO:
  1073 |     //   Login ke SPA, buka modal form, isi semua field, klik "Simpan Draft",
  1074 |     //   dan verifikasi:
  1075 |     //   1. Modal tertutup setelah submit berhasil
  1076 |     //   2. Notifikasi sukses muncul (alert)
  1077 |     //   3. Badge count Draf di #summaryStats terupdate
  1078 |     //
  1079 |     // REFERENSI KODE:
  1080 |     //   app.js baris 347-412: setupReportForm()
  1081 |     //   - btnDraft → kirimLaporan('DRAFT')
  1082 |     //   - Jika response.status 200/201 → reportModalInstance.hide(), alert, loadDashboardData()
  1083 |     //   - loadDashboardData() memanggil loadSummaryStats() → update badge
  1084 |     // =========================================================================
  1085 |     test('UI-05: Isi form dan simpan draft → modal tutup, notifikasi muncul', async ({ page }) => {
  1086 |         // -------------------------------------------------------------------
  1087 |         // LANGKAH 1: Setup environment
  1088 |         // -------------------------------------------------------------------
  1089 |         await page.goto(SPA_URL);
  1090 |         await page.unroute('http://103.151.63.71:8013/api/**');
  1091 | 
  1092 |         // Variabel untuk tracking apakah POST draft berhasil
  1093 |         let draftSubmitted = false;
  1094 | 
  1095 |         // Mock API endpoint dengan respons yang sesuai
  1096 |         await page.route('**/api/report/**', async (route) => {
  1097 |             const method = route.request().method();
  1098 |             const url = route.request().url();
  1099 | 
  1100 |             if (method === 'POST') {
  1101 |                 // -----------------------------------------------------------
  1102 |                 // Mock untuk POST /api/report/ (membuat laporan baru)
  1103 |                 // -----------------------------------------------------------
  1104 |                 draftSubmitted = true;
  1105 | 
  1106 |                 // Ambil data dari request body untuk verifikasi
  1107 |                 const postData = route.request().postDataJSON();
  1108 |                 console.log(`[UI-05] POST received: ${JSON.stringify(postData)}`);
  1109 | 
  1110 |                 await route.fulfill({
  1111 |                     status: 201, // 201 Created
  1112 |                     contentType: 'application/json',
  1113 |                     body: JSON.stringify({
  1114 |                         id: 99,
```