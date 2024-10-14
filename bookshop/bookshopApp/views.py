from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "bookshopApp/home.html", {})


def books(request):
    return render(request, "bookshopApp/all-books.html", {})


def about(request):
    return render(request, "bookshopApp/about.html", {})
