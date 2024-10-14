from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("all-books/", views.books, name="books"),
    path("about/", views.about, name="about"),
]
