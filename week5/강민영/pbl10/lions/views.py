from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .models import Lion, Task, LionProfile, Tag

# 1. 목록 조회
def lion_list(request):
    keyword = request.GET.get('keyword', '')
    track = request.GET.get('track', '')
    
    lions = Lion.objects.all().order_by('-id') 
    
    if keyword:
        lions = lions.filter(name__icontains=keyword)
    if track:
        lions = lions.filter(track=track)
        
    return render(request, 'lions/list.html', {'lions': lions, 'keyword': keyword, 'track': track})

# 2. 사자 등록
@transaction.atomic
def lion_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        track = request.POST.get('track', '').strip()

        if not name or not track:
            return render(request, 'lions/new.html', {'error_message': '이름과 트랙을 모두 입력해주세요.'})

        try:
            lion = Lion.objects.create(name=name, track=track)
            # 1:1 프로필 자동 생성
            LionProfile.objects.create(lion=lion)
            # 1:N 기본 과제 자동 생성
            default_tasks = ['Git 교육 이수', 'Django 기초 학습', '첫 프로젝트 시작']
            for title in default_tasks:
                Task.objects.create(lion=lion, title=title)
            
            return redirect('lion_detail', id=lion.id)
        except Exception as e:
            return render(request, 'lions/new.html', {'error_message': '생성 중 오류가 발생했습니다.'})
            
    return render(request, 'lions/new.html')

# 3. 상세 조회
def lion_detail(request, id):
    lion = get_object_or_404(Lion, id=id)
    profile, created = LionProfile.objects.get_or_create(lion=lion)
    all_tags = Tag.objects.all()
    return render(request, 'lions/detail.html', {'lion': lion, 'all_tags': all_tags, 'profile': profile})

# 4. 기본 정보 수정
def lion_edit(request, id):
    lion = get_object_or_404(Lion, id=id)
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        track = request.POST.get('track', '').strip()
        
        if not name or not track:
            return render(request, 'lions/edit.html', {'lion': lion, 'error_message': '빈 값을 입력할 수 없습니다.'})
            
        lion.name = name
        lion.track = track
        lion.save()
        return redirect('lion_detail', id=lion.id)
    return render(request, 'lions/edit.html', {'lion': lion})

# 5. 사자 삭제
def lion_delete(request, id):
    if request.method == 'POST':
        lion = get_object_or_404(Lion, id=id)
        lion.delete()
    return redirect('lion_list')

# 6. 과제 상태 토글
def task_toggle(request, lion_id, task_id):
    if request.method == 'POST':
        
        task = get_object_or_404(Task, id=task_id, lion_id=lion_id)
        task.completed = not task.completed
        task.save()
    return redirect('lion_detail', id=lion_id)

# 7. 프로필 수정
def profile_edit(request, id):
    lion = get_object_or_404(Lion, id=id)
    profile, created = LionProfile.objects.get_or_create(lion=lion)
    
    if request.method == 'POST':
        profile.github_url = request.POST.get('github_url', '')
        profile.bio = request.POST.get('bio', '')
        profile.save()
        return redirect('lion_detail', id=lion.id)
    return render(request, 'lions/profile_edit.html', {'lion': lion, 'profile': profile})

# 8. 태그 토글
def tag_toggle(request, lion_id, tag_id):
    if request.method == 'POST':
        lion = get_object_or_404(Lion, id=lion_id)
        tag = get_object_or_404(Tag, id=tag_id)
        if tag in lion.tags.all():
            lion.tags.remove(tag)
        else:
            lion.tags.add(tag)
    return redirect('lion_detail', id=lion_id)

def home(request):
    return render(request, 'home.html')