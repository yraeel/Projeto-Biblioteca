from book.models import Book
from rest_framework.serializers import ModelSerializer, CharField


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"



class BookDetailSerializer(ModelSerializer):

    author = CharField(source="fk_author")
    publisher = CharField(source="fk_publisher")

    class Meta:
        model = Book
        fields = ['id_book', 
                  'book_name', 
                  'pages', 
                  'edition', 
                  'language', 
                  'release', 
                  'country', 
                  'author',
                  'publisher']
        # depth = 1