# 🦁 아기사자 관리 웹 (Django ORM)

## 프로젝트 소개

### 프로젝트 목적
멋쟁이사자처럼 백엔드 트랙 학습 과정에서 Django의 MVT 패턴과 ORM 관계 매핑(1:N, 1:1, N:M)을 직접 구현하며 익히기 위한 학습용 프로젝트입니다.

### 구현 기능 요약
- 아기사자(Lion) CRUD: 등록 / 목록 / 상세 / 수정 / 삭제
- 이름 검색(`?keyword=`) + 트랙 필터(`?track=`)
- 성장 과제(Task) 1:N 연결 — Lion 생성 시 기본 과제 3개 자동 생성, 완료 토글, 상태별 필터
- 프로필(LionProfile) 1:1 연결 — Lion 생성 시 자동 생성, GitHub URL · 자기소개 수정
- 태그(Tag) N:M 연결 — 태그 추가/제거 토글, 태그별 사자 목록 조회
- `transaction.atomic()` 기반 안전한 다중 객체 생성 (Lion + Task 3개 + Profile)

### 사용 기술
- Python 3.x
- Django 4.x
- MySQL
- Django ORM (raw SQL 미사용)

---

## 실행 방법

```bash
git clone <repository>
cd <project>
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

접속: `http://127.0.0.1:8000/lions/`

---

## ERD 구조

```
┌──────────────┐  1     N  ┌──────────────┐
│    Lion      │ ────────► │    Task      │   ForeignKey, CASCADE
│              │           │              │
│ - name       │  1     1  ┌──────────────┐
│ - track      │ ────────► │ LionProfile  │   OneToOneField, CASCADE
│ - created_at │           │              │
│              │  N     M  ┌──────────────┐
│              │ ◄───────► │    Tag       │   ManyToManyField (중간 테이블 자동)
└──────────────┘           └──────────────┘
```

- Lion (1) : Task (N) — `ForeignKey`, `on_delete=CASCADE`, `related_name='tasks'`
- Lion (1) : LionProfile (1) — `OneToOneField`, `on_delete=CASCADE`, `related_name='profile'`
- Lion (N) : Tag (M) — `ManyToManyField`, 중간 테이블 자동 생성, `related_name='tags'`

---

## 핵심 설계 설명

### 1:N / 1:1 / N:M 관계 설계 이유

| 관계 | 모델 | 선택 이유 |
|------|------|----------|
| 1:N | Lion : Task | 한 명의 사자가 여러 개의 과제를 가질 수 있고, 각 과제는 하나의 사자에 속함. 자식 쪽(Task)에 `ForeignKey`를 두는 것이 자연스러움. |
| 1:1 | Lion : LionProfile | 사자당 프로필이 정확히 하나만 존재. 프로필 정보(GitHub URL, 자기소개)는 Lion 본체보다 부가적이고 변경 빈도가 다르므로 분리. `OneToOneField` 사용. |
| N:M | Lion ↔ Tag | 한 사자가 여러 태그를, 한 태그가 여러 사자를 가질 수 있음. 중간 테이블이 필요하지만 Django의 `ManyToManyField`가 자동 생성/관리해줌. |

### `transaction.atomic()` 적용 이유
`lion_create` 뷰는 한 번의 요청에서 Lion 1개 + Task 3개 + LionProfile 1개, 총 5개의 DB INSERT를 수행합니다. 만약 중간에 예외가 발생하면 일부만 저장되어 데이터 정합성이 깨집니다(예: Lion은 있는데 Profile은 없는 상태). `@transaction.atomic` 데코레이터로 감싸 모든 INSERT를 하나의 트랜잭션으로 묶으면, 중간에 실패해도 전부 롤백되어 "전부 성공 또는 전부 실패"가 보장됩니다.

### ORM만 사용한 이유
- DB 종속성 제거 — SQLite/MySQL/PostgreSQL 어떤 DB로 바꿔도 코드 수정이 거의 없음
- SQL 인젝션 방지 — ORM이 자동으로 파라미터 바인딩 처리
- 가독성과 유지보수성 — `Lion.objects.filter(name__icontains=keyword)`처럼 의도가 명확
- 마이그레이션 자동화 — 모델 변경이 곧 스키마 변경

---

## 자주 묻는 질문 (학습 정리)

### MVT 패턴에서 Model / View / Template의 역할은?
- Model: DB 스키마와 비즈니스 데이터를 정의 (`models.py`). ORM을 통해 데이터 접근.
- View: 요청을 받아 Model에서 데이터를 가져오고, Template에 넘겨주는 제어 로직. (Django의 View ≒ 다른 프레임워크의 Controller)
- Template: View에서 받은 데이터를 HTML로 렌더링하는 표현 계층.

### ForeignKey / OneToOneField / ManyToManyField는 언제 쓰는가?
- ForeignKey (1:N): 자식이 부모를 하나만 참조할 때. 예: 댓글 → 게시글
- OneToOneField (1:1): 양쪽이 정확히 하나씩 짝지어질 때. 예: User → Profile
- ManyToManyField (N:M): 양쪽이 여러 개씩 연결될 때. 예: 학생 ↔ 수업

### 단방향 접근과 양방향 접근의 차이는?
- 단방향: `task.lion` (자식 → 부모) — `ForeignKey`를 정의한 쪽에서 자동 생성됨
- 양방향: `lion.tasks.all()` (부모 → 자식들) — `related_name`을 통해 역참조

### `related_name`이 필요한 이유는?
역참조 시 사용할 이름을 명시적으로 지정하기 위함. 기본값은 `<모델명소문자>_set`이라 `lion.task_set.all()`처럼 어색해짐. `related_name='tasks'`를 주면 `lion.tasks.all()`로 자연스럽게 쓸 수 있고, 한 모델이 같은 모델을 여러 번 참조할 때 충돌도 막아줌.

### 트랜잭션이 없다면 어떤 문제가 발생하는가?
`lion_create`에서 Lion은 저장됐는데 Task 생성 중 예외가 터지면, Lion은 DB에 남고 Task는 없는 불완전한 상태가 됩니다. 사용자가 다시 시도하면 같은 이름의 사자가 또 생기는 중복도 발생할 수 있어 데이터 무결성이 깨집니다.

### 6주차 → 10주차 발전 과정

| 주차 | 핵심 내용 |
|------|----------|
| 6주차 | Django 프로젝트 구조, View와 Template 연결 |
| 7주차 | Model 도입, 단일 모델 CRUD (Lion 등록/목록/상세) |
| 8주차 | 1:N 관계 (Lion-Task) 추가, 검색·필터 기능 |
| 9주차 | 1:1, N:M 관계 추가 (LionProfile, Tag), 트랜잭션 |
| 10주차 | 리팩토링 — `get_object_or_404`, `get_or_create`, `Meta.ordering`, 예외 처리 일관화, README 정비 |

---

## 디렉터리 구조 (요약)

```
project/
├── lions/
│   ├── models.py         # Lion / Task / LionProfile / Tag
│   ├── views.py          # 9개 뷰 함수
│   ├── urls.py           # /lions/ 하위 라우팅
│   └── templates/lions/
│       ├── list.html
│       ├── new.html
│       ├── detail.html
│       ├── edit.html
│       ├── profile_edit.html
│       └── tag_lions.html
├── templates/
│   ├── base.html
│   └── home.html
├── manage.py
└── requirements.txt
```
