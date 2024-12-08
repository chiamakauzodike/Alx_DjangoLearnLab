from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'auth/logout.html'

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        return redirect('profile')

    return render(request, 'auth/profile.html', {'user': request.user})

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'posts/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'posts/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post_id)
    else:
        form = CommentForm()
    return render(request, 'comments/comment_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/comment_form.html'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.id})

@method_decorator(login_required, name='dispatch')
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comments/comment_confirm_delete.html'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.id})
