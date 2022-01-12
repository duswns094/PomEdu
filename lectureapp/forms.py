from django import forms
from django.forms import ModelForm

from lectureapp.models import Lecture


class LectureCreationForm(ModelForm):

    class Meta:
        model = Lecture
        fields = ['name', 'teacher','image', 'subject', 'description',
                  'is_activated', 'opendate', 'cost']
