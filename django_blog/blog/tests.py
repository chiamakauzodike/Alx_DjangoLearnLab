from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

# Create your tests here.


class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(title='Test Post', content='Content', author=self.user)
        self.comment = Comment.objects.create(post=self.post, author=self.user, content='Test Comment')

    def test_add_comment(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(f'/posts/{self.post.id}/comments/new/', {'content': 'New Comment'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful comment

    def test_edit_comment(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(f'/comments/{self.comment.id}/edit/', {'content': 'Updated Comment'})
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated Comment')

    def test_delete_comment(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(f'/comments/{self.comment.id}/delete/')
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())
