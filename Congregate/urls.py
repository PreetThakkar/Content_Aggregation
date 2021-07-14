from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_home, name = "redirect_home"),
    path('home/', views.home, name = "home"),
    path('home/<str:source>', views.home, name = "main"),
    path('home/<str:source>/#<str:cat>', views.home, name = "particular"),
]