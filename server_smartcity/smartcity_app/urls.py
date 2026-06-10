from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from usermanagement_24782033.api_views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('about/', include('about.urls')),
    path('contacts/', include('contacts.urls')),
    path('auth/', include('usermanagement_24782033.urls')),
    path('dashboard/', include('dashboard.urls')),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API Register
    path('api/register/', RegisterView.as_view(), name='api_register'),
]