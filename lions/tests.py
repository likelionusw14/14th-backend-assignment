import inspect
from pathlib import Path
from unittest.mock import patch

from django.apps import apps
from django.contrib import admin
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

import lions.views
from .models import Lion


class RelationshipModelRegistryTests(SimpleTestCase):
    def test_relationship_models_are_registered(self):
        app_models = apps.all_models["lions"]

        self.assertIn("task", app_models)
        self.assertIn("lionprofile", app_models)
        self.assertIn("tag", app_models)


class ProjectWrapUpContractTests(SimpleTestCase):
    def _model(self, model_name):
        return apps.get_model("lions", model_name)

    def test_models_define_default_latest_ordering(self):
        self.assertEqual(self._model("Lion")._meta.ordering, ["-created_at"])
        self.assertEqual(self._model("Task")._meta.ordering, ["-created_at"])

    def test_mutating_views_use_defensive_lookup_and_post_only_guards(self):
        source = inspect.getsource(lions.views)

        self.assertIn("get_object_or_404(Lion, id=lion_id)", source)
        self.assertIn("get_object_or_404(Task, id=task_id, lion_id=lion_id)", source)
        self.assertIn("if request.method != \"POST\"", source)
        self.assertNotIn("Task.objects.get(id=task_id, lion_id=lion_id)", source)

    def test_task_create_route_exists(self):
        self.assertEqual(reverse("task_create", args=[1]), "/lions/1/tasks/new/")

    def test_readme_documents_project_structure_and_design(self):
        readme = Path("README.md")

        self.assertTrue(readme.exists())
        content = readme.read_text(encoding="utf-8")
        required_phrases = [
            "## 프로젝트 소개",
            "## 실행 방법",
            "## ERD 구조",
            "ForeignKey",
            "OneToOneField",
            "ManyToManyField",
            "transaction.atomic()",
            "MVT",
            "6주차",
            "10주차",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, content)


class LionViewTests(TestCase):
    def test_create_lion_with_post(self):
        response = self.client.post(
            reverse("lion_create"),
            {"name": "아기사자1", "track": Lion.TRACK_DJANGO},
        )

        self.assertRedirects(response, reverse("lion_list"))
        self.assertTrue(
            Lion.objects.filter(name="아기사자1", track=Lion.TRACK_DJANGO).exists()
        )

    def test_list_filters_by_keyword_and_track(self):
        Lion.objects.create(name="아기사자1", track=Lion.TRACK_DJANGO)
        Lion.objects.create(name="백엔드사자", track=Lion.TRACK_SPRINGBOOT)

        response = self.client.get(
            reverse("lion_list"),
            {"keyword": "백엔드", "track": Lion.TRACK_SPRINGBOOT},
        )

        self.assertContains(response, "백엔드사자")
        self.assertNotContains(response, "아기사자1")
        self.assertContains(response, "총 1명의 아기사자가 있습니다.")

    def test_list_uses_queryset_search_count_and_latest_order(self):
        old_lion = Lion.objects.create(name="오래된사자", track=Lion.TRACK_DJANGO)
        new_lion = Lion.objects.create(name="최신사자", track=Lion.TRACK_REACT)

        response = self.client.get(reverse("lion_list"), {"keyword": "React"})

        self.assertEqual(list(response.context["lions"]), [new_lion])
        self.assertContains(response, "최신사자")
        self.assertNotContains(response, "오래된사자")
        self.assertContains(response, "총 1명의 아기사자가 있습니다.")

        response = self.client.get(reverse("lion_list"))
        self.assertEqual(list(response.context["lions"]), [new_lion, old_lion])

    def test_edit_lion_with_post(self):
        lion = Lion.objects.create(name="아기사자1", track=Lion.TRACK_DJANGO)

        response = self.client.post(
            reverse("lion_edit", args=[lion.id]),
            {"name": "수정사자", "track": Lion.TRACK_REACT},
        )

        self.assertRedirects(response, reverse("lion_detail", args=[lion.id]))
        lion.refresh_from_db()
        self.assertEqual(lion.name, "수정사자")
        self.assertEqual(lion.track, Lion.TRACK_REACT)

    def test_delete_lion_requires_post(self):
        lion = Lion.objects.create(name="아기사자1", track=Lion.TRACK_DJANGO)

        get_response = self.client.get(reverse("lion_delete", args=[lion.id]))
        self.assertRedirects(get_response, reverse("lion_detail", args=[lion.id]))
        self.assertTrue(Lion.objects.filter(id=lion.id).exists())

        post_response = self.client.post(reverse("lion_delete", args=[lion.id]))
        self.assertRedirects(post_response, reverse("lion_list"))
        self.assertFalse(Lion.objects.filter(id=lion.id).exists())


