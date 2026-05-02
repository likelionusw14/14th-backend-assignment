from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def lion_list(request):
    lions_data = ['아기사자1', '아기사자2', '아기사자3']
    return render(request, 'lions.html', {'lions': lions_data})