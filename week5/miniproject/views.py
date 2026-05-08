from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .models import Lion, Task, LionProfile, Tag


@transaction.atomic
def lion_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        track = request.POST.get('track', '').strip()

        if not name or not track:
            return render(request, 'miniproject/new.html', {'error': '이름과 트랙을 입력해주세요.'})

        lion = Lion.objects.create(name=name, track=track)

        Task.objects.create(author=lion, title="기초 과제")
        Task.objects.create(author=lion, title="중급 과제")
        Task.objects.create(author=lion, title="심화 과제")

        LionProfile.objects.create(user=lion, bio="")

        return redirect('miniproject:lion_list')

    return render(request, 'miniproject/new.html')


def lion_list(request):
    keyword = request.GET.get('keyword', '')
    track = request.GET.get('track', '')

    lions = Lion.objects.all()

    if keyword:
        lions = lions.filter(name__contains=keyword)
    if track:
        lions = lions.filter(track=track)

    return render(request, 'miniproject/list.html', {
        'lions': lions,
        'keyword': keyword,
        'track': track,
    })


def lion_detail(request, pk):
    lion = get_object_or_404(Lion, pk=pk)
    tasks = lion.tasks.all()
    profile, _ = LionProfile.objects.get_or_create(user=lion)
    tags = Tag.objects.all()

    return render(request, 'miniproject/detail.html', {
        'lion': lion,
        'tasks': tasks,
        'profile': profile,
        'tags': tags,
        'task_count': tasks.count(),
    })


def lion_edit(request, pk):
    lion = get_object_or_404(Lion, pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        track = request.POST.get('track', '').strip()

        if not name or not track:
            return render(request, 'miniproject/edit.html', {
                'lion': lion,
                'error': '이름과 트랙을 입력해주세요.'
            })

        lion.name = name
        lion.track = track
        lion.save()
        return redirect('miniproject:lion_detail', pk=pk)

    return render(request, 'miniproject/edit.html', {'lion': lion})


def lion_delete(request, pk):
    lion = get_object_or_404(Lion, pk=pk)

    if request.method == 'POST':
        lion.delete()
        return redirect('miniproject:lion_list')

    return redirect('miniproject:lion_detail', pk=pk)


def task_toggle(request, pk, task_id):

    lion = get_object_or_404(Lion, pk=pk)
    task = get_object_or_404(Task, id=task_id, author=lion)

    if request.method == 'POST':
        task.completed = not task.completed
        task.save()

    return redirect('miniproject:lion_detail', pk=pk)


def profile_edit(request, pk):
    lion = get_object_or_404(Lion, pk=pk)

    profile, _ = LionProfile.objects.get_or_create(user=lion)

    if request.method == 'POST':
        profile.bio = request.POST.get('bio', '').strip()
        profile.github_url = request.POST.get('github_url', '').strip()
        profile.save()
        return redirect('miniproject:lion_detail', pk=pk)

    return render(request, 'miniproject/profile_edit.html', {
        'lion': lion,
        'profile': profile,
    })


def tag_toggle(request, pk, tag_id):
    lion = get_object_or_404(Lion, pk=pk)
    tag = get_object_or_404(Tag, id=tag_id)

    if request.method == 'POST':
        if tag.lions.filter(pk=lion.pk).exists():
            tag.lions.remove(lion)
        else:
            tag.lions.add(lion)

    return redirect('miniproject:lion_detail', pk=pk)