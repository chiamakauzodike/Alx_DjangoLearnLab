from django.urls import path

from . import views
from django.views.generic import TemplateView
from .views import list_books
from .views import LibraryDetailView
from .views import relationship

urlpatterns = [
    # function based view for listing books
    path('books/', list_books, name='list-books'),
    # class based view for displaying library details
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    #path("", views.relationship, name="relationship"),
]