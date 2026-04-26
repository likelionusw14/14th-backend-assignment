from django.shortcuts import get_object_or_404, redirect, render

from .models import Lion


def _track_choices():
    return Lion.TRACK_CHOICES


def _valid_track_values():
    return {value for value, _label in Lion.TRACK_CHOICES}


def _clean_track(track):
    track = track.strip()
    if track in _valid_track_values():
        return track
    return Lion.TRACK_DJANGO


def home(request):
    context = {
        "message": "환영합니다!",
        "description": "아기사자 관리 웹 페이지입니다.",
    }
    return render(request, "lions/home.html", context)


def lion_list(request):
    keyword = request.GET.get("keyword", "").strip()
    track = request.GET.get("track", "").strip()

    lions = Lion.objects.all()
    if keyword:
        lions = lions.filter(name__icontains=keyword)
    if track:
        lions = lions.filter(track=track)

    context = {
        "lions": lions,
        "keyword": keyword,
        "track": track,
        "track_choices": _track_choices(),
    }
    return render(request, "lions/list.html", context)


def lion_create(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        track = _clean_track(request.POST.get("track", ""))

        if not name:
            return render(
                request,
                "lions/new.html",
                {
                    "error_message": "이름은 필수 입력입니다.",
                    "name": name,
                    "selected_track": track,
                    "track_choices": _track_choices(),
                },
            )

        Lion.objects.create(name=name, track=track)
        return redirect("lion_list")

    return render(
        request,
        "lions/new.html",
        {
            "selected_track": Lion.TRACK_DJANGO,
            "track_choices": _track_choices(),
        },
    )


def lion_detail(request, lion_id):
    lion = get_object_or_404(Lion, id=lion_id)

    return render(request, "lions/detail.html", {"lion": lion})


def lion_edit(request, lion_id):
    lion = get_object_or_404(Lion, id=lion_id)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        track = _clean_track(request.POST.get("track", ""))

        if not name:
            context = {
                "lion": lion,
                "error_message": "이름은 필수 입력입니다.",
                "selected_track": track,
                "track_choices": _track_choices(),
            }
            return render(request, "lions/edit.html", context)

        lion.name = name
        lion.track = track
        lion.save()
        return redirect("lion_detail", lion_id=lion.id)

    return render(
        request,
        "lions/edit.html",
        {
            "lion": lion,
            "selected_track": lion.track,
            "track_choices": _track_choices(),
        },
    )


def lion_delete(request, lion_id):
    if request.method != "POST":
        return redirect("lion_detail", lion_id=lion_id)

    lion = get_object_or_404(Lion, id=lion_id)
    lion.delete()
    return redirect("lion_list")
