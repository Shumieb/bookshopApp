from django.urls import path
from .views import HomePageView, BooksPageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("all-books/", BooksPageView.as_view(), name="books"),
    path("about/", AboutPageView.as_view(), name="about"),
]
