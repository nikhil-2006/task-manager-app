from django.contrib import admin
from django.urls import path
from users.views import RegisterView, ProfileView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('auth/register/', RegisterView.as_view(), name = 'register'),
    path('auth/profile/', ProfileView.as_view()),

    # 🔥 ADD THESE TWO LINES
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
