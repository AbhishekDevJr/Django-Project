from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def greet_universe(request):
    return HttpResponse('Hello Universe!')

def template_response(request):
    test = 1
    temp = True
    return render(request, 'hello.html', {'userName':'Abhishek Choudhari'})

def current_time(request):
    return HttpResponse('Just look at the Top or Bottom of your Screen!!')

def get_movie_list(request):
    movies = Movie.objects.all()
    serializedData = MovieSerializer(movies, many = True)
    return JsonResponse({'movies' : serializedData.data})

@api_view(['GET', 'POST'])
def add_view_movies(request):
    
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializedData = MovieSerializer(movies, many = True)
        return JsonResponse({'movies' : serializedData.data})
    
    if request.method == 'POST':
        serializedData = MovieSerializer(data = request.data)
        if serializedData.is_valid():
            serializedData.save()
            return Response(serializedData.data, status = status.HTTP_201_CREATED)