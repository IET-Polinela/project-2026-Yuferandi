import random
from django.core.management.base import BaseCommand
from faker import Faker
from main_app.models import Report 

# Locale tetap Indo biar nama jalan tambahannya masih familiar
fake = Faker('id_ID')

class Command(BaseCommand):
    help = 'Bikin data laporan fiktif buat Kota Axel (Edisi Konosuba)'

    def add_arguments(self, parser):
        parser.add_argument('num_records', type=int, help='Mau bikin berapa data?')

    def handle(self, *args, **kwargs):
        num_records = kwargs['num_records']
        
        # Daftar masalah yang sering muncul di dunia Konosuba
        context_data = {
            'Gangguan Monster': {
                'titles': ['Serangan Kubis Liar', 'Katak Raksasa Dekat Gerbang', 'Gerombolan Hawks Berisik', 'Gritter Bell di Pemukiman'],
                'desc': 'Monster muncul dan bikin warga panik. Tolong kirim Adventurer yang beneran jago buat beresin ini.'
            },
            'Sihir & Ledakan': {
                'titles': ['Ledakan Misterius di Kastil Tua', 'Hujan Salju di Musim Panas', 'Lingkaran Sihir Aneh', 'Efek Samping Sihir Pertukaran'],
                'desc': 'Ada suara ledakan gede tiap hari di jam yang sama. Curiga ada penyihir aneh yang lagi latihan di sana.'
            },
            'Fasilitas Publik': {
                'titles': ['Gerbang Kota Axel Rusak', 'Papan Misi Guild Berdebu', 'Air Pancuran Kota Keruh', 'Kandang Kuda Penginapan Bau'],
                'desc': 'Fasilitas umum mulai gak terawat. Air pancuran yang biasanya jernih sekarang malah kotor, perlu dibersihin.'
            },
            'Gangguan Kultus': {
                'titles': ['Kultus Axis Maksa Warga', 'Anggota Kultus Eris Kurang Dana', 'Debat Kusir di Alun-alun', 'Pendaftaran Agama Berkedok Penipuan'],
                'desc': 'Warga risih dipaksa daftar organisasi (Kultus Axis). Mohon administrasi kota kasih teguran keras.'
            },
            'Keamanan': {
                'titles': ['Pencurian di kota (Steal)', 'Adventurer Kabur Belum Bayar Bir', 'Vandalisme di Toko Wiz', 'Gangguan Roh Gentayangan'],
                'desc': 'Laporan kriminal di area pasar. Pelakunya kalau nggak punya skill Steal tinggi, ya paling lagi mabok berat.'
            }
        }

        # Lokasi ikonik biar Axel City-nya berasa
        axel_locations = [
            'Gerbang Utama Kota Axel',
            'Alun-alun Kota (Dekat Air Pancuran)',
            'Markas Besar Adventurer Guild',
            'Toko Item Sihir Wiz',
            'Penginapan Kuda Terbang',
            'Kastil Tua di Pinggiran Kota',
            'Area Pertanian (Ladang Kubis)',
            'Distrik Perbelanjaan Axel',
            'Kandang Kuda Pemukiman Pemula',
            'Sungai di Luar Dinding Kota',
            'Gereja Kultus Axis',
            'Gereja Kultus Eris'
        ]
        
        status_choices = ['REPORTED', 'VERIFIED', 'IN_PROGRESS', 'RESOLVED']
        
        count = 0
        for _ in range(num_records):
            # Acak kategori dan lokasinya
            category = random.choice(list(context_data.keys()))
            title_template = random.choice(context_data[category]['titles'])
            description_base = context_data[category]['desc']
            fantasy_spot = random.choice(axel_locations)
            
            # Eksekusi insert ke database
            Report.objects.create(
                title=f"{title_template} ({fantasy_spot})",
                category=category,
                # Deskripsi campur antara tema Konosuba sama detail random dari Faker
                description=f"{description_base} Kejadiannya di sekitar {fantasy_spot}. Detail lokasi: {fake.street_name()}.",
                location=f"{fantasy_spot}, Kota Axel",
                status=random.choice(status_choices),
            )
            count += 1
            
        self.stdout.write(self.style.SUCCESS(f'Mantap! {count} laporan Konosuba berhasil masuk ke database.'))