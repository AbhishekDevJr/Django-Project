from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer, AuthenticationSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
import sys

# Create your views here.

@api_view(['POST'])
def user_register(request):
    try:
        serializedData = UserSerializer(data = request.data)
        
        if serializedData.is_valid():
            serializedData.save()
            return Response({
                "title" : "User Created",
                "message" : "User Created Successfully",
                "user" : serializedData.data
            }, status = status.HTTP_201_CREATED)
        else:
            return Response({
                "title" : "Bad Payload",
                "message" : "Bad Request Payload.",
                "errors" : serializedData.errors
            }, status = status.HTTP_400_BAD_REQUEST)
        
    except IOError:
        type, value, traceback = sys.exc_info()
        print('Error opening %s: %s' % (value.filename, value.strerror))
        return Response({
            "title" : "Unhandled Server Exception",
            "message": "Unhandled Server Exception occurred on the Server."
        }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['POST'])
def user_authentication(request):
    try:
        serializedData = AuthenticationSerializer(data = request.data)
        if serializedData.is_valid():
            username = serializedData._validated_data['username']
            password = serializedData._validated_data['password']
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                login(request, user)
                return Response({
                    "title" : "User Authenticated",
                    "message" : "User Successfully Authenticated",
                    "username" : username
                }, status = status.HTTP_200_OK)
            else:
                return Response({
                    "title" : "User Auth Failed",
                    "message" : "User auth failed due to Invalid Credentials"
                })
        else:
            return Response({
                "title" : 'Bad Payload',
                "message" : "Bad Request Payload",
                "errors" : serializedData.errors
            })
    except:
        return Response({
            "title" : "Unhandled Server Exception",
            "message": "Unhandled Server Exception occurred on the Server."
        }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    try:
        logout(request)
        return Response({
            "title" : "User Logout Successfull",
            "message" : "User Successfully Logged Out."
        }, status = status.HTTP_200_OK)
    except Exception as e:
        print(f"Logout Error String------> {str(e)}")
        return Response({
             "title" : "Unhandled Server Exception",
            "message": "Unhandled Server Exception occurred on the Server."
        }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)