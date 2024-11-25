from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from publisher.models import Publisher
from publisher.serializers import PublisherSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


# Create your views here.


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer



# class PublisherAPIView(APIView):
    
#     def get(self, request, id_publisher = None):

#         if id_publisher: # Se um ID for fornecido, busque pelo ID
            
#             publisher = get_object_or_404(Publisher.objects.all(), id_publisher=id_publisher)
#             serializer = PublisherSerializer(publisher)
#             return Response({"Publisher": serializer.data}, status=status.HTTP_202_ACCEPTED)
    
        
#         else:# Caso contrário, retorne todos os autores
#             publishers = Publisher.objects.all()
#             serializer = PublisherSerializer(publishers, many=True)
#             return Response({"Publishers": serializer.data})
        
    

#     def post(self, request):
#         serializer = PublisherSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

#     def put(self, request, id_publisher):
          
#         publisher = get_object_or_404(Publisher.objects.all(), id_publisher=id_publisher)
#         serializer = PublisherSerializer(publisher, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            

#     def delete(self, request, id_publisher):
        
#         publisher = get_object_or_404(Publisher.objects.all(), id_publisher=id_publisher)
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        