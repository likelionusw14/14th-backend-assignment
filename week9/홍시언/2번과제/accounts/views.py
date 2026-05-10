from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages

@transaction.atomic
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 가입 성공 -> 로그인 페이지로
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html', {'form': form})

@login_required
# 로그인한 사용자만 접근 가능
def login_success(request):
    return render(request,
'accounts/success.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
            username=username,
            password=password)
        
        if user is not None:
            login(request, user)
            return redirect('accounts:success')
        else:
            return render(request,'accounts/login.html',
                {'error':'아이디 또는 비밀번호 오류'})
    return render(request, 'accounts/login.html', {})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

@login_required
def change_password(request):
    if request.method == 'POST':
        current_pw = request.POST.get('current_password')
        new_pw = request.POST.get('new_password')
        
        user = request.user
        
        # 현재 비밀번호 확인
        if user.check_password(current_pw):
            user.set_password(new_pw)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:profile')
        else:
            messages.error(request, "현재 비밀번호가 틀렸습니다.")
            
    return render(request, 'accounts/change_password.html')