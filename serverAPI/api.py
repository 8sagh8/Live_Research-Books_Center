from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from haq.models import *
import json

# Get, Put, Post, Delete

class TopicsList(APIView):
    def get(self, request):

        model = Topic.objects.all()
        
        serializer = TopicsSerializer(model, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TopicsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If there is any error and post does not return and below error will be returned 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 