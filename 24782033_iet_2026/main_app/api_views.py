from rest_framework import viewsets, permissions
from django.db.models import Q
from .models import Report
from .serializers import ReportSerializer
from .permissions import SmartCityRolePermission

class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer

    def get_permissions(self):
        # Gunakan aturan SmartCityRolePermission khusus untuk aksi ubah/hapus
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), SmartCityRolePermission()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        # Otomatis mengisi pelapor dengan user yang sedang login
        serializer.save(reporter=self.request.user)

    def get_queryset(self):
        user = self.request.user
        
        # Admin bisa melihat seluruh laporan
        if user.is_staff:
            return Report.objects.all()
        
        # Citizen melihat SEMUA laporan (kecuali DRAFT), ditambah DRAFT miliknya sendiri
        return Report.objects.filter(
            Q(status__in=['REPORTED', 'VERIFIED', 'IN_PROGRESS', 'RESOLVED']) | 
            Q(reporter=user)
        )

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