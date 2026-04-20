from django.shortcuts import render,redirect
from .models import Lions

def index(request):
    lions = Lions.objects.all()
    return render(request, 'baby_lion/home.html', {'lions':lions})

def lion_new(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        track = request.POST.get('track')
        if not name or not track:
            return render(request, 'baby_lion/new.html', {
                'error_message': '이름과 트랙을 입력해주세요!'
            })
        Lions.objects.create(name = name, track = track)
        return redirect('index')
    return render(request, 'baby_lion/new.html')
    
def lion_detail(request, id):
    lion= Lions.objects.get(id=id)
    return render(request, 'baby_lion/detail.html', {'lion': lion})

def lion_list(request):
    keyword = request.GET.get('keyword', '')
    track = request.GET.get('track', '')
    lions = Lions.objects.all()

    if keyword:
        lions = lions.filter(name__icontains=keyword)  # 부분 검색
    if track:
        lions = lions.filter(track=track)

    return render(request, 'baby_lion/list.html', {
        'lions': lions,
        'keyword': keyword,
        'track': track,
    })

def lion_edit(request,id):
    lion = Lions.objects.get(id=id)
    if request.method == 'POST':
        lion.name = request.POST.get('name')
        lion.track = request.POST.get('track')
        lion.save()
        return redirect('index')
    return render(request, 'baby_lion/edit.html', {'lion': lion})

def lion_delete(request,id):
    lion = Lions.objects.get(id=id)
    if request.method == 'POST':
        lion.delete()
        return redirect('index')
    return render(request, 'baby_lion/detail.html')
        