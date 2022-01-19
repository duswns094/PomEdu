from django import forms
from django.forms import ModelForm, ChoiceField, TextInput
from studentapp.models import Student


class StudentCreationForm(ModelForm):
    year_choices = (
        ('M1', '중1'), ('M2', '중2'), ('M3', '중3'),
        ('H1', '고1'), ('H2', '고2'), ('H3', '고3'),
        ('E4', '초4'), ('E5', '초5'), ('E6', '초6')
    )
    grade = ChoiceField(choices=year_choices, widget=forms.Select(
        attrs={'class': 'custom-select custom-select-sm form-control form-control-sm'}), label='학년:')
    class Meta:
        model = Student
        fields = ['name', 'school', 'grade', 'phone_number',
                  ]
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control form-control-user",
                'style': 'max-width: 300px;',
                'placeholder': '이름'
            }),
            'school': TextInput(attrs={
                'class': "form-control form-control-user",
                'style': 'max-width: 300px;',
                'placeholder': '학교'
            }),
            'phone_number': TextInput(attrs={
                'class': "form-control form-control-user",
                'style': 'max-width: 300px;',
                'placeholder': 'ex)01012345678'
            }),
        }
        labels = {
            'name': '이름:',
            'school': '설명:',
            'phone_number': '전화번호:',
        }
