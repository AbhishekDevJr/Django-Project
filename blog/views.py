from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from rest_framework.decorators import api_view
import datetime
import uuid
# Create your views here.

@api_view(['POST'])
def create_blog(request):
    try:
        blog = request.data.copy()
        blog['createdDate'] = datetime.date.today
        blog['blogId'] = uuid.uuid4()
        blogSerialized = BlogSerializer(data = blog)
        
        if blogSerialized.is_valid():
            blogSerialized.save()
            return Response({
                "title" : "Blog Created Successfully",
                "message" : "Blog has been created successfully.",
                "data" : blogSerialized.data
            }, status = status.HTTP_201_CREATED)
        else:
            return Response({
                "title" : "Bad Request",
                "message" : "Bad Request Payload",
                }, status = status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        Response({
            "title" : "Sever Error",
            "message" : "Unhandled Server Error"
        }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        