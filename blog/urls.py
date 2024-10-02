from django.urls import path
from . import views

# API URL(Routes) Configuration
urlpatterns = [
    path('create-blog/', views.create_blog)
]