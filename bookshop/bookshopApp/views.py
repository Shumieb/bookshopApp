from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class HomePageView(TemplateView):
    template_name = "bookshopApp/home.html"


class BooksPageView(TemplateView):
    template_name = "bookshopApp/all-books.html"


class AddBookPageView(TemplateView):
    template_name = "bookshopApp/add-book.html"


class EditBookPageView(TemplateView):
    template_name = "bookshopApp/edit-book.html"


class AboutPageView(TemplateView):
    template_name = "bookshopApp/about.html"
