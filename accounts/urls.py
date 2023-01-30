from django.urls import path
from .views import *

urlpatterns = [
    path('', enter, name="enter_page"),
]
