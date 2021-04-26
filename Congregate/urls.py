from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('source/<str:s>/#<str:c>', views.home_cat, name = "particular"),
    path('source/<str:s>', views.home_all, name = "main"),
    # path('store/', views.store, name = "store"),
]