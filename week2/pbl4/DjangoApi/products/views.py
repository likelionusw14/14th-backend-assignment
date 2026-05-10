from django.shortcuts import render

# Create your views here.
def index(request):
    text = {
        "mbti": "INTJ",
        "github": "https://github.com/kanatainari",
        "bio": "Stdying Django"
    }
    return render(request, 'products/index.html', {'text': text})
