from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment

# Create your tests here.


class CommentTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Create a post
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user
        )

        # Client for making requests
        self.client = Client()
        
    def test_comment_create_view_redirects_for_anonymous(self):
        """Ensure the CommentCreateView redirects unauthenticated users."""
        response = self.client.get(reverse('add-comment', kwargs={'post_id': self.post.id}))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_comment_create_view_loads_for_authenticated_user(self):
        """Ensure the CommentCreateView is accessible to authenticated users."""
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('add-comment', kwargs={'post_id': self.post.id}))
        self.assertEqual(response.status_code, 200)  # Success
        self.assertTemplateUsed(response, 'comments/comment_form.html')

    def test_comment_create(self):
        """Ensure authenticated users can create comments."""
        self.client.login(username='testuser', password='password')
        response = self.client.post(
            reverse('add-comment', kwargs={'post_id': self.post.id}),
            {'content': 'This is a test comment.'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().content, 'This is a test comment.')
        self.assertEqual(Comment.objects.first().author, self.user)
        self.assertEqual(Comment.objects.first().post, self.post)

    def test_comment_create_with_invalid_data(self):
        """Ensure invalid data does not create a comment."""
        self.client.login(username='testuser', password='password')
        response = self.client.post(
            reverse('add-comment', kwargs={'post_id': self.post.id}),
            {'content': ''}  # Invalid: content is required
        )
        self.assertEqual(response.status_code, 200)  # Renders form with errors
        self.assertEqual(Comment.objects.count(), 0)

class TaggingAndSearchTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(title="Test Post", content="Some content", author=self.user)
        self.post.tags.add('django', 'python')

    def test_search_by_tag(self):
        response = self.client.get(reverse('posts_by_tag', kwargs={'tag_name': 'django'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertNotContains(response, self.post.title)

                # Test posts by tag 'python'
        response = self.client.get(reverse('posts_by_tag', kwargs={'tag_name': 'python'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.title)

    def test_search_no_results(self):
        # Test search with no results
        response = self.client.get(reverse('search_posts') + '?q=Nonexistent')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No results found.")

