from django.shortcuts import render
from django.http import HttpResponse


def book(request):
    return HttpResponse("Hello, world. You're at the bookstore with various bookshelf.")

# Create your views here.
