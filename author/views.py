from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from author.models import Author
from book.models import Book
from book.serializers import BookSerializer
from author.serializers import AuthorSerializer
from rest_framework.views import APIView

# Create your views here.


class AuthorAPIView(APIView):
    

    def get(self, request, id_author = None):

        if id_author: # Se um ID for fornecido, busque pelo ID
            
            author = get_object_or_404(Author.objects.all(),id_author=id_author)
            serializer = AuthorSerializer(author)
            return Response({"Author": serializer.data}, status=status.HTTP_202_ACCEPTED)
        

        else:# Caso contrário, retorne todos os autores
            authors = Author.objects.all()
            serializer = AuthorSerializer(authors, many=True)
            return Response({"Authors": serializer.data})
        
    

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



    def put(self, request, id_author):

        author = get_object_or_404(Author.objects.all(), id_author=id_author)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

    def delete(self, request, id_author):
        author = get_object_or_404(Author.objects.all(), id_author=id_author)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    





