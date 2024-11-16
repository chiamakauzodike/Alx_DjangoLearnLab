from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def relationship(request):
    return HttpResponse("Hello, world. You're at the relationship_app with various bookshelf and other connection to Author Library and Librarian class.")