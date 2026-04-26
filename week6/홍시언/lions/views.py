from django.shortcuts import render, redirect, get_object_or_404
from .models import Lion
from .forms import LionForm

def lion_list(request):
    lions = Lion.objects.all()
    query = request.GET.get('name')
    if query:
        lions = lions.filter(name__icontains=query)
    return render(request, 'lions/lion_list.html', {'lions': lions}) # 파일명 확인

def lion_create(request):
    if request.method == 'POST':
        form = LionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lions:lion_list')
    else:
        form = LionForm()
    return render(request, 'lions/lion_new.html', {'form': form}) # 파일명 확인

def lion_detail(request, pk):
    lion = get_object_or_404(Lion, pk=pk)
    return render(request, 'lions/lion_detail.html', {'lion': lion}) # 파일명 확인

def lion_update(request, pk):
    lion = get_object_or_404(Lion, pk=pk)
    if request.method == 'POST':
        form = LionForm(request.POST, instance=lion)
        if form.is_valid():
            form.save()
            return redirect('lions:lion_detail', pk=pk)
    else:
        form = LionForm(instance=lion)
    return render(request, 'lions/lion_form.html', {'form': form, 'lion': lion}) # 파일명 확인

def lion_delete(request, pk):
    lion = get_object_or_404(Lion, pk=pk)
    if request.method == 'POST':
        lion.delete()
    return redirect('lions:lion_list')