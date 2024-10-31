from django.shortcuts import render
from rest_framework import viewsets
from author.models import Author
from author.serializers import AuthorSerializer
# Create your views here.


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer