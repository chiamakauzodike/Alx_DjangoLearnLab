from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView
#from rest_framework.generics.ListAPIView import ListAPIView
from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BookList(generics.ListAPIView): #pass the test
#class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
#class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
