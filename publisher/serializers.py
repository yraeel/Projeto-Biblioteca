from publisher.models import Publisher
from rest_framework.serializers import ModelSerializer, CharField
from rest_framework import serializers
from author.serializers import AuthorSerializer


class PublisherSerializer(ModelSerializer):

    class Meta:
        model = Publisher
        fields = "__all__"



class PublisherDetailSerializer(serializers.ModelSerializer):

    authors = serializers.SerializerMethodField()

    class Meta:
        model = Publisher
        fields = ["id_publisher",
                  "publisher_name",
                  "created",
                  "updated",
                  "authors"]
        
    def get_authors(self, obj):
        # Retorna apenas os nomes dos autores
        return [author.author_name for author in obj.authors.all()]


