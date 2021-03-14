from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('' , views.home , name = 'cyberHome'),
        path('random/' , views.random , name = 'random'),
        path('logistic/' , views.Logistic , name = 'logistic')
]
