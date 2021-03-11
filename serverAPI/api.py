from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from haq.models import *
import json
from .getData import *

# Get, Put, Post, Delete
# Authorized Person List
class AuthPersonList(APIView):
    def get(self, request):
        model = get_authPerson_json()
        for data in model.values():
            return Response(data)

# Topics List
class TopicList(APIView):
    def get(self, request):
        model = get_topics_json()
        for data in model.values():
            return Response(data)

    def post(self, request):
        serializer = TopicsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If there is any error and post does not return and below error will be returned 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# Categories List
class CategoryList(APIView):
    def get(self, request):
        model = get_categories_json()
        for data in model.values():
            return Response(data)

# Status List
class StatusList(APIView):
    def get(self, request):
        model = get_status_json()
        for data in model.values():
            return Response(data)

# Religion List
class ReligionList(APIView):
    def get(self, request):
        model = get_religion_json()
        for data in model.values():
            return Response(data)

# Person List
class PersonList(APIView):
    def get(self, request):
        model = get_person_json()
        for data in model.values():
            return Response(data)

# Need List
class NeedList(APIView):
    def get(self, request):
        model = get_need_json()
        for data in model.values():
            return Response(data)

# Language List
class LanguageList(APIView):
    def get(self, request):
        model = get_language_json()
        for data in model.values():
            return Response(data)

# Books List
class BookList(APIView):
    def get(self, request):
        model = get_book_json()
        for data in model.values():
            return Response(data)

# References List
class ReferenceList(APIView):
    def get(self, request):
        model = get_reference_json()
        for data in model.values():
            return Response(data)
