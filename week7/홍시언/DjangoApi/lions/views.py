from django.shortcuts import render, redirect, get_object_or_404
from .models import Lion

def lion_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        track = request.POST.get('track')
        Lion.objects.create(name=name, track=track)
        return redirect('lion_list')

    # GET 요청: 검색 및 필터링 처리
    search_query = request.GET.get('name', '')
    track_filter = request.GET.get('track', '')
    
    lions = Lion.objects.all()
    if search_query:
        lions = lions.filter(name__icontains=search_query)
    if track_filter:
        lions = lions.filter(track=track_filter)
        
    return render(request, 'lions/list.html', {'lions': lions.order_by('-created_at')})

def lion_new(request):
    return render(request, 'lions/new.html')

def lion_detail_update(request, pk):
    lion = get_object_or_404(Lion, pk=pk)
    if request.method == 'POST':
        lion.name = request.POST.get('name')
        lion.track = request.POST.get('track')
        lion.save()
        return redirect('lion_list')
    return render(request, 'lions/detail.html', {'lion': lion})

def lion_edit(request, pk):
    lion = get_object_or_404(Lion, pk=pk)
    return render(request, 'lions/edit.html', {'lion': lion})

def lion_delete(request, pk):
    if request.method == 'POST':
        lion = get_object_or_404(Lion, pk=pk)
        lion.delete()
    return redirect('lion_list')