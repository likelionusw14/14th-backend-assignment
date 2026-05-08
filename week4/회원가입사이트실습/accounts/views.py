from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
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


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_success')
        else:
            return render(request, 'accounts/login.html', {
                'error': '아이디 또는 비밀번호 오류'
            })
    return render(request, 'accounts/login.html', {})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def login_success(request):
    return render(request, 'accounts/success.html')


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')

        if request.user.check_password(current_password):
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            return redirect('login_success')
        else:
            return render(request, 'accounts/change_password.html', {
                'error': '현재 비밀번호가 틀렸습니다.'
            })
    return render(request, 'accounts/change_password.html')
