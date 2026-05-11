from django.shortcuts import render, redirect, get_object_or_404

from .models import Lion


def home(request):
    return render(request, 'home.html')


def lion_list(request):

    lions = Lion.objects.all()

    keyword = request.GET.get('keyword', '')

    track = request.GET.get('track', '')

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


def lion_detail(request, id):

    lion = get_object_or_404(Lion, id=id)

    return render(request, 'lions/detail.html', {
        'lion': lion
    })


def lion_create(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        track = request.POST.get('track')

        if not name or not track:
            return render(request, 'lions/new.html', {
                'error_message': '이름과 트랙을 입력하세요.'
            })

        Lion.objects.create(
            name=name,
            track=track,
        )

        return redirect('lion_list')

    return render(request, 'lions/new.html')


def lion_edit(request, id):

    lion = get_object_or_404(Lion, id=id)

    if request.method == 'POST':

        lion.name = request.POST.get('name')
        lion.track = request.POST.get('track')

        lion.save()

        return redirect('lion_detail', lion.id)

    return render(request, 'lions/edit.html', {
        'lion': lion
    })


def lion_delete(request, id):

    lion = get_object_or_404(Lion, id=id)

    if request.method == 'POST':
        lion.delete()

    return redirect('lion_list')