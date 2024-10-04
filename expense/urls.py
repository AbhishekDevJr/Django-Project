from . import views
from django.urls import path

urlpatterns = [
    path('create-expense/', views.create_expense),
]