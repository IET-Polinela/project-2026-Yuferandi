from django.urls import path
from .views import UserLoginView, RegisterView, user_logout

urlpatterns = [
    # Login & Register tetap Class-Based View
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    
    # Logout 
    path('logout/', user_logout, name='logout'),
]