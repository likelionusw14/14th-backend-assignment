from django.shortcuts import render

lions = [
    {'name': '아기사자1', 'track': 'SpringBoot', 'is_present': True},
    {'name': '아기사자2', 'track': 'Django', 'is_present': False},
    {'name': '아기사자3', 'track': 'CSS', 'is_present': True},
]

def index(request):
    return render(request, 'baby_lion/index.html')

def lion_list(request):
    return render(request, 'baby_lion/lion_list.html', {'lions': lions})

def lion_detail(request, name):
    lion = next((l for l in lions if l['name'] == name), None)
    return render(request, 'baby_lion/lion_detail.html', {'lion': lion})