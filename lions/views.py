from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import Lion, LionProfile, Tag, Task


DEFAULT_TASK_TITLES = [
    "기본 과제 1",
    "기본 과제 2",
    "기본 과제 3",
]


def _track_choices():
    return Lion.TRACK_CHOICES


def _valid_track_values():
    return {value for value, _label in Lion.TRACK_CHOICES}


def _clean_track(track):
    track = track.strip()
    if track in _valid_track_values():
        return track
    return Lion.TRACK_DJANGO


def _get_lion(lion_id):
    return get_object_or_404(Lion, id=lion_id)


def _lion_detail_context(lion, task_status="", task_error_message=""):
    profile, _created = LionProfile.objects.get_or_create(lion=lion)
    tasks = lion.tasks.all()
    if task_status == "completed":
        tasks = tasks.filter(completed=True)
    elif task_status == "incomplete":
        tasks = tasks.filter(completed=False)

    return {
        "lion": lion,
        "profile": profile,
        "tasks": tasks,
        "task_count": lion.tasks.count(),
        "task_status": task_status,
        "task_error_message": task_error_message,
        "lion_tags": lion.tags.all().order_by("name"),
        "available_tags": Tag.objects.all().order_by("name"),
    }


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
        lions = lions.filter(Q(name__icontains=keyword) | Q(track__icontains=keyword))
    if track:
        lions = lions.filter(track=track)

    context = {
        "lions": lions,
        "lion_count": lions.count(),
        "keyword": keyword,
        "track": track,
        "track_choices": _track_choices(),
    }
    return render(request, "lions/list.html", context)


@transaction.atomic
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

        lion = Lion.objects.create(name=name, track=track)
        Task.objects.bulk_create(
            [Task(lion=lion, title=title) for title in DEFAULT_TASK_TITLES]
        )
        LionProfile.objects.create(lion=lion)
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
    lion = _get_lion(lion_id)
    task_status = request.GET.get("task_status", "").strip()
    return render(request, "lions/detail.html", _lion_detail_context(lion, task_status))


def lion_edit(request, lion_id):
    lion = _get_lion(lion_id)

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

    lion = _get_lion(lion_id)
    lion.delete()
    return redirect("lion_list")


def task_toggle(request, lion_id, task_id):
    if request.method != "POST":
        return redirect("lion_detail", lion_id=lion_id)

    task = get_object_or_404(Task, id=task_id, lion_id=lion_id)
    task.completed = not task.completed
    task.save()
    return redirect("lion_detail", lion_id=lion_id)


def task_create(request, lion_id):
    if request.method != "POST":
        return redirect("lion_detail", lion_id=lion_id)

    lion = _get_lion(lion_id)
    title = request.POST.get("title", "").strip()
    if not title:
        return render(
            request,
            "lions/detail.html",
            _lion_detail_context(lion, task_error_message="Task 제목은 필수 입력입니다."),
        )

    Task.objects.create(lion=lion, title=title)
    return redirect("lion_detail", lion_id=lion_id)


def profile_edit(request, lion_id):
    if request.method != "POST":
        return redirect("lion_detail", lion_id=lion_id)

    lion = _get_lion(lion_id)
    profile, _created = LionProfile.objects.get_or_create(lion=lion)

    profile.github_url = request.POST.get("github_url", "").strip()
    profile.bio = request.POST.get("bio", "").strip()
    profile.save()

    return redirect("lion_detail", lion_id=lion_id)


def tag_toggle(request, lion_id):
    if request.method != "POST":
        return redirect("lion_detail", lion_id=lion_id)

    lion = _get_lion(lion_id)
    tag_name = request.POST.get("name", "").strip()
    if tag_name:
        tag, _created = Tag.objects.get_or_create(name=tag_name)
        if lion.tags.filter(id=tag.id).exists():
            lion.tags.remove(tag)
        else:
            lion.tags.add(tag)

    return redirect("lion_detail", lion_id=lion_id)
