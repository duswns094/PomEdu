from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from lectureapp.models import Lecture
from teacherapp.models import Teacher


class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.filter(is_activated=1)
    context_object_name = 'teacher_list'
    template_name = 'teacherapp/list.html'


class TeacherDetailView(DetailView,MultipleObjectMixin):
    model = Teacher
    context_object_name = 'target_teacher'
    template_name = 'teacherapp/detail.html'

    def get_context_data(self, **kwargs):
        teacher = self.object
        if teacher.lecture:
            object_list = Lecture.objects.filter(teacher=self.get_object())
        else:
            object_list = None
        return super(TeacherDetailView, self).get_context_data(object_list=object_list,**kwargs)

