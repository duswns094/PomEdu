from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.list import MultipleObjectMixin

from lectureapp.decorators import lecture_enroll_required, login_required
from lectureapp.forms import LectureCreationForm
from lectureapp.models import Lecture, Video, Enrollment


class LectureListView(ListView):
    model = Lecture
    queryset = Lecture.objects.filter(is_activated=1)
    context_object_name = 'lecture_list'
    template_name = 'lectureapp/list.html'



class LectureCreateView(CreateView):
    model = Lecture
    context_object_name = 'target_lecture'
    form_class = LectureCreationForm
    template_name = 'lectureapp/create.html'

    def get_success_url(self):
        return reverse('lectureapp:list')

@method_decorator(login_required,'get')
@method_decorator(lecture_enroll_required, 'get')
class LectureDetailView(DetailView, MultipleObjectMixin):
    model = Lecture
    context_object_name = 'target_lecture'
    template_name = 'lectureapp/detail.html'

    def get_context_data(self, **kwargs):
        # lecture = self.object
        # user = self.request.user
        # enrollment = Enrollment.objects.filter(student=user, lecture=self.get_object())
        # if enrollment.exists():
        object_list = Video.objects.filter(lecture=self.get_object())
        # else:
        #     object_list = None
        return super(LectureDetailView, self).get_context_data(object_list=object_list,**kwargs)

class VideoDetailView(DetailView):
    model = Video
    context_object_name = 'target_video'
    template_name = 'lectureapp/v_detail.html'
