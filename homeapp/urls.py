from django.contrib import admin
from django.urls import path

from homeapp.views import index

app_name = 'homeapp'

urlpatterns = [
    path('index/', index, name='index'),
]

