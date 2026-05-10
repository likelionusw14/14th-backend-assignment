from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .models import Lion, LionProfile, Tag, Task


# ---------------------------------------------------------------------------
# Lion 목록
# ---------------------------------------------------------------------------
def lion_list(request):
    """GET /lions/ → Lion 목록 + 검색/필터"""
    query = request.GET.get('q', '').strip()

    if query:
        lions = Lion.objects.filter(name__icontains=query)
    else:
        lions = Lion.objects.all()

    context = {
        'lions': lions,
        'query': query,
    }
    return render(request, 'lions/list.html', context)


# ---------------------------------------------------------------------------
# Lion 생성 (트랜잭션)
# ---------------------------------------------------------------------------
def lion_new(request):
    """
    GET  /lions/new/ → 생성 폼 표시
    POST /lions/new/ → Lion 생성 + Task 3개 + LionProfile 자동 생성 (atomic)
    """
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()

        # 빈 값 검증
        if not name:
            return render(request, 'lions/new.html', {
                'error': '이름을 입력해주세요.',
            })

        try:
            with transaction.atomic():
                # Lion 생성
                lion = Lion.objects.create(name=name)

                # Task 3개 자동 생성
                default_tasks = [
                    '자기소개 작성하기',
                    '팀원 인사하기',
                    '첫 번째 과제 제출하기',
                ]
                for task_title in default_tasks:
                    Task.objects.create(lion=lion, title=task_title)

                # LionProfile 자동 생성
                LionProfile.objects.create(lion=lion)

            return redirect('lions:detail', lion_id=lion.id)

        except Exception:
            return render(request, 'lions/new.html', {
                'error': 'Lion 생성 중 오류가 발생했습니다.',
            })

    # GET 요청
    return render(request, 'lions/new.html')


# ---------------------------------------------------------------------------
# Lion 상세
# ---------------------------------------------------------------------------
def lion_detail(request, lion_id):
    """GET /lions/<id>/ → Lion 상세 + Task(1:N) + Profile(1:1) + Tag(N:M)"""
    lion = get_object_or_404(Lion, id=lion_id)

    # LionProfile이 없는 경우 안전하게 get_or_create
    profile, _ = LionProfile.objects.get_or_create(lion=lion)

    tasks = lion.tasks.all()
    tags = lion.tags.all()
    all_tags = Tag.objects.all()

    context = {
        'lion': lion,
        'profile': profile,
        'tasks': tasks,
        'tags': tags,
        'all_tags': all_tags,
    }
    return render(request, 'lions/detail.html', context)


# ---------------------------------------------------------------------------
# Lion 수정
# ---------------------------------------------------------------------------
def lion_edit(request, lion_id):
    """
    GET  /lions/<id>/edit/ → 수정 폼 표시
    POST /lions/<id>/edit/ → Lion 이름 수정
    """
    lion = get_object_or_404(Lion, id=lion_id)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()

        # 빈 값 검증
        if not name:
            return render(request, 'lions/edit.html', {
                'lion': lion,
                'error': '이름을 입력해주세요.',
            })

        lion.name = name
        lion.save()
        return redirect('lions:detail', lion_id=lion.id)

    # GET 요청
    return render(request, 'lions/edit.html', {'lion': lion})


# ---------------------------------------------------------------------------
# Lion 삭제
# ---------------------------------------------------------------------------
def lion_delete(request, lion_id):
    """POST /lions/<id>/delete/ → Lion 삭제 (CASCADE: Task, LionProfile 자동 삭제)"""
    lion = get_object_or_404(Lion, id=lion_id)

    if request.method == 'POST':
        lion.delete()
        return redirect('lions:list')

    # GET 요청은 상세 페이지로 리다이렉트 (삭제는 POST만 허용)
    return redirect('lions:detail', lion_id=lion.id)


# ---------------------------------------------------------------------------
# Task 완료 토글
# ---------------------------------------------------------------------------
def task_toggle(request, lion_id, task_id):
    """POST /lions/<id>/tasks/<task_id>/toggle/ → Task 완료 상태 토글"""
    lion = get_object_or_404(Lion, id=lion_id)
    task = get_object_or_404(Task, id=task_id, lion_id=lion.id)

    if request.method == 'POST':
        task.is_done = not task.is_done
        task.save()

    return redirect('lions:detail', lion_id=lion.id)


# ---------------------------------------------------------------------------
# LionProfile 수정
# ---------------------------------------------------------------------------
def profile_edit(request, lion_id):
    """
    GET  /lions/<id>/profile/edit/ → 프로필 수정 폼 표시
    POST /lions/<id>/profile/edit/ → 프로필 수정
    """
    lion = get_object_or_404(Lion, id=lion_id)

    # LionProfile이 없는 경우 안전하게 get_or_create
    profile, _ = LionProfile.objects.get_or_create(lion=lion)

    if request.method == 'POST':
        bio = request.POST.get('bio', '').strip()
        github_url = request.POST.get('github_url', '').strip()

        profile.bio = bio
        profile.github_url = github_url
        profile.save()
        return redirect('lions:detail', lion_id=lion.id)

    # GET 요청
    context = {
        'lion': lion,
        'profile': profile,
    }
    return render(request, 'lions/edit.html', context)


# ---------------------------------------------------------------------------
# Tag 추가/제거 토글
# ---------------------------------------------------------------------------
def tag_toggle(request, lion_id, tag_id):
    """POST /lions/<id>/tags/<tag_id>/toggle/ → Tag 추가/제거 토글 (N:M)"""
    lion = get_object_or_404(Lion, id=lion_id)
    tag = get_object_or_404(Tag, id=tag_id)

    if request.method == 'POST':
        if tag in lion.tags.all():
            lion.tags.remove(tag)
        else:
            lion.tags.add(tag)

    return redirect('lions:detail', lion_id=lion.id)
