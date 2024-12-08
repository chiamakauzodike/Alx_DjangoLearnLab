from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView, ProfileView
from django.contrib.auth.decorators import login_required
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import add_comment, CommentUpdateView, CommentDeleteView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    #path('profile/', profile_view, name='profile'),
    path('profile/', login_required(ProfileView.as_view()), name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:post_id>/comments/new/', add_comment, name='add-comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
