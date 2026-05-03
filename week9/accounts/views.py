from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
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
        form=UserCreationForm()

    return render(request,'accounts/signup.html',{'form':form})

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
            return render(request,'accounts/login.html',
                {'error':'아이디 또는 비밀번호 오류'})
    return render(request, 'accounts/login.html', {})

def logout_view(request):
    logout(request)
    return redirect('login_view')