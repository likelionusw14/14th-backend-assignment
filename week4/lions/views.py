from django.shortcuts import render, redirect
from django.urls import reverse

# 임시 저장소 (Database 미사용)
baby_lions = []


def lion_list(request):
    """
    GET /lions/ → 아기사자 목록 페이지
    """
    context = {
        'lions': baby_lions,
    }
    return render(request, 'lions/list.html', context)


def lion_create(request):
    """
    GET  /lions/new/ → 등록 Form
    POST /lions/new/ → 입력 처리 후 Redirect (POST/Redirect 패턴)
    """
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()

        # 보너스: 빈 값이면 에러 메시지 출력
        if not name:
            context = {'error_message': '이름을 입력해주세요.'}
            return render(request, 'lions/new.html', context)

        baby_lions.append(name)

        # POST 처리 후 Template 직접 렌더링 금지 → Redirect
        return redirect(reverse('lion_list'))

    # GET 요청 → Form 렌더링
    return render(request, 'lions/new.html')
