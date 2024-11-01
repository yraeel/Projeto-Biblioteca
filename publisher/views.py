from django.shortcuts import render
from rest_framework import viewsets
from publisher.models import Publisher
from publisher.serializers import PublisherSerializer
# Create your views here.


class PublishersViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer