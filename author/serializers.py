from author.models import Author
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):


    class Meta:
        model = Author
        fields = ['id_author', 'created', 'updated', 'author_name']

