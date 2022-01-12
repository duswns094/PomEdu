from django.contrib import admin
from django.urls import path

from studentapp.views import StudentListView, StudentCreateView

app_name = 'studentapp'

urlpatterns = [
    path('list/', StudentListView.as_view(), name='list'),
    path('create/', StudentCreateView.as_view(), name='create'),
]
