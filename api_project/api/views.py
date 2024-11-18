from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics.ListAPIView import ListAPIView
from .serializers import BookSerializer
from .models import Book

# Create your views here.

class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
