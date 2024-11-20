from publisher.models import Publisher
from author.models import Author
from rest_framework import serializers


class PublisherSerializer(serializers.ModelSerializer):

    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)

    class Meta:
        model = Publisher
        fields = ['id_publisher', 'publisher_name', 'created', 'updated', 'authors']

