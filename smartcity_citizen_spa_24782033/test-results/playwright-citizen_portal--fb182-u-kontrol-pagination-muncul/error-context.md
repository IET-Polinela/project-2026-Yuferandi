# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: playwright\citizen_portal.spec.js >> Modul 5: Interaktivitas UI (UI-01 through UI-06) >> UI-03: Pagination Feed Kota — maks 10 kartu, kontrol pagination muncul
- Location: playwright\citizen_portal.spec.js:834:5

# Error details

```
TimeoutError: page.waitForSelector: Timeout 10000ms exceeded.
Call log:
  - waiting for locator('#btnBukaModal') to be visible

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
            - generic [ref=e21]: "2"
          - generic [ref=e22]:
            - generic [ref=e23]:
              - generic [ref=e24]: 
              - text: "Verified:"
            - generic [ref=e25]: "3"
          - generic [ref=e26]:
            - generic [ref=e27]:
              - generic [ref=e28]: 
              - text: "In Progress:"
            - generic [ref=e29]: "3"
          - generic [ref=e30]:
            - generic [ref=e31]:
              - generic [ref=e32]: 
              - text: "Resolved:"
            - generic [ref=e33]: "2"
      - generic [ref=e34]:
        - list [ref=e35]:
          - listitem [ref=e36]:
            - button "Laporan Saya" [ref=e37] [cursor=pointer]
          - listitem [ref=e38]:
            - button "Feed Kota" [ref=e39] [cursor=pointer]
        - generic [ref=e40]:
          - generic [ref=e42]:
            - generic [ref=e43]:
              - generic [ref=e44]: VERIFIED
              - generic [ref=e45]: 7/3/2026
            - 'heading "Laporan Test #1" [level=5] [ref=e46]'
            - heading " Lokasi Test 1" [level=6] [ref=e47]:
              - generic [ref=e48]: 
              - text: Lokasi Test 1
            - paragraph [ref=e49]: Deskripsi laporan pengujian nomor 1
            - generic [ref=e50]:
              - generic [ref=e51]:
                - generic [ref=e52]: Status Penanganan
                - generic [ref=e53]: 60%
              - progressbar [ref=e55]
            - generic [ref=e57]:
              - generic [ref=e58]: 
              - text: undefined
          - generic [ref=e60]:
            - generic [ref=e61]:
              - generic [ref=e62]: IN_PROGRESS
              - generic [ref=e63]: 7/3/2026
            - 'heading "Laporan Test #2" [level=5] [ref=e64]'
            - heading " Lokasi Test 2" [level=6] [ref=e65]:
              - generic [ref=e66]: 
              - text: Lokasi Test 2
            - paragraph [ref=e67]: Deskripsi laporan pengujian nomor 2
            - generic [ref=e68]:
              - generic [ref=e69]:
                - generic [ref=e70]: Status Penanganan
                - generic [ref=e71]: 80%
              - progressbar [ref=e73]
            - generic [ref=e75]:
              - generic [ref=e76]: 
              - text: undefined
          - generic [ref=e78]:
            - generic [ref=e79]:
              - generic [ref=e80]: RESOLVED
              - generic [ref=e81]: 7/3/2026
            - 'heading "Laporan Test #3" [level=5] [ref=e82]'
            - heading " Lokasi Test 3" [level=6] [ref=e83]:
              - generic [ref=e84]: 
              - text: Lokasi Test 3
            - paragraph [ref=e85]: Deskripsi laporan pengujian nomor 3
            - generic [ref=e86]:
              - generic [ref=e87]:
                - generic [ref=e88]: Status Penanganan
                - generic [ref=e89]: 100%
              - progressbar [ref=e91]
            - generic [ref=e93]:
              - generic [ref=e94]: 
              - text: undefined
          - generic [ref=e96]:
            - generic [ref=e97]:
              - generic [ref=e98]: REPORTED
              - generic [ref=e99]: 7/3/2026
            - 'heading "Laporan Test #4" [level=5] [ref=e100]'
            - heading " Lokasi Test 4" [level=6] [ref=e101]:
              - generic [ref=e102]: 
              - text: Lokasi Test 4
            - paragraph [ref=e103]: Deskripsi laporan pengujian nomor 4
            - generic [ref=e104]:
              - generic [ref=e105]:
                - generic [ref=e106]: Status Penanganan
                - generic [ref=e107]: 40%
              - progressbar [ref=e109]
            - generic [ref=e111]:
              - generic [ref=e112]: 
              - text: undefined
          - generic [ref=e114]:
            - generic [ref=e115]:
              - generic [ref=e116]: VERIFIED
              - generic [ref=e117]: 7/3/2026
            - 'heading "Laporan Test #5" [level=5] [ref=e118]'
            - heading " Lokasi Test 5" [level=6] [ref=e119]:
              - generic [ref=e120]: 
              - text: Lokasi Test 5
            - paragraph [ref=e121]: Deskripsi laporan pengujian nomor 5
            - generic [ref=e122]:
              - generic [ref=e123]:
                - generic [ref=e124]: Status Penanganan
                - generic [ref=e125]: 60%
              - progressbar [ref=e127]
            - generic [ref=e129]:
              - generic [ref=e130]: 
              - text: undefined
          - generic [ref=e132]:
            - generic [ref=e133]:
              - generic [ref=e134]: IN_PROGRESS
              - generic [ref=e135]: 7/3/2026
            - 'heading "Laporan Test #6" [level=5] [ref=e136]'
            - heading " Lokasi Test 6" [level=6] [ref=e137]:
              - generic [ref=e138]: 
              - text: Lokasi Test 6
            - paragraph [ref=e139]: Deskripsi laporan pengujian nomor 6
            - generic [ref=e140]:
              - generic [ref=e141]:
                - generic [ref=e142]: Status Penanganan
                - generic [ref=e143]: 80%
              - progressbar [ref=e145]
            - generic [ref=e147]:
              - generic [ref=e148]: 
              - text: undefined
          - generic [ref=e150]:
            - generic [ref=e151]:
              - generic [ref=e152]: RESOLVED
              - generic [ref=e153]: 7/3/2026
            - 'heading "Laporan Test #7" [level=5] [ref=e154]'
            - heading " Lokasi Test 7" [level=6] [ref=e155]:
              - generic [ref=e156]: 
              - text: Lokasi Test 7
            - paragraph [ref=e157]: Deskripsi laporan pengujian nomor 7
            - generic [ref=e158]:
              - generic [ref=e159]:
                - generic [ref=e160]: Status Penanganan
                - generic [ref=e161]: 100%
              - progressbar [ref=e163]
            - generic [ref=e165]:
              - generic [ref=e166]: 
              - text: undefined
          - generic [ref=e168]:
            - generic [ref=e169]:
              - generic [ref=e170]: REPORTED
              - generic [ref=e171]: 7/3/2026
            - 'heading "Laporan Test #8" [level=5] [ref=e172]'
            - heading " Lokasi Test 8" [level=6] [ref=e173]:
              - generic [ref=e174]: 
              - text: Lokasi Test 8
            - paragraph [ref=e175]: Deskripsi laporan pengujian nomor 8
            - generic [ref=e176]:
              - generic [ref=e177]:
                - generic [ref=e178]: Status Penanganan
                - generic [ref=e179]: 40%
              - progressbar [ref=e181]
            - generic [ref=e183]:
              - generic [ref=e184]: 
              - text: undefined
          - generic [ref=e186]:
            - generic [ref=e187]:
              - generic [ref=e188]: VERIFIED
              - generic [ref=e189]: 7/3/2026
            - 'heading "Laporan Test #9" [level=5] [ref=e190]'
            - heading " Lokasi Test 9" [level=6] [ref=e191]:
              - generic [ref=e192]: 
              - text: Lokasi Test 9
            - paragraph [ref=e193]: Deskripsi laporan pengujian nomor 9
            - generic [ref=e194]:
              - generic [ref=e195]:
                - generic [ref=e196]: Status Penanganan
                - generic [ref=e197]: 60%
              - progressbar [ref=e199]
            - generic [ref=e201]:
              - generic [ref=e202]: 
              - text: undefined
          - generic [ref=e204]:
            - generic [ref=e205]:
              - generic [ref=e206]: IN_PROGRESS
              - generic [ref=e207]: 7/3/2026
            - 'heading "Laporan Test #10" [level=5] [ref=e208]'
            - heading " Lokasi Test 10" [level=6] [ref=e209]:
              - generic [ref=e210]: 
              - text: Lokasi Test 10
            - paragraph [ref=e211]: Deskripsi laporan pengujian nomor 10
            - generic [ref=e212]:
              - generic [ref=e213]:
                - generic [ref=e214]: Status Penanganan
                - generic [ref=e215]: 80%
              - progressbar [ref=e217]
            - generic [ref=e219]:
              - generic [ref=e220]: 
              - text: undefined
        - navigation [ref=e222]:
          - list [ref=e223]:
            - listitem [ref=e224]:
              - button "«"
            - listitem [ref=e225]:
              - button "1" [ref=e226] [cursor=pointer]
            - listitem [ref=e227]:
              - button "2" [ref=e228] [cursor=pointer]
            - listitem [ref=e229]:
              - button "3" [ref=e230] [cursor=pointer]
            - listitem [ref=e231]:
              - button "»" [ref=e232] [cursor=pointer]
      - complementary [ref=e233]:
        - generic [ref=e234]:
          - heading " Pengumuman" [level=6] [ref=e235]:
            - generic [ref=e236]: 
            - text: Pengumuman
          - paragraph [ref=e237]: Gunakan portal ini untuk melaporkan masalah infrastruktur dan layanan kota secara langsung.
  - text:  
```

