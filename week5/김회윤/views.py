from django.shortcuts import redirect, render

LION_NAMES = []


def home(request):
    context = {
        "message": "환영합니다!",
        "description": "아기사자 관리 웹 페이지입니다.",
    }
    return render(request, "lions/home.html", context)


def lion_list(request):
    context = {"lions": LION_NAMES}
    return render(request, "lions/lions.html", context)


def lion_new(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        if name:
            LION_NAMES.append(name)
        return redirect("lion_list")

    return render(request, "lions/new.html")
