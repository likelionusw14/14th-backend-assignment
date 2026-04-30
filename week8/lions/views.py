from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Lion


def lion_list(request):
    keyword = request.GET.get('keyword', '')
    track = request.GET.get('track', '')

    lions = Lion.objects.all()

    if keyword:
        lions = lions.filter(name__icontains=keyword)
    if track:
        lions = lions.filter(track=track)

    context = {
        'lions': lions,
        'keyword': keyword,
        'track': track,
    }
    return render(request, 'lions/list.html', context)


def lion_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        track = request.POST.get('track', '').strip()

        if not name or not track:
            context = {'error_message': '이름과 트랙을 모두 입력해주세요.'}
            return render(request, 'lions/new.html', context)

        Lion.objects.create(name=name, track=track)
        return redirect(reverse('lion_list'))

    return render(request, 'lions/new.html')


def lion_detail(request, id):
    lion = get_object_or_404(Lion, id=id)
    return render(request, 'lions/detail.html', {'lion': lion})


def lion_edit(request, id):
    lion = get_object_or_404(Lion, id=id)

    if request.method == 'POST':
        lion.name = request.POST.get('name', '').strip()
        lion.track = request.POST.get('track', '').strip()
        lion.save()
        return redirect(reverse('lion_detail', args=[id]))

    return render(request, 'lions/edit.html', {'lion': lion})


def lion_delete(request, id):
    if request.method == 'POST':
        lion = get_object_or_404(Lion, id=id)
        lion.delete()
    return redirect(reverse('lion_list'))
