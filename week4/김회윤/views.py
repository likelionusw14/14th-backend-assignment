from django.shortcuts import render


def home(request):
    context = {
        "message": "환영합니다!",
        "description": "아기사자 관리 웹 페이지입니다.",
    }
    return render(request, "lions/home.html", context)


def lion_list(request):
    lions = ["아기사자1", "아기사자2", "아기사자3"]
    context = {"lions": lions}
    return render(request, "lions/lions.html", context)
