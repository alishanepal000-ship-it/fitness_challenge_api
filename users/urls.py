from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterView, ProfileView, register_page, login_page, profile_page


urlpatterns = [
    #API endpoints
    path("register/", RegisterView.as_view(), name="register"),
    
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", ProfileView.as_view(), name="profile"),

    #frontend page
    path("register-page/", register_page, name="register_page"),
    path("login-page/", login_page, name="login_page"),
    path("profile-page/", profile_page, name="profile_page"),


]