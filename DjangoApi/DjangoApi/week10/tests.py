from unittest.mock import patch

from django.db import IntegrityError
from django.test import TestCase

from .models import Lion, LionProfile, Tag, Task


class LionCreationTransactionTest(TestCase):
    """Lion 생성 시 트랜잭션(transaction.atomic) 검증 테스트"""

    def test_lion_creation_creates_tasks_and_profile(self):
        """정상 생성: Lion + Task 3개 + LionProfile 자동 생성 확인"""
        response = self.client.post('/lions/new/', {'name': '홍길동'})

        # Lion 1개 생성 확인
        self.assertEqual(Lion.objects.count(), 1)
        lion = Lion.objects.first()
        self.assertEqual(lion.name, '홍길동')

        # Task 3개 자동 생성 확인
        self.assertEqual(Task.objects.filter(lion=lion).count(), 3)

        # LionProfile 자동 생성 확인
        self.assertTrue(LionProfile.objects.filter(lion=lion).exists())

        # 상세 페이지로 리다이렉트 확인
        self.assertEqual(response.status_code, 302)

    def test_transaction_rollback_on_error(self):
        """
        트랜잭션 롤백 테스트:
        LionProfile 생성 시 강제 오류 발생 → Lion과 Task 모두 롤백되어야 함
        """
        with patch.object(
            LionProfile.objects, 'create',
            side_effect=IntegrityError('강제 오류'),
        ):
            response = self.client.post('/lions/new/', {'name': '실패케이스'})

        # 롤백 확인: Lion, Task, LionProfile 모두 0개
        self.assertEqual(Lion.objects.count(), 0)
        self.assertEqual(Task.objects.count(), 0)
        self.assertEqual(LionProfile.objects.count(), 0)

    def test_empty_name_rejected(self):
        """빈 이름 제출 시 생성 거부"""
        response = self.client.post('/lions/new/', {'name': ''})

        self.assertEqual(Lion.objects.count(), 0)
        self.assertEqual(response.status_code, 200)  # 폼 다시 표시


class LionCascadeDeleteTest(TestCase):
    """CASCADE 삭제 검증 테스트"""

    def setUp(self):
        """테스트 데이터 생성"""
        self.lion = Lion.objects.create(name='테스트사자')
        Task.objects.create(lion=self.lion, title='과제1')
        Task.objects.create(lion=self.lion, title='과제2')
        LionProfile.objects.create(lion=self.lion, bio='테스트 소개')

    def test_cascade_delete(self):
        """Lion 삭제 시 Task, LionProfile CASCADE 삭제 확인"""
        lion_id = self.lion.id
        self.client.post(f'/lions/{lion_id}/delete/')

        self.assertEqual(Lion.objects.count(), 0)
        self.assertEqual(Task.objects.filter(lion_id=lion_id).count(), 0)
        self.assertEqual(LionProfile.objects.filter(lion_id=lion_id).count(), 0)


class TaskToggleTest(TestCase):
    """Task 완료 토글 테스트"""

    def setUp(self):
        self.lion = Lion.objects.create(name='토글사자')
        self.task = Task.objects.create(lion=self.lion, title='토글 과제')

    def test_toggle_task(self):
        """Task 완료 상태 토글 확인"""
        self.assertFalse(self.task.is_done)

        self.client.post(
            f'/lions/{self.lion.id}/tasks/{self.task.id}/toggle/'
        )
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)

        # 다시 토글 → False
        self.client.post(
            f'/lions/{self.lion.id}/tasks/{self.task.id}/toggle/'
        )
        self.task.refresh_from_db()
        self.assertFalse(self.task.is_done)


class TagToggleTest(TestCase):
    """Tag 추가/제거 토글 테스트"""

    def setUp(self):
        self.lion = Lion.objects.create(name='태그사자')
        self.tag = Tag.objects.create(name='백엔드')

    def test_toggle_tag(self):
        """Tag 추가 → 제거 토글 확인"""
        # 추가
        self.client.post(
            f'/lions/{self.lion.id}/tags/{self.tag.id}/toggle/'
        )
        self.assertIn(self.tag, self.lion.tags.all())

        # 제거
        self.client.post(
            f'/lions/{self.lion.id}/tags/{self.tag.id}/toggle/'
        )
        self.assertNotIn(self.tag, self.lion.tags.all())


class LionProfileGetOrCreateTest(TestCase):
    """LionProfile get_or_create 안전 처리 테스트"""

    def test_profile_auto_created_on_detail(self):
        """LionProfile이 없는 Lion 상세 접근 시 자동 생성 확인"""
        lion = Lion.objects.create(name='프로필없는사자')

        # 프로필이 없는 상태 확인
        self.assertFalse(LionProfile.objects.filter(lion=lion).exists())

        # 상세 페이지 접근 → get_or_create로 자동 생성
        self.client.get(f'/lions/{lion.id}/')
        self.assertTrue(LionProfile.objects.filter(lion=lion).exists())


class NotFoundTest(TestCase):
    """존재하지 않는 리소스 접근 시 404 테스트"""

    def test_lion_not_found(self):
        """존재하지 않는 Lion 접근 → 404"""
        response = self.client.get('/lions/99999/')
        self.assertEqual(response.status_code, 404)

    def test_task_not_found(self):
        """존재하지 않는 Task 토글 → 404"""
        lion = Lion.objects.create(name='사자')
        response = self.client.post(
            f'/lions/{lion.id}/tasks/99999/toggle/'
        )
        self.assertEqual(response.status_code, 404)

    def test_tag_not_found(self):
        """존재하지 않는 Tag 토글 → 404"""
        lion = Lion.objects.create(name='사자')
        response = self.client.post(
            f'/lions/{lion.id}/tags/99999/toggle/'
        )
        self.assertEqual(response.status_code, 404)
