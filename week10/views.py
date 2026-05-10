# products/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction #
from .models import Lion, Task, LionProfile, Tag

# 1. 아기사자 목록 조회 (검색 기능 포함)
def lion_list(request):
    keyword = request.GET.get('keyword', '')
    if keyword:
        lions = Lion.objects.filter(name__icontains=keyword)
    else:
        lions = Lion.objects.all()
    return render(request, 'lions/list.html', {'lions': lions, 'keyword': keyword})

# 2. 아기사자 생성 (트랜잭션 적용)
@transaction.atomic #
def lion_create(request):
    if request.method == 'POST': #
        name = request.POST.get('name')
        track = request.POST.get('track')
        
        if not name:
            return render(request, 'lions/new.html', {'error': '이름을 입력해주세요.'})
        
        # 사자 생성 및 연관 데이터(Profile, Task 3개) 자동 생성
        lion = Lion.objects.create(name=name, track=track) #
        LionProfile.objects.create(lion=lion) 
        for i in range(1, 4):
            Task.objects.create(lion=lion, title=f"필수 과제 {i}") 
            
        return redirect('lion_list')
    return render(request, 'lions/new.html')

def lion_detail(request, id):
    lion = get_object_or_404(Lion, id=id) 
    
    profile, created = LionProfile.objects.get_or_create(lion=lion)
    
    ongoing_count = lion.tasks.filter(is_completed=False).count()
    
    # 과제 필터링 (전체/미완료/완료)
    status = request.GET.get('status', 'all')
    if status == 'incomplete':
        tasks = lion.tasks.filter(is_completed=False)
    elif status == 'complete':
        tasks = lion.tasks.filter(is_completed=True)
    else:
        tasks = lion.tasks.all()

    return render(request, 'lions/detail.html', {
        'lion': lion,
        'tasks': tasks,
        'ongoing_count': ongoing_count,
        'status': status,
    })

# 4. 과제 완료 토글 버튼
def task_toggle(request, lion_id, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id, lion_id=lion_id)
        task.is_completed = not task.is_completed 
        task.save() 
    return redirect('lion_detail', id=lion_id)

# 5. 수정 및 삭제
def lion_edit(request, id):
    lion = get_object_or_404(Lion, id=id)
    if request.method == 'POST':
        lion.name = request.POST.get('name')
        lion.track = request.POST.get('track')
        lion.save()
        return redirect('lion_detail', id=lion.id)
    return render(request, 'lions/edit.html', {'lion': lion})

def lion_delete(request, id):
    if request.method == 'POST':
        lion = get_object_or_404(Lion, id=id)
        lion.delete() 
    return redirect('lion_list')


def tag_toggle(request, lion_id, tag_id):
    if request.method == 'POST':
        lion = get_object_or_404(Lion, id=lion_id)
        tag = get_object_or_404(Tag, id=tag_id)
        
        if tag in lion.tags.all():
            lion.tags.remove(tag) 
        else:
            lion.tags.add(tag)  
            
    return redirect('lion_detail', id=lion_id)