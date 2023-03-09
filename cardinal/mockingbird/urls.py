from django.urls import path
from mockingbird import views

urlpatterns = [
    path("", views.home, name = "Home"),
]
