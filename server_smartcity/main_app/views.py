from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Report
from .serializers import ReportSerializer

# ROLE HELPER (Memastikan penggunaan is_staff bawaan Django)
def is_admin(user):
    return user.is_authenticated and user.is_staff

class HomeView(TemplateView):
    template_name = 'main_app/home.html'

# LIST (LOGIN REQUIRED) - INI YANG MENGHILANGKAN DRAFT DARI LAYAR ADMIN
class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'main_app/report_list.html'
    context_object_name = 'reports'
    login_url = '/auth/login/'

    def get_queryset(self):
        user = self.request.user
        # Sesuai Aturan: Admin Exclude DRAFT
        if is_admin(user):
            return Report.objects.exclude(status='DRAFT').order_by('-created_at')
        
        # Sesuai Aturan: Citizen = Publik + DRAFT miliknya sendiri
        return Report.objects.filter(
            ~Q(status='DRAFT') | Q(reporter=user, status='DRAFT')
        ).order_by('-created_at')

# CREATE (CITIZEN ONLY)
class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    fields = ['title', 'category', 'location', 'description']
    template_name = 'main_app/report_form.html'
    success_url = reverse_lazy('report_list')

    def dispatch(self, request, *args, **kwargs):
        if is_admin(request.user):
            messages.error(request, "Akses ditolak! Admin tidak diizinkan membuat laporan baru.")
            return redirect('report_list')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        form.instance.status = 'DRAFT'
        return super().form_valid(form)

# UPDATE (CITIZEN ONLY)
class ReportUpdateView(LoginRequiredMixin, UpdateView):
    model = Report
    fields = ['title', 'category', 'location', 'description']
    template_name = 'main_app/report_form.html'
    success_url = reverse_lazy('report_list')

    def dispatch(self, request, *args, **kwargs):
        report = self.get_object()
        # Admin dilarang mengedit teks (hanya boleh via update status)
        if is_admin(request.user):
            messages.error(request, "Akses ditolak! Admin hanya diperbolehkan mengubah status laporan.")
            return redirect('report_list')
        # Citizen hanya boleh edit miliknya saat masih DRAFT
        if report.reporter != request.user or report.status != 'DRAFT':
            messages.error(request, "Akses ditolak! Anda hanya bisa mengedit DRAFT milik Anda sendiri.")
            return redirect('report_list')
            
        return super().dispatch(request, *args, **kwargs)

# DELETE (CITIZEN ONLY)
class ReportDeleteView(LoginRequiredMixin, DeleteView):
    model = Report
    template_name = 'main_app/delete_confirm.html'
    success_url = reverse_lazy('report_list')

    def dispatch(self, request, *args, **kwargs):
        report = self.get_object()
        if is_admin(request.user):
            messages.error(request, "Akses ditolak! Admin dilarang menghapus laporan.")
            return redirect('report_list')
        if report.reporter != request.user or report.status != 'DRAFT':
            messages.error(request, "Akses ditolak! Anda hanya bisa menghapus DRAFT milik Anda sendiri.")
            return redirect('report_list')
            
        return super().dispatch(request, *args, **kwargs)

# DETAIL (LOGIN REQUIRED)
class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = 'main_app/report_detail.html'
    login_url = '/auth/login/'

# UPDATE STATUS (ADMIN ONLY)
def update_status(request, pk):
    if not is_admin(request.user):
        messages.error(request, "Akses ditolak! Hanya admin yang bisa update status.")
        return redirect('report_list')

    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        report.status = request.POST.get('status')
        report.save()
        messages.success(request, "Status berhasil diupdate!")
    return redirect('report_list')

# ==========================================
# ENDPOINT API BAWAAN (DISESUAIKAN ATURANNYA)
# ==========================================
@api_view(['GET', 'POST'])
def api_reports(request):
    if request.method == 'GET':
        if is_admin(request.user):
            reports = Report.objects.exclude(status='DRAFT').order_by('-created_at')
        else:
            reports = Report.objects.filter(~Q(status='DRAFT') | Q(reporter=request.user, status='DRAFT')).order_by('-created_at')
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        if is_admin(request.user):
            return Response({"error": "Admin cannot create"}, status=403)
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(reporter=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def api_report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    
    if request.method == 'GET':
        serializer = ReportSerializer(report)
        return Response(serializer.data)

    if request.method in ['PUT', 'DELETE']:
        if is_admin(request.user) and request.method == 'DELETE':
            return Response({"error": "Admin cannot delete"}, status=403)
        if not is_admin(request.user) and (report.reporter != request.user or report.status != 'DRAFT'):
            return Response({"error": "Forbidden"}, status=403)

    if request.method == 'PUT':
        # Mencegah Admin ubah isi via endpoint lama
        if is_admin(request.user):
            return Response({"error": "Admin can only update status via specific mechanism"}, status=403)
            
        serializer = ReportSerializer(report, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        report.delete()
        return Response(status=204)

def api_search_reports(request):
    query = request.GET.get('q', '')
    
    # Filter basis sesuai role
    if is_admin(request.user):
        base_qs = Report.objects.exclude(status='DRAFT')
    else:
        base_qs = Report.objects.filter(~Q(status='DRAFT') | Q(reporter=request.user, status='DRAFT'))
        
    if query:
        reports = base_qs.filter(
            Q(title__icontains=query) | Q(category__icontains=query) | Q(location__icontains=query)
        ).order_by('-created_at')[:20]
    else:
        reports = base_qs.order_by('-created_at')[:20]
    
    data = [{
        'id': r.id, 'title': r.title, 'category': r.category,
        'location': r.location, 'status': r.status, 'is_admin': is_admin(request.user)
    } for r in reports]
    
    return JsonResponse({'results': data})