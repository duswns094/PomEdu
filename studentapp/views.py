
# Create your views here.
import json

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, TemplateView

from lectureapp.models import Enrollment, Lecture
from studentapp.forms import StudentCreationForm
from studentapp.models import Student


class StudentListView(ListView):
    model = Student
    queryset = Student.objects.all
    context_object_name = 'student_list'
    template_name = 'studentapp/list.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            student_ids = request.POST.getlist('id[]')
            for id in student_ids:
                try:
                    student = Student.objects.get(pk=id)
                    student.delete()
                except Student.DoesNotExist:
                    messages.add_message(self.request, messages.INFO, "삭제에 실패하였습니다.")
        messages.add_message(self.request,messages.INFO,"성공적으로 삭제되었습니다.")
        return HttpResponse()

class StudentCreateView(CreateView):
    model = Student
    context_object_name = 'target_student'
    form_class = StudentCreationForm
    template_name = 'studentapp/create.html'

    def get_success_url(self):
        messages.success(self.request,"성공적으로 등록되었습니다.")
        return reverse('studentapp:list')

class EnrollmentListView(ListView):
    model = Enrollment
    queryset = Enrollment.objects.filter(is_activated=1)
    context_object_name = 'enrollment_list'
    template_name = 'studentapp/enrollment_list.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            enrollment_ids = request.POST.getlist('id[]')
            for id in enrollment_ids:
                enrollment = Enrollment.objects.get(pk=id)
                enrollment.is_activated=False
                enrollment.save()
                messages.success(request,"{{enrollment.student.name}}의 {{enrollment.lecture.name}}에 대한 수강이 비활성화 되었습니다")
            render(request, 'studentapp/enrollment_list.html')

class EnrollmentCreateView(TemplateView):
    template_name = 'studentapp/enrollment_create.html'

    def get_context_data(self):
        context = super().get_context_data()
        student = Student.objects.all
        lecture = Lecture.objects.filter(is_activated=1)
        context = {'student_list': student,
                   'lecture_list': lecture,
                   }
        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            student_ids = request.POST.getlist('student_id[]')
            lecture_ids = request.POST.getlist('lecture_id[]')
            for student_id in student_ids:
                for lecture_id in lecture_ids:
                    student = Student.objects.get(id=student_id)
                    lecture = Lecture.objects.get(id=lecture_id)
                    if Enrollment.objects.filter(student=student,lecture=lecture).exists():
                        enrollment = Enrollment.objects.get(student=student,lecture=lecture)
                        if enrollment.is_activated==1:
                            messages.success(request,
                                             "{{enrollment.student.name}}의 {{enrollment.lecture.name}}에 대한 수강이 이미 등록 되어 있습니다")
                        elif enrollment.is_activated==0:
                            enrollment.is_activated=1
                            enrollment.save()
                            messages.success(request,
                                             "{{enrollment.student.name}}의 {{enrollment.lecture.name}}에 대한 수강을 비활성화 상태에서 활성화 상태로 변경하였습니다")
                    else:
                        enrollment = Enrollment(student=student,lecture=lecture)
                        enrollment.save()
                    messages.success(request,"{{enrollment.student.name}}의 {{enrollment.lecture.name}}에 대한 수강이 등록 되었습니다")
            return render(request, 'studentapp/enrollment_list.html')

