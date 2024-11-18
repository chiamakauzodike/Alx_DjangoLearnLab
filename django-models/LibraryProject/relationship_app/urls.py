from django.urls import path

from . import views
from django.views.generic import TemplateView
from .views import list_books
from .views import LibraryDetailView
from .views import relationship
from .views import register
from views.register import registers
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import admin_view
from .views import librarian_view
from .views import member_view

urlpatterns = [
    # function based view for listing books
    path('books/', list_books, name='list-books'),
    # class based view for displaying library details
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logot.html'), name='logout'),
    path('admin/', admin_view, name='admin_view'),
    path('librarain/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='memeber_view'), 
    path('books/add/', add_book, name='add_book'),
    path('book/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', delete_book, name='delete_book'),                             
    #path("", views.relationship, name="relationship"),
]