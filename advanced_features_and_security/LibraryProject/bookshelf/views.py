from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book


def book(request):
    return HttpResponse("Hello, world. You're at the bookstore with various bookshelf.")

# Create your views here.
@permission_required('myapp.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books}) 

@permission_required('myapp.can_create', raise_exception=True)
def book_create(request):
    if request.method == "BOOK": 
        # Handle form submission 
        pass
    return render(request, 'myapp/book_form.html')

@permission_required('myapp.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "BOOK":
    # Handle form submission 
        pass
    return render(request, 'myapp/book_form.html', {'book': book})

@permission_required('myapp.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "BOOK":
        book.delete()
        return redirect('book_list')
    return render(request, 'myapp/book_confirm_delete.html', {'book': book})