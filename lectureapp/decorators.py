from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, resolve

from lectureapp.models import Lecture, Enrollment

def login_required(func):
    def decorated(request, *args, **kwargs):
        lecture = Lecture.objects.get(pk=kwargs['pk'])
        teacher = lecture.teacher
        if not request.user.is_authenticated:
             messages.warning(request, '로그인이 필요합니다')
             return redirect('teacherapp:detail',teacher.id)
        return func(request, *args, **kwargs)
    return decorated

def lecture_enroll_required(func):
    def decorated(request, *args, **kwargs):
        lecture = Lecture.objects.get(pk=kwargs['pk'])
        teacher = lecture.teacher
        enrollment = Enrollment.objects.filter(lecture=lecture)
        if not enrollment.filter(student=request.user).exists():
             messages.warning(request, '수강 신청이 필요합니다')
             return redirect('teacherapp:detail',teacher.id)
        return func(request, *args, **kwargs)
    return decorated