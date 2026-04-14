from django.shortcuts import render, get_object_or_404, redirect
from .models import Lion

# -----------------------------------------------
# 1. 목록 조회 (/lions/)
# -----------------------------------------------
def lion_list(request):
    keyword = request.GET.get('keyword', '')
    track   = request.GET.get('track', '')

    lions = Lion.objects.all().order_by('-created_at') #최근 가입한 순서대로

    if keyword:
        lions = lions.filter(name__icontains=keyword)

    if track:
        lions = lions.filter(track=track)

    return render(request, 'lions/list.html', {
        'lions': lions,
        'keyword': keyword,
        'track': track,
    })

# -----------------------------------------------
# 2. 등록 (/lions/new/)
# -----------------------------------------------
def lion_create(request):
    if request.method == 'POST':
        name  = request.POST.get('name')
        track = request.POST.get('track', '')
        Lion.objects.create(name=name, track=track)
        return redirect('lion_list')

    return render(request, 'lions/new.html', {
        'track_choices': Lion.TRACK_CHOICES,
    })

# -----------------------------------------------
# 3. 상세 조회 (/lions/<id>/)
# -----------------------------------------------
def lion_detail(request, pk):
    lion = get_object_or_404(Lion, pk=pk)
    return render(request, 'lions/datail.html', {
        'lion': lion,
    })

# -----------------------------------------------
# 4. 수정 (/lions/<id>/edit/)
# -----------------------------------------------
def lion_edit(request, pk):
    lion = get_object_or_404(Lion, pk=pk)

    if request.method == 'POST':
        lion.name  = request.POST.get('name')
        lion.track = request.POST.get('track', '')
        lion.save()
        return redirect('lion_detail', pk=pk)

    return render(request, 'lions/edit.html', {
        'lion': lion,
        'track_choices': Lion.TRACK_CHOICES,
    })

# -----------------------------------------------
# 5. 삭제 (/lions/<id>/delete/)
# -----------------------------------------------
def lion_delete(request, pk):
    lion = get_object_or_404(Lion, pk=pk)

    if request.method == 'POST':
        lion.delete()
        return redirect('lion_list')

    return redirect('lion_list')

# # 1. 목록 (/lions/)
# def lion_list(request):
#     keyword = request.GET.get('keyword', '')  # list.html이 'keyword' 사용!
#     lions = Lion.objects.all() #전체 목록 조회
#     if keyword:
#         lions = lions.filter(name__icontains=keyword) #조건 조회 ... name__icontains=keyword인 것
#     return render(request, 'lions/list.html', {
#         'lions': lions,
#         'keyword': keyword,
#     }) #요청 정보 request/ html에 어떤 파일을 보여줄지 'lion/list.html'/ html에 전달할 데이터 {{lions}}, {{keyword}}

# # 2. 등록 (/lions/new/)
# def lion_create(request):           # ← 함수 이름도 lion_create로!
#     if request.method == 'POST':
#         name  = request.POST.get('name')
#         track = request.POST.get('track')
#         Lion.objects.create(name=name, track=track) #DB에 새로운 아기사자 저장
#         return redirect('lion_list') #저장 후 lion_list(별명) 페이지로 이동
#     return render(request, 'lions/new.html')

# # 3. 상세 (/lions/<id>/)
# def lion_detail(request, pk):
#     lion = get_object_or_404(Lion, pk=pk) #없는 pk 주소에 접속하면 404에러
#     return render(request, 'lions/detail.html', {  
#         'lion': lion,
#     })

# # 4. 수정 (/lions/<id>/edit/)
# def lion_edit(request, pk):
#     lion = get_object_or_404(Lion, pk=pk)
#     if request.method == 'POST':
#         lion.name  = request.POST.get('name')
#         lion.track = request.POST.get('track')
#         lion.save()
#         return redirect('lion_detail', pk=lion.pk) #lion_datail(별명) 페이지로 이동, pk=3이면 → /lions/3/ 으로 이동
#     return render(request, 'lions/edit.html', {
#         'lion': lion,
#     })

# # 5. 삭제 (/lions/<id>/delete/)
# def lion_delete(request, pk):
#     # lion = get_object_or_404(Lion, pk=pk) #GET으로 오면 돌려보내기 반드시 POST로만 삭제
#     if request.method == 'POST':
#         Lion.delete()
#         return redirect('lion_list')
#     return redirect('lion_list')