from django.shortcuts import render
from rest_framework.generics import ListAPIView
#from rest_framework.generics.ListAPIView import ListAPIView
from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets

# Create your views here.

class BookList(rest_framework.generics.ListAPIView): #pass the test
#class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(rest_framework.viewsets.ModelViewSet):
#class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
