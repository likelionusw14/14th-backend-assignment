from django.shortcuts import render, redirect
from django.urls import reverse

# 임시 저장소 (Database 미사용)
baby_lions = [
    {'id': 1, 'name': '아기사자1', 'track': 'Django'},
    {'id': 2, 'name': '아기사자2', 'track': 'SpringBoot'},
]
next_id = 3


def get_lion_by_id(lion_id):
    """id로 아기사자 딕셔너리 찾기"""
    for lion in baby_lions:
        if lion['id'] == lion_id:
            return lion
    return None


def lion_list(request):
    """
    GET /lions/          → 전체 목록
    GET /lions/?keyword= → 이름 검색 결과
    """
    keyword = request.GET.get('keyword', '')

    if keyword:
        lions = [l for l in baby_lions if keyword in l['name']]
    else:
        lions = baby_lions

    context = {
        'lions': lions,
        'keyword': keyword,
    }
    return render(request, 'lions/list.html', context)


def lion_create(request):
    """
    GET  /lions/new/ → 등록 Form
    POST /lions/new/ → 저장 후 목록으로 Redirect
    """
    global next_id

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        track = request.POST.get('track', '').strip()

        if not name or not track:
            context = {'error_message': '이름과 트랙을 모두 입력해주세요.'}
            return render(request, 'lions/new.html', context)

        baby_lions.append({'id': next_id, 'name': name, 'track': track})
        next_id += 1

        return redirect(reverse('lion_list'))

    return render(request, 'lions/new.html')


def lion_detail(request, id):
    """
    GET /lions/<id>/ → 상세 페이지
    """
    lion = get_lion_by_id(id)
    return render(request, 'lions/detail.html', {'lion': lion})


def lion_edit(request, id):
    """
    GET  /lions/<id>/edit/ → 수정 Form (기존 값 채워서)
    POST /lions/<id>/edit/ → 수정 후 상세 페이지로 Redirect
    """
    lion = get_lion_by_id(id)

    if request.method == 'POST':
        lion['name'] = request.POST.get('name', '').strip()
        lion['track'] = request.POST.get('track', '').strip()
        return redirect(reverse('lion_detail', args=[id]))

    return render(request, 'lions/edit.html', {'lion': lion})


def lion_delete(request, id):
    """
    POST /lions/<id>/delete/ → 삭제 후 목록으로 Redirect
    """
    global baby_lions
    if request.method == 'POST':
        baby_lions = [l for l in baby_lions if l['id'] != id]
    return redirect(reverse('lion_list'))
