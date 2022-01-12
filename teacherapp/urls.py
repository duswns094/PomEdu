from django.contrib import admin
from django.urls import path

from teacherapp.views import TeacherListView, TeacherDetailView

app_name = 'teacherapp'

urlpatterns = [
    path('list/', TeacherListView.as_view(), name='list'),
    path('detail/<int:pk>',TeacherDetailView.as_view(),name='detail')
]

