from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author, Book, Library, Librarian
# Create your views here.

def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})

"""class based view displaying library details and its book"""
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_dtail.html'
    context_object_name = 'library'

def relationship(request):
    return HttpResponse("Hello, world. You're at the relationship_app with various bookshelf and other connection to Author Library and Librarian class.")