from django.shortcuts import render

# Create your views here.
def index(request):
    # 첫 번째 인자는 request, 두 번째는 보여줄 템플릿 파일 이름이에요.
    return render(request, 'web_first/index.html')

# web_first/views.py
def baby_lion_list(request):
    lions = ['아기사자1', '아기사자2', '아기사자3'] 
    return render(request, 'web_first/list.html', {'lions': lions})