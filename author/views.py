from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from author.models import Author
from author.serializers import AuthorSerializer
from rest_framework.views import APIView

# Create your views here.


class AuthorAPIView(APIView):
    

    def get(self, request, id_author = None):

        if id_author: # Se um ID for fornecido, busque pelo ID
            try:
                author = Author.objects.get(id_author=id_author)
                serializer = AuthorSerializer(author)
                return Response({"Author": serializer.data}, status=status.HTTP_202_ACCEPTED)
            
            except Author.DoesNotExist:
                return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)
        
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
        author = Author.objects.get(id_author=id_author)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

    def delete(self, request, id_author):
        author = Author.objects.get(id_author=id_author)
        author.delete()
        return Response({"Deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)