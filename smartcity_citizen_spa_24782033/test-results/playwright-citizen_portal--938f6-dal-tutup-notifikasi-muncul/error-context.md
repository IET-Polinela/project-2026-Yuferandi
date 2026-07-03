# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: playwright\citizen_portal.spec.js >> Modul 5: Interaktivitas UI (UI-01 through UI-06) >> UI-05: Isi form dan simpan draft → modal tutup, notifikasi muncul
- Location: playwright\citizen_portal.spec.js:1085:5

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
            - generic [ref=e17]: "1"
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
          - generic [ref=e42]: 
          - heading "Belum ada laporan" [level=5] [ref=e43]
        - navigation [ref=e45]:
          - list [ref=e46]:
            - listitem [ref=e47]:
              - button "«"
            - listitem [ref=e48]:
              - button "1" [ref=e49] [cursor=pointer]
            - listitem [ref=e50]:
              - button "»"
      - complementary [ref=e51]:
        - generic [ref=e52]:
          - heading " Pengumuman" [level=6] [ref=e53]:
            - generic [ref=e54]: 
            - text: Pengumuman
          - paragraph [ref=e55]: Gunakan portal ini untuk melaporkan masalah infrastruktur dan layanan kota secara langsung.
  - text:  
```

# Test source

```ts
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
  1115 |                         title: postData?.title || 'Test Draft',
  1116 |                         category: postData?.category || 'Infrastruktur',
  1117 |                         location: postData?.location || 'Test Location',
  1118 |                         description: postData?.description || 'Test Description',
  1119 |                         status: 'DRAFT',
  1120 |                         reporter_name: 'testwarga',
  1121 |                         is_owner: true
  1122 |                     })
  1123 |                 });
  1124 |             } else if (method === 'GET' && url.includes('page_size=1000')) {
  1125 |                 // -----------------------------------------------------------
  1126 |                 // Mock untuk GET /api/report/?tab=my_reports&page_size=1000
  1127 |                 // (digunakan oleh loadSummaryStats() untuk menghitung badge)
  1128 |                 //
  1129 |                 // -----------------------------------------------------------
  1130 |                 await route.fulfill({
  1131 |                     status: 200,
  1132 |                     contentType: 'application/json',
  1133 |                     body: JSON.stringify({
  1134 |                         count: 1,
  1135 |                         results: [{
  1136 |                             id: 99,
  1137 |                             title: 'Test Draft',
  1138 |                             status: 'DRAFT',
  1139 |                             category: 'Infrastruktur',
  1140 |                             location: 'Gedung Lab',
  1141 |                             description: 'Deskripsi test',
  1142 |                             reporter_name: 'testwarga',
  1143 |                             is_owner: true
  1144 |                         }]
  1145 |                     })
  1146 |                 });
  1147 |             } else {
  1148 |                 // Mock default: kembalikan list kosong
  1149 |                 await route.fulfill({
  1150 |                     status: 200,
  1151 |                     contentType: 'application/json',
  1152 |                     body: JSON.stringify({ count: 0, results: [] })
  1153 |                 });
  1154 |             }
  1155 |         });
  1156 | 
  1157 |         // Setup token
  1158 |         await setupAuthTokens(page, VALID_ACCESS_TOKEN, EXPIRED_REFRESH_TOKEN);
  1159 | 
  1160 |         // -------------------------------------------------------------------
  1161 |         // LANGKAH 2: Handle dialog alert
  1162 |         // -------------------------------------------------------------------
  1163 |         // app.js menampilkan alert setelah berhasil simpan draft:
  1164 |         //   alert('Laporan berhasil disimpan sebagai DRAFT')
  1165 |         //
  1166 |         let alertMessage = '';
  1167 |         page.on('dialog', async (dialog) => {
  1168 |             alertMessage = dialog.message();
  1169 |             console.log(`[UI-05] Alert: "${alertMessage}"`);
  1170 |             await dialog.accept();
  1171 |         });
  1172 | 
  1173 |         // -------------------------------------------------------------------
  1174 |         // LANGKAH 3: Navigasi ke dashboard dan buka modal
  1175 |         // -------------------------------------------------------------------
  1176 |         await page.goto(`${SPA_URL}#dashboard`);
