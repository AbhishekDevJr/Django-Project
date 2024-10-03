from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def create_expense(request):
    try:
        pass
    except Exception as e:
        return Response({
            "title" : "Server Error",
            "message" : "Unhandled Server Error",
            "error" : str(e)
        })
