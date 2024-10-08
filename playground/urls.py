from django.urls import path
from . import views

# URL(Routes) Configuration
urlpatterns = [
    path('hello/', views.greet_universe),
    path('hello-html/', views.template_response),
    path('current-time/', views.current_time),
    path('get-all-movies/', views.get_movie_list),
    path('add-get-movies/', views.add_view_movies),
    path('movie-details/<int:id>', views.movie_details),
]