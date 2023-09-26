from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import ProfileView, UserLoginAPIView, UserRegisterAPIView


urlpatterns = [
    path("register/", UserRegisterAPIView.as_view(), name="user-register"),
    path("login/", UserLoginAPIView.as_view(), name="user-login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", ProfileView.as_view(), name="user-profile"),
]
