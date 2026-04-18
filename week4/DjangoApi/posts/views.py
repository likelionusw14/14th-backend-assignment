from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <h1>환영합니다!<h1>
        <br> <h2>아기 사자 관리 웹 페이지입니다<h2>
        <br> <a href="/lions/">아기사자 목록 보기</a>
    """)
   
    
# Create your views here.
