from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("task/", views.task, name="task"),
    path("aboutus/", views.AboutUs, name="AboutUs"),
    path("add/", views.add, name = "add")
]