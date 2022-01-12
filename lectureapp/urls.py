from django.contrib import admin
from django.urls import path

from lectureapp.views import LectureListView, LectureDetailView, VideoDetailView, LectureCreateView

app_name = 'lectureapp'

urlpatterns = [
    path('list/', LectureListView.as_view(), name='list'),
    path('create/', LectureCreateView.as_view(), name='create'),
    path('detail/<int:pk>',LectureDetailView.as_view(), name='detail'),
    path('v_detail/<int:pk>',VideoDetailView.as_view(), name='v_detail'),
]

