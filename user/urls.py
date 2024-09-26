from django.urls import path
from . import views

#URL Routes Configuration
urlpatterns = [
    path('register/', views.user_register),
]