from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from publisher.models import Publisher
from publisher.serializers import PublisherSerializer
from rest_framework.views import APIView


# Create your views here.


class PublishersAPIView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    


class PublisherAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = 'id_publisher' 