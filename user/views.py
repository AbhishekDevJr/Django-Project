from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer, AuthenticationSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
import sys
import logging

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
            "message": "Unhandled Server Exception occurred on the Server.",
            "errors" : serializedData.errors
        }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# @csrf_exempt 
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
                token, created = Token.objects.get_or_create(user = user)
                
                response = Response({
                    "title" : "User Authenticated",
                    "message" : "User Successfully Authenticated",
                    "username" : username,
                    'token' : token.key
                }, status = status.HTTP_200_OK)
                
                response.set_cookie(
                    key="Authorization",
                    value=f'Token {token.key}',
                    httponly=True,
                    secure=False,
                    samesite="Lax",
                    path='/',
                    max_age=24 * 60 * 60
                )
                
                return response
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

logger = logging.getLogger(__name__)

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def verify_user(request):
    try:
        logger.info(f"Request received: {request.COOKIES}")
        print(request.header)
        print(f"Request Cookies: {request.COOKIES}")
        token_key = request.COOKIES.get('Authorization')
        
        if not token_key:
            raise AuthenticationFailed('Token Not Found in Cookies.')
        
        try:
            token_key = token_key.replace('Token ', '')
            print(f"Token ----------------> {token_key}")
            token = Token.objects.get(key = token_key)
            user = token.user
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid Token')
        
        return Response({
            "title" : "User Authenticated",
            "message" : "User is Authenticated",
            "username" : user.username
        }, status = status.HTTP_200_OK)
        
    except AuthenticationFailed as e:
        print(f"Request Cookies: {str(e)}")
        return Response({
            "title": "Authentication Failed",
            "message": str(e),
        }, status=status.HTTP_401_UNAUTHORIZED)
        
    except Exception as e:
        return Response({
             "title" : "Unhandled Server Exception",
            "message": "Unhandled Server Exception occurred on the Server."
        }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)