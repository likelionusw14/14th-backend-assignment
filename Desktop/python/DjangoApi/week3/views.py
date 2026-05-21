from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'week3/home.html')

def lion_list(request):
    context = { 'baby_lions': ['아기사자1', '아기사자2','아기사자3']}
    return render(request, 'week3/lion_list.html', context)