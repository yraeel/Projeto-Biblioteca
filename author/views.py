from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from author.models import Author
from author.serializers import AuthorSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# class AuthorAPIView(APIView):
    

#     def get(self, request, id_author = None):

#         if id_author: # Se um ID for fornecido, busque pelo ID
            
#             author = get_object_or_404(Author.objects.all(),id_author=id_author)
#             serializer = AuthorSerializer(author)
#             return Response({"Author": serializer.data}, status=status.HTTP_202_ACCEPTED)
        

#         else:# Caso contrário, retorne todos os autores
#             authors = Author.objects.all()
#             serializer = AuthorSerializer(authors, many=True)
#             return Response({"Authors": serializer.data})
        
    

#     def post(self, request):
#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



#     def put(self, request, id_author):

#         author = get_object_or_404(Author.objects.all(), id_author=id_author)
#         serializer = AuthorSerializer(author, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

#     def delete(self, request, id_author):
#         author = get_object_or_404(Author.objects.all(), id_author=id_author)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    





# class AuthorDetails(APIView):

#     def get(self, request, id_author=None):
#         # Verifica se o autor existe
#         author = get_object_or_404(Author, id_author=id_author)
        
#         # Obtém os livros associados ao autor
#         books = author.books.all()  
        
#         # Se não houver livros associados ao autor
#         if not books:
#             return Response({"message": "No books found for this author"}, status=status.HTTP_404_NOT_FOUND)
        
#         # Serializa os dados dos livros
#         serializer = BookSerializer(books, many=True)
        
#         return Response(serializer.data, status=status.HTTP_200_OK)