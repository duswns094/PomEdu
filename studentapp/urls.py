from django.contrib import admin
from django.urls import path

from studentapp.views import StudentListView, StudentCreateView, EnrollmentListView, EnrollmentCreateView

app_name = 'studentapp'

urlpatterns = [
    path('enrollment_create/', EnrollmentCreateView.as_view(), name='enrollment_create'),
    path('enrollment_list/', EnrollmentListView.as_view(), name='enrollment_list'),
    path('list/', StudentListView.as_view(), name='list'),
    path('create/', StudentCreateView.as_view(), name='create'),
]
