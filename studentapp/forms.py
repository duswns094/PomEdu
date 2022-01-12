from django import forms
from django.forms import ModelForm
from studentapp.models import Student


class StudentCreationForm(ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'school', 'grade', 'phone_number',
                  ]
