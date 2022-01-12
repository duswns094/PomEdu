import re

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render
# Create your views here.
from django.contrib.auth import login as django_login, authenticate, login, logout
from django.http import JsonResponse

from accountapp.models import Profile


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def user_signup(request):
    # request 요청이 ajax 요청인 경우 is_ajax() 함수 사용
    if is_ajax(request=request):
        # POST 방식으로 요청한 경우, 해당 name이 email인 값을 가져오고 싶은 경우, request.POST.get('email') 사용
        # request 보낸 email 이 빈 문자열인 경우
        if request.POST.get('userid') == "":
            return JsonResponse({'noUserid':True})
        elif request.POST.get('email') == "":
            return JsonResponse({'noEmail':True})
        elif request.POST.get('phone_number') == "":
            return JsonResponse({'noPhoneNumber': True})
        elif request.POST.get('password') == "":
            return JsonResponse({'noPassword':True})
        elif request.POST.get('password2') == "":
            return JsonResponse({'noPassword2':True})

        # request로 받은 email 값이 이메일 형식이 아닌 경우
        signup_email = request.POST.get('email')
        if '@' not in signup_email or '.' not in signup_email:
            return JsonResponse({'wrongEmail':True})

        index = signup_email.index('.')
        try:
            signup_email[index + 1]
        except IndexError:
            return JsonResponse({'wrongEmail': True})

        # request로 받은 email 값이 이미 등록된 email인 경우
        if User.objects.filter(email=request.POST.get('email')).exists():
            return JsonResponse({'emailExists':True})

        # request로 받은 phone_number 값이 이미 등록된 phoneNumber인 경우
        if Profile.objects.filter(phone_number=request.POST.get('phone_number')).exists():
            return JsonResponse({'phoneNumberExists':True})

        # request로 받은 phoneNumber 길이가 적합하지 않은 경우
        try:
            int(request.POST.get('phone_number'))
            pass
        except ValueError:
            return JsonResponse({'notNumber':True})

        if len(request.POST.get('phone_number'))>11:
            return JsonResponse({'tooLongNumber':True})
        if len(request.POST.get('phone_number')) < 10:
            return JsonResponse({'tooShortNumber':True})

        # request로 받은 name에 영문자, 숫자, 특수문자가 존재하는 경우
        wrong_str = re.compile('[a-zA-Z0-9-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]')
        if wrong_str.search(request.POST.get('name')):
            return JsonResponse({'wrongName':True})

        # request로 받은 realName 길이가 5자리를 초과한 경우
        if len(request.POST.get('name')) > 5:
            return JsonResponse({'tooLongName':True})

        # request로 받은 password가 비밀번호 형식에 적합하지 않은 경우 (8자리이상 & 영어 소문자/대문자/특수문자/숫자 중 3개 이상 조합)
        password = request.POST.get('password')
        if len(password) < 8:
            return JsonResponse({'shortLength':True})
        lower_case = re.compile('[a-z]')
        higher_case = re.compile('[A-Z]')
        number = re.compile('[0-9]')
        symbol = re.compile('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]')

        i = 0
        count = 0
        if re.search(lower_case, password):
            count += 1
        if re.search(higher_case, password):
            count += 1
        if re.search(number, password):
            count += 1
        if re.search(symbol, password):
            count += 1
        # 문자 조합이 3가지 미만일 경우
        if count < 3:
            return JsonResponse({'wrongCombination':True})

        # request로 받은 password2와 password 값이 일치하지 않는 경우
        if request.POST.get('password') != request.POST.get('password2'):
            return JsonResponse({'notMatch':True})


        # 사용자가 작성한 회원가입 내용 형식이 정상인 경우
        userid = request.POST.get('userid')
        name = request.POST.get('name')
        email = request.POST.get('email')
        school = request.POST.get('school')
        birth_date = request.POST.get('birth_date')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')


        user = User(username=userid,first_name=name[1:],last_name=name[0], email=email)
        user.set_password(password)
        user.save()
        user.profile.name=name
        user.profile.phone_number=phone_number
        user.profile.birth_date=birth_date
        user.profile.school=school
        user.profile.save()

        return JsonResponse({'works':True})

    return JsonResponse({'notValid':True})

def user_login(request):
    if is_ajax(request=request):
        # 아이디를 입력하지 않은 경우
        if request.POST.get('userid')=="":
            return JsonResponse({'noUserid':True})

        # 비밀번호를 입력하지 않은 경우
        elif request.POST.get('password')=="":
            return JsonResponse({'noPassword':True})

        userid = request.POST.get('userid')
        password = request.POST.get('password')
        user = authenticate(username=userid, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'works':True})
        return JsonResponse({'wrongInformation':True})

    return JsonResponse({'notAjax':True})


