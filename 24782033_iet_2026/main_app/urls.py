from django.urls import path
from .views import (
    HomeView,
    ReportListView,
    ReportCreateView,
    ReportUpdateView,
    ReportDeleteView,
    ReportDetailView,
    update_status,

    api_reports,
    api_report_detail
)

urlpatterns = [
    # HOME
    path('', HomeView.as_view(), name='home'),

    # WEB REPORT
    path('reports/', ReportListView.as_view(), name='report_list'),
    path('reports/create/', ReportCreateView.as_view(), name='report_create'),
    path('reports/<int:pk>/update/', ReportUpdateView.as_view(), name='report_update'),
    path('reports/<int:pk>/delete/', ReportDeleteView.as_view(), name='report_delete'),
    path('reports/<int:pk>/', ReportDetailView.as_view(), name='report_detail'),
    path('reports/<int:pk>/status/', update_status, name='update_status'),

    # API
    path('api/reports/', api_reports),
    path('api/reports/<int:pk>/', api_report_detail),
]