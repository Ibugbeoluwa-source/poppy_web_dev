from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index"),
        path("Jake/", views.Jake, name="Jake"),
        path("Brian/", views.Brian, name="Brian"),
        path("<str:name>", views.greet, name="greet"),

]