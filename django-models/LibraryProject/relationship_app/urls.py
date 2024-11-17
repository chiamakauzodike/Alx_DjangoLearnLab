from django.urls import path

from . import views
from django.views.generic import TemplateView
from .views import list_books
from .views import LibraryDetailView
from .views import relationship
from .views import register
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # function based view for listing books
    path('books/', list_books, name='list-books'),
    # class based view for displaying library details
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/lologout.html'), name='logout'),
    path('register/', (template_name='relationship_app/register.html'), name='register'),
                                     
    #path("", views.relationship, name="relationship"),
]