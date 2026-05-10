# 🦁 Week10 — Lion 서비스 통합 프로젝트

## 📋 프로젝트 소개

### 프로젝트 목적
Django ORM의 다양한 관계 설정(1:N, 1:1, N:M)을 실습하고,
트랜잭션(`transaction.atomic`)을 활용하여 **데이터 무결성이 보장되는 완성도 있는 웹 서비스**를 구현합니다.

### 구현 기능 요약
| 기능 | 설명 |
|------|------|
| Lion CRUD | 멤버 생성 / 목록(검색) / 상세 / 수정 / 삭제 |
| Task 관리 | Lion 생성 시 기본 Task 3개 자동 생성, 완료 토글 |
| LionProfile | 1:1 프로필 자동 생성, 수정 |
| Tag | N:M 태그 추가/제거 토글 |
| 트랜잭션 | Lion 생성 시 atomic 블록으로 일괄 처리 |
| 예외 처리 | 404 처리, 빈 값 검증, GET/POST 구분 |

### 사용 기술
- Python, Django, MySQL, Django ORM

---

## 🛠 기술 스택

| 구분 | 기술 |
|------|------|
| Language | Python 3.10+ |
| Framework | Django 4.2 |
| Database | MySQL 8.0 |
| ORM | Django ORM |
| 기타 | django-cors-headers, djangorestframework |

---

## 🚀 실행 방법

```bash
# 1. 레포지토리 클론
git clone <repository>
cd <project>/DjangoApi/DjangoApi

# 2. 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate         # Windows

# 3. 의존성 설치
pip install -r requirements.txt

# 4. 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 5. 서버 실행
python manage.py runserver
```

---

## 📊 ERD 구조

```
┌──────────────┐       ┌──────────────┐
│     Lion     │       │     Task     │
├──────────────┤       ├──────────────┤
│ id (PK)      │──1:N─▶│ id (PK)      │
│ name         │       │ lion_id (FK)  │
│ created_at   │       │ title        │
└──────┬───────┘       │ is_done      │
       │               │ created_at   │
       │               └──────────────┘
       │
       │ 1:1     ┌──────────────┐
       ├────────▶│ LionProfile  │
       │         ├──────────────┤
       │         │ id (PK)      │
       │         │ lion_id (FK)  │
       │         │ bio          │
       │         │ github_url   │
       │         └──────────────┘
       │
       │ N:M     ┌──────────────┐
       └────────▶│     Tag      │
                 ├──────────────┤
                 │ id (PK)      │
                 │ name         │
                 └──────────────┘
                 (중간 테이블 자동 생성: week10_tag_lions)
```

### 관계 정리
| 관계 | 모델 | Django 필드 | 삭제 정책 |
|------|------|------------|----------|
| 1:N | Lion → Task | `ForeignKey` | `CASCADE` |
| 1:1 | Lion → LionProfile | `OneToOneField` | `CASCADE` |
| N:M | Lion ↔ Tag | `ManyToManyField` | 중간 테이블 자동 생성 |

---

## 🏗 핵심 설계 설명

### 1:N / 1:1 / N:M 관계 설계 이유

- **1:N (Lion → Task)**: 한 명의 Lion이 여러 개의 Task를 가질 수 있음. `ForeignKey`로 구현하며, Lion 삭제 시 관련 Task도 함께 삭제(`CASCADE`).
- **1:1 (Lion → LionProfile)**: 각 Lion은 하나의 프로필만 가짐. `OneToOneField`로 구현하여 중복 생성을 방지하며, Lion 삭제 시 프로필도 함께 삭제(`CASCADE`).
- **N:M (Lion ↔ Tag)**: 여러 Lion이 여러 Tag를 공유할 수 있음. `ManyToManyField`로 구현하며 Django가 중간 테이블을 자동 생성.

### transaction.atomic() 적용 이유

Lion 생성 시 **Lion + Task 3개 + LionProfile**을 한 번에 생성합니다.
만약 중간에 오류가 발생하면 **부분적으로 생성된 데이터가 DB에 남는 것을 방지**해야 합니다.

```python
with transaction.atomic():
    lion = Lion.objects.create(name=name)
    for task_title in default_tasks:
        Task.objects.create(lion=lion, title=task_title)
    LionProfile.objects.create(lion=lion)
```

- LionProfile 생성 중 오류 발생 → Lion, Task 모두 **롤백**
- 모든 작업이 성공해야만 DB에 **커밋**

### ORM만 사용한 이유

- **SQL 인젝션 방지**: ORM이 자동으로 파라미터를 이스케이프 처리
- **DB 독립성**: MySQL, PostgreSQL, SQLite 등 DB 변경 시 코드 수정 불필요
- **유지보수성**: Python 코드로 DB 조작이 가능하여 가독성 향상
- **마이그레이션**: `makemigrations` / `migrate`로 스키마 버전 관리 가능

### 데이터 무결성 보장 방식

| 방식 | 설명 |
|------|------|
| `CASCADE` | Lion 삭제 시 연관 Task, LionProfile 자동 삭제 |
| `transaction.atomic()` | 생성 중 오류 발생 시 전체 롤백 |
| `get_object_or_404` | 존재하지 않는 리소스 접근 시 404 반환 |
| `get_or_create` | LionProfile 없는 Lion 접근 시 자동 생성 |
| `unique=True` | Tag 이름 중복 방지 |
| POST/GET 구분 | 데이터 변경은 POST만 허용 |

---

## 🔗 서비스 URL 구조

```
/lions/                              → Lion 목록 (GET)
/lions/new/                          → Lion 생성 (GET: 폼, POST: 생성)
/lions/<id>/                         → Lion 상세 (GET)
/lions/<id>/edit/                    → Lion 수정 (GET: 폼, POST: 수정)
/lions/<id>/delete/                  → Lion 삭제 (POST)
/lions/<id>/tasks/<task_id>/toggle/  → Task 완료 토글 (POST)
/lions/<id>/profile/edit/            → LionProfile 수정 (GET: 폼, POST: 수정)
/lions/<id>/tags/<tag_id>/toggle/    → Tag 추가/제거 토글 (POST)
```

---

## ✅ 트랜잭션 테스트 설명

### 테스트 실행 방법
```bash
python manage.py test week10
```

### 테스트 항목

#### 1. 정상 생성 테스트
- Lion 생성 시 **Task 3개 + LionProfile** 자동 생성 확인
- 생성 후 상세 페이지로 리다이렉트 확인

#### 2. 트랜잭션 롤백 테스트 (Atomicity 검증)
- LionProfile 생성 시 **강제 `IntegrityError` 발생**
- `transaction.atomic()` 블록 내에서 오류 발생 시 **Lion, Task 모두 롤백** 확인
- DB에 Lion 0개, Task 0개, LionProfile 0개 확인 → **Atomicity 보장**

#### 3. CASCADE 삭제 테스트
- Lion 삭제 시 **연관된 Task, LionProfile이 함께 삭제**되는지 확인

#### 4. Task 토글 테스트
- `is_done = False → True → False` 토글 동작 확인

#### 5. Tag 토글 테스트
- Tag 추가 → 제거 토글 동작 확인

#### 6. LionProfile get_or_create 테스트
- LionProfile이 없는 Lion 상세 페이지 접근 시 **자동 생성** 확인

#### 7. 404 처리 테스트
- 존재하지 않는 Lion / Task / Tag 접근 시 **404 반환** 확인
