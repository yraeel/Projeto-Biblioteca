from django.shortcuts import render
from rest_framework import viewsets, status, generics
from book.models import Book
from book.serializers import BookSerializer
# Create your views here.


class BooksAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id_book'