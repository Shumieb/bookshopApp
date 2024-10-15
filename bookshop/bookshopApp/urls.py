from django.urls import path
from .views import (
    HomePageView,
    BooksPageView,
    AboutPageView,
    AddBookPageView,
    EditBookPageView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("all-books/", BooksPageView.as_view(), name="books"),
    path("add-book/", AddBookPageView.as_view(), name="about"),
    path("edit-book/", EditBookPageView.as_view(), name="about"),
    path("about/", AboutPageView.as_view(), name="about"),
]
