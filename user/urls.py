from django.urls import path
from . import views

#URL Routes Configuration
urlpatterns = [
    path('register/', views.user_register),
    path('login/', views.user_authentication),
    path('logout/', views.user_logout)
]