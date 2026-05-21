from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required


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

@login_required(login_url='/accounts/login/')
def login_success(request):
    return render(request,

                  'accounts/success.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login_success')
        else:
            return render(request, 'accounts/login.html',
                          {'error': '아이디 또는 비밀번호 오류'})
    return render(request, 'accounts/login.html', {})


def logout_view(request):
    logout(request)
    return redirect('login_view')

@login_required(login_url='/accounts/login/')
def profile_view(request):
    user = request.user
    context = {
        'username' : user.username,
        'email'  : user.email,
        'date_joined' : user.date_joined,
    }
    return render(request, 'accounts/profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'accounts/change_password.html', {"form": form})



