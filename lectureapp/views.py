from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
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

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            lecture_ids = request.POST.getlist('lecture_id[]')
            if request.POST.get('del-action'):
                for id in lecture_ids:
                    try:
                        lecture = Lecture.objects.get(pk=id)
                        lecture.delete()
                        messages.info(request, "'"+lecture.name+"'" + "이(가) 삭제되었습니다.")
                    except:
                        messages.add_message(self.request, messages.INFO, "강의 삭제에 실패하였습니다.")
            elif request.POST.get('dis-action'):
                for id in lecture_ids:
                    try:
                        lecture = Lecture.objects.get(pk=id)
                        lecture.is_activated = False
                        lecture.save()
                        messages.info(request, "'"+lecture.name+"'" + "이(가) 비활성화되었습니다.")
                    except:
                        messages.add_message(self.request, messages.INFO, "강의 비활성화에 실패하였습니다.")
        new_queryset = Lecture.objects.filter(is_activated=1)
        context = {'lecture_list': new_queryset}
        return render(request,'lectureapp/list.html',context)



class LectureCreateView(CreateView):
    model = Lecture
    context_object_name = 'target_lecture'
    form_class = LectureCreationForm
    template_name = 'lectureapp/create.html'

    def get_success_url(self):
        messages.success(self.request, "성공적으로 등록되었습니다.")
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
