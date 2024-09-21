from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greet_universe(request):
    return HttpResponse('Hello Universe!')

def template_response(request):
    test = 1
    temp = True
    return render(request, 'hello.html', {'userName':'Abhishek Choudhari'})

def current_time(request):
    return HttpResponse('Just look at the Top or Bottom of your Screen!!')