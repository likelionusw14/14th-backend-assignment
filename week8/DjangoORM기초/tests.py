from django.test import TestCase
from django.urls import reverse

from .models import Lion


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
