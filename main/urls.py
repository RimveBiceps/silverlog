from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.handle_home, name = "home"),
    path('register', views.handle_register, name = "register"),
    path("login", views.handle_login, name = "login"),
    path("logout", views.handle_logout, name= "logout"),
]
