from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from book.models import Book
from book.serializers import BookSerializer, BookDetailSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    # serializer_class = BookSerializer

    def get_serializer_class(self):
        
        if self.action == "list":
            return BookDetailSerializer
        if self.action == "retrieve":
            return BookDetailSerializer
        return BookSerializer
    
    
# class BookAPIView(APIView):


#     def get(self, request, id_book = None):

#         if id_book: # Se um ID for fornecido, busque pelo ID
            
#             book = get_object_or_404(Book.objects.all(),id_book=id_book)
#             serializer = BookSerializer(book)
#             return Response({"Book": serializer.data}, status=status.HTTP_202_ACCEPTED)
        

#         else:# Caso contrário, retorne todos os autores
#             books = Book.objects.all()
#             serializer = BookSerializer(books, many=True)
#             return Response({"Books": serializer.data})
    



#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

#     def put(self, request, id_book):

#         book = get_object_or_404(Book.objects.all(), id_book=id_book)
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

#     def delete(self, request, id_book):
#         book = get_object_or_404(Book.objects.all(), id_book=id_book)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    






