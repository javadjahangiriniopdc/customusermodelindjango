from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
]
