from django.shortcuts import render

def intro(request):
    context = {
        'name': '김회윤',
        'role': '백엔드 개발자',
        'description': '안녕하세요! 웹 개발을 좋아하는 개발자입니다.',
        'skills': ['Python', 'Django', 'JavaScript', 'PostgreSQL'],
        'email': 'email@example.com',
    }
    return render(request, 'about/intro.html', context)