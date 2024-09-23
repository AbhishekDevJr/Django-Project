from django.http import HttpResponse
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({'title' : 'Home Response', 'message' : 'Hello Everyone! This is Django Project Home URL Endpoint Response.'})