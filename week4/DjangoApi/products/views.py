from django.shortcuts import render

# Create your views here.
def index(request):
    # context={
    #     'mbti':'ISFP',
    #     'github':'https://github.com/phrin13'
    # }
    return render(request, 'products/index.html')