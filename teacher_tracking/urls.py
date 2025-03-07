from django.contrib import admin
from django.urls import path, include
from schedule_management.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule_management/user/register', CreateUserView.as_view(), name='register'),
    path('schedule_management/token', TokenObtainPairView.as_view(), name='get_token'),
    path('schedule_management/token/refresh', TokenRefreshView.as_view(), name='refresh'),
    path('schedule_management-auth/', include('rest_framework.urls')),
]
