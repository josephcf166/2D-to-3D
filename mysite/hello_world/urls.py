from django.urls import path
from hello_world import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("hello_world", views.hello_world, name="hello_world"),
]
