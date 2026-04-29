from django.shortcuts import redirect, get_object_or_404
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView,
    DetailView, TemplateView
)
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Report
from .serializers import ReportSerializer


# =========================
# ROLE HELPER
# =========================
def is_admin(user):
    return user.is_authenticated and getattr(user, 'is_admin', False)


# =========================
# WEB VIEWS
# =========================

class HomeView(TemplateView):
    template_name = 'main_app/home.html'


# LIST (LOGIN REQUIRED)
class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'main_app/report_list.html'
    context_object_name = 'reports'
    login_url = '/auth/login/'


# CREATE (ADMIN ONLY)
class ReportCreateView(CreateView):
    model = Report
    fields = ['title', 'category', 'location', 'description']
    template_name = 'main_app/report_form.html'
    success_url = reverse_lazy('report_list')

    def dispatch(self, request, *args, **kwargs):
        if not is_admin(request.user):
            messages.error(request, "Akses ditolak! Hanya admin yang bisa membuat laporan.")
            return redirect('report_list')
        return super().dispatch(request, *args, **kwargs)


# UPDATE (ADMIN ONLY)
class ReportUpdateView(UpdateView):
    model = Report
    fields = ['title', 'category', 'location', 'description']
    template_name = 'main_app/report_form.html'
    success_url = reverse_lazy('report_list')

    def dispatch(self, request, *args, **kwargs):
        if not is_admin(request.user):
            messages.error(request, "Akses ditolak! Hanya admin yang bisa mengedit laporan.")
            return redirect('report_list')
        return super().dispatch(request, *args, **kwargs)


# DELETE (ADMIN ONLY)
class ReportDeleteView(DeleteView):
    model = Report
    template_name = 'main_app/delete_confirm.html'
    success_url = reverse_lazy('report_list')

    def dispatch(self, request, *args, **kwargs):
        if not is_admin(request.user):
            messages.error(request, "Akses ditolak! Hanya admin yang bisa menghapus laporan.")
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
        messages.error(request, "❌ Akses ditolak! Hanya admin yang bisa update status.")
        return redirect('report_list')

    report = get_object_or_404(Report, pk=pk)

    if request.method == 'POST':
        report.status = request.POST.get('status')
        report.save()
        messages.success(request, "✅ Status berhasil diupdate!")

    return redirect('report_list')


# =========================
# API
# =========================

@api_view(['GET', 'POST'])
def api_reports(request):

    # GET (public / optional login)
    if request.method == 'GET':
        reports = Report.objects.all().order_by('-created_at')
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    # POST (ADMIN ONLY)
    if request.method == 'POST':
        if not request.user.is_authenticated or not getattr(request.user, 'is_admin', False):
            return Response({"error": "Forbidden"}, status=403)

        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def api_report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)

    if request.method == 'GET':
        serializer = ReportSerializer(report)
        return Response(serializer.data)

    # ADMIN ONLY for PUT/DELETE
    if request.method in ['PUT', 'DELETE']:
        if not request.user.is_authenticated or not getattr(request.user, 'is_admin', False):
            return Response({"error": "Forbidden"}, status=403)

    if request.method == 'PUT':
        serializer = ReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        report.delete()
        return Response(status=204)