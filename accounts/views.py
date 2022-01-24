import re

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.shortcuts import redirect, render
from accounts.decorators import logout_message_required


def user_signup(request):
    # request 요청이 ajax 요청인 경우 is_ajax() 함수 사용
    if request.method=="POST":
        # request로 받은 id 값이 이미 등록된 아이디인 경우
        if User.objects.filter(username=request.POST.get('username')).exists():
            messages.error(request,'이미 존재하는 아이디입니다')
            return redirect('accounts:register')
        # request로 받은 email 값이 이미 등록된 email인 경우
        if User.objects.filter(email=request.POST.get('email')).exists():
            messages.error(request, '이미 존재하는 이메일입니다')
            return redirect('accounts:register')

        # request로 받은 name에 영문자, 숫자, 특수문자가 존재하는 경우
        wrong_str = re.compile('[a-zA-Z0-9-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]')
        if wrong_str.search(request.POST.get('last_name')):
            messages.error(request, '이름에 영문자, 숫자, 특수문자가 존재합니다')
            return redirect('accounts:register')
        if wrong_str.search(request.POST.get('first_name')):
            messages.error(request, '이름에 영문자, 숫자, 특수문자가 존재합니다')
            return redirect('accounts:register')

        # request로 받은 realName 길이가 5자리를 초과한 경우
        if len(request.POST.get('first_name')) > 3:
            messages.error(request, '이름이 너무 깁니다')
            return redirect('accounts:register')
        if len(request.POST.get('last_name')) > 3:
            messages.error(request, '이름이 너무 깁니다')
            return redirect('accounts:register')

        # request로 받은 password가 비밀번호 형식에 적합하지 않은 경우 (8자리이상 & 영어 소문자/대문자/특수문자/숫자 중 3개 이상 조합)
        password = request.POST.get('password1')
        if len(password) < 8:
            messages.error(request, '비밀번호가 너무 짧습니다. 8자 이상 입력해주세요')
            return redirect('accounts:register')
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
        # 문자 조합이 2가지 미만일 경우
        if count < 2:
            messages.error(request, '비밀번호가 너무 쉽습니다. 대문자, 소문자, 숫자, 특수문자 중 2가지 이상 조합하세요')
            return redirect('accounts:register')

        # request로 받은 password2와 password 값이 일치하지 않는 경우
        if request.POST.get('password1') != request.POST.get('password2'):
            messages.error(request, '비밀번호가 서로 맞지 않습니다. 다시 확인해주세요')
            return redirect('accounts:register')


        # 사용자가 작성한 회원가입 내용 형식이 정상인 경우
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password1')


        user = User(username=username,first_name=first_name,last_name=last_name, email=email)
        user.set_password(password)
        user.save()

        messages.success(request, '회원가입이 완료되었습니다')

        return render(request, 'accounts/login.html')

    return render(request, 'accounts/register.html')

@logout_message_required
def user_login(request):
    if request.method == "POST":
        # 아이디를 입력하지 않은 경우
        if request.POST.get('username')=="":
            messages.error(request, '아이디를 입력하세요')
            return redirect('accounts:login')

        # 비밀번호를 입력하지 않은 경우
        elif request.POST.get('password')=="":
            messages.error(request, '비밀번호를 입력하세요')
            return redirect('accounts:login')


        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, '로그인하였습니다')
            return render(request, 'homeapp/index.html')

        messages.error(request, '로그인 정보가 없습니다')

        return redirect('accounts:login')

    return render(request, 'accounts/login.html')