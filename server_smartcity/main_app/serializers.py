from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    # Menyembunyikan nama asli pelapor (dari lab sebelumnya)
    reporter = serializers.SerializerMethodField()
    
    # Field untuk mengecek kepemilikan laporan
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = [
            'id', 'title', 'category', 'description', 
            'location', 'status', 'reporter', 
            'created_at', 'updated_at', 'is_owner' # Pastikan is_owner dimasukkan ke dalam fields
        ]

    def get_reporter(self, obj):
        return "Warga Anonim"

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request and request.user and request.user.is_authenticated:
            # Mengembalikan True jika user yang request sama dengan user pelapor di database
            return obj.reporter == request.user
        return False