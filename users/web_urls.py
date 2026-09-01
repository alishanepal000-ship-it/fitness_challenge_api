from django.urls import path
from .views import register_page, login_page, profile_page

urlpatterns = [
    path("register/", register_page, name="register_page"),
    path("login/", login_page, name="login_page"),
    path("profile/", profile_page, name="profile_page"),
]