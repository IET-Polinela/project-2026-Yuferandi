from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Report


# LIST
class HomeView(ListView):
    model = Report
    template_name = 'main_app/home.html'
    context_object_name = 'reports'


# CREATE
class ReportCreateView(CreateView):
    model = Report
    fields = ['title', 'category', 'location', 'description']
    template_name = 'main_app/report_form.html'
    success_url = reverse_lazy('report_list')


# UPDATE
class ReportUpdateView(UpdateView):
    model = Report
    fields = ['title', 'category', 'location', 'description']
    template_name = 'main_app/report_form.html'
    success_url = reverse_lazy('report_list')


# DELETE
class ReportDeleteView(DeleteView):
    model = Report
    template_name = 'main_app/delete_confirm.html'
    success_url = reverse_lazy('report_list')


# DETAIL
class ReportDetailView(DetailView):
    model = Report
    template_name = 'main_app/report_detail.html'


# UPDATE STATUS
def update_status(request, pk):
    report = get_object_or_404(Report, pk=pk)

    if request.method == 'POST':
        report.status = request.POST.get('status')
        report.save()

    return redirect('report_list')