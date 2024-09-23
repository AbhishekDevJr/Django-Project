from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Movie
from .serializers import MovieSerializer

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
    return JsonResponse(serializedData.data, safe = False)