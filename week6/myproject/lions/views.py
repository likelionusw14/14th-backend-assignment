from django.shortcuts import render, redirect, get_object_or_404
from .models import Lion


# 목록
def lion_list(request):

    keyword = request.GET.get('keyword', '')

    lions = Lion.objects.all()

    if keyword:
        lions = lions.filter(name__icontains=keyword)

    return render(request, 'lions/list.html', {
        'lions': lions,
        'keyword': keyword,
    })


# 상세
def lion_detail(request, lion_id):

    lion = get_object_or_404(Lion, id=lion_id)

    return render(request, 'lions/detail.html', {
        'lion': lion
    })


# 등록
def lion_create(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        track = request.POST.get('track')

        if not name:
            return render(request, 'lions/new.html', {
                'error_message': '이름은 필수입니다.'
            })

        Lion.objects.create(
            name=name,
            track=track
        )

        return redirect('lions:lion_list')

    return render(request, 'lions/new.html')


# 수정
def lion_edit(request, lion_id):

    lion = get_object_or_404(Lion, id=lion_id)

    if request.method == 'POST':

        lion.name = request.POST.get('name')
        lion.track = request.POST.get('track')

        lion.save()

        return redirect('lions:lion_detail', lion.id)

    return render(request, 'lions/edit.html', {
        'lion': lion
    })


# 삭제
def lion_delete(request, lion_id):

    lion = get_object_or_404(Lion, id=lion_id)

    if request.method == 'POST':
        lion.delete()
        return redirect('lions:lion_list')

    return redirect('lions:lion_detail', lion.id)