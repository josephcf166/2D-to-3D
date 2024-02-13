from django.urls import path
from web_2dto3d import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("home", views.home, name="home"),
]