class LionRelationshipTests(TestCase):
    def _model(self, model_name):
        return apps.get_model("lions", model_name)

    def test_relationship_models_and_admin_are_configured(self):
        Task = self._model("Task")
        LionProfile = self._model("LionProfile")
        Tag = self._model("Tag")

        self.assertTrue(admin.site.is_registered(Task))
        self.assertTrue(admin.site.is_registered(LionProfile))
        self.assertTrue(admin.site.is_registered(Tag))

        task_field = Task._meta.get_field("lion")
        self.assertEqual(task_field.remote_field.on_delete.__name__, "CASCADE")
        self.assertEqual(task_field.remote_field.related_name, "tasks")

        profile_field = LionProfile._meta.get_field("lion")
        self.assertTrue(profile_field.unique)
        self.assertEqual(profile_field.remote_field.related_name, "profile")

        tag_field = Tag._meta.get_field("lions")
        self.assertEqual(tag_field.remote_field.related_name, "tags")

    def test_create_lion_creates_default_tasks_and_profile_in_one_transaction(self):
        Task = self._model("Task")
        LionProfile = self._model("LionProfile")

        response = self.client.post(
            reverse("lion_create"),
            {"name": "트랜잭션사자", "track": Lion.TRACK_DJANGO},
        )

        self.assertRedirects(response, reverse("lion_list"))
        lion = Lion.objects.get(name="트랜잭션사자")
        self.assertEqual(Task.objects.filter(lion=lion).count(), 3)
        self.assertTrue(LionProfile.objects.filter(lion=lion).exists())

    def test_create_lion_rolls_back_when_profile_creation_fails(self):
        Task = self._model("Task")

        with patch(
            "lions.views.LionProfile.objects.create",
            side_effect=Exception("강제 롤백"),
        ):
            with self.assertRaises(Exception):
                self.client.post(
                    reverse("lion_create"),
                    {"name": "롤백사자", "track": Lion.TRACK_DJANGO},
                )

        self.assertFalse(Lion.objects.filter(name="롤백사자").exists())
        self.assertEqual(Task.objects.filter(title__contains="기본").count(), 0)

    def test_detail_shows_profile_tags_and_incomplete_task_queryset(self):
        Task = self._model("Task")
        LionProfile = self._model("LionProfile")
        Tag = self._model("Tag")
        lion = Lion.objects.create(name="상세사자", track=Lion.TRACK_REACT)
        incomplete_task = Task.objects.create(lion=lion, title="미완료 과제")
        Task.objects.create(lion=lion, title="완료 과제", completed=True)
        LionProfile.objects.create(
            lion=lion,
            github_url="https://github.com/likelion",
            bio="연관관계 실습 중",
        )
        tag = Tag.objects.create(name="ORM")
        lion.tags.add(tag)

        response = self.client.get(
            reverse("lion_detail", args=[lion.id]),
            {"task_status": "incomplete"},
        )

        self.assertEqual(list(response.context["tasks"]), [incomplete_task])
        self.assertEqual(response.context["task_count"], 2)
        self.assertEqual(response.context["profile"].bio, "연관관계 실습 중")
        self.assertEqual(list(response.context["lion_tags"]), [tag])
        self.assertContains(response, "미완료 과제")
        self.assertNotContains(response, "완료 과제")
        self.assertContains(response, "https://github.com/likelion")
        self.assertContains(response, "ORM")

    def test_task_profile_and_tag_views_update_relationships(self):
        Task = self._model("Task")
        LionProfile = self._model("LionProfile")
        Tag = self._model("Tag")
        lion = Lion.objects.create(name="액션사자", track=Lion.TRACK_DJANGO)
        task = Task.objects.create(lion=lion, title="토글 과제")
        LionProfile.objects.create(lion=lion)

        self.client.post(reverse("task_toggle", args=[lion.id, task.id]))
        task.refresh_from_db()
        self.assertTrue(task.completed)

        self.client.post(
            reverse("profile_edit", args=[lion.id]),
            {
                "github_url": "https://github.com/action-lion",
                "bio": "프로필 수정 완료",
            },
        )
        profile = LionProfile.objects.get(lion=lion)
        self.assertEqual(profile.github_url, "https://github.com/action-lion")
        self.assertEqual(profile.bio, "프로필 수정 완료")

        self.client.post(reverse("tag_toggle", args=[lion.id]), {"name": "Django"})
        tag = Tag.objects.get(name="Django")
        self.assertEqual(list(tag.lions.all()), [lion])
        self.assertEqual(list(lion.tags.all()), [tag])

        self.client.post(reverse("tag_toggle", args=[lion.id]), {"name": "Django"})
        self.assertFalse(lion.tags.filter(name="Django").exists())

    def test_task_create_view_adds_task_and_rejects_empty_title(self):
        Task = self._model("Task")
        lion = Lion.objects.create(name="과제사자", track=Lion.TRACK_DJANGO)

        empty_response = self.client.post(
            reverse("task_create", args=[lion.id]),
            {"title": ""},
        )
        self.assertEqual(empty_response.status_code, 200)
        self.assertContains(empty_response, "Task 제목은 필수 입력입니다.")
        self.assertEqual(Task.objects.filter(lion=lion).count(), 0)

        response = self.client.post(
            reverse("task_create", args=[lion.id]),
            {"title": "추가 과제"},
        )

        self.assertRedirects(response, reverse("lion_detail", args=[lion.id]))
        self.assertTrue(Task.objects.filter(lion=lion, title="추가 과제").exists())

    def test_missing_task_toggle_returns_404_without_does_not_exist_error(self):
        lion = Lion.objects.create(name="404사자", track=Lion.TRACK_DJANGO)

        response = self.client.post(reverse("task_toggle", args=[lion.id, 9999]))

        self.assertEqual(response.status_code, 404)
