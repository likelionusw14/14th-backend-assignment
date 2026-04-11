from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'home.html')

def lion_list(request):
    lions = ['아기사자1', '아기사자2', '아기사자3']
    return render(request, 'lions.html', {'lions': lions})