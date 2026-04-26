from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'lions/home.html') 

def lions_list(request):
    context = {
        'lions_data': ['아기사자1', '아기사자2', '아기사자3']
    }
    return render(request, 'lions/lions_list.html', context) 