
# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.list import MultipleObjectMixin

from lectureapp.decorators import lecture_enroll_required, login_required
from studentapp.forms import StudentCreationForm
from studentapp.models import Student


class StudentListView(ListView):
    model = Student
    queryset = Student.objects.all
    context_object_name = 'student_list'
    template_name = 'studentapp/list.html'

class StudentCreateView(CreateView):
    model = Student
    context_object_name = 'target_student'
    form_class = StudentCreationForm
    template_name = 'studentapp/create.html'

    def get_success_url(self):
        return reverse('studentapp:list')
