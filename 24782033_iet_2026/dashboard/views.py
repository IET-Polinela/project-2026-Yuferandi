from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db.models import Count
from main_app.models import Report

class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

def get_dashboard_data(request):
    # 1. Agregasi Status Laporan
    status_distribution = list(Report.objects.values('status').annotate(total=Count('id')))
    
    # 2. Agregasi Kategori Laporan
    category_distribution = list(Report.objects.values('category').annotate(total=Count('id')))
    
    # 3. Ambil 5 Laporan Terbaru & 5 Laporan Selesai
    latest_reported = list(Report.objects.filter(status='REPORTED').order_by('-created_at')[:5].values('title', 'status', 'created_at'))
    latest_resolved = list(Report.objects.filter(status='RESOLVED').order_by('-created_at')[:5].values('title', 'status', 'created_at'))
    
    return JsonResponse({
        'status_data': status_distribution,
        'category_data': category_distribution,
        'latest_reported': latest_reported,
        'latest_resolved': latest_resolved
    })