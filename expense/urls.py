from . import views
from django.urls import path

urlpatterns = [
    path('create-expense/', views.create_expense),
    path('get-expense/', views.get_expense),
    path('update-expense/', views.update_expense),
    path('delete-expense/', views.delete_expense)
]