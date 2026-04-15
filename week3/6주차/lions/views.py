from django.shortcuts import render, redirect

# -----------------------------------------------
# DB 대신 메모리 리스트로 데이터 관리
# -----------------------------------------------
lions = []      # 아기사자들을 담는 리스트
next_id = 1     # 새 아기사자에게 줄 id 번호 (자동 증가)

# -----------------------------------------------
# 1. 목록 조회 (/lions/)
# -----------------------------------------------
def lion_list(request):
    global lions  # 전역 변수 lions를 이 함수 안에서 사용

    # 검색 기능 (keyword)
    keyword = request.GET.get('keyword', '')

    # 트랙 필터 기능 (track)
    track = request.GET.get('track', '')

    # 필터링 결과를 담을 리스트
    result = lions

    if keyword:
        # 이름에 keyword가 포함된 것만 필터링
        result = [lion for lion in result if keyword in lion['name']]

    if track:
        # 트랙이 일치하는 것만 필터링
        result = [lion for lion in result if lion['track'] == track]

    return render(request, 'lions/list.html', {
        'lions': result,
        'keyword': keyword,
        'track': track,
    })

# -----------------------------------------------
# 2. 등록 (/lions/new/)
# -----------------------------------------------
def lion_create(request):
    global lions, next_id   # 전역 변수 두 개 사용

    if request.method == 'POST':
        name  = request.POST.get('name')
        track = request.POST.get('track', '')

        # 딕셔너리로 새 아기사자 만들기
        new_lion = {
            'id': next_id,       # 현재 next_id를 이 아기사자의 id로
            'name': name,
            'track': track,
        }

        lions.append(new_lion)   # 리스트에 추가
        next_id += 1             # 다음번엔 1 증가된 id 사용

        return redirect('lion_list')

    return render(request, 'lions/new.html')

# -----------------------------------------------
# 3. 상세 조회 (/lions/<id>/)
# -----------------------------------------------
def lion_detail(request, pk):
    # 리스트에서 id가 pk인 아기사자 찾기
    lion = None
    for l in lions:
        if l['id'] == pk:
            lion = l
            break

    # 못 찾으면 목록으로 돌려보내기
    if lion is None:
        return redirect('lion_list')

    return render(request, 'lions/detail.html', {
        'lion': lion,
    })

# -----------------------------------------------
# 4. 수정 (/lions/<id>/edit/)
# -----------------------------------------------
def lion_edit(request, pk):
    # 리스트에서 id가 pk인 아기사자 찾기
    lion = None
    for l in lions:
        if l['id'] == pk:
            lion = l
            break

    if lion is None:
        return redirect('lion_list')

    if request.method == 'POST':
        # 딕셔너리 값을 직접 수정
        lion['name']  = request.POST.get('name')
        lion['track'] = request.POST.get('track', '')
        return redirect('lion_detail', pk=pk)

    return render(request, 'lions/edit.html', {
        'lion': lion,
    })

# -----------------------------------------------
# 5. 삭제 (/lions/<id>/delete/)
# -----------------------------------------------
def lion_delete(request, pk):
    global lions

    if request.method == 'POST':
        # id가 pk인 것을 제외한 나머지만 남기기
        lions = [lion for lion in lions if lion['id'] != pk]
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