> 1177 |         await page.waitForSelector('#btnBukaModal', { state: 'visible', timeout: 10000 });
       |                    ^ TimeoutError: page.waitForSelector: Timeout 10000ms exceeded.
  1178 | 
  1179 |         // Klik tombol buka modal
  1180 |         await page.locator('#btnBukaModal').click();
  1181 | 
  1182 |         // Tunggu modal muncul
  1183 |         await expect(page.locator('#reportModal')).toBeVisible({ timeout: 5000 });
  1184 | 
  1185 |         // -------------------------------------------------------------------
  1186 |         // LANGKAH 4: Isi form laporan dengan data test
  1187 |         // -------------------------------------------------------------------
  1188 |         // Mengisi setiap field form satu per satu
  1189 | 
  1190 |         // 4a. Judul Laporan / Report Title
  1191 |         await page.locator('#inputTitle').fill('AC Mati di Lab CPS 1');
  1192 | 
  1193 |         // 4b. Kategori / Category
  1194 |         //     Ini adalah <select>, kita gunakan selectOption() bukan fill()
  1195 |         await page.locator('#inputCategory').selectOption('Infrastruktur');
  1196 | 
  1197 |         // 4c. Lokasi Kejadian / Incident Location
  1198 |         await page.locator('#inputLocation').fill('Gedung Lab Analisis, Lantai 2');
  1199 | 
  1200 |         // 4d. Deskripsi / Description
  1201 |         //     Ini adalah <textarea>, fill() juga bisa digunakan
  1202 |         await page.locator('#inputDescription').fill(
  1203 |             'Unit AC di ruang Lab CPS 1 tidak berfungsi sejak tadi pagi. ' +
  1204 |             'Suhu ruangan sangat panas dan mengganggu kegiatan praktikum.'
  1205 |         );
  1206 | 
  1207 |         // -------------------------------------------------------------------
  1208 |         // LANGKAH 5: Klik tombol "Simpan Draft" (#btnDraft)
  1209 |         // -------------------------------------------------------------------
  1210 |         // Tombol ini akan memanggil kirimLaporan('DRAFT') di app.js
  1211 |         await page.locator('#btnDraft').click();
  1212 | 
  1213 |         // Tunggu proses POST selesai dan modal menutup
  1214 |         await page.waitForTimeout(2000);
  1215 | 
  1216 |         // -------------------------------------------------------------------
  1217 |         // LANGKAH 6: Verifikasi modal tertutup setelah submit berhasil
  1218 |         // -------------------------------------------------------------------
  1219 |         // Setelah berhasil, app.js memanggil reportModalInstance.hide()
  1220 |         const reportModal = page.locator('#reportModal');
  1221 |         await expect(reportModal).not.toBeVisible({ timeout: 5000 });
  1222 | 
  1223 |         // -------------------------------------------------------------------
  1224 |         // LANGKAH 7: Verifikasi notifikasi sukses muncul
  1225 |         // -------------------------------------------------------------------
  1226 |         // Kita sudah menangkap alert message di event handler di atas
  1227 |         //
  1228 |         // app.js baris 387: alert('Laporan berhasil disimpan sebagai DRAFT')
  1229 |         expect(alertMessage).toContain('berhasil');
  1230 | 
  1231 |         // -------------------------------------------------------------------
  1232 |         // LANGKAH 8: Verifikasi badge Draf di summaryStats terupdate
  1233 |         // -------------------------------------------------------------------
  1234 |         // Setelah simpan berhasil, loadDashboardData() dipanggil yang
  1235 |         // memanggil loadSummaryStats(). Badge Draf harus menunjukkan angka > 0.
  1236 |         //
  1237 |         await page.waitForTimeout(2000);
  1238 | 
  1239 |         const summaryStats = page.locator('#summaryStats');
  1240 |         await expect(summaryStats).toBeVisible();
  1241 | 
  1242 |         // Cek bahwa ada setidaknya satu badge yang menunjukkan angka > 0
  1243 |         // Badge Draf adalah badge pertama di summaryStats
  1244 |         const draftBadge = summaryStats.locator('.badge.bg-secondary').first();
  1245 |         const draftCountText = await draftBadge.textContent();
  1246 |         const draftCount = parseInt(draftCountText, 10);
  1247 | 
  1248 |         expect(draftCount).toBeGreaterThanOrEqual(1);
  1249 | 
  1250 |         console.log(`[UI-05] ✅ Draft tersimpan: modal tutup, alert muncul, badge Draf = ${draftCount}`);
  1251 |     });
  1252 | 
  1253 |     // =========================================================================
  1254 |     // TEST CASE: UI-06
  1255 |     // =========================================================================
  1256 |     // JUDUL:
  1257 |     //   Responsive Design: Navbar collapse pada viewport mobile
  1258 |     //
  1259 |     // SKENARIO:
  1260 |     //   Set viewport ke ukuran mobile (400x800), muat halaman SPA, dan
  1261 |     //   verifikasi bahwa navbar dalam keadaan collapsed (tombol toggler
  1262 |     //   terlihat, atau menu collapse tidak ditampilkan secara default).
  1263 |     //
  1264 |     // KONSEP TEKNIS:
  1265 |     //   - Bootstrap Responsive Navbar:
  1266 |     //     - navbar-expand-lg: collapse di bawah breakpoint lg (992px)
  1267 |     //     - navbar-toggler: tombol hamburger yang muncul saat collapsed
  1268 |     //     - collapse navbar-collapse: div yang di-toggle show/hide
  1269 |     //
  1270 |     // REFERENSI KODE:
  1271 |     //   index.html baris 16-23:
  1272 |     //     <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  1273 |     //       ...
  1274 |     //       <div id="nav-menus" class="ms-auto">
  1275 |     //
  1276 |     //   CATATAN: Navbar SPA ini menggunakan struktur sederhana tanpa
  1277 |     //   Bootstrap collapse standard (tidak ada .navbar-collapse).
```