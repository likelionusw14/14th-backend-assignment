from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from .models import Lion, Task, LionProfile, Tag


# ── 1. 목록 (/lions/) ─────────────────────────────
def lion_list(request):
    keyword = request.GET.get('keyword', '')
    track   = request.GET.get('track', '')

    lions = Lion.objects.all().order_by('-created_at')

    if keyword:
        lions = lions.filter(name__icontains=keyword)
    if track:
        lions = lions.filter(track=track)

    return render(request, 'lions/list.html', {
        'lions':   lions,
        'keyword': keyword,
        'track':   track,
    })


# ── 2. 등록 (/lions/new/) ─────────────────────────
@transaction.atomic
def lion_create(request):
    if request.method == 'POST':
        name  = request.POST.get('name', '').strip()
        track = request.POST.get('track', '').strip()

        if not name:
            return render(request, 'lions/new.html', {
                'error_message': '이름을 입력해주세요.',
                'track_choices': Lion.TRACK_CHOICES,
            })

        # Lion 생성
        lion = Lion.objects.create(name=name, track=track)

        # 기본 Task 3개 자동 생성 (1:N)
        default_tasks = ['기초 과제', '중급 과제', '심화 과제']
        for title in default_tasks:
            Task.objects.create(lion=lion, title=title)

        # LionProfile 자동 생성 (1:1)
        LionProfile.objects.create(lion=lion)

        # ── 롤백 테스트 시 아래 주석 해제 ──
        # raise Exception("의도적 롤백 테스트: Lion/Task/LionProfile 모두 저장 안 됨")

        return redirect('lion_detail', pk=lion.id)

    return render(request, 'lions/new.html', {
        'track_choices': Lion.TRACK_CHOICES,
    })


# ── 3. 상세 (/lions/<pk>/) ────────────────────────
def lion_detail(request, pk):
    lion   = get_object_or_404(Lion, pk=pk)
    status = request.GET.get('status', '')

    # 1:N QuerySet
    if status == 'todo':
        tasks = lion.tasks.filter(completed=False)
    elif status == 'done':
        tasks = lion.tasks.filter(completed=True)
    else:
        tasks = lion.tasks.all()

    task_count = tasks.count()

    # N:M QuerySet
    all_tags  = Tag.objects.all()
    lion_tags = lion.tags.all()

    return render(request, 'lions/detail.html', {
        'lion':       lion,
        'tasks':      tasks,
        'task_count': task_count,
        'status':     status,
        'all_tags':   all_tags,
        'lion_tags':  lion_tags,
    })


# ── 4. 수정 (/lions/<pk>/edit/) ───────────────────
def lion_edit(request, pk):
    lion = get_object_or_404(Lion, pk=pk)

    if request.method == 'POST':
        lion.name  = request.POST.get('name', '').strip()
        lion.track = request.POST.get('track', '').strip()
        lion.save()
        return redirect('lion_detail', pk=pk)

    return render(request, 'lions/edit.html', {
        'lion':         lion,
        'track_choices': Lion.TRACK_CHOICES,
    })


# ── 5. 삭제 (/lions/<pk>/delete/) ────────────────
def lion_delete(request, pk):
    lion = get_object_or_404(Lion, pk=pk)
    if request.method == 'POST':
        lion.delete()   # CASCADE → Task, LionProfile 함께 삭제
        return redirect('lion_list')
    return redirect('lion_list')


# ── 6. Task 완료 토글 ─────────────────────────────
def task_toggle(request, pk, task_id):
    task = get_object_or_404(Task, id=task_id, lion_id=pk)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
    return redirect('lion_detail', pk=pk)


# ── 7. 프로필 수정 (1:1) ─────────────────────────
def profile_edit(request, pk):
    lion    = get_object_or_404(Lion, pk=pk)
    profile, _ = LionProfile.objects.get_or_create(lion=lion)   # 없으면 생성

    if request.method == 'POST':
        profile.github_url = request.POST.get('github_url', '').strip()
        profile.bio        = request.POST.get('bio', '').strip()
        profile.save()
        return redirect('lion_detail', pk=pk)

    return render(request, 'lions/profile_edit.html', {
        'lion':    lion,
        'profile': profile,
    })


# ── 8. 태그 토글 (N:M) ───────────────────────────
def tag_toggle(request, pk, tag_id):
    lion = get_object_or_404(Lion, pk=pk)
    tag  = get_object_or_404(Tag, id=tag_id)

    if request.method == 'POST':
        if tag in lion.tags.all():
            lion.tags.remove(tag)   # 중간 테이블 DELETE
        else:
            lion.tags.add(tag)      # 중간 테이블 INSERT

    return redirect('lion_detail', pk=pk)


# ── 9. 태그별 사자 목록 (N:M 역방향) ────────────
def tag_lions(request, tag_id):
    tag   = get_object_or_404(Tag, id=tag_id)
    lions = tag.lions.all()     # 역방향 접근

    return render(request, 'lions/tag_lions.html', {
        'tag':   tag,
        'lions': lions,
    })