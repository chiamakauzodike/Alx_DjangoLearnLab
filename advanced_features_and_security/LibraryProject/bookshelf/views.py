from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Post


def book(request):
    return HttpResponse("Hello, world. You're at the bookstore with various bookshelf.")

# Create your views here.
@permission_required('myapp.can_view', raise_exception=True)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myapp/post_list.html', {'posts': posts}) 

@permission_required('myapp.can_create', raise_exception=True)
def post_create(request):
    if request.method == "POST": 
        # Handle form submission 
        pass
    return render(request, 'myapp/post_form.html')

@permission_required('myapp.can_edit', raise_exception=True)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
    # Handle form submission 
        pass
    return render(request, 'myapp/post_form.html', {'post': post})

@permission_required('myapp.can_delete', raise_exception=True)
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'myapp/post_confirm_delete.html', {'post': post})