from django import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#
# class RegisterForm(UserCreationForm):
#   username = auth.forms.UsernameField(widget=forms.TextInput(attrs={'autocapitalize': 'none',
#                                       'autocomplete': 'username',
#                                       'class': 'form-control form-control-user',
#                                       'placeholder' : "아이디",
#                                       'required': 'true',}))
#   email = forms.EmailField(widget=forms.EmailInput(attrs={'autocomplete': 'off',
#                                       'class': 'form-control form-control-user',
#                                       'placeholder' : "이메일 주소",
#                                       'required': 'true',}))
#   first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'autocomplete': 'off',
#                                       'class': 'form-control form-control-user',
#                                       'placeholder' : "이름",
#                                       'required': 'true',}))
#   last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'autocomplete': 'off',
#                                       'class': 'form-control form-control-user',
#                                       'placeholder' : "성",
#                                       'required': 'true',}))
#   password1 = forms.CharField(
#     strip=False,
#     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
#                                       'class': 'form-control form-control-user',
#                                       'placeholder' : "비밀번호",
#                                       'required': 'true',}),
#   )
#   password2 = forms.CharField(
#     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
#                                       'class': 'form-control form-control-user',
#                                       'placeholder' : "비밀번호 확인",
#                                       'required': 'true',}),
#     strip=False,
#   )
#   class Meta:
#     model = User
#     fields = ['username','first_name','last_name','email','password1', 'password2',]
#
#   def save(self, commit=True):  # save메소드 오버라이
#     user = super(RegisterForm, self).save(commit=False)  # 기존의 id와 pw를 저장. commit이 Flase인 이유는 2번 저장하는것 방지.
#     user.email = self.cleaned_data["email"]  # user 객체에 email 값 추가.
#     user.first_name = self.cleaned_data["first_name"]
#     user.last_name = self.cleaned_data["last_name"]
#     if commit:
#       user.save()  # 객체에 대한 모든 정보를 DB에 저장.
#     return user