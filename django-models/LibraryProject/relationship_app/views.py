from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import UserProfile

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
    
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


def relationship(request):
    return HttpResponse("Hello, world. You're at the relationship_app with various bookshelf and other connection to Author Library and Librarian class.")

@permission_required('relationship_app.can_add_book', raise_exception=True) 
def add_book(request): 
    if request.method == 'POST': 
        form = BookForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('book_list') 
    else: 
        form = BookForm() 
        return render(request, 'relationship_app/add_book.html', {'form': form})
    
     # Edit an existing book
@permission_required('relationship_app.can_change_book', raise_exception=True) 
def edit_book(request, book_id): 
    book = get_object_or_404(Book, id=book_id) 
    if request.method == 'POST': 
        form = BookForm(request.POST, instance=book) 
        if form.is_valid(): 
            form.save() 
            return redirect('book_list') 
    else: form = BookForm(instance=book) 
    return render(request, 'relationship_app/edit_book.html', {'form': form}) 

# Delete a book 
@permission_required('relationship_app.can_delete_book', raise_exception=True) 
def delete_book(request, book_id): 
    book = get_object_or_404(Book, id=book_id) 
    if request.method == 'POST': 
        book.delete() 
        return redirect('book_list') 
    return render(request, 'relationship_app/delete_book.html', {'book': book})


class AdminViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_user(username='admin', password='admin123')
        self.admin_user.userprofile.role = 'Admin'
        self.admin_user.userprofile.save()
        
    def test_admin_access(self):
        self.client.login(username='admin', password='admin123')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome, Admin!")
        
    def test_non_admin_access(self):
        non_admin_user = User.objects.create_user(username='member', password='member123')
        non_admin_user.userprofile.role = 'Member'
        non_admin_user.userprofile.save()
        
        self.client.login(username='member', password='member123')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302) # Redirect to /forbidden/
        self.assertRedirects(response, '/forbidden/')