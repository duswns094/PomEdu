from django import forms
from django.forms import ModelForm, TextInput, ChoiceField, ModelChoiceField, DateInput, \
    NumberInput, Textarea, ImageField

from lectureapp.models import Lecture
from teacherapp.models import Teacher


class LectureCreationForm(ModelForm):
    subject_choices = (
        ('Korean', '국어'),
        ('Math', '수학'),
        ('English', '영어'),
        ('Science', '과학'),
        ('Social', '사회'),
    )
    teacher = ModelChoiceField(queryset=Teacher.objects.all(),widget=forms.Select(
        attrs={'class':'custom-select custom-select-sm form-control form-control-sm'}),label='강사:')
    subject = ChoiceField(choices= subject_choices,widget=forms.Select(
        attrs={'class': 'custom-select custom-select-sm form-control form-control-sm'}), label='과목:')
    image = ImageField(required=False)
    class Meta:
        model = Lecture
        fields = ['name', 'teacher','image', 'subject', 'description',
                  'is_activated', 'opendate', 'cost']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control form-control-user",
                'style': 'max-width: 300px;',
                'placeholder': '이름'
            }),
            'description': Textarea(attrs={
                'class': "form-control form-control-user",
                'style': 'max-width: 500px;',
                'rows': 5,
                'placeholder': '설명'
            }),
            'opendate': DateInput(attrs={
                'format' : '%Y-%m-%d',
                'class': "form-control form-control-user",
                'style': 'max-width: 300px;',
                'placeholder': 'ex. yyyy-mm-dd'
            }),
            'cost': NumberInput(attrs={
                'class': "form-control form-control-user",
                'style': 'max-width: 300px;',
                'placeholder': 'ex. 300000'
            }),

        }

        labels = {
            'name': '이름:',
            'description': '설명:',
            'is_activated': '현재 진행중',
            'opendate' : '개설일:',
            'cost': '수강료',
            'image': '강의 포스터',

        }