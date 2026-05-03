from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db import transaction

@transaction.atomic 
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

@login_required
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
            return redirect('login_success')
        else:
            return render(request, 'accounts/login.html',
                {'error': '아이디 또는 비밀번호 오류'})
    else:
        return render(request, 'accounts/login.html', {})
    
def logout_view(request):
    logout(request)
    return redirect('login_view')


@login_required # 로그인한 사용자만 접근 가능하도록 데코레이터 추가
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if not request.user.check_password(current_password):
            return render(request, 'accounts/change_password.html', {'error': '현재 비밀번호가 일치하지 않습니다.'})

        if new_password != confirm_password:
            return render(request, 'accounts/change_password.html', {'error': '새 비밀번호와 확인이 일치하지 않습니다.'})

        request.user.set_password(new_password)
        request.user.save()
        update_session_auth_hash(request, request.user)  # 세션 유지
        return redirect('login')
    else:
        return render(request, 'accounts/change_password.html', {})