from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from rest_framework.decorators import api_view
from .models import Blog
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
        
@api_view(['GET'])
def get_blog(request):
    try:
        blogs = Blog.objects.all()
        serializedData = BlogSerializer(blogs, many = True)
        if serializedData.data:
            return Response({
                    "title" : "All Blogs",
                    "message" : "Total Active Blogs in the DB.",
                    "data" : serializedData.data
                })        
        return Response({
            "title" : "No Data Found or Data Invalid",
            "message" : "No Data was Found or Data is Invalid.",
        })
        
    except Exception as e:
        return Response({
            "title" : "Server Error",
            "message" : "Unhandled Server Error",
            "error" : str(e)
        }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['POST'])
def update_blog(request):
    try:
        if request.data.get('blogId') and request.data.get('title') and request.data.get('content'):
            try:
                blog = Blog.objects.get(blogId = request.data.get('blogId'))
                print('-------------->', blog)
                blog.title = request.data.get('title')
                blog.content = request.data.get('content')
                blog.save()
                return Response({
                    "title" : "Blog Updated Successfully",
                    "message" : "Requested blog updated successfully",
                    "data" : BlogSerializer(blog, many = False).data
                })
            except Exception as e:
                return Response({
                    "title" : "Blog not Found",
                    "message" : "No Blog with the requested Blog Id was found.",
                    "error" : str(e)
                })
        else:
            return Response({
                "title" : "Bad Request",
                "message" : "Bad Request Payload."
            })
    except Exception as e:
        return Response({
             "title" : "Server Error",
            "message" : "Unhandled Server Error",
            "error" : str(e)
        }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['DELETE'])
def delete_blog(request):
    try:
        if request.data.get('blogId'):
            try:
                blog = Blog.objects.get(blogId = request.data.get('blogId'))
                blog.delete()
                return Response({
                    "title" : "Blog Deleted",
                    "message" : "Blog Successfully Deleted.",
                    "blogId" : request.data.get('blogId')
                })
            except Exception as e:
                return Response({
                    "title" : "Blog Not Found",
                    "message" : "Blog for requested Blog Id Not Found."
                }, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "title" : "Bad Request",
                "message" : "Bad Request Payload",
            }, status = status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "title" : "Server Error",
            "message" : "Unhandled Server Error",
            "error" : str(e)
        }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        