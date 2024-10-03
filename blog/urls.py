from django.urls import path
from . import views

# API URL(Routes) Configuration
urlpatterns = [
    path('create-blog/', views.create_blog),
    path('get-blogs/', views.get_blog),
    path('update-blog/', views.update_blog),
    path('delete-blog/', views.delete_blog),
]