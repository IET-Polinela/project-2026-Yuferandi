from django.urls import path, include
from .views import (
    HomeView,
    ReportListView,
    ReportCreateView,
    ReportUpdateView,
    ReportDeleteView,
    ReportDetailView,
    update_status,
    report_detail_api,

    api_reports,
    api_report_detail,
    api_search_reports
)

urlpatterns = [
    # HOME
    path('', HomeView.as_view(), name='home'),

    # WEB REPORT
    path('reports/', ReportListView.as_view(), name='report_list'),
    path('reports/create/', ReportCreateView.as_view(), name='report_create'),
    path('reports/add/', ReportCreateView.as_view(), name='add_report'),
    path('reports/<int:pk>/update/', ReportUpdateView.as_view(), name='report_update'),
    path('reports/<int:pk>/edit/', ReportUpdateView.as_view(), name='update_report'),
    path('reports/<int:pk>/delete/', ReportDeleteView.as_view(), name='report_delete'),
    path('reports/<int:pk>/remove/', ReportDeleteView.as_view(), name='delete_report'),
    path('reports/<int:pk>/', ReportDetailView.as_view(), name='report_detail'),
    path('reports/<int:pk>/status/', update_status, name='update_status'),
    
    # API LAMA
    path('api/reports/', api_reports),
    path('api/reports/<int:pk>/', api_report_detail),

    # API BARU
    path('api/search/', api_search_reports, name='api_search_reports'),
    path('reports/search/', api_search_reports, name='report_search'),
    path('reports/detail-api/<int:pk>/', report_detail_api, name='report_detail_api'),
    path('api/detail/<int:pk>/', api_report_detail, name='api_detail_modal'),
    
    # Menghubungkan ViewSet baru
    path('api/', include('main_app.api_urls')),
]
