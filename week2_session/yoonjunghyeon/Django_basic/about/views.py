from django.shortcuts import render

# Create your views here.
def intro(request):
    context = {
        'name' : '윤정현',
        'job' : '대학생',
        'skill' : ['java', 'python','spring boot'],
        'mail' : '1234@naver.com'
    }
    return render(request, 'about/intro.html', context)


