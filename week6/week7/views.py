from django.shortcuts import render, redirect, get_object_or_404
from .models import Lion


def index(request):
    return render(request, 'lions/home.html')

def lion_list(request):
    keyword = request.GET.get('keyword', '')
    if keyword:
        lions = Lion.objects.filter(name__icontains=keyword)
    else:
        lions = Lion.objects.all()
    return render(request, 'lions/list.html', {'lions': lions, 'keyword': keyword})

def lion_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        track = request.POST.get('track')
        if name:
            Lion.objects.create(name=name, track=track)
            return redirect('lion_list')
    return render(request, 'lions/new.html')

def lion_detail(request, id):
    lion = get_object_or_404(Lion, id=id)
    return render(request, 'lions/detail.html', {'lion': lion})

def lion_edit(request, id):
    lion = get_object_or_404(Lion, id=id)
    if request.method == 'POST':
        lion.name = request.POST.get('name')
        lion.track = request.POST.get('track')
        lion.save() 
        return redirect('lion_detail', id=id)
    return render(request, 'lions/edit.html', {'lion': lion})

def lion_delete(request, id):
    lion = get_object_or_404(Lion, id=id)
    if request.method == 'POST':
        lion.delete()
    return redirect('lion_list')