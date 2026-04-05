from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_report, name='add_report'),
    path('edit/<int:id>/', views.edit_report, name='edit_report'),
    path('delete/<int:id>/', views.delete_report, name='delete_report'),
    path('process/<int:id>/', views.process_report, name='process_report'),
    path('accept/<int:id>/', views.accept_report, name='accept_report'),
]