# Test source

```ts
  812  |     // =========================================================================
  813  |     // TEST CASE: UI-03
  814  |     // =========================================================================
  815  |     // JUDUL:
  816  |     //   Pagination: Daftar laporan publik (Feed Kota) dibatasi maks 10 item
  817  |     //
  818  |     // SKENARIO:
  819  |     //   Dengan asumsi ada 25+ laporan di database, navigasi ke SPA #dashboard,
  820  |     //   klik tab "Feed Kota (Publik)", hitung jumlah kartu laporan di
  821  |     //   #listContainer, dan pastikan tidak lebih dari 10. Juga verifikasi
  822  |     //   bahwa kontrol pagination ada di #paginationContainer.
  823  |     //
  824  |     // KONSEP TEKNIS:
  825  |     //   - Pagination server-side: API mengembalikan data terpaginasi
  826  |     //   - app.js menggunakan page_size=10 sebagai default
  827  |     //   - totalPages dihitung dari: Math.ceil(count / 10)
  828  |     //
  829  |     // REFERENSI KODE:
  830  |     //   app.js baris 64: const response = await requestAPI(`/report/?tab=${tab}&page=${page}`)
  831  |     //   app.js baris 69: totalPages = Math.ceil(count / 10) || 1;
  832  |     //   app.js baris 230-264: renderPagination() → membuat navigasi halaman
  833  |     // =========================================================================
  834  |     test('UI-03: Pagination Feed Kota — maks 10 kartu, kontrol pagination muncul', async ({ page }) => {
  835  |         // -------------------------------------------------------------------
  836  |         // LANGKAH 1: Siapkan environment (navigasi ke SPA dan setup mock)
  837  |         // -------------------------------------------------------------------
  838  |         await page.goto(SPA_URL);
  839  |         await mockSPAApiUrl(page);
  840  | 
  841  |         // -------------------------------------------------------------------
  842  |         // LANGKAH 2: Simulasi login dengan menyimpan token
  843  |         // -------------------------------------------------------------------
  844  |         // Untuk test ini, kita perlu berada dalam state "login" agar bisa
  845  |         // mengakses dashboard. Kita gunakan mock API untuk token dan data.
  846  |         // -------------------------------------------------------------------
  847  | 
  848  |         // Hapus route interceptor sebelumnya
  849  |         await page.unroute('http://103.151.63.71:8013/api/**');
  850  | 
  851  |         // Buat data mock: 25 laporan dummy untuk simulasi pagination
  852  |         const mockReports = [];
  853  |         for (let i = 1; i <= 25; i++) {
  854  |             mockReports.push({
  855  |                 id: i,
  856  |                 title: `Laporan Test #${i}`,
  857  |                 description: `Deskripsi laporan pengujian nomor ${i}`,
  858  |                 category: i % 2 === 0 ? 'Infrastruktur' : 'Kebersihan',
  859  |                 location: `Lokasi Test ${i}`,
  860  |                 status: ['REPORTED', 'VERIFIED', 'IN_PROGRESS', 'RESOLVED'][i % 4],
  861  |                 reporter_name: 'testwarga',
  862  |                 is_owner: false,
  863  |                 updated_at: new Date().toISOString()
  864  |             });
  865  |         }
  866  | 
  867  |         // Mock API endpoint untuk report list (feed tab, halaman 1)
  868  |         await page.route('**/api/report/**', async (route) => {
  869  |             const url = route.request().url();
  870  | 
  871  |             if (url.includes('tab=feed') || url.includes('tab=my_reports')) {
  872  |                 // Ambil nomor halaman dari URL (default: 1)
  873  |                 const pageMatch = url.match(/page=(\d+)/);
  874  |                 const pageNum = pageMatch ? parseInt(pageMatch[1]) : 1;
  875  | 
  876  |                 // Hitung subset data untuk halaman ini (10 per halaman)
  877  |                 const pageSize = 10;
  878  |                 const startIdx = (pageNum - 1) * pageSize;
  879  |                 const endIdx = startIdx + pageSize;
  880  |                 const pageData = mockReports.slice(startIdx, endIdx);
  881  | 
  882  |                 await route.fulfill({
  883  |                     status: 200,
  884  |                     contentType: 'application/json',
  885  |                     body: JSON.stringify({
  886  |                         count: mockReports.length,   // Total: 25
  887  |                         results: pageData,            // 10 per halaman
  888  |                         next: endIdx < mockReports.length ? 'next_page_url' : null,
  889  |                         previous: pageNum > 1 ? 'prev_page_url' : null
  890  |                     })
  891  |                 });
  892  |             } else {
  893  |                 // Untuk endpoint lain, kembalikan respons kosong
  894  |                 await route.fulfill({
  895  |                     status: 200,
  896  |                     contentType: 'application/json',
  897  |                     body: JSON.stringify({ count: 0, results: [] })
  898  |                 });
  899  |             }
  900  |         });
  901  | 
  902  |         // Simpan token valid ke localStorage agar bisa akses dashboard
  903  |         await setupAuthTokens(page, VALID_ACCESS_TOKEN, EXPIRED_REFRESH_TOKEN);
  904  | 
  905  |         // Handle alert dialog (jika muncul)
  906  |         page.on('dialog', async (dialog) => await dialog.accept());
  907  | 
  908  |         // -------------------------------------------------------------------
  909  |         // LANGKAH 3: Navigasi ke dashboard
  910  |         // -------------------------------------------------------------------
  911  |         await page.goto(`${SPA_URL}#dashboard`);
> 912  |         await page.waitForSelector('#btnBukaModal', { state: 'visible', timeout: 10000 });
       |                    ^ TimeoutError: page.waitForSelector: Timeout 10000ms exceeded.
  913  | 
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
```