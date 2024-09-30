from django.urls import path
from . import views

#URL Routes Configuration
urlpatterns = [
    path('register/', views.user_register),
    path('login/', views.user_authentication),
    path('logout/', views.user_logout),
    path('verify-auth/', views.verify_user),
    path('get-user-data/', views.get_all_users)
]