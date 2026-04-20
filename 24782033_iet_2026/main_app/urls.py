from django.urls import path
from .views import (
    HomeView,
    ReportCreateView,
    ReportUpdateView,
    ReportDeleteView,
    ReportDetailView,
    update_status
)

urlpatterns = [
    path('', HomeView.as_view(), name='report_list'),

    path('create/', ReportCreateView.as_view(), name='report_create'),
    path('<int:pk>/update/', ReportUpdateView.as_view(), name='report_update'),
    path('<int:pk>/delete/', ReportDeleteView.as_view(), name='report_delete'),
    path('<int:pk>/', ReportDetailView.as_view(), name='report_detail'),

    path('<int:pk>/status/', update_status, name='update_status'),
]