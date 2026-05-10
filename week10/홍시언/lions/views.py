from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.core.paginator import Paginator
from .models import Lion, Task, LionProfile, Tag

def lion_list(request):
    keyword = request.GET.get('keyword', '')
    track = request.GET.get('track', '')
    
    lions = Lion.objects.all()
    if keyword:
        lions = lions.filter(name__icontains=keyword)
    if track:
        lions = lions.filter(track=track)

    paginator = Paginator(lions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'lions/list.html', {
        'lions': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'keyword': keyword,
        'track': track,
        'count': lions.count()
    })

def lion_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        track = request.POST.get('track')

        if not name or not track:
            return render(request, 'lions/new.html', {'error_message': '이름과 트랙을 모두 입력해주세요.'})

        try:
            with transaction.atomic():
                new_lion = Lion.objects.create(name=name, track=track)
                LionProfile.objects.create(lion=new_lion)
                Task.objects.create(lion=new_lion, title="기초 강의 수강하기")
                Task.objects.create(lion=new_lion, title="첫 과제 제출하기")
                Task.objects.create(lion=new_lion, title="동료 피드백 남기기")
            
            return redirect('lion_detail', lion_id=new_lion.id)
        except Exception:
            return render(request, 'lions/new.html', {'error_message': '생성 중 오류가 발생했습니다.'})

    return render(request, 'lions/new.html')

def lion_detail(request, lion_id):
    lion = get_object_or_404(Lion, id=lion_id)
    profile, created = LionProfile.objects.get_or_create(lion=lion)
    
    status = request.GET.get('status')
    tasks = lion.tasks.all()
    if status == 'todo':
        tasks = tasks.filter(completed=False)
    elif status == 'done':
        tasks = tasks.filter(completed=True)

    all_tags = Tag.objects.all()
    
    return render(request, 'lions/detail.html', {
        'lion': lion,
        'tasks': tasks,
        'task_count': tasks.count(),
        'profile': profile,
        'status': status,
        'all_tags': all_tags
    })

def lion_edit(request, lion_id):
    lion = get_object_or_404(Lion, id=lion_id)
    if request.method == 'POST':
        lion.name = request.POST.get('name')
        lion.track = request.POST.get('track')
        lion.save()
        return redirect('lion_detail', lion_id=lion.id)
    return render(request, 'lions/edit.html', {'lion': lion})

def lion_delete(request, lion_id):
    if request.method == 'POST':
        lion = get_object_or_404(Lion, id=lion_id)
        lion.delete()
        return redirect('lion_list')
    return redirect('lion_detail', lion_id=lion_id)

def task_toggle(request, lion_id, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id, lion_id=lion_id)
        task.completed = not task.completed
        task.save()
    return redirect('lion_detail', lion_id=lion_id)

def profile_edit(request, lion_id):
    if request.method == 'POST':
        lion = get_object_or_404(Lion, id=lion_id)
        profile, created = LionProfile.objects.get_or_create(lion=lion)
        profile.bio = request.POST.get('bio')
        profile.save()
    return redirect('lion_detail', lion_id=lion_id)

def tag_toggle(request, lion_id, tag_id):
    if request.method == 'POST':
        lion = get_object_or_404(Lion, id=lion_id)
        tag = get_object_or_404(Tag, id=tag_id)
        
        if tag in lion.tags.all():
            lion.tags.remove(tag)
        else:
            lion.tags.add(tag)
    return redirect('lion_detail', lion_id=lion_id)