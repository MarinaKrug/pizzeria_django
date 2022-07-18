from django.urls import path, include
from .views import *
app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]
