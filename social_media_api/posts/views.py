from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Post, Comment, Like
from accounts.models import CustomUser
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from  notifications.models import Notification

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get posts from followed users
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    
        # Serialize the posts
        from .serializers import PostSerializer
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailView(APIView):
    """Retrieve a single post by its ID."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # Ensure a 404 is raised if the post is not found
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LikePostView(APIView):
    """
    Handle liking a post.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # Use get_object_or_404 to fetch the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            return Response({'message': 'Post liked successfully'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
            return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)
        return Response({'message': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)
