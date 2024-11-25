from book.models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):

    author_name = serializers.CharField(source='fk_author.author_name', read_only=True)
    publisher_name = serializers.CharField(source='fk_publisher.publisher_name', read_only=True)


    class Meta:
        model = Book
        fields = ['id_book', 
                  'book_name', 
                  'pages', 
                  'edition', 
                  'language', 
                  'release', 
                  'country', 
                  'author_name',
                  'fk_author', 
                  'publisher_name',
                  'fk_publisher']

