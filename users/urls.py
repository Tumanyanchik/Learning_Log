"""Define users URLs schemes"""
from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # Authorization with default implementation
    path('', include('django.contrib.auth.urls')),
    # Registration path
    path('register/', views.register, name='register'),
]
