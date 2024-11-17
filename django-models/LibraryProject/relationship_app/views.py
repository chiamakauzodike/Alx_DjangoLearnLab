from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
    
def relationship(request):
    return HttpResponse("Hello, world. You're at the relationship_app with various bookshelf and other connection to Author Library and Librarian class.")