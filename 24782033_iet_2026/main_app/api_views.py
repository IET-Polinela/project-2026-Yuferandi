from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from .models import Report
from .serializers import ReportSerializer
from .permissions import SmartCityRolePermission

# Kelas Paginasi
class ReportPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    pagination_class = ReportPagination

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), SmartCityRolePermission()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        # Otomatis mengisi pelapor dengan user yang sedang login
        serializer.save(reporter=self.request.user)

    def get_queryset(self):
        user = self.request.user
        
        # Tambahan Lab 12: Mekanisme sorting berdasarkan tanggal pembaruan terkini
        queryset = Report.objects.all().order_by('-updated_at')
        
        # Sesuai aturan layar: Admin melihat semua laporan kecuali DRAFT
        if user.is_staff:
            return queryset.exclude(status='DRAFT')
        
        # Tambahan Lab 12: Mekanisme filtering berdasarkan jenis tab dari parameter URL
        tab = self.request.query_params.get('tab', None)
        
        if tab == 'my_reports':
            # Tab "Laporan Saya": Hanya tampilkan milik user
            queryset = queryset.filter(reporter=user)
        elif tab == 'feed':
            # Tab "Feed Kota": Tampilkan milik orang lain yang BUKAN DRAFT
            queryset = queryset.filter(~Q(reporter=user) & ~Q(status='DRAFT'))
        else:
            # Default: Citizen melihat laporan publik (selain DRAFT) + DRAFT miliknya sendiri
            queryset = queryset.filter(
                ~Q(status='DRAFT') | Q(reporter=user, status='DRAFT')
            )

        return queryset

    def perform_update(self, serializer):
        if self.request.user.is_staff:
            # Cegah Admin ubah isi laporan, timpa kembali dengan data aslinya
            instance = self.get_object()
            serializer.save(
                title=instance.title,
                category=instance.category,
                description=instance.description,
                location=instance.location
            )
        else:
            serializer.save()