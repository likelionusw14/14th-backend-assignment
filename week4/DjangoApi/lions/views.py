from django.shortcuts import render

def lion_list(request):
    lions = ['아기사자1', '아기사자2', '아기사자3']
    return render(request, 'lions.html', {'lions': lions})
# Create your views here.
