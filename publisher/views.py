from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from publisher.models import Publisher
from publisher.serializers import PublisherSerializer
from rest_framework.views import APIView


# Create your views here.


class PublisherAPIView(APIView):
    
    def get(self, request, id_publisher = None):

        if id_publisher: # Se um ID for fornecido, busque pelo ID
            try:
                publisher = Publisher.objects.get(id_publisher=id_publisher)
                serializer = PublisherSerializer(publisher)
                return Response({"Publisher": serializer.data}, status=status.HTTP_202_ACCEPTED)
            
            except publisher.DoesNotExist:
                return Response({"error": "publisher not found"}, status=status.HTTP_404_NOT_FOUND)
        
        else:# Caso contrário, retorne todos os autores
            publishers = Publisher.objects.all()
            serializer = PublisherSerializer(publishers, many=True)
            return Response({"Publishers": serializer.data})
        
    

    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)