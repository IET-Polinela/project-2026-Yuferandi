from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('api/data/', views.get_dashboard_data, name='dashboard_data'),
]