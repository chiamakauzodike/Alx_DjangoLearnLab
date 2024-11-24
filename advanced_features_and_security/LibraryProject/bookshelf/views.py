from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book
from .forms import BookForm


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

def unsafe_search(request):
    query = request.GET.get('q','')
    results = Book.objects.raw(f"SELECT * FROM books WHERE title LIKE '%{query}%'")

def safe_search(request):
    query = request.GET.get('q','')
    results = Book.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'results': results})

def create_book(request):
    if request.method == "BOOK":
        form = BookForm(request.BOOK)
        if form.is_valid():
            # Safe input handling
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            Book.objects.create(title=title, content=content)
            return redirect('success_page')
        else:
            form = BookForm()
        return render(request, 'create_post.html', {'form': form})