from django.shortcuts import render, redirect, get_object_or_404
from .models import Lion

def lion_list(request):
    # 등록 처리 (POST /lions/)
    if request.method == 'POST':
        name = request.POST.get('name')
        track = request.POST.get('track')
        if name and track:
            Lion.objects.create(name=name, track=track)
            return redirect('lion_list')
        
    # 조회 및 필터 처리 (GET /lions/)
    keyword = request.GET.get('keyword', '')
    track = request.GET.get('track', '')
    
    lions = Lion.objects.all().order_by('-id')
    
    if keyword:
        lions = lions.filter(name__icontains=keyword)
    if track:
        lions = lions.filter(track=track)
        
    return render(request, 'lions/list.html', {
        'lions': lions,
        'keyword': keyword,
        'selected_track': track,
    })

def lion_create_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        track = request.POST.get('track')
        if name and track:
            new_lion = Lion.objects.create(name=name, track=track)
            return redirect('lion_detail', id=new_lion.id)
    return render(request, 'lions/new.html')

def lion_detail(request, id):
    lion = get_object_or_404(Lion, pk=id)
    return render(request, 'lions/detail.html', {'lion': lion})

def lion_edit_form(request, id):
    lion = get_object_or_404(Lion, pk=id)
    if request.method == 'POST':
        lion.name = request.POST.get('name')
        lion.track = request.POST.get('track')
        lion.save()
        return redirect('lion_detail', id=id)
    return render(request, 'lions/edit.html', {'lion': lion})

def lion_delete(request, id):
    if request.method == 'POST':
        lion = get_object_or_404(Lion, pk=id)
        lion.delete()
    return redirect('lion_list')
