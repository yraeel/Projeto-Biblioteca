from django.shortcuts import render
from rest_framework import viewsets
from book.models import Book
from book.serializers import BookSerializer
# Create your views here.


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer