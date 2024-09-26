from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['POST'])
def user_register(request):
    try:
        print('Request------->', request.headers, request.body, request.method, request.query_params)
        return Response({
            "title" : "Unhandled Server Exception",
            "message": "Unhandled Server Exception occurred on the Server."
        }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    except:
        return Response({
            "title" : "Unhandled Server Exception",
            "message": "Unhandled Server Exception occurred on the Server."
        }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)