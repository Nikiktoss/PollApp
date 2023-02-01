from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('', registrate_user, name="registration_page"),
    path('login', sign_in_user, name="login_page"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
