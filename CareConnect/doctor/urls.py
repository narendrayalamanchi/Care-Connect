
from django.urls import path, include,re_path  
from . import views
from django.contrib.auth import views as auth_views

app_name="doctor"

urlpatterns = [
    path("home/", views.home, name="home"),
    path('login/', views.doctor_login, name='doctorlogin'),
]