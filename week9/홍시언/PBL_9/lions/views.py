from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .models import Lion, Task, LionProfile, Tag

@transaction.atomic
def lion_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        track = request.POST.get('track')
        
        lion = Lion.objects.create(name=name, track=track)
        
        Task.objects.create(lion=lion, title="기본 과제 1")
        Task.objects.create(lion=lion, title="기본 과제 2")
        Task.objects.create(lion=lion, title="기본 과제 3")
        
        LionProfile.objects.create(lion=lion)

        return redirect('lion_list')
    
    return render(request, 'lions/create.html')

def lion_list(request):
    lions = Lion.objects.all()
    return render(request, 'lions/list.html', {'lions': lions})

def lion_detail(request, id):
    lion = get_object_or_404(Lion, id=id)
    all_tags = Tag.objects.all()
    
    if request.method == 'POST':
        if 'bio' in request.POST:
            profile, created = LionProfile.objects.get_or_create(lion=lion)
            profile.github_url = request.POST.get('github_url')
            profile.bio = request.POST.get('bio')
            profile.save()
            
        elif 'tag_id' in request.POST:
            tag_id = request.POST.get('tag_id')
            tag = get_object_or_404(Tag, id=tag_id)
            if tag in lion.tags.all():
                lion.tags.remove(tag)
            else:
                lion.tags.add(tag)
        
        return redirect('lion_detail', id=lion.id)

    return render(request, 'lions/detail.html', {
        'lion': lion,
        'all_tags': all_tags
    })

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('lion_detail', id=task.lion.id)

def lion_delete(request, id):
    if request.method == 'POST':
        lion = get_object_or_404(Lion, id=id)
        lion.delete() # Lion을 지우면 연관된 Task, Profile도 CASCADE로 같이 지워집니다!
    return redirect('lion_list')

def lion_update(request, id):
    lion = get_object_or_404(Lion, id=id)
    
    if request.method == 'POST':
        # 폼에서 보낸 새로운 데이터를 가져와서 저장
        lion.name = request.POST.get('name')
        lion.track = request.POST.get('track')
        lion.save()
        return redirect('lion_detail', id=lion.id) # 수정 후 상세페이지로 이동
        
    return render(request, 'lions/edit.html', {'lion': lion})