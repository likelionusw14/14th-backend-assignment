from django.shortcuts import render

# about/views.py

def intro(request):
    # 1. 홈 페이지용 데이터
    context = {
        'message': '아기사자 관리 웹 페이지 입니다.'
    }
    return render(request, 'about/intro.html', context)

def lions_list(request):
    # 2. 아기사자 목록용 데이터 (리스트 형태)
    lions_data = {
        'lions': ['강민영', '강민일', '강민이', '강민삼']
    }
    return render(request, 'about/lions_list.html', lions_data)