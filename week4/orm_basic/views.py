from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .models import  Lion, Task, LionProfile

@transaction.atomic
def lion_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        track  = request.POST.get('track')

        lion = Lion.objects.create(name=name, track = track)

        Task.objects.create(author=lion, title="기초 과제")
        Task.objects.create(author=lion, title="중급 과제")
        Task.objects.create(author=lion, title="심화 과제")

        LionProfile.objects.create(user=lion, bio="")

        return redirect('orm_basic:lion_list')

    return render(request, 'lions/new.html')

def lion_list(request):
    keyword = request.GET.get('keyword', '')
    track = request.GET.get('track', '')

    lions = Lion.objects.all()

    if keyword:
        lions = lions.filter(name__contains=keyword)

    if track:
        lions = lions.filter(track=track)
    return render(request, 'lions/list.html', {
        'lions': lions,
        'keyword': keyword,
        'track': track,
    })

def lion_detail(request, pk):
    lion = Lion.objects.get(pk=pk)
    tasks = lion.tasks.all()
    return render(request, 'lions/detail.html', {
        'lion': lion,
        'tasks': tasks,
    })

def lion_edit(request, pk):
    lion = get_object_or_404(Lion, pk=pk)

    if request.method == 'POST':
        lion.name = request.POST.get('name')
        lion.track = request.POST.get('track')
        lion.save()
        return redirect('orm_basic:lion_detail', pk=pk)

    return render(request, 'lions/edit.html', {'lion': lion})


def lion_delete(request, pk):
    lion = get_object_or_404(Lion, pk=pk)
    lion.delete()
    return redirect('orm_basic:lion_list')

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('orm_basic:lion_detail', pk=task.author.pk)
