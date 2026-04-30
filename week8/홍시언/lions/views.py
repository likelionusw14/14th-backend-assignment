from django.shortcuts import render, redirect, get_object_or_404
from .models import Lion

def home(request):
    return render(request, 'home.html')

def lion_list(request):
    keyword = request.GET.get('keyword', '')
    track = request.GET.get('track', '')
    
    lions = Lion.objects.all().order_by('-created_at')
    
    if keyword:
        lions = lions.filter(name__icontains=keyword)
    if track:
        lions = lions.filter(track=track)
        
    return render(request, 'lions/list.html', {
        'lions': lions, 
        'keyword': keyword, 
        'track': track
    })

def lion_detail(request, pk):
    lion = get_object_or_404(Lion, pk=pk)
    return render(request, 'lions/detail.html', {'lion': lion})

def lion_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        track = request.POST.get('track')
        
        if name and track:
            Lion.objects.create(name=name, track=track)
            return redirect('lion_list')
        else:
            return render(request, 'lions/new.html', {'error_message': '모든 필드를 입력해주세요.'})
            
    return render(request, 'lions/new.html')

def lion_edit(request, pk):
    lion = get_object_or_404(Lion, pk=pk)
    
    if request.method == 'POST':
        lion.name = request.POST.get('name')
        lion.track = request.POST.get('track')
        lion.save() 
        return redirect('lion_detail', pk=lion.pk)
        
    return render(request, 'lions/edit.html', {'lion': lion})

def lion_delete(request, pk):
    if request.method == 'POST':
        lion = get_object_or_404(Lion, pk=pk)
        lion.delete() 
    return redirect('lion_list')