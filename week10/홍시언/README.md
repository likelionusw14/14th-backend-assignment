## 프로젝트 소개
- 프로젝트 목적 : 10주차에 걸쳐 만든 Django 프로젝트 입니다
- 구현 기능 요약:
    - Lion 관리: 목록 조회(검색/필터/페이징), 생성, 상세 조회, 수정, 삭제.
    - 자동화 로직: Lion 생성 시 기본 Task 3개 및 Profile 자동 생성 (트랜잭션 적용).
    - 과제(Task) 관리: 각 사자별 과제 완료 상태 토글(Toggle).
    - 프로필(Profile) 및 태그(Tag): 1:1 프로필 수정 및 N:M 태그 추가/제거 기능.
- 사용 기술: Python, Django, MySQL, Django ORM

## 실행 방법

```
git clone <repository_url>
cd <project_directory>

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# MYSQL DB 생성 후 실행
mysql> CREATE DATABASE lion_db;

python3 manage.py makemigrations lions
python3 manage.py migrate

python3 manage.py runserver
```

## ERD 구조
- Lion (1) : Task (N)
    - 타입: `ForeignKey`
    - 설정: `on_delete=models.CASCADE`, `related_name='tasks'`
    - 설명: 한 명의 사자는 여러 성장 과제를 가집니다. 사자가 삭제되면 해당 사자의 모든 과제도 함께 삭제되어 데이터 고립을 방지합니다.
- Lion (1) : LionProfile (1)
    - 타입: `OneToOneField`
    - 설정: `on_delete=models.CASCADE`, `related_name='profile'`
    - 설명: 사자 1명당 1개의 상세 프로필을 가집니다. 확장 정보(자기소개 등)를 별도 테이블로 분리하여 메인 테이블의 경량화를 유지합니다.
- Lion (N) : Tag (M)
    - 타입: `ManyToManyField`
    - 설정: `related_name='lions'`
    - 설명: 사자는 여러 태그를 가질 수 있고, 하나의 태그도 여러 사자에게 부여될 수 있습니다. Django ORM을 통해 `lions_lion_tags` 중간 테이블이 자동 생성되어 관리됩니다.

## 핵심 설계 설명

### 1️⃣ 관계형 데이터베이스(RDB) 설계 이유
단순히 정보를 저장하는 것을 넘어, 데이터의 성격과 생명주기를 고려해 설계했습니다.
- 확장성 (1:1): 사자의 기본 인적 사항 외에 수시로 변하거나 내용이 방대한 '자기소개' 등을 별도 테이블로 분리하여 성능 저하를 방지했습니다.
- 데이터 정합성 (1:N): 사자가 삭제되었을 때 의미가 없어지는 '과제' 데이터들을 `CASCADE` 옵션으로 묶어 DB의 무결성을 유지했습니다.
- 재사용성 (N:M): 태그 정보를 문자열이 아닌 독립된 객체로 관리하여 중복 입력을 방지하고, 특정 태그를 가진 사자들을 빠르게 필터링할 수 있도록 했습니다.

### 2️⃣ `transaction.atomic()` 적용 이유
Lion 등록 프로세스는 [Lion 레코드 생성 -> Profile 생성 -> 기본 Task 3개 생성] 순으로 이루어집니다.
- 문제 상황: 만약 사자 정보는 저장됐는데, 서버 에러로 과제가 생성되지 않는다면 해당 사자는 '과제 없는 사자'라는 불완전한 상태가 됩니다.
- 해결: `@transaction.atomic`을 통해 이 모든 과정을 하나의 원자적(Atomic) 단위로 묶었습니다. 과정 중 단 하나라도 실패하면 DB는 작업 전 상태로 Rollback되어 데이터의 일관성을 완벽히 보장합니다.

### 3️⃣ Django ORM 활용의 이점
직접 SQL을 작성하지 않고 ORM(Object-Relational Mapping)만을 사용하여 개발했습니다.
- 보안성: `QuerySet` API를 사용하여 SQL Injection 공격을 프레임워크 수준에서 원천 차단했습니다.
- 가독성: `lion.tasks.all()`과 같이 파이썬 객체 지향 문법을 사용하여 복잡한 JOIN 쿼리 없이도 데이터 간의 관계를 직관적으로 제어했습니다.
- 유지보수: 현재 MySQL을 사용 중이지만, 향후 다른 DB(PostgreSQL 등)로 교체하더라도 비즈니스 로직 수정 없이 설정만으로 대응 가능한 유연성을 확보했습니다.

### 4️⃣ 예외 상황 대응 (Defense Code)
- get_object_or_404: 잘못된 ID로 접근 시 서버 에러(500) 대신 클라이언트에게 정확한 에러(404)를 반환하도록 설계했습니다.
- get_or_create: 수동으로 DB를 조작하여 프로필이 유실된 데이터에 접근하더라도 에러를 내지 않고 즉석에서 프로필을 생성해 보여주는 방어적 로직을 구현했습니다.