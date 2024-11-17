from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .models import Library
# Create your views here.

def list_books(request):
    """This view should render a simple text list of book titles and their authors"""
    books = Book.objects.all()
    #book_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return render(request, 'relationship_app/list_books.html', {'books': books})

"""class based view displaying library details and its book"""
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def relationship(request):
    return HttpResponse("Hello, world. You're at the relationship_app with various bookshelf and other connection to Author Library and Librarian class.")