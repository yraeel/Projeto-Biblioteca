from author.models import Author
from rest_framework import serializers
from book.models import Book
from book.serializers import BookSerializer


class AuthorSerializer(serializers.ModelSerializer):

    books = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = ['id_author', 'created', 'updated', 'author_name', 'books']

    
    def get_books(self, obj):
        # Filtra os livros relacionados ao autor
        books = Book.objects.filter(fk_author=obj)
        return [book.book_name for book in books]
    
        
