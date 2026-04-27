from django.http import Http404
from django.shortcuts import redirect, render

LIONS = []
NEXT_LION_ID = 1


def _generate_lion_id():
    global NEXT_LION_ID
    current = NEXT_LION_ID
    NEXT_LION_ID += 1
    return current


def _find_lion(lion_id):
    for lion in LIONS:
        if lion["id"] == lion_id:
            return lion
    return None


def home(request):
    context = {
        "message": "환영합니다!",
        "description": "아기사자 관리 웹 페이지입니다.",
    }
    return render(request, "lions/home.html", context)


def lion_list(request):
    keyword = request.GET.get("keyword", "").strip()
    track = request.GET.get("track", "").strip()

    lions = list(LIONS)
    if keyword:
        lowered_keyword = keyword.lower()
        lions = [lion for lion in lions if lowered_keyword in lion["name"].lower()]
    if track:
        lowered_track = track.lower()
        lions = [lion for lion in lions if lion["track"].lower() == lowered_track]

    context = {
        "lions": lions,
        "keyword": keyword,
        "track": track,
    }
    return render(request, "lions/lions.html", context)


def lion_create(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        track = request.POST.get("track", "").strip()

        if not name:
            return render(
                request,
                "lions/new.html",
                {"error_message": "이름은 필수 입력입니다.", "name": name, "track": track},
            )

        LIONS.append(
            {
                "id": _generate_lion_id(),
                "name": name,
                "track": track or "미정",
            }
        )
        return redirect("lion_list")

    return render(request, "lions/new.html")


def lion_detail(request, lion_id):
    lion = _find_lion(lion_id)
    if lion is None:
        raise Http404("해당 아기사자를 찾을 수 없습니다.")

    return render(request, "lions/detail.html", {"lion": lion})


def lion_edit(request, lion_id):
    lion = _find_lion(lion_id)
    if lion is None:
        raise Http404("해당 아기사자를 찾을 수 없습니다.")

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        track = request.POST.get("track", "").strip()

        if not name:
            context = {
                "lion": lion,
                "error_message": "이름은 필수 입력입니다.",
            }
            return render(request, "lions/edit.html", context)

        lion["name"] = name
        lion["track"] = track or "미정"
        return redirect("lion_detail", lion_id=lion["id"])

    return render(request, "lions/edit.html", {"lion": lion})


def lion_delete(request, lion_id):
    if request.method != "POST":
        return redirect("lion_detail", lion_id=lion_id)

    lion = _find_lion(lion_id)
    if lion is None:
        raise Http404("해당 아기사자를 찾을 수 없습니다.")

    LIONS.remove(lion)
    return redirect("lion_list")
