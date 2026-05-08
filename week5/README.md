# 🦁 아기사자 관리 서비스

## 프로젝트 소개

### 목적
Django ORM의 다양한 관계형 데이터 모델(1:N, 1:1, N:M)을 실습하고,
트랜잭션 처리와 예외 처리를 포함한 완성도 있는 웹 서비스를 구현합니다.

### 구현 기능 요약
- 아기사자(Lion) 등록 / 목록 조회 / 상세 조회 / 수정 / 삭제
- Lion 생성 시 Task 3개 + LionProfile 자동 생성 (트랜잭션)
- Task 완료 여부 토글
- LionProfile 수정 (1:1 관계)
- Tag 추가 / 제거 토글 (N:M 관계)
- 검색 및 트랙 필터링

### 사용 기술
- Python
- Django
- MySQL
- Django ORM

---

## 실행 방법

```bash
git clone <repository>
cd <project>
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## ERD 구조

```
Lion (1) : Task (N)        → ForeignKey, CASCADE
Lion (1) : LionProfile (1) → OneToOneField, CASCADE
Lion (N) : Tag (M)         → ManyToManyField, 중간 테이블 자동 생성
```

| 모델 | 관계 | 방식 | 삭제 정책 |
|------|------|------|-----------|
| Lion → Task | 1:N | ForeignKey | CASCADE |
| Lion → LionProfile | 1:1 | OneToOneField | CASCADE |
| Lion ↔ Tag | N:M | ManyToManyField | 중간 테이블 자동 관리 |

---

## 핵심 설계 설명

### 1:N / 1:1 / N:M 관계 설계 이유

**1:N (Lion - Task)**  
하나의 아기사자는 여러 개의 과제를 가질 수 있습니다.
과제는 반드시 하나의 아기사자에 속하므로 ForeignKey로 설계했습니다.
Lion 삭제 시 관련 Task도 함께 삭제되도록 CASCADE를 적용했습니다.

**1:1 (Lion - LionProfile)**  
아기사자 한 명당 프로필은 반드시 하나만 존재합니다.
OneToOneField를 사용해 중복 프로필 생성을 DB 레벨에서 방지했습니다.
Lion 삭제 시 프로필도 함께 삭제되도록 CASCADE를 적용했습니다.

**N:M (Lion - Tag)**  
하나의 태그는 여러 아기사자에게 붙을 수 있고,
하나의 아기사자는 여러 태그를 가질 수 있습니다.
ManyToManyField를 사용해 Django가 중간 테이블을 자동으로 생성하도록 했습니다.

---

### transaction.atomic() 적용 이유

Lion 생성 시 Task 3개와 LionProfile을 함께 생성합니다.
이 과정 중 하나라도 실패하면 나머지도 모두 롤백되어야 데이터 정합성이 유지됩니다.
`@transaction.atomic`을 적용해 모든 생성 작업이 하나의 트랜잭션으로 묶이도록 했습니다.

```python
# Lion 생성 중 오류 발생 시 Task, LionProfile 모두 롤백
@transaction.atomic
def lion_create(request):
    lion = Lion.objects.create(...)
    Task.objects.create(author=lion, ...)  # 실패 시 전체 롤백
    LionProfile.objects.create(user=lion)  # 실패 시 전체 롤백
```

---

### ORM만 사용한 이유

- **생산성**: SQL을 직접 작성하지 않고 Python 코드로 DB를 조작할 수 있습니다.
- **안전성**: ORM이 SQL Injection을 자동으로 방어합니다.
- **유지보수**: 코드와 DB 구조가 모델 클래스로 일원화되어 관리가 편합니다.
- **이식성**: DB 종류(MySQL, SQLite 등)가 바뀌어도 코드 변경 없이 동작합니다.
