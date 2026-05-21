from django.shortcuts import render, redirect, get_object_or_404
from .models import Lion

def lion_list(request):
    # Requirement: POST /lions/ -> Create process
    if request.method == 'POST':
        name = request.POST.get('name')
        track = request.POST.get('track')
        if name and track:
            new_lion = Lion.objects.create(name=name, track=track)
            return redirect('lion_detail', id=new_lion.id)
        
    # GET /lions/ -> List & Filter process
    keyword = request.GET.get('keyword', '')
    track = request.GET.get('track', '')
    
    lions = Lion.objects.all()
    
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
    # Handle POST if form action is current URL (/lions/new/)
    if request.method == 'POST':
        name = request.POST.get('name')
        track = request.POST.get('track')
        if name and track:
            new_lion = Lion.objects.create(name=name, track=track)
            return redirect('lion_detail', id=new_lion.id)
            
    return render(request, 'lions/new.html')

def lion_detail(request, id):
    lion = get_object_or_404(Lion, id=id)
    
    # Requirement: POST /lions/<id>/ -> Update process
    if request.method == 'POST':
        name = request.POST.get('name')
        track = request.POST.get('track')
        if name and track:
            lion.name = name
            lion.track = track
            lion.save()
            return redirect('lion_detail', id=id)
        
    return render(request, 'lions/detail.html', {'lion': lion})

def lion_edit_form(request, id):
    # Handle POST if form action is current URL (/lions/<id>/edit/)
    lion = get_object_or_404(Lion, id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        track = request.POST.get('track')
        if name and track:
            lion.name = name
            lion.track = track
            lion.save()
            return redirect('lion_detail', id=id)
            
    return render(request, 'lions/edit.html', {'lion': lion})

def lion_delete(request, id):
    if request.method == 'POST':
        lion = get_object_or_404(Lion, id=id)
        lion.delete()
    return redirect('lion_list